import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import time

def create_heatmap(video_path, save_path_1, save_path_2=None):
    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    heat_map_1 = np.zeros((height, width), dtype=np.float32)
    heat_map_2 = np.zeros((height, width), dtype=np.float32)

    ret, prev_frame = cap.read()
    prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    tqdm_bar = tqdm(total=frame_count, desc="Isı haritası oluşturuluyor", leave=False)

    frame_number = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    half_frames = total_frames // 2

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        diff = cv2.absdiff(prev_frame, gray)

        if frame_number < half_frames:
            heat_map_1 += diff
        else:
            heat_map_2 += diff

        prev_frame = gray
        frame_number += 1

        tqdm_bar.update(1)

    tqdm_bar.close()

    max_val_1 = np.max(heat_map_1)
    max_val_2 = np.max(heat_map_2)

    threshold_high_1 = np.percentile(heat_map_1, 99)
    threshold_low_1 = np.percentile(heat_map_1, 50)

    threshold_high_2 = np.percentile(heat_map_2, 99)
    threshold_low_2 = np.percentile(heat_map_2, 50)

    heat_map_clipped_1 = np.clip(heat_map_1, threshold_low_1, threshold_high_1)
    heat_map_normalized_1 = (heat_map_clipped_1 - threshold_low_1) / (threshold_high_1 - threshold_low_1)

    heat_map_clipped_2 = np.clip(heat_map_2, threshold_low_2, threshold_high_2)
    heat_map_normalized_2 = (heat_map_clipped_2 - threshold_low_2) / (threshold_high_2 - threshold_low_2)

    plt.imshow(heat_map_normalized_1, cmap='Blues', vmin=0, vmax=1)
    plt.colorbar()
    plt.savefig(save_path_1)
    plt.show()

    if save_path_2:
        plt.imshow(heat_map_normalized_2, cmap='Blues', vmin=0, vmax=1)
        plt.colorbar()
        plt.savefig(save_path_2)
        plt.show()

    cap.release()

def print_welcome_message():
    welcome_message = """
                                                                                                   
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
    for char in welcome_message:
        print(char, end='', flush=True)
        time.sleep(0.000000000000000000001)

def main():
    print_welcome_message()
    video_path = input("\nLütfen halı saha video dosyasının yolunu girin: ")
    split_video = input("Takımlar devre arası yarısaha değişiliği yaptı mı? (E/H): ").upper()

    if split_video == "E":
        save_path_1 = input("İlk yarının ısı harittasının kaydediliceği yol: ")
        save_path_2 = input("İkinci yarının ısı harittasının kaydediliceği yol: ")
        create_heatmap(video_path, save_path_1, save_path_2)
    elif split_video == "H":
        save_path = input("Maçın ısı haritasının kaydediliceği yol: ")
        create_heatmap(video_path, save_path)
    else:
        print("Geçersiz seçim! Lütfen 'E' veya 'H' girin.")

if __name__ == "__main__":
    main()
