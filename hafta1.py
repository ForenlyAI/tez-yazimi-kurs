"""Hafta 1 · Soru ve Kaynak — Ders 1.1–1.4 (+ tanıtım dersi için bir şekil).
  python hafta1.py   → ekran/1.x/*.txt + *.png, ekran/0.1/*.png, cikti/notlar.csv, OLCUMLER.json (d1_*)"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from ortak import kayit, yumusat, olc, oturum, sekil, LAB

TURUNCU, MAVI, YESIL, MOR, GRI = "#C2410C", "#1D4ED8", "#0F766E", "#7E22CE", "#6B7280"
EVRE_AD = ["kaldırma", "taşıma", "bırakma"]
EVRE_RENK = [MAVI, TURUNCU, YESIL]
(LAB / "cikti").mkdir(exist_ok=True)


def kutu(ax, x, y, w, h, metin, renk, boy=24, yazi="#ffffff"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03", fc=renk, ec="none"))
    ax.text(x + w / 2, y + h / 2, metin, ha="center", va="center", color=yazi, fontsize=boy, linespacing=1.4)


def bos_eksen(baslik):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off"); ax.set_title(baslik)
    return fig, ax


def evreler():
    """Yatay hız eşiğiyle üç evre: eşiğin üstündeki ilk andan son ana kadar taşıma; öncesi kaldırma, sonrası bırakma."""
    k = kayit(); t = k["zaman_s"]
    p = yumusat(np.column_stack([k["bardak_x_m"], k["bardak_y_m"], k["bardak_z_m"]]))
    v = np.gradient(p, t, axis=0)
    hiz = np.linalg.norm(v, axis=1)
    ivme = np.linalg.norm(np.gradient(v, t, axis=0), axis=1)
    yatay = np.linalg.norm(v[:, :2], axis=1) > 0.05
    ilk, son = np.argmax(yatay), len(t) - 1 - np.argmax(yatay[::-1])
    evre = np.where(np.arange(len(t)) < ilk, 0, np.where(np.arange(len(t)) > son, 2, 1))
    return t, hiz, ivme, evre, ilk, son


def ders_1_1():
    """Konudan soruya: konu daraltma, sorunun dört parçası, verinin soruyu taşıyıp taşımadığına ilk bakış."""
    fig, ax = bos_eksen("Konudan soruya: her adımda bir sınır daha")
    adim = [("Konu", "İnsansı robotlar", GRI, 0.74),
            ("Alt konu", "İnsansı robotla servis", MAVI, 0.62),
            ("Odak", "Robotun taşıdığı bardağın hareketi", YESIL, 0.52),
            ("Soru", "Bardak, taşımanın hangi evresinde\nen çok ivmeleniyor?", TURUNCU, 0.44)]
    for i, (ad, metin, renk, w) in enumerate(adim):
        y = 0.78 - i * 0.235
        kutu(ax, 0.59 - w / 2, y, w, 0.17, metin, renk, boy=26)
        ax.text(0.03, y + 0.085, ad, ha="left", va="center", fontsize=24, color="#111111", weight="bold")
    sekil("1.1", "soru-hunisi")

    ns = oturum("1.1", "soru-denetimi", """
soru = {
    "metin": "Bardak, taşımanın hangi evresinde en çok ivmeleniyor?",
    "olculen": "bardağın ivmesi (m/s²)",
    "karsilastirilan": "kaldırma, taşıma ve bırakma evreleri",
    "veri": "G1 çay servisi benzetim kaydı",
    "kapsam_disi": "başka robot, başka görev, gerçek robot ölçümü",
}
for ad, deger in soru.items():
    print(f"{ad:16s} {deger}")
eksik = [ad for ad, deger in soru.items() if not deger]
eksik
""")
    ns = oturum("1.1", "kaydi-tanimak", """
import numpy as np
from ortak import kayit
k = kayit()
for ad in k:
    print(ad)
t = k["zaman_s"]
len(t), t[-1]
""")
    t, hiz, ivme, evre, ilk, son = evreler()
    fig, ax = plt.subplots()
    for i in range(3):
        m = evre == i
        ax.axvspan(t[m][0], t[m][-1], color=EVRE_RENK[i], alpha=0.12)
        ax.text((t[m][0] + t[m][-1]) / 2, hiz.max() * 1.06, f"{EVRE_AD[i]}\n{t[m][-1] - t[m][0]:.1f} s".replace(".", ","),
                ha="center", va="bottom", color=EVRE_RENK[i], fontsize=24, weight="bold")
    ax.plot(t, hiz, color="#111111")
    ax.set_ylim(0, hiz.max() * 1.32); ax.set_xlabel("zaman (s)"); ax.set_ylabel("bardağın hızı (m/s)")
    ax.set_title("Veri soruyu taşıyor mu: kayıtta üç evre ayrılıyor · benzetim kaydı")
    sekil("1.1", "evreler")
    sure = [float(t[evre == i][-1] - t[evre == i][0]) for i in range(3)]
    olc(d1_1_sutun=len(kayit()), d1_1_ornek=len(t), d1_1_sure_s=float(t[-1]), d1_1_evre_sure_s=sure,
        d1_1_tasima_bas_s=float(t[ilk]), d1_1_tasima_son_s=float(t[son]), d1_1_hiz_max=float(hiz.max()))


def ders_1_2():
    """Kaynak taramak: kavram tablosu, arama cümlesi, tarama günlüğü."""
    ns = oturum("1.2", "kavram-tablosu", """
