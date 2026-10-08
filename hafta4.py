"""Hafta 4 · Düzen ve Savunma — Ders 4.1–4.4.
  python hafta4.py   → ekran/4.x/*.txt + *.png, OLCUMLER.json (d4_*)   (hafta3.py'den sonra koşulur: cikti/tez_iskeleti.md)"""
import numpy as np
import matplotlib.pyplot as plt
from ortak import olc, oturum, sekil, LAB
from arac import evre_verisi, evre_ozeti, kutu, ok, bos_eksen, tr, TURUNCU, MAVI, YESIL, MOR, GRI, EVRE_AD, EVRE_RENK


def ders_4_1():
    """Biçim ve düzen: tezin parçaları, başlık düzeni denetimi, şekil ve tablo göndermeleri."""
    fig, ax = bos_eksen("Bir tezin parçaları ve sırası")
    on = ["Kapak", "Özet", "İçindekiler", "Şekil ve tablo\nlisteleri"]
    ana = ["Giriş", "Yöntem", "Bulgular", "Tartışma"]
    son = ["Kaynakça", "Ekler"]
    for baslik, liste, renk, y in [("Ön bölüm", on, GRI, 0.70), ("Ana metin", ana, TURUNCU, 0.42), ("Son bölüm", son, MAVI, 0.14)]:
        ax.text(0.02, y + 0.09, baslik, fontsize=26, weight="bold", va="center")
        for i, ad in enumerate(liste):
            kutu(ax, 0.22 + i * 0.195, y, 0.145, 0.18, ad, renk, boy=22)
    sekil("4.1", "tez-parcalari")
    ns = oturum("4.1", "baslik-denetimi", """
import pathlib
satirlar = pathlib.Path("cikti/tez_iskeleti.md").read_text(encoding="utf-8").splitlines()
duzeyler = [len(s) - len(s.lstrip("#")) for s in satirlar]
len(satirlar), max(duzeyler)
atlama = [satirlar[i] for i in range(1, len(duzeyler)) if duzeyler[i] > duzeyler[i - 1] + 1]
atlama
bozuk = satirlar[:5] + ["#### 1.3.1.1 Ayrıntı"] + satirlar[5:]
d2 = [len(s) - len(s.lstrip("#")) for s in bozuk]
[bozuk[i] for i in range(1, len(d2)) if d2[i] > d2[i - 1] + 1]
""")
    ns = oturum("4.1", "gonderme-denetimi", """
import re
metin = ("Evre başına ivme Tablo 1'de verilmiştir. Evreler arasındaki fark Şekil 1'de görülür. "
         "Sağlamlık denetimi yanıtı değiştirmemiştir.")
var_olan = ["Tablo 1", "Şekil 1", "Şekil 2"]
anilan = re.findall(r"(?:Tablo|Şekil) \\d+", metin)
anilan
[ad for ad in var_olan if ad not in anilan]
""", ns)
    olc(d4_1_baslik=len(ns["satirlar"]), d4_1_duzey=max(ns["duzeyler"]), d4_1_atlama=len(ns["atlama"]), d4_1_anilmayan=1)


