"""Hafta 3 · Bulgu ve Yazım — Ders 3.1–3.4.
  python hafta3.py   → ekran/3.x/*.txt + *.png, cikti/tablo1.csv, cikti/tez_iskeleti.md, OLCUMLER.json (d3_*)"""
import numpy as np
import matplotlib.pyplot as plt
from ortak import olc, oturum, sekil, LAB
from arac import evre_verisi, evre_ozeti, karar, kutu, ok, bos_eksen, tr, TURUNCU, MAVI, YESIL, MOR, GRI, EVRE_AD, EVRE_RENK

(LAB / "cikti").mkdir(exist_ok=True)


def ders_3_1():
    """Veriden bulguya: çözümleme planını olduğu gibi uygulamak, karar kuralı, sağlamlık denetimi."""
    ns = oturum("3.1", "evre-ozeti", """
from arac import evre_verisi, evre_ozeti, karar
t, hiz, ivme, evre = evre_verisi()
ozet = evre_ozeti(ivme, evre)
for ad, o in ozet.items():
    print(f'{ad:9s} n {o["n"]:5d}  ortalama {o["ortalama"]:.3f}', end="  ")
    print(f'yüzde 95 {o["yuzde95"]:.3f}  en büyük {o["en_buyuk"]:.3f}')
ortalamalar = {ad: o["ortalama"] for ad, o in ozet.items()}
karar(ortalamalar)
round(ozet["taşıma"]["ortalama"] / ozet["kaldırma"]["ortalama"], 1)
""")
    t, ivme, evre = ns["t"], ns["ivme"], ns["evre"]
    fig, ax = plt.subplots()
    for i in range(3):
        m = evre == i
        ax.axvspan(t[m][0], t[m][-1], color=EVRE_RENK[i], alpha=0.12)
        ax.text((t[m][0] + t[m][-1]) / 2, ivme.max() * 1.06, f"{EVRE_AD[i]}\nortalama {tr(ivme[m].mean())}", ha="center", va="bottom",
                color=EVRE_RENK[i], fontsize=24, weight="bold")
    ax.plot(t, ivme, color="#111111", lw=1.8)
    ax.set_ylim(0, ivme.max() * 1.32); ax.set_xlabel("zaman (s)"); ax.set_ylabel("bardağın ivmesi (m/s²)")
    ax.set_title("Bardağın ivmesi ve üç evre · benzetim kaydı")
    sekil("3.1", "ivme-evreler")
    ns = oturum("3.1", "saglamlik", """
for esik in [0.03, 0.05, 0.08]:
    t2, hiz2, ivme2, evre2 = evre_verisi(esik=esik)
    o2 = {ad: o["ortalama"] for ad, o in evre_ozeti(ivme2, evre2).items()}
    print(f"eşik {esik:.2f}  {o2}  yanıt: {karar(o2)}")
for pencere in [13, 25, 51]:
    t2, hiz2, ivme2, evre2 = evre_verisi(pencere=pencere)
    o2 = {ad: o["ortalama"] for ad, o in evre_ozeti(ivme2, evre2).items()}
    print(f"pencere {pencere:3d}  {o2}  yanıt: {karar(o2)}")
""", ns)
    oz = ns["ozet"]
    olc(d3_1_ozet=oz, d3_1_karar=karar(ns["ortalamalar"]), d3_1_oran_tasima_kaldirma=round(oz["taşıma"]["ortalama"] / oz["kaldırma"]["ortalama"], 1))
    return ns


