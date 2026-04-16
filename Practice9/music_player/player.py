import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder

        # Load only mp3 files from folder
        self.playlist = [
            f for f in os.listdir(music_folder)
            if f.endswith(".mp3")
        ]

        # Sort playlist for consistent order
        self.playlist.sort()

        self.index = 0
        self.is_playing = False

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

    def load_track(self):
        # Load current track from playlist
        if not self.playlist:
            return

        track_path = os.path.join(self.music_folder, self.playlist[self.index])
        pygame.mixer.music.load(track_path)

    def play(self):
        # Start or resume playback
        if not self.playlist:
            return

        if not self.is_playing:
            self.load_track()
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            pygame.mixer.music.unpause()

    def stop(self):
        # Stop playback completely
        pygame.mixer.music.stop()
        self.is_playing = False

    def pause(self):
        # Pause current track
        pygame.mixer.music.pause()
        self.is_playing = False

    def next_track(self):
        # Switch to next track in playlist
        if not self.playlist:
            return

        self.index = (self.index + 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True

    def prev_track(self):
        # Switch to previous track in playlist
        if not self.playlist:
            return

        self.index = (self.index - 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True

    def get_current_track(self):
        # Return current track name
        if not self.playlist:
            return "No music found"

        return self.playlist[self.index]

    def get_status(self):
        # Return playback status
        return "Playing" if pygame.mixer.music.get_busy() else "Stopped"