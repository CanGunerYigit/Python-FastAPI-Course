from pytube import Playlist, Youtube
from moviepy.editor import *
import os

class Youtubedownloader:
    def download_single_video(self,url,save_path):
        try:
            yt=Youtube(url)
            stream=yt.stream.filter(file_extension='mp4').get_highest_resolution()
            print("Video Title: ",yt.title)
            filename = yt.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('&', '_').replace('%', '_').replace('#', '_').replace('{', '_').replace('}', '_').replace('[', '_').replace(']', '_').replace('=', '_').replace('+', '_').replace('-', '_').replace('--', '_').replace(';', '_').replace('!', '_').replace('@', '_').replace('$', '_').replace('^', '_').replace('`', '_').replace('~', '_').replace(',', '_').replace('.', '_').replace(' ', '_')        
            stream.download(output_path=save_path,filename=filename)
            print(f"Download completed! Video saved as -> {filename}, in the location -> {save_path}")
            new_extension='.mp4'
            sepa='/'
            full_path=save_path + sepa +filename

            if not os.path.exists(full_path):
                print(f"The file {filename} does not exist")

            new_full_path= full_path + new_extension 
        except Exception as e:
            print(f"an error has occured: {e}")
    def download_playlist(self,url,save_path):
        try:
            p=Playlist(url)
            for video_url in p.video_url:
               print(f"Downloading video: {video_url}")
               Youtubedownloader.download_single_video(video_url,save_path)
            print("All videos have been downloaded in .mp4 format")


        except Exception as e:
            print(f"an error has occured: {e}")
    def download_video_as_audio(self,url,save_path):
        try:
            yt=Youtube(url)
            print("Downloading audio from: ",yt.title)
          
            audio_stream=yt.streams.filter(only_audio=True).first()
            if not audio_stream:
                print("No audio stream available")
                return
            output_file=audio_stream.download(output_path=save_path)
            print("Download audio file:",output_file)
            new_file=os.path.splitext(output_file)[0] + '.mp3'
            print("Converting file to MP3....")
            audio_clip=AudioFileClip(output_file)
            audio_clip.write_audiofile(new_file,codec='mp3')
            audio_clip.close()
            os.remove(output_file)
            print("Conversion complete. Saved as: ",new_file)
        except Exception as e:
            print(f"an error has occured: {e}")
    def download_playlist_as_mp3(self,url,save_path):
        try:
            p=Playlist(url)
            for video_url in p.video_urls:
                print(f"Downloading video: {video_url}")
                Youtubedownloader.download_video_as_audio(video_url,save_path)
            print("All videos have been downloaded and converted to mp3.")
        except Exception as e:
            print(f"an error has occured: {e}")