def ders_3_2(ns):
    """Tablo ve şekil: aynı veri, özensiz ve özenli şekil; son şekil ve tablo."""
    t, ivme, evre, oz = ns["t"], ns["ivme"], ns["evre"], ns["ozet"]
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(ivme, lw=1); ax[0].grid(False); ax[0].set_title("Özensiz: eksen adı yok, birim yok, evre yok", fontsize=22)
    veri = [ivme[evre == i] for i in range(3)]
    kg = ax[1].boxplot(veri, patch_artist=True, showfliers=False, widths=0.55, medianprops=dict(color="#111111", lw=3))
    for parca, renk in zip(kg["boxes"], EVRE_RENK):
        parca.set_facecolor(renk); parca.set_alpha(0.55)
    ax[1].set_xticks([1, 2, 3]); ax[1].set_xticklabels(EVRE_AD); ax[1].set_ylabel("bardağın ivmesi (m/s²)")
    ax[1].set_title("Özenli: tek ileti, eksen adı, birim", fontsize=22)
    sekil("3.2", "iki-sekil")

    fig, ax = plt.subplots()
    x = np.arange(3); ort = [oz[a]["ortalama"] for a in EVRE_AD]; y95 = [oz[a]["yuzde95"] for a in EVRE_AD]
    ax.bar(x, ort, 0.5, color=EVRE_RENK, alpha=0.75, label="ortalama")
    ax.plot(x, y95, "D", color="#111111", ms=16, label="yüzde doksan beşlik değer")
    for i in range(3):
        ax.text(i + 0.09, y95[i], tr(y95[i]), ha="left", va="center", fontsize=22)
    ax.set_xticks(x); ax.set_xticklabels([f"{a}\nortalama {tr(o)}" for a, o in zip(EVRE_AD, ort)], fontsize=26); ax.set_ylabel("bardağın ivmesi (m/s²)"); ax.set_ylim(0, max(y95) * 1.2); ax.legend(loc="upper right")
    ax.set_title("Şekil 1. Evre başına bardağın ivmesi (benzetim kaydı, 5666 örnek)")
    sekil("3.2", "sekil1")
    ns = oturum("3.2", "tablo1", """
import csv
baslik = "Tablo 1. Evre başına bardağın ivmesi (m/s²); benzetim kaydı"
satirlar = []
for ad, o in ozet.items():
    sayilar = [f"{o[k]:.2f}" for k in ["ortalama", "yuzde95", "en_buyuk"]]
    satirlar.append([ad, o["n"]] + sayilar)
with open("cikti/tablo1.csv", "w", newline="", encoding="utf-8") as f:
    yazici = csv.writer(f)
    yazici.writerow(["evre", "örnek sayısı", "ortalama", "yüzde 95", "en büyük"])
    yazici.writerows(satirlar)
print(baslik)
print("evre         örnek  ortalama  yüzde 95  en büyük")
for s in satirlar:
    print(f"{s[0]:10s}{s[1]:>8d}{s[2]:>10s}{s[3]:>10s}{s[4]:>10s}")
""", ns)
    olc(d3_2_tablo_satir=len(ns["satirlar"]))
    return ns


def ders_3_3(ns):
    """Bölümleri yazmak: bölüm ↔ soru haritası, sayıları veriden alan bulgu cümlesi, tez iskeleti."""
    fig, ax = bos_eksen("Her bölüm tek bir soruyu yanıtlar")
    bolum = [("Giriş", "Neden bu soru?", "konudan soruya huni\nboşluk ve katkı", MAVI), ("Yöntem", "Ne yaptım?", "başkası yineleyebilsin\ndiye yeterli ayrıntı", YESIL),
             ("Bulgular", "Ne buldum?", "tablo, şekil, sayı\nyorum yok", TURUNCU), ("Tartışma", "Bu ne demek?", "yorum, kaynaklarla\nkarşılaştırma, sınırlar", MOR)]
    for i, (ad, soru, icerik, renk) in enumerate(bolum):
        x = 0.02 + i * 0.25
        kutu(ax, x, 0.68, 0.20, 0.18, ad, renk, boy=28)
        kutu(ax, x, 0.42, 0.20, 0.18, soru, "#F3F4F6", boy=24, yazi="#111111")
        kutu(ax, x, 0.12, 0.20, 0.22, icerik, "#FFF7ED", boy=20, yazi="#111111")
    sekil("3.3", "bolum-haritasi")
    ns = oturum("3.3", "bulgu-cumlesi", """
import textwrap
def tr(x):
    return f"{x:.2f}".replace(".", ",")
o = ozet
cumle = (f'Bardağın ivmesi taşıma evresinde ortalama {tr(o["taşıma"]["ortalama"])} m/s², '
         f'kaldırma evresinde {tr(o["kaldırma"]["ortalama"])} m/s² ve '
         f'bırakma evresinde {tr(o["bırakma"]["ortalama"])} m/s² olarak ölçüldü (Tablo 1). '
         f'En büyük ivme {tr(o["taşıma"]["en_buyuk"])} m/s² ile taşıma evresinde görüldü (Şekil 1).')
print(textwrap.fill(cumle, 72))
sinir = "Bulgular tek bir benzetim kaydına dayanır; başka robotlara ve gerçek robota genellenemez."
print(textwrap.fill(sinir, 72))
""", ns)
    ns = oturum("3.3", "tez-iskeleti", """
from iskelet import iskelet
len(iskelet), sum(len(altlar) for bolum, altlar in iskelet)
satir = []
for bolum, altlar in iskelet:
    satir.append("# " + bolum)
    satir += ["## " + a for a in altlar]
import pathlib
dosya = pathlib.Path("cikti/tez_iskeleti.md")
uzunluk = dosya.write_text("\\n".join(satir) + "\\n", encoding="utf-8")
print("\\n".join(satir))
""", ns)
    olc(d3_3_bolum=len(ns["iskelet"]), d3_3_alt_baslik=sum(len(a) for _, a in ns["iskelet"]), d3_3_bulgu_cumlesi=ns["cumle"])
    return ns


