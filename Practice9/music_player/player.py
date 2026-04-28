import pygame
import os
from mutagen.mp3 import MP3 

class MusicPlayer:
    def __init__(self, music_folder):
        try:
            pygame.mixer.init()
        except:
            print("Audio init error")

        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.current_index = 0
        self.is_playing = False

        self.start_time = 0
        self.track_length = 0

    def load_music(self):
        if not os.path.exists(self.music_folder):
            print(f"Folder not found: {self.music_folder}")
            return []

        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3"): 
                files.append(os.path.join(self.music_folder, file))

        print("Loaded:", files)
        return files

    def play(self):
        if not self.playlist:
            print("No MP3 files!")
            return

        path = self.playlist[self.current_index]

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        audio = MP3(path)
        self.track_length = audio.info.length

        self.start_time = pygame.time.get_ticks()
        self.is_playing = True

        print(f"Playing: {self.get_current_track_name()}")

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No Track"
        name = os.path.basename(self.playlist[self.current_index])
        return os.path.splitext(name)[0]  

    def get_progress(self):
        if not self.is_playing:
            return 0

        current_time = (pygame.time.get_ticks() - self.start_time) / 1000

        if self.track_length == 0:
            return 0

        return min(current_time / self.track_length, 1)