from dotenv import load_dotenv
from spotipy import Spotify, SpotifyOAuth


from loguru import logger
from .database import Database

from rich.pretty import pprint
from pynput import keyboard
from threading import Thread


class Hotkey(Thread):
    def __init__(self):
        pass

    def run(self):
        self.hotkeys = keyboard.GlobalHotKeys({"<ctrl>+l": lambda: print("Received")})
        self.hotkeys.start()


class SpotiLikeAPI:
    def __init__(self):
        load_dotenv()
        self.db = Database()

        self.sp = Spotify(auth_manager=SpotifyOAuth())

        try:
            self.username = self.sp.me()["display_name"]
        except Exception as e:
            raise

        logger.info(f"Client authorised with username {self.username}")

    def run(self):
        playlists: dict = self.get_user_playlists()
        self.db.update_playlists(data=playlists)

    def error(self, e=None):
        print("error")

    def _get_all_playlists(self):
        results = self.sp.current_user_playlists()

        tracks = results["items"]
        while results["next"]:
            results = self.sp.next(results)
            tracks.extend(results["items"])

        return tracks

    def get_user_playlists(self):
        """
        {
            "id": "playlist_name"
        }
        """
        data = self._get_all_playlists()
        _id = self.sp.me()["id"]

        return {item["id"]: item["name"] for item in data if item["owner"]["id"] == _id}


if __name__ == "__main__":
    SpotiLikeAPI().run()
