"""Hafta 2 · Yöntem ve Veri — Ders 2.1–2.4.
  python hafta2.py   → ekran/2.x/*.txt + *.png, cikti/veri_kunyesi.json, OLCUMLER.json (d2_*)"""
import numpy as np
import matplotlib.pyplot as plt
from ortak import olc, oturum, sekil, LAB
from arac import evre_verisi, evre_ozeti, kutu, ok, bos_eksen, tr, TURUNCU, MAVI, YESIL, MOR, GRI, EVRE_AD, EVRE_RENK

(LAB / "cikti").mkdir(exist_ok=True)


def ders_2_1():
    """Soruya uygun yöntem: soru türü → araştırma deseni; örnek araştırmanın deseni ve akışı."""
    fig, ax = bos_eksen("Sorunun türü yöntemi seçer")
    satir = [("Ne kadar, nasıl dağılıyor?", "Betimleyici", "özet ve dağılım", GRI),
             ("Gruplar arasında fark var mı?", "Karşılaştırmalı", "grupları aynı ölçüyle karşılaştırma", TURUNCU),
             ("Biri değişince öteki değişiyor mu?", "İlişkisel", "iki ölçümü birlikte izleme", MAVI),
             ("Bunu değiştirirsem ne olur?", "Deneysel", "tek şeyi değiştirip sonucu ölçme", YESIL),
             ("İnsanlar bunu nasıl yaşıyor?", "Nitel", "görüşme, gözlem, belge", MOR)]
    for j, b in enumerate(["soru", "desen", "ne yapılır"]):
        ax.text([0.02, 0.47, 0.70][j], 0.93, b, fontsize=24, weight="bold", va="center")
    for i, (soru, desen, yapilan, renk) in enumerate(satir):
        y = 0.76 - i * 0.175
        ax.text(0.02, y + 0.06, soru, fontsize=24, va="center")
        kutu(ax, 0.47, y, 0.19, 0.12, desen, renk, boy=23)
        ax.text(0.70, y + 0.06, yapilan, fontsize=22, va="center")
    sekil("2.1", "soru-ve-desen")

    ns = oturum("2.1", "yontem-karti", """
yontem = {
    "soru": "Bardak, taşımanın hangi evresinde en çok ivmeleniyor?",
    "soru_turu": "gruplar arasında fark var mı",
    "desen": "karşılaştırmalı, nicel",
    "gruplar": "kaldırma, taşıma, bırakma",
    "veri": "var olan benzetim kaydı (yeni veri toplanmıyor)",
    "neden_deneysel_degil": "hiçbir şeyi değiştirmiyoruz, yalnız ölçüyoruz",
}
for ad, deger in yontem.items():
    print(f"{ad:22s} {deger}")
""")
    fig, ax = bos_eksen("Örnek araştırmanın akışı: kayıttan yanıta dört adım")
    adim = [("Benzetim kaydı", "bardağın konumu\n113,3 s", GRI), ("Evrelere ayır", "kaldırma · taşıma\nbırakma", MAVI),
            ("İvmeyi hesapla", "her örnek için\nm/s²", YESIL), ("Karşılaştır", "evre başına özet\nkarar kuralı", TURUNCU)]
    for i, (ad, alt, renk) in enumerate(adim):
        x = 0.02 + i * 0.25
        kutu(ax, x, 0.52, 0.20, 0.20, ad, renk, boy=24)
        kutu(ax, x, 0.24, 0.20, 0.20, alt, "#F3F4F6", boy=22, yazi="#111111")
        if i < 3:
            ok(ax, x + 0.225, 0.62, x + 0.245, 0.62)
    sekil("2.1", "arastirma-akisi")
    olc(d2_1_desen=len(satir), d2_1_adim=len(adim))


