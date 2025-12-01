class Media:
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

music_item = Music("song.mp3")
music_item.play()

video_item = Video("video.mp4")
video_item.play()
