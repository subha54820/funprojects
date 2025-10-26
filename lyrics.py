import time
import sys
import pygame
#changes
def play_music():
    pygame.init()
    
    # 🎵 Replace the below path with your actual Sahiba song file path
    pygame.mixer.music.load(r"C:\Users\pradh\Documents\WhatsApp Audio 2025-10-22 at 15.09.09_ff318645.mp3")
    pygame.mixer.music.play()

def print_lyrics():
    lyrics = [
        "Teri talab mujhko",
        "teri talab jaana ho",
        "tu kabhi rubaroo",
        "Shor sharaba jo",
        "seene mein hai mere,",
        "kaise bayaan main karun?",
        "Haal jo mera hai",
        "main kisko bataun?",
        "Mere...",
        "",
        "Sahiba dil naa kiraaye ka,",
        "Thoda toh sambhaalo naa,",
        "Naazuk hai yeh toot jaata hai",
        "Sahiba neendein veendein aaye naa",
        "Raatein kaati jaaye naa",
        "Tera hi khayaal",
        "din rain aata hai!"
    ]

    delays = [0.9, 0.8, 1.0, 0.8, 0.7, 0.8, 0.7, 0.8, 1.0,
              0.8, 0.9, 0.8, 1.0, 0.9, 0.8, 0.9, 1.0]

    print("\n🎶 Playing: Sahiba - Aditya Rikhari 🎶\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        if i < len(delays):
            time.sleep(delays[i])

play_music()
print_lyrics()

# Wait until song finishes
while pygame.mixer.music.get_busy():
    time.sleep(1)

pygame.quit()