def ders_2_2():
    """Değişkenler ve ölçüm: işlemsel tanım; tanımdaki seçimlerin (eşik, yumuşatma) sonuca etkisi."""
    ns = oturum("2.2", "degisken-tablosu", """
degiskenler = [
    ("evre", "gruplayan", "üç evre", "yatay hız 0,05 m/s üstü: taşıma"),
    ("ivme", "ölçülen", "m/s²", "yumuşatılmış konumun ikinci türevi"),
    ("yumuşatma", "sabit tutulan", "0,5 s", "25 örnekte hareketli ortalama"),
]
for ad, tur, birim, tanim in degiskenler:
    print(f"{ad:10s} {tur:14s} {birim:8s} {tanim}")
""")
    ns = oturum("2.2", "esik-denemesi", """
from arac import evre_verisi, evre_ozeti
for esik in [0.03, 0.05, 0.08]:
    t, hiz, ivme, evre = evre_verisi(esik=esik)
    sure = [round(float((evre == i).sum() / 50), 1) for i in range(3)]
    ort = evre_ozeti(ivme, evre)["taşıma"]["ortalama"]
    print(f"eşik {esik:.2f} m/s  evre süreleri {sure} s  taşıma ortalama ivme {ort} m/s²")
""")
    pencereler = [5, 13, 25, 51, 101]
    enb, ort = [], []
    for n in pencereler:
        t, hiz, ivme, evre = evre_verisi(pencere=n)
        o = evre_ozeti(ivme, evre)["taşıma"]; enb.append(o["en_buyuk"]); ort.append(o["ortalama"])
    fig, ax = plt.subplots()
    x = np.arange(len(pencereler))
    ax.plot(x, enb, "o-", color=TURUNCU, ms=14, label="taşıma evresinde en büyük ivme")
    ax.plot(x, ort, "s-", color=MAVI, ms=14, label="taşıma evresinde ortalama ivme")
    for i in range(len(x)):
        ax.text(x[i], enb[i] + max(enb) * 0.04, tr(enb[i]), ha="center", fontsize=22, color=TURUNCU, weight="bold")
        ax.text(x[i], ort[i] - max(enb) * 0.07, tr(ort[i]), ha="center", fontsize=22, color=MAVI, weight="bold")
    ax.axvspan(1.6, 2.4, color=YESIL, alpha=0.12); ax.text(2, max(enb) * 0.55, "seçilen\ntanım", ha="center", color=YESIL, fontsize=22, weight="bold")
    ax.set_xticks(x); ax.set_xticklabels([f"{n} örnek\n{tr(n / 50, 2)} s" for n in pencereler])
    ax.set_xlabel("yumuşatma penceresi"); ax.set_ylabel("ivme (m/s²)"); ax.set_ylim(-max(enb) * 0.12, max(enb) * 1.15); ax.legend(loc="upper right")
    ax.set_title("Ölçüm tanımı sonucu değiştirir: yumuşatma penceresi ve ivme · benzetim kaydı")
    sekil("2.2", "yumusatma-etkisi")
    esik = {}
    for e in [0.03, 0.05, 0.08]:
        t, hiz, ivme, evre = evre_verisi(esik=e)
        esik[str(e)] = dict(sure=[round(float((evre == i).sum() / 50), 1) for i in range(3)], tasima_ort=evre_ozeti(ivme, evre)["taşıma"]["ortalama"])
    olc(d2_2_esik=esik, d2_2_pencere=pencereler, d2_2_tasima_max=enb, d2_2_tasima_ort=ort)