kavramlar = {
    "robot": ["humanoid robot", "insansı robot"],
    "görev": ["object transport", "carrying", "nesne taşıma"],
    "ölçüm": ["acceleration", "smoothness", "ivme"],
}
for ad, terimler in kavramlar.items():
    print(f"{ad:6s} {len(terimler)} terim: " + " | ".join(terimler))
""")
    ns = oturum("1.2", "arama-cumlesi", """
def arama_cumlesi(kavramlar):
    grup = []
    for terimler in kavramlar.values():
        grup.append("(" + " OR ".join(f'"{s}"' for s in terimler) + ")")
    return "\\nAND ".join(grup)
print(arama_cumlesi(kavramlar))
dar = {ad: terimler[:1] for ad, terimler in kavramlar.items()}
print(arama_cumlesi(dar))
sum(len(terimler) for terimler in kavramlar.values())
""", ns)
    fig, ax = bos_eksen("Tarama günlüğü: kaç kaynak bulundu, kaçı kaldı · sayılar ÖRNEK")
    adim = [("Arama cümlesiyle\nbulunan", 240, GRI, 0.66), ("Başlığına bakılıp\nayrılan", 40, MAVI, 0.50),
            ("Özeti okunup\nayrılan", 15, YESIL, 0.36), ("Tam metni\nokunan", 8, TURUNCU, 0.24)]
    for i, (ad, n, renk, w) in enumerate(adim):
        y = 0.78 - i * 0.235
        kutu(ax, 0.63 - w / 2, y, w, 0.17, f"{n} kaynak", renk, boy=28)
        ax.text(0.02, y + 0.085, ad, ha="left", va="center", fontsize=22, color="#111111", weight="bold")
    sekil("1.2", "tarama-gunlugu")
    olc(d1_2_kavram=len(ns["kavramlar"]), d1_2_terim=sum(len(v) for v in ns["kavramlar"].values()),
        d1_2_gunluk_ornek=[a[1] for a in adim])


def ders_1_3():
    """Okumak ve not tutmak: üç geçiş, not kartı, notları tek dosyada tutmak."""
    fig, ax = bos_eksen("Bir kaynağı üç geçişte okumak")
    gecis = [("1. geçiş · göz atmak", "başlık · özet\nşekiller · sonuç", "Karar: bu kaynak\nsorumla ilgili mi?", MAVI),
             ("2. geçiş · kavramak", "giriş · yöntem\nbulgular", "Not kartı\ndoldurulur", YESIL),
             ("3. geçiş · sınamak", "ayrıntılar\nvarsayımlar", "Yalnız tezin\ndayandığı kaynaklar", TURUNCU)]
    for i, (ad, okunan, sonuc, renk) in enumerate(gecis):
        x = 0.03 + i * 0.33
        kutu(ax, x, 0.66, 0.26, 0.20, ad, renk, boy=24)
        kutu(ax, x, 0.36, 0.26, 0.24, okunan, "#F3F4F6", boy=24, yazi="#111111")
        kutu(ax, x, 0.08, 0.26, 0.22, sonuc, "#FFF7ED", boy=23, yazi="#111111")
    sekil("1.3", "uc-gecis")

    ns = oturum("1.3", "not-karti", """
from kaynaklar import NOTLAR
len(NOTLAR)
kart = NOTLAR[0]
for alan in ["anahtar", "yazar", "yil", "soru", "yontem", "bulgu", "sinir", "katki"]:
    print(f"{alan:8s} {kart[alan]}")
""")
    ns = oturum("1.3", "notlar-dosyasi", """
import csv
alanlar = ["anahtar", "yazar", "yil", "baslik", "yayin", "soru", "yontem", "bulgu", "sinir", "katki"]
with open("cikti/notlar.csv", "w", newline="", encoding="utf-8") as f:
    yazici = csv.DictWriter(f, fieldnames=alanlar, extrasaction="ignore")
    yazici.writeheader()
    yazici.writerows(NOTLAR)
eksik = [(n["anahtar"], a) for n in NOTLAR for a in alanlar if not n[a]]
eksik
for n in NOTLAR:
    print(f'{n["anahtar"]:12s} {n["katki"]}')