def ders_3_4():
    """Atıf, benzerlik ve yapay zekâ araçları: atıf kararı, metin–kaynakça eşleşmesi, sözcük örtüşmesi."""
    fig, ax = bos_eksen("Atıf gerekir mi?")
    satir = [("Başkasının bulgusu, verisi ya da fikri", "ATIF VER", TURUNCU), ("Kaynaktan aynen alınan cümle", "TIRNAK + ATIF + SAYFA", TURUNCU),
             ("Başkasının şekli ya da tablosu", "ATIF VER, GEREKİRSE İZİN AL", TURUNCU), ("Alanda herkesin bildiği genel bilgi", "ATIF GEREKMEZ", GRI),
             ("Kendi verin, kendi bulgun, kendi yorumun", "ATIF GEREKMEZ", GRI)]
    for i, (durum, sonuc, renk) in enumerate(satir):
        y = 0.78 - i * 0.175
        kutu(ax, 0.02, y, 0.52, 0.12, durum, "#F3F4F6", boy=23, yazi="#111111")
        ok(ax, 0.565, y + 0.06, 0.60, y + 0.06)
        kutu(ax, 0.62, y, 0.36, 0.12, sonuc, renk, boy=21)
    sekil("3.4", "atif-karari")
    ns = oturum("3.4", "atif-denetimi", """
import re
from kaynaklar import NOTLAR
paragraf = ("İnsan elinin düzgün hareketi için bir ölçüt önerilmiştir (Flash vd., 1985). "
            "Benzetim motorları çok eklemli sistemleri hızlı çözer (Todorov vd., 2012). "
            "Servis robotlarında bardak taşıma yaygın bir görevdir (Yılmaz, 2020).")
metindeki = re.findall(r"\\(([^()]+?), (\\d{4})\\)", paragraf)
metindeki
kaynakca = {(n["yazar"].split(",")[0] + " vd.", str(n["yil"])) for n in NOTLAR}
kaynakcada_yok = [a for a in metindeki if a not in kaynakca]
kaynakcada_yok
metinde_gecmeyen = sorted(k for k in kaynakca if k not in metindeki)
metinde_gecmeyen
""")
    ns = oturum("3.4", "ortusme", """
def ortusme(a, b):
    a, b = set(a.lower().split()), set(b.lower().split())
    return round(len(a & b) / len(a | b), 2)
kaynak = "ivmenin değişimini en aza indiren model elin yolunu iyi öngörüyor"
yakin = "ivmenin değişimini en aza indiren model elin izlediği yolu iyi öngörüyor"
kendi = "el, sarsıntıyı azaltan bir yol izliyor ve model bu yolu doğru tahmin ediyor"
ortusme(kaynak, yakin)
ortusme(kaynak, kendi)
""", ns)
    olc(d3_4_metindeki=len(ns["metindeki"]), d3_4_kaynakcada_yok=len(ns["kaynakcada_yok"]), d3_4_metinde_gecmeyen=len(ns["metinde_gecmeyen"]),
        d3_4_ortusme_yakin=ns["ortusme"](ns["kaynak"], ns["yakin"]), d3_4_ortusme_kendi=ns["ortusme"](ns["kaynak"], ns["kendi"]))


if __name__ == "__main__":
    ns = ders_3_1(); ns = ders_3_2(ns); ders_3_3(ns); ders_3_4()
    print("hafta 3 tamam")
