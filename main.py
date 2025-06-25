# main.py

import os
import yt_dlp
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Dark background
Window.clearcolor = (0.06, 0.06, 0.06, 1)

# Download folder
DOWNLOAD_FOLDER = "PH_Downloader"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


class PHDownloaderApp(App):
    def build(self):
        self.video_formats = []
        self.video_info = None

        # UI Elements
        self.url_input = TextInput(
            hint_text="🔗 Enter Pornhub video link here...",
            multiline=False,
            size_hint_y=None,
            height=50,
            font_size=16,
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.6, 0.6, 0.6, 1)
        )

        self.status_label = Label(
            text="",
            size_hint_y=None,
            height=30,
            font_size=14,
            color=(1, 1, 1, 1)
        )

        self.spinner = Spinner(
            text="⬇️ Select available quality",
            size_hint_y=None,
            height=50,
            font_size=14,
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )

        self.main_layout = BoxLayout(
            orientation='vertical',
            padding=15,
            spacing=12,
            size_hint_y=None
        )
        self.main_layout.bind(minimum_height=self.main_layout.setter('height'))

        self.main_layout.add_widget(Label(
            text="🎥 PH Video Downloader",
            font_size=22,
            size_hint_y=None,
            height=50,
            color=(0.2, 1, 0.2, 1)
        ))

        self.main_layout.add_widget(self.url_input)

        # Button to check formats
        btn_check = Button(
            text="🔍 Check Available Qualities",
            size_hint_y=None,
            height=45,
            font_size=14,
            background_color=(0, 0.6, 0, 1),
            color=(1, 1, 1, 1)
        )
        btn_check.bind(on_press=self.get_formats)
        self.main_layout.add_widget(btn_check)

        self.main_layout.add_widget(self.spinner)

        # Download button
        btn_download = Button(
            text="⬇️ Download Video",
            size_hint_y=None,
            height=45,
            font_size=14,
            background_color=(0, 0.4, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        btn_download.bind(on_press=self.download_video)
        self.main_layout.add_widget(btn_download)

        self.main_layout.add_widget(self.status_label)

        # ScrollView for mobile support
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.main_layout)

        return scroll

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.85, 0.35)
        )
        popup.open()

    def get_formats(self, instance):
        url = self.url_input.text.strip()
        self.status_label.text = "Fetching video qualities..."

        if "pornhub.com" not in url:
            self.show_popup("Invalid Link", "Please enter a valid pornhub.com link.")
            return

        try:
            ydl_opts = {'quiet': True, 'skip_download': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.video_info = ydl.extract_info(url, download=False)

            formats = self.video_info.get('formats', [])
            self.video_formats = [f for f in formats if f.get('ext') == 'mp4' and f.get('height')]

            if not self.video_formats:
                self.show_popup("No Formats", "No supported MP4 qualities found.")
                return

            self.spinner.values = [
                f"{f['format_id']} - {f['height']}p - {round(f.get('filesize', 0)/1024/1024, 2)}MB"
                for f in self.video_formats
            ]
            self.spinner.text = self.spinner.values[0]
            self.status_label.text = "✔️ Qualities loaded successfully."

        except Exception as e:
            self.show_popup("Error", f"Could not fetch formats:\n{e}")

    def download_video(self, instance):
        if not self.video_formats or not self.spinner.text:
            self.show_popup("No Selection", "Please select a video quality first.")
            return

        selected_index = self.spinner.values.index(self.spinner.text)
        selected_format = self.video_formats[selected_index]
        format_id = selected_format["format_id"]
        output_path = os.path.join(DOWNLOAD_FOLDER, f"PH_video_{format_id}.mp4")
        url = self.url_input.text.strip()

        self.status_label.text = "Downloading video..."

        try:
            ydl_opts = {
                'format': format_id,
                'outtmpl': output_path,
                'quiet': True,
                'noplaylist': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.status_label.text = "✅ Download completed."
            self.show_popup("Download Finished", f"Saved to:\n{output_path}")

        except Exception as e:
            self.show_popup("Download Error", str(e))


if __name__ == '__main__':
    PHDownloaderApp().run()