""", ns)
    olc(d1_3_kaynak=len(ns["NOTLAR"]), d1_3_alan=len(ns["alanlar"]), d1_3_eksik=len(ns["eksik"]))


def ders_1_4():
    """Kaynak çizelgesi ve kaynakça: kaynakları aynı sütunlarla karşılaştırmak, boşluğu görmek, kaynakçayı biçimlemek."""
    ns = oturum("1.4", "cizelge", """
from kaynaklar import NOTLAR
sutunlar = ["insansi_robot", "duzgunluk_olcutu", "evre_karsilastirmasi"]
for n in NOTLAR:
    isaret = ["evet " if n[s] else "hayır" for s in sutunlar]
    print(f'{n["anahtar"]:12s} {n["veri"]:20s} ' + "  ".join(isaret))
hepsi = [n["anahtar"] for n in NOTLAR if all(n[s] for s in sutunlar)]
hepsi
""")
    from kaynaklar import NOTLAR, BIZIM
    sut = ns["sutunlar"]; bas = ["insansı\nrobot", "düzgünlük\nölçütü", "evre\nkarşılaştırması"]
    fig, ax = bos_eksen("Kaynak çizelgesi: taranan dört kaynak ve bu çalışma")
    satir = NOTLAR + [BIZIM]; x0 = [0.02, 0.22, 0.52, 0.70, 0.88]
    for j, b in enumerate(["kaynak", "veri"] + bas):
        ax.text(x0[j], 0.90, b, fontsize=23, weight="bold", ha="left" if j < 2 else "center", va="center")
    for i, n in enumerate(satir):
        y = 0.76 - i * 0.15; bizim = n is BIZIM
        if bizim:
            ax.add_patch(FancyBboxPatch((0.0, y - 0.06), 1.0, 0.12, boxstyle="round,pad=0.0,rounding_size=0.02", fc="#FFF7ED", ec=TURUNCU, lw=3))
        ax.text(x0[0], y, n["anahtar"], fontsize=24, va="center", weight="bold" if bizim else "normal")
        ax.text(x0[1], y, n["veri"], fontsize=24, va="center")
        for j, s in enumerate(sut):
            ax.text(x0[2 + j], y, "evet" if n[s] else "—", fontsize=26, va="center", ha="center",
                    color=YESIL if n[s] else GRI, weight="bold")
    sekil("1.4", "cizelge-sekil")

    ns = oturum("1.4", "kaynakca", """
import textwrap
def kaynakca_satiri(n):
    return f'{n["yazar"]} ({n["yil"]}). {n["baslik"]}. {n["yayin"]}.'
for n in sorted(NOTLAR, key=lambda n: n["yazar"]):
    print(textwrap.fill(kaynakca_satiri(n), 76, subsequent_indent="    "))
def metin_ici(n):
    return f'({n["yazar"].split(",")[0]} vd., {n["yil"]})'
[metin_ici(n) for n in NOTLAR]
""", ns)
    olc(d1_4_kaynak=len(NOTLAR), d1_4_sutun=len(sut), d1_4_ucunu_karsilayan=len(ns["hepsi"]),
        d1_4_duzgunluk_olcutu_olan=sum(n["duzgunluk_olcutu"] for n in NOTLAR))


def tanitim():
    """Tanıtım dersi için: örnek araştırmanın yanıtına ön bakış — evre başına ortalama ve en büyük ivme."""
    t, hiz, ivme, evre, ilk, son = evreler()
    ort = [ivme[evre == i].mean() for i in range(3)]; enb = [ivme[evre == i].max() for i in range(3)]
    fig, ax = plt.subplots()
    x = np.arange(3)
    ax.bar(x - 0.2, ort, 0.38, color=EVRE_RENK, alpha=0.55, label="ortalama")
    ax.bar(x + 0.2, enb, 0.38, color=EVRE_RENK, label="en büyük")
    for i in range(3):
        ax.text(i - 0.2, ort[i] + 0.03, f"{ort[i]:.2f}".replace(".", ","), ha="center", fontsize=24)
        ax.text(i + 0.2, enb[i] + 0.03, f"{enb[i]:.2f}".replace(".", ","), ha="center", fontsize=24, weight="bold")
    ax.set_xticks(x); ax.set_xticklabels(EVRE_AD, fontsize=26); ax.set_ylabel("bardağın ivmesi (m/s²)"); ax.set_ylim(0, max(enb) * 1.15)
    ax.set_title("Evre başına ivme: soluk çubuk ortalama, koyu çubuk en büyük · benzetim kaydı")
    sekil("0.1", "evre-ivme")
    olc(d0_1_ivme_ort=ort, d0_1_ivme_max=enb)


if __name__ == "__main__":
    ders_1_1(); ders_1_2(); ders_1_3(); ders_1_4(); tanitim()
    print("hafta 1 tamam")
