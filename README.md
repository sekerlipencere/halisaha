# Halı Saha Maçları Hareket Isı Haritası Oluşturma Projesi

Bu proje, hali saha maçlarının video kayıtlarını kullanarak hareket ısı haritaları oluşturmayı amaçlar. Oluşturulan ısı haritaları, maç sırasında hangi bölgelerin daha fazla hareketli olduğunu görsel olarak gösterir. Bu bilgi, takımların performansını değerlendirmek ve taktiksel analiz yapmak için kullanılabilir.

## Nasıl Çalışır?

1. **Video Yüklenmesi:** İlk adımda, hali saha maçının video kaydı projeye yüklenir.
2. **Isı Haritası Oluşturma:** Video kaydı işlenerek her bir karedeki hareket yoğunluğu hesaplanır ve bir ısı haritası oluşturulur.
3. **Görselleştirme ve Analiz:** Oluşturulan ısı haritası, matplotlib kütüphanesi kullanılarak görselleştirilir. Elde edilen sonuçlar, takım performansının değerlendirilmesi ve taktiksel analiz için kullanılabilir.

## Proje Yapısı


- `main.py`: Isı haritası oluşturma işlemlerini gerçekleştiren Python betiği.
- `README.md`: Proje hakkında genel bilgilerin ve kullanım talimatlarının bulunduğu dosya.
- `colab.ipynb` : Otomatik kurulumlu colab sayfası.
## Örnek Isı Haritası
![Isı Haritası](https://github.com/PolarBear110/halisaha/blob/main/%C4%B1ns_map.png)
## Gereksinimler

- Python 3.x
- OpenCV
- NumPy
- Matplotlib
- tqdm

## Kurulum
- [![Colabta Aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PolarBear110/halisaha/blob/main/colab.ipynb)

- ```pip install opencv-python matplotlib numpy```
  
- ```git clone https://github.com/sekerlipencere/halisaha.git```
  
- ```cd halisaha```

- ```python main.py```
