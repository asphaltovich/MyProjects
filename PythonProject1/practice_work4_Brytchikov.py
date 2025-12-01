class Media:
    def __init__(self, media):
        self.media = media

    def play(self):
        print(f"Playing {self.media}")

    def pause(self):
        print("Pausing media")

media_item = Media("song.mp3")
media_item.play()
media_item.pause()class Media:
    def __init__(self, media):
        self.media = media

    def play(self):
        print(f"Playing {self.media}")

    def pause(self):
        print("Pausing media")


class Music(Media):
    def play(self):
        print("Playing music track")


class Video(Media):
    def play(self):
        print("Playing video file")


# Пример использования
music_item = Music("song.mp3")
music_item.play()  # Выведет: Playing music track
music_item.pause() # Выведет: Pausing media

video_item = Video("video.mp4")
video_item.play()   # Выведет: Playing video file
video_item.pause()  # Выведет: Pausing media
