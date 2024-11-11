from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

Builder.load_string('''
<StyledButton>:
    background_normal: ''
    background_color: (0, 0, 0, 0)
    color: (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [10]
''')
from backend1 import Youtubedownloader
import tkinter as tk
from tkinter import filedialog

Window.clearcolor =get_color_from_hex('#FFFFFF')

class StyledButton(Button):
    pass

class DownloaderGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.padding=20
        self.spacing=10
        
        

        self.spinner = Spinner(
            text='Select Download Type',
            values=('Download Video', 'Download Playlist', 'Download Video as Audio', 'Download Playlist as MP3'),
            size_hint=(1, 0.1),
            background_color=get_color_from_hex('#1E88E5'),  # Blue
            background_normal=''
        )
        self.add_widget(self.spinner)

        # URL input with rounded corners and shadows
        self.url_input = TextInput(
            size_hint=(1, 0.2),
            multiline=False,
            hint_text='Enter YouTube URL here',
            background_normal='',
            background_color=get_color_from_hex('#333333'),
            foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.url_input)
        self.path_input = TextInput(
            size_hint=(1, 0.15),
            multiline=False,
            readonly=True,
            hint_text='Enter save path here',
            background_normal='',
            background_color=get_color_from_hex('#333333'),
            foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.path_input)

        self.path_button=StyledButton(
            text="Browse",
            size_hint=(1,0.1),
            background_color=get_color_from_hex("#4CAF50"),
        )
        self.path_button.bind(on_press=self.open_file_dialog)
        self.add_widget(self.path_button)
        self.download_button=StyledButton(
            text="Download",
            size_hint=(1,0.1),
            background_color=get_color_from_hex("#BDBDBD"),
        )
        self.download_button.bind(on_press=self.start_download)
        self.add_widget(self.download_button)

        self.message_label=Label(
            size_hint=(1,0.1),
            color=get_color_from_hex("#BDBDBD")

        )
        self.add_widget(self.message_label)

    def open_file_dialog(self,instance):
        root=tk.Tk()
        root.withdraw()
        dir_path=filedialog.askdirectory()
        if dir_path:
            self.path_input=dir_path
    def start_download(self,instance):
        print("Download button pressed")
        download_type=self.spinner.text
        url=self.url_input.text.strip()
        save_path=self.path_input.text.strip()

        if not url:
            self.message_label.text="Please enter a valid URL"
            return
        if not save_path:
            self.message_label.text="You must choose a file path"

        downloader=Youtubedownloader()
        try:
            if download_type=="Download Video":
                downloader.download_single_video(url,save_path)
            elif download_type=="Download Playlist":
                downloader.download_playlist(url,save_path)
            elif download_type=="Download Video as Audio":
                downloader.download_video_as_audio(url,save_path)
            elif download_type=="Download Playlist as MP3":
                downloader.download_playlist_as_mp3(url,save_path)
        except Exception as e :
            self.message_label.text=f"Error: {str(e)}"
            print("Error details: ",str(e))
            
class YoutubeDownloaderApp(App):
    def build(self):
        return DownloaderGUI()
if __name__=="__main__":
    YoutubeDownloaderApp().run()