def ders_2_3():
    """Veri toplama ve etik: veriyi tanımak, ham veriyi korumak, etik karar ağacı."""
    ns = oturum("2.3", "veri-denetimi", """
import numpy as np
from ortak import kayit
k = kayit()
t = k["zaman_s"]
len(t), len(k)
adim = np.diff(t)
round(float(adim.min()), 3), round(float(adim.max()), 3)
eksik = {ad: int(np.isnan(k[ad]).sum()) for ad in k}
sum(eksik.values())
round(float(k["bardak_z_m"].min()), 3), round(float(k["bardak_z_m"].max()), 3)
""")
    ns = oturum("2.3", "veri-kunyesi", """
import hashlib, json, pathlib
dosya = pathlib.Path("veri/cay_servisi_kaydi.csv")
iz = hashlib.sha256(dosya.read_bytes()).hexdigest()
kunye = {
    "dosya": dosya.name,
    "tur": "benzetim kaydı (gerçek robot ölçümü değil)",
    "kaynak": "Forenly AI, G1 insansı robot çay servisi benzetimi",
    "ornek_sayisi": len(t),
    "ornekleme": "saniyede 50 örnek",
    "kisisel_veri": "yok",
    "parmak_izi": iz[:16],
}
metin = json.dumps(kunye, ensure_ascii=False, indent=1)
uzunluk = pathlib.Path("cikti/veri_kunyesi.json").write_text(metin, encoding="utf-8")
for ad, deger in kunye.items():
    print(f"{ad:14s} {deger}")
""", ns)
    fig, ax = bos_eksen("Veri toplamadan önce üç soru")
    soru = [("İnsanlardan veri\ntoplanıyor mu?", "Evet → etik kurul onayı\nveri toplamadan önce", "Örnek araştırma:\nhayır, benzetim kaydı", MAVI),
            ("Kişisel veri\nvar mı?", "Evet → aydınlatılmış onam\nve kimliksizleştirme", "Örnek araştırma:\nkişisel veri yok", YESIL),
            ("Veri başkasına\nmı ait?", "Evet → kullanım izni\nve kaynağın belirtilmesi", "Örnek araştırma:\nkaynak künyede yazılı", TURUNCU)]
    for i, (s, evet, biz, renk) in enumerate(soru):
        x = 0.03 + i * 0.33
        kutu(ax, x, 0.68, 0.26, 0.20, s, renk, boy=24)
        kutu(ax, x, 0.38, 0.26, 0.22, evet, "#F3F4F6", boy=21, yazi="#111111")
        kutu(ax, x, 0.08, 0.26, 0.22, biz, "#FFF7ED", boy=21, yazi="#111111")
    sekil("2.3", "etik-sorular")
    olc(d2_3_ornek=len(ns["t"]), d2_3_sutun=len(ns["k"]), d2_3_adim_min=float(ns["adim"].min()), d2_3_adim_max=float(ns["adim"].max()),
        d2_3_eksik=sum(ns["eksik"].values()), d2_3_z_min=float(ns["k"]["bardak_z_m"].min()), d2_3_z_max=float(ns["k"]["bardak_z_m"].max()))


def ders_2_4():
    """Çözümleme planı: veri çözümlenmeden önce yazılan plan, boş tablo ve karar kuralı."""
    ns = oturum("2.4", "cozumleme-plani", """
plan = {
    "olcu": "evre başına ivmenin ortalaması",
    "ek_olculer": "yüzde doksan beşlik değer ve en büyük değer",
    "karsilastirma": "üç evrenin ortalaması yan yana",
    "karar_kurali": "en büyük ortalama ikinciden en az yüzde on büyükse o evre",
    "saglamlik": "eşik 0,03 ve 0,08 ile yinelenir, yanıt değişmemeli",
    "yazilmayacak": "başka robotlar ve gerçek robot için genelleme",
}
for ad, deger in plan.items():
    print(f"{ad:14s} {deger}")
""")
    fig, ax = bos_eksen("Boş tablo: veriye bakmadan önce çizilir")
    bas = ["evre", "örnek\nsayısı", "ortalama\n(m/s²)", "yüzde 95\n(m/s²)", "en büyük\n(m/s²)"]
    x0 = [0.10, 0.32, 0.50, 0.68, 0.86]
    for j, b in enumerate(bas):
        ax.text(x0[j], 0.86, b, fontsize=24, weight="bold", ha="center", va="center")
    ax.plot([0.02, 0.98], [0.76, 0.76], color="#111111", lw=2)
    for i, ad in enumerate(EVRE_AD):
        y = 0.62 - i * 0.18
        ax.text(x0[0], y, ad, fontsize=26, ha="center", va="center", color=EVRE_RENK[i], weight="bold")
        for j in range(1, 5):
            ax.text(x0[j], y, "?", fontsize=30, ha="center", va="center", color=GRI)
    ax.plot([0.02, 0.98], [0.16, 0.16], color="#111111", lw=2)
    ax.text(0.5, 0.07, "Karar kuralı: en büyük ortalama ikinciden en az yüzde on büyükse o evre", fontsize=22, ha="center", va="center")
    sekil("2.4", "bos-tablo")
    ns = oturum("2.4", "karar-kurali", """
from arac import karar
ornek_a = {"kaldırma": 0.20, "taşıma": 0.90, "bırakma": 0.10}
karar(ornek_a)
ornek_b = {"kaldırma": 0.50, "taşıma": 0.52, "bırakma": 0.10}
karar(ornek_b)
ornek_c = {"kaldırma": 0.50, "taşıma": 0.56, "bırakma": 0.10}
karar(ornek_c)
""", ns)
    olc(d2_4_plan_madde=len(ns["plan"]), d2_4_karar_ornek=[ns["karar"](ns[f"ornek_{h}"]) for h in "abc"])


if __name__ == "__main__":
    ders_2_1(); ders_2_2(); ders_2_3(); ders_2_4()
    print("hafta 2 tamam")