def ders_4_2():
    """Özet ve başlık: dört parçalı özet (sayılar veriden), sözcük sayısı, başlık adayları."""
    fig, ax = bos_eksen("Özetin dört parçası")
    parca = [("Amaç", "Neyi, neden\naraştırdım?", MAVI), ("Yöntem", "Hangi veriyle,\nnasıl?", YESIL), ("Bulgu", "Sayılarıyla\nne buldum?", TURUNCU), ("Sonuç", "Bu ne demek,\nsınırı ne?", MOR)]
    for i, (ad, soru, renk) in enumerate(parca):
        x = 0.02 + i * 0.25
        kutu(ax, x, 0.58, 0.20, 0.22, ad, renk, boy=30)
        kutu(ax, x, 0.26, 0.20, 0.24, soru, "#F3F4F6", boy=24, yazi="#111111")
        if i < 3:
            ok(ax, x + 0.225, 0.69, x + 0.245, 0.69)
    ax.text(0.5, 0.12, "Her parça bir ya da iki cümle · özette atıf, şekil ve kısaltma yok", fontsize=24, ha="center")
    sekil("4.2", "ozet-parcalari")
    ns = oturum("4.2", "ozet", """
import textwrap
from arac import evre_verisi, evre_ozeti
t, hiz, ivme, evre = evre_verisi()
o = evre_ozeti(ivme, evre)
def tr(x):
    return f"{x:.2f}".replace(".", ",")
a, b, c = [tr(o[ad]["ortalama"]) for ad in ["taşıma", "kaldırma", "bırakma"]]
ozet = {
    "amaç": "Bu çalışma, insansı bir robotun taşıdığı bardağın "
            "taşımanın hangi evresinde en çok ivmelendiğini inceler.",
    "yöntem": f"Çay servisi benzetim kaydı ({len(t)} örnek) üç evreye "
              "ayrılmış, evre başına ivme karşılaştırılmıştır.",
    "bulgu": f"Ortalama ivme taşımada {a}, kaldırmada {b} "
             f"ve bırakmada {c} m/s² bulunmuştur.",
    "sonuç": "Bardak en çok taşıma evresinde ivmelenmektedir; "
             "bulgu tek bir benzetim kaydıyla sınırlıdır.",
}
for ad, cumle in ozet.items():
    print(textwrap.fill(f"[{ad}] {cumle}", 66, subsequent_indent="   "))
sum(len(c.split()) for c in ozet.values())
""")
    ns = oturum("4.2", "baslik-adaylari", """
adaylar = [
    "İnsansı Robotlar Üzerine Bir İnceleme",
    "İnsansı Robotla Bardak Taşımada Evrelere Göre İvme: Bir Benzetim Çözümlemesi",
    "Bardak Taşıma",
]
gerekli = ["insansı robot", "ivme", "benzetim"]
for a in adaylar:
    eksik = [g for g in gerekli if g not in a.lower().replace("i̇", "i")]
    print(f"{len(a.split()):2d} sözcük  eksik: {eksik}")
    print("   " + a)
""", ns)
    olc(d4_2_ozet_sozcuk=sum(len(c.split()) for c in ns["ozet"].values()), d4_2_baslik_aday=len(ns["adaylar"]))


def ders_4_3():
    """Danışmanla düzeltme döngüsü: döngü, düzeltme çizelgesi, iki sürüm arasındaki fark."""
    fig, ax = bos_eksen("Düzeltme döngüsü")
    adim = [("Taslağı\ngönder", MAVI, 0.05, 0.60), ("Yorumları\ntopla", YESIL, 0.40, 0.60), ("Düzeltme\nçizelgesine yaz", TURUNCU, 0.75, 0.60),
            ("Düzelt ve\nişaretle", MOR, 0.75, 0.18), ("Çizelgeyle birlikte\nyeni sürümü gönder", GRI, 0.30, 0.18)]
    for ad, renk, x, y in adim:
        kutu(ax, x, y, 0.22 if "Çizelgeyle" not in ad else 0.32, 0.22, ad, renk, boy=24)
    ok(ax, 0.29, 0.71, 0.385, 0.71); ok(ax, 0.64, 0.71, 0.735, 0.71); ok(ax, 0.86, 0.575, 0.86, 0.425); ok(ax, 0.735, 0.29, 0.645, 0.29); ok(ax, 0.30, 0.425, 0.17, 0.575)
    sekil("4.3", "duzeltme-dongusu")
    ns = oturum("4.3", "duzeltme-cizelgesi", """
from cizelge import cizelge
len(cizelge)
for no, yorum, yapilan, durum in cizelge:
    print(f"{no}  {durum:10s} {yorum}")
    print(f"              → {yapilan or '—'}")
from collections import Counter
Counter(durum for _, _, _, durum in cizelge)
""")
    ns = oturum("4.3", "surum-farki", """
import difflib
onceki = ["Bardak en çok taşıma evresinde ivmeleniyor.",
          "Şekil 1 evreleri gösterir.",
          "Sonuç bütün robotlar için geçerlidir."]
yeni = ["Bardak en çok taşıma evresinde ivmeleniyor.",
        "Şekil 1 evre başına ivmeyi m/s² olarak gösterir.",
        "Sonuç yalnız bu benzetim kaydı için geçerlidir."]
fark = difflib.unified_diff(onceki, yeni, "tez-v3.md", "tez-v4.md", lineterm="", n=0)
for satir in fark:
    print(satir)
""", ns)
    say = ns["Counter"](d for _, _, _, d in ns["cizelge"])
    olc(d4_3_yorum=len(ns["cizelge"]), d4_3_bitti=say["bitti"], d4_3_yanitlandi=say["yanıtlandı"], d4_3_bekliyor=say["bekliyor"])


