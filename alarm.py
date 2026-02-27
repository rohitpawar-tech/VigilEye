import pygame
import os
import logging

class SoundAlarm:
    def __init__(self, sound_path):
        self.sound_path = sound_path
        self.is_playing = False
        self.sound = None
        
        try:
            pygame.mixer.init()
            if os.path.exists(self.sound_path):
                self.sound = pygame.mixer.Sound(self.sound_path)
            else:
                logging.warning(f"Audio file missing at {self.sound_path}. Alarm disabled.")
        except Exception as e:
            logging.error(f"Failed to initialize audio system: {e}")

    def start(self):
        """Starts the alarm loop."""
        if self.sound and not self.is_playing:
            try:
                self.sound.play(loops=-1) # Loop indefinitely
                self.is_playing = True
                print("[ALARM] ACTIVATED")
            except Exception as e:
                logging.error(f"Error playing sound: {e}")

    def stop(self):
        """Stops the alarm."""
        if self.sound and self.is_playing:
            try:
                self.sound.stop()
                self.is_playing = False
                print("[ALARM] DEACTIVATED")
            except Exception as e:
                logging.error(f"Error stopping sound: {e}")