"""Tez Yazımı: Sorudan Savunmaya — örnek araştırmanın kaynakları ve okuma notları (Hafta 1).
Dört kaynak gerçektir (yazar, yıl, başlık, yayın yeri); not alanları kaynağın kendi özetinden kendi cümlemizle yazıldı, alıntı değildir.
Öğrenci aynı alanları kendi konusundaki kaynaklarla doldurur."""

NOTLAR = [
    dict(anahtar="flash1985", yazar="Flash, T., & Hogan, N.", yil=1985,
         baslik="The coordination of arm movements: An experimentally confirmed mathematical model",
         yayin="Journal of Neuroscience",
         soru="İnsan eli bir noktadan ötekine giderken hangi yolu izler?",
         yontem="düzlemde kol hareketi deneyleri ve matematiksel model",
         bulgu="ivmenin değişimini en aza indiren model elin yolunu iyi öngörüyor",
         sinir="düzlemde, yük taşımayan kol hareketleri",
         katki="taşımanın düzgünlüğünü ölçmek için ölçüt fikri",
         veri="insan deneyi", insansi_robot=False, duzgunluk_olcutu=True, evre_karsilastirmasi=False),
    dict(anahtar="todorov2012", yazar="Todorov, E., Erez, T., & Tassa, Y.", yil=2012,
         baslik="MuJoCo: A physics engine for model-based control",
         yayin="IEEE/RSJ International Conference on Intelligent Robots and Systems",
         soru="Model tabanlı kontrol için hızlı ve doğru fizik benzetimi nasıl kurulur?",
         yontem="genelleştirilmiş koordinatlar ve temas çözücüsü olan benzetim motoru",
         bulgu="çok eklemli sistemler gerçek zamandan hızlı benzetilebiliyor",
         sinir="benzetim sonucu, gerçek ölçüm değil",
         katki="benzetim verisinin neyi gösterip neyi göstermediğini tartışmak",
         veri="benzetim motoru", insansi_robot=False, duzgunluk_olcutu=False, evre_karsilastirmasi=False),
    dict(anahtar="mittal2023", yazar="Mittal, M., Yu, C., Yu, Q., et al.", yil=2023,
         baslik="Orbit: A unified simulation framework for interactive robot learning environments",
         yayin="IEEE Robotics and Automation Letters",
         soru="Robot öğrenmesi için farklı görevler tek bir benzetim çerçevesinde nasıl toplanır?",
         yontem="grafik işlemcide koşan benzetim üzerinde ortak görev arayüzü",
         bulgu="çok sayıda robot ve görev aynı çerçevede koşulabiliyor",
         sinir="çerçeve tanıtımı; tek bir görevin ayrıntılı ölçümü yok",
         katki="örnek kaydın üretildiği benzetim ortamını tanımlamak",
         veri="benzetim çerçevesi", insansi_robot=False, duzgunluk_olcutu=False, evre_karsilastirmasi=False),
    dict(anahtar="black2024", yazar="Black, K., Brown, N., Driess, D., et al.", yil=2024,
         baslik="π0: A vision-language-action flow model for general robot control",
         yayin="arXiv:2410.24164",
         soru="Tek bir model farklı robotlarda farklı görevleri yapabilir mi?",
         yontem="görüntü ve dil modeli üzerine eylem üreten bir katman; çok robotlu veriyle eğitim",
         bulgu="çamaşır katlama gibi uzun görevler gerçek robotlarda gösterildi",
         sinir="başarı görev tamamlama ile ölçülüyor; taşınan nesnenin hareketi ölçülmüyor",
         katki="robotun bir görevi gösterimden nasıl öğrendiğinin arka planı",
         veri="gerçek robot", insansi_robot=False, duzgunluk_olcutu=False, evre_karsilastirmasi=False),
]

BIZIM = dict(anahtar="bu çalışma", veri="benzetim kaydı", insansi_robot=True, duzgunluk_olcutu=True, evre_karsilastirmasi=True)
