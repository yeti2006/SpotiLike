import sqlite3

from loguru import logger


class Database:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS playlists (
                id TEXT,
                name TEXT
            )"""
        )

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS hotkeys (
                id TEXT,
                hotkey TEXT
            )"""
        )

        self.db.commit()

        # TODO: Create settings table.

    def _get(self, database: str):
        pass

    def update_playlists(self, data: dict):
        records = [x for x in data.items()]  # [(id, name), (id, name)]

        self.cursor.execute(
            "DELETE FROM playlists"
        )  # Delete everything in playlists to update.

        self.cursor.executemany(
            "INSERT INTO playlists (id, name) VALUES (?, ?)", records
        )
        self.db.commit()

        logger.info("Updated user playlists.")

        self.update_hotkeys([x[0] for x in records])

    def update_hotkeys(self, data: list):

        self.cursor.execute("SELECT * FROM hotkeys")
        hotkey_data = self.cursor.fetchall()

        if not hotkey_data:  # first time
            self.cursor.executemany(
                "INSERT INTO hotkeys (id, hotkey) VALUES (?,?)",
                [(x, None) for x in data],
            )
            self.cursor.execute(
                "INSERT INTO hotkeys (id, hotkey) VALUES (?,?)",
                ("liked_songs", "<ctrl>+l"),
            )
            self.db.commit()
            return

        new_playlist = []
        remove_playlist = []

        for id in [x[0] for x in hotkey_data]:
            if id not in data:
                if not id == "liked_songs":
                    remove_playlist.append(id)

        for id in data:
            if id not in [x[0] for x in hotkey_data]:
                if not id == "liked_songs":
                    new_playlist.append(id)

        if new_playlist:
            self.cursor.executemany(
                "INSERT INTO hotkeys (id, hotkey) VALUES (?,?)",
                [(x, None) for x in new_playlist],
            )

        if remove_playlist:
            self.cursor.executemany(
                "DELETE FROM hotkeys WHERE id IN (?)", [tuple(remove_playlist)]
            )

        self.db.commit()

    def get_playlists(self):
        self.cursor.execute("SELECT * FROM playlists")
        all_playlists = self.cursor.fetchall()

        return all_playlists

    def get_hotkeys(self, id):

        self.cursor.execute("SELECT * FROM hotkeys WHERE id=?", (id,))

        return self.cursor.fetchone()
