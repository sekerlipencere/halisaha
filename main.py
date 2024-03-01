import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import time

def create_heatmap(video_path, save_path_1, save_path_2=None):
    # Videoyu yükleyin
    cap = cv2.VideoCapture(video_path)

    # Değişim miktarlarını toplamak için bir matris oluştur
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    heat_map = np.zeros((height, width), dtype=np.float32)

    # İlk frame'i oku
    ret, prev_frame = cap.read()
    prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    tqdm_bar = tqdm(total=frame_count, desc="Isı haritası oluşturuluyor", leave=False)

    while True:
        # Sonraki frame'i oku
        ret, frame = cap.read()
        if not ret:
            break

        # Frame'i griye çevir
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Frame'ler arasındaki farkı hesapla
        diff = cv2.absdiff(prev_frame, gray)

        # Farkı ısı haritasına ekle
        heat_map += diff

        # Şimdiki frame'i bir sonraki iterasyon için sakla
        prev_frame = gray

        tqdm_bar.update(1)

    tqdm_bar.close()

    # Heatmap'i normalize edelim ve bir eşik değeri belirleyelim
    # Burada en yüksek %1'lik değerleri vurgulayacak şekilde ayar yapıyoruz
    max_val = np.max(heat_map)
    threshold_high = np.percentile(heat_map, 99)  # En yüksek %1
    threshold_low = np.percentile(heat_map, 50)   # Orta değer

    # Eşik değerler arasını normalize edelim
    heat_map_clipped = np.clip(heat_map, threshold_low, threshold_high)
    heat_map_normalized = (heat_map_clipped - threshold_low) / (threshold_high - threshold_low)

    # Isı haritasını görselleştir
    plt.imshow(heat_map_normalized, cmap='Blues', vmin=0, vmax=1)
    plt.colorbar()

    # Isı haritasını bir dosyaya kaydet
    plt.savefig(save_path_1)

    # Görseli göster
    plt.show()

    # Kaynakları serbest bırak
    cap.release()

    if save_path_2:
        # İkinci bir kayıt yolu verilmişse, ikinci bir ısı haritası oluştur
        create_heatmap(video_path, save_path_2)

def print_welcome_message():
    welcome_message = """
 
                                                                                               
                       .---.                                                                   
   .                   |   |.--.                                 .                             
 .'|                   |   ||__|                               .'|                             
<  |                   |   |.--.                              <  |                             
 | |             __    |   ||  |                         __    | |             __              
 | | .'''-.   .:--.'.  |   ||  |                 _    .:--.'.  | | .'''-.   .:--.'.            
 | |/.'''. \ / |   \ | |   ||  |               .' |  / |   \ | | |/.'''. \ / |   \ |           
 |  /    | | `" __ | | |   ||  |              .   | /`" __ | | |  /    | | `" __ | |           
 | |     | |  .'.''| | |   ||__|            .'.'| |// .'.''| | | |     | |  .'.''| |           
 | |     | | / /   | |_'---'              .'.'.-'  / / /   | |_| |     | | / /   | |_          
 | '.    | '.\ \._,\ '/                   .'   \_.'  \ \._,\ '/| '.    | '.\ \._,\ '/          
 '---'   '---'`--'  `"                                `--'  `" '---'   '---'`--'  `"           

                                                                          
    """
    for char in welcome_message:
        print(char, end='', flush=True)
        time.sleep(0.001)

def main():
    print_welcome_message()
    video_path = input("\nLütfen video dosyasının yolunu girin: ")
    split_video = input("Videoyu ikiye bölmek istiyor musunuz? (E/H): ").upper()

    if split_video == "E":
        save_path_1 = input("Isı haritasının kaydedileceği yolun ilk kısmını girin: ")
        save_path_2 = input("Isı haritasının kaydedileceği yolun ikinci kısmını girin: ")
        create_heatmap(video_path, save_path_1, save_path_2)
    elif split_video == "H":
        save_path = input("Isı haritasının kaydedileceği yolun tamamını girin: ")
        create_heatmap(video_path, save_path)
    else:
        print("Geçersiz seçim! Lütfen 'E' veya 'H' girin.")

if __name__ == "__main__":
    main()
