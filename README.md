# Tez Yazımı: Sorudan Savunmaya — kurs dosyaları

Forenly AI Academy'deki **Tez Yazımı: Sorudan Savunmaya** kursunun örnek araştırma dosyaları. Derslerde ekranda gördüğünüz her Python oturumu, tablo ve şekil bu betiklerle üretildi.

Kursu izlemek için program yazmanız gerekmez. Bu dosyalar, örnek araştırmanın adımlarını kendi bilgisayarınızda yinelemek isteyenler içindir.

## Gerekenler

- **Python 3.10 veya üstü**, `numpy` (2.0 ya da üstü) ve `matplotlib`. Hepsi ücretsizdir.
- Kurulum: `python -m pip install -r requirements.txt`
- Bilgisayarınıza kurmak istemezseniz tarayıcıda çalışan bir not defterine (ör. Google Colab) bu klasörü yükleyip aynı betikleri çalıştırabilirsiniz.

## Nasıl çalıştırılır

1. Bu depoyu indirin (Code → Download ZIP) ve klasörde bir terminal açın.
2. Haftaları sırayla çalıştırın: `python hafta1.py`, `python hafta2.py`, `python hafta3.py`, `python hafta4.py`. Dördüncü hafta, üçüncü haftanın yazdığı `cikti/tez_iskeleti.md` dosyasını okur.
3. Betikler çalışınca `ekran/<ders>/` klasöründe şekiller (`.png`) ve Python oturum kayıtları (`.txt`), `cikti/` klasöründe tablolar, kökte de ölçülen sayılar (`OLCUMLER.json`) oluşur.
4. İsteğe bağlı: `python komut_ciz.py` oturum kayıtlarını derslerdeki gibi resme çizer (Pillow gerekir).

## Sonucunuzu karşılaştırın

`beklenen/OLCUMLER.json` ekibimizin 2026-10-08 koşumunda ölçtüğü sayılardır; `beklenen/ekran/` aynı koşumun şekilleri ve oturum kayıtlarıdır, `beklenen/cikti/` ise tablolar.

## Dosyalar

| Dosya | İçerik |
|---|---|
| `ortak.py` | Kaydı okuma (`kayit`), yumuşatma (`yumusat`), ölçüm yazma, oturum kaydı ve şekil kaydetme |
| `arac.py` | Örnek araştırmanın ortak hesapları: evrelere ayırma, evre özeti, karar kuralı; çizim yardımcıları |
| `kaynaklar.py` | Örnek araştırmanın dört kaynağı ve okuma notları |
| `iskelet.py`, `cizelge.py` | Örnek tez iskeleti ve örnek düzeltme çizelgesi |
| `hafta1.py` | Soru ve kaynak: soru hunisi, arama cümlesi, not kartı, kaynak çizelgesi, kaynakça |
| `hafta2.py` | Yöntem ve veri: yöntem kartı, değişken tablosu, eşik ve yumuşatma denemesi, veri künyesi, çözümleme planı |
| `hafta3.py` | Bulgu ve yazım: evre özeti, sağlamlık denetimi, Şekil 1, Tablo 1, bulgu cümlesi, atıf denetimi |
| `hafta4.py` | Düzen ve savunma: başlık ve gönderme denetimi, özet, düzeltme çizelgesi, sürüm farkı, süre bütçesi |
| `komut_ciz.py` | Oturum kayıtlarını resme çizer (isteğe bağlı) |
| `veri/cay_servisi_kaydi.csv` | Çay servisi benzetim kaydı: zaman, kol eklem açıları, bardağın konumu × 5666 örnek (saniyede 50) |

## Veri ve kaynaklar hakkında

Robot verisi **benzetim kaydıdır**, gerçek robot ölçümü değildir. Kayıt, Forenly AI'nin [kafe projesinde](https://forenly.ai/work/cafe) Unitree G1 insansı robotunun çay servisini benzetimde yaptığı bir bölümden alınmıştır. Örnek araştırmanın bulgusu yalnız bu kayıt için geçerlidir.

`kaynaklar.py` içindeki dört kaynak gerçek yayınlardır; not alanları kendi cümlemizle yazılmıştır. Tarama günlüğündeki sayılar, düzeltme çizelgesindeki yorumlar, süre bütçesi, başlık adayları ve Ders 3.4'teki "(Yılmaz, 2020)" atfı **ÖRNEKTİR**; sonuncusu, var olmayan bir kaynağın nasıl yakalandığını göstermek için bilerek uydurulmuştur.

Kurs yöntem öğretir; tezinizi sizin yerinize yazmaz. Biçim kuralları için kendi enstitünüzün yazım kılavuzu geçerlidir.
