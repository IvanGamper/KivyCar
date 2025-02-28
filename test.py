from kivy.app import App
from kivy.uix.video import Video

class TestVideoApp(App):
    def build(self):
        video = Video(source="pushups.mp4", state='play', options={'allow_stretch': True})
        return video

if __name__ == '__main__':
    TestVideoApp().run()