def ders_4_4():
    """Savunma sunumu: beş slayt, süre bütçesi, tek bakışta tez."""
    fig, ax = bos_eksen("Beş slaytlık savunma")
    slayt = [("1", "Soru", "Neyi, neden\nsordum?", MAVI), ("2", "Yöntem", "Hangi veri,\nhangi ölçüm?", YESIL), ("3", "Bulgu", "Tek şekil,\ntek sayı", TURUNCU),
             ("4", "Sınır", "Neyi\nsöyleyemem?", MOR), ("5", "Katkı", "Ne eklendi,\nsırada ne var?", GRI)]
    for i, (no, ad, soru, renk) in enumerate(slayt):
        x = 0.015 + i * 0.198
        kutu(ax, x + 0.01, 0.60, 0.14, 0.22, f"{no} · {ad}", renk, boy=26)
        kutu(ax, x + 0.01, 0.28, 0.14, 0.24, soru, "#F3F4F6", boy=22, yazi="#111111")
    ax.text(0.5, 0.13, "Her slaytta tek ileti · ayrıntı yedek slaytlarda", fontsize=24, ha="center")
    sekil("4.4", "bes-slayt")
    ns = oturum("4.4", "sure-butcesi", """
toplam_dakika = 10
pay = {"Soru": 0.15, "Yöntem": 0.20, "Bulgu": 0.35, "Sınır": 0.15, "Katkı": 0.15}
round(sum(pay.values()), 2)
for ad, oran in pay.items():
    saniye = round(toplam_dakika * 60 * oran)
    print(f"{ad:8s} {saniye // 60} dk {saniye % 60:02d} sn")
olasi_sorular = [
    "Evre sınırını neden böyle seçtiniz?",
    "Sonuç gerçek robotta da geçerli mi?",
    "Yumuşatma penceresi değişince ne oluyor?",
]
for i, soru in enumerate(olasi_sorular, 1):
    print(i, soru)
""")
    t, hiz, ivme, evre = evre_verisi(); o = evre_ozeti(ivme, evre)
    fig = plt.figure(); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.94, "Tek bakışta tez", fontsize=30, ha="center", weight="bold")
    kutu(ax, 0.03, 0.70, 0.44, 0.16, "SORU\nBardak, taşımanın hangi evresinde\nen çok ivmeleniyor?", MAVI, boy=21)
    kutu(ax, 0.03, 0.48, 0.44, 0.16, "YÖNTEM\nBenzetim kaydı · üç evre\nevre başına ortalama ivme", YESIL, boy=21)
    kutu(ax, 0.03, 0.26, 0.44, 0.16, "SINIR\nTek benzetim kaydı\ngerçek robot ölçümü değil", MOR, boy=21)
    kutu(ax, 0.03, 0.04, 0.44, 0.16, f"KATKI\nTaşıma evresi, kaldırmanın\nyaklaşık {round(o['taşıma']['ortalama'] / o['kaldırma']['ortalama'])} katı ivme", GRI, boy=21)
    ic = fig.add_axes([0.58, 0.14, 0.38, 0.64])
    ort = [o[a]["ortalama"] for a in EVRE_AD]
    ic.bar(range(3), ort, 0.55, color=EVRE_RENK, alpha=0.8)
    for i in range(3):
        ic.text(i, ort[i] + 0.012, tr(ort[i]), ha="center", fontsize=26, weight="bold")
    ic.set_xticks(range(3)); ic.set_xticklabels(EVRE_AD, fontsize=24); ic.set_ylabel("ortalama ivme (m/s²)"); ic.set_ylim(0, max(ort) * 1.2)
    ic.set_title("BULGU", fontsize=24, color=TURUNCU, weight="bold")
    yol = LAB / "ekran/4.4/tek-bakista-tez.png"; fig.savefig(yol, dpi=100); plt.close(fig)
    olc(d4_4_slayt=len(slayt), d4_4_dakika=ns["toplam_dakika"], d4_4_soru=len(ns["olasi_sorular"]),
        d4_4_kat=round(o["taşıma"]["ortalama"] / o["kaldırma"]["ortalama"]))


if __name__ == "__main__":
    ders_4_1(); ders_4_2(); ders_4_3(); ders_4_4()
    print("hafta 4 tamam")
