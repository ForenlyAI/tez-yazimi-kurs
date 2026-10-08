"""Tez Yazımı: Sorudan Savunmaya — örnek araştırmanın ortak hesapları ve çizim yardımcıları (Hafta 2–4).
  evre_verisi(esik, pencere) : kayıttan zaman, hız, ivme ve evre numarası (0 kaldırma · 1 taşıma · 2 bırakma)
  evre_ozeti(ivme, evre)     : evre başına örnek sayısı, ortalama, yüzde doksan beşlik değer ve en büyük ivme
  karar(ozet, esik_orani)    : çözümleme planındaki karar kuralı"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from ortak import kayit, yumusat

TURUNCU, MAVI, YESIL, MOR, GRI = "#C2410C", "#1D4ED8", "#0F766E", "#7E22CE", "#6B7280"
EVRE_AD = ["kaldırma", "taşıma", "bırakma"]
EVRE_RENK = [MAVI, TURUNCU, YESIL]


def evre_verisi(esik=0.05, pencere=25):
    k = kayit(); t = k["zaman_s"]
    p = yumusat(np.column_stack([k["bardak_x_m"], k["bardak_y_m"], k["bardak_z_m"]]), pencere)
    v = np.gradient(p, t, axis=0)
    hiz = np.linalg.norm(v, axis=1)
    ivme = np.linalg.norm(np.gradient(v, t, axis=0), axis=1)
    yatay = np.linalg.norm(v[:, :2], axis=1) > esik
    ilk, son = np.argmax(yatay), len(t) - 1 - np.argmax(yatay[::-1])
    sira = np.arange(len(t))
    evre = np.where(sira < ilk, 0, np.where(sira > son, 2, 1))
    return t, hiz, ivme, evre


def evre_ozeti(ivme, evre):
    ozet = {}
    for i, ad in enumerate(EVRE_AD):
        a = ivme[evre == i]
        ozet[ad] = dict(n=int(a.size), ortalama=round(float(a.mean()), 3), yuzde95=round(float(np.percentile(a, 95)), 3),
                        en_buyuk=round(float(a.max()), 3))
    return ozet


def karar(ortalamalar, esik_orani=0.10):
    """En büyük ortalama ikinciden en az esik_orani kadar büyükse o evre; değilse 'ayırt edilemedi'."""
    sirali = sorted(ortalamalar.items(), key=lambda x: -x[1])
    (ad1, d1), (ad2, d2) = sirali[0], sirali[1]
    return ad1 if d1 >= d2 * (1 + esik_orani) else "ayırt edilemedi"


def kutu(ax, x, y, w, h, metin, renk, boy=24, yazi="#ffffff"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03", fc=renk, ec="none"))
    ax.text(x + w / 2, y + h / 2, metin, ha="center", va="center", color=yazi, fontsize=boy, linespacing=1.4)


def ok(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color="#111111", lw=3, mutation_scale=28))


def bos_eksen(baslik):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off"); ax.set_title(baslik)
    return fig, ax


def tr(x, basamak=2):
    return f"{x:.{basamak}f}".replace(".", ",")
