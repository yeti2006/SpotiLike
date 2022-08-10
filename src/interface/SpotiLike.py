import sys

sys.path.append("../")

from textual.app import App
from textual.widgets import (
    Footer,
    Placeholder,
    ScrollView,
    Header,
    Static,
    DirectoryTree,
    Button,
)
from .widgets import CMD, ListViewUo, PlaylistButton, ShortcutInput
from loguru import logger
from api.database import Database
from api.main import SpotiLikeAPI

from rich.panel import Panel
from rich.text import Text

from .commands import command_list


from textual.views import GridView, DockView
from textual.widget import Widget
from textual.layouts.dock import DockLayout, Dock


class W(Widget):
    def render(self):

        return GridView(
            DockLayout(
                [
                    Dock(
                        edge="left",
                        widgets=[
                            Placeholder(),
                            Placeholder(),
                        ],
                    )
                ]
            )
        )


class SpotiLike(App):
    db = Database()

    async def on_load(self):
        # self.api = SpotiLikeAPI()
        # self.api.run()

        await self.bind("b", "view.toggle('sidebar')", "Show/Hide playlists")
        await self.bind("/", "focus_command_area()", "Focus Command Area.")
        await self.bind("q", "quit", "Quit")

    async def action_focus_command_area(self):
        await self.command_area.focus()

    async def on_mount(self):
        # await self.view.dock(Footer(), edge="bottom")
        # await self.view.dock(
        #     Header(tall=False, style="dark_goldenrod on black"), edge="top"
        # )

        # self.logo = Static(asciiart.logo_art)

        self.command_area = CMD()
        self.playlists_view = ListViewUo(
            [
                PlaylistButton(
                    ("Liked Songs", self.db.get_hotkeys("liked_songs")[1]),
                    "liked_songs",
                )
            ]
            + [
                PlaylistButton((x[1], self.db.get_hotkeys(x[0])[1]), x[0])
                for x in self.db.get_playlists()
            ]
        )
        self.status = ListViewUo(
            [
                Button(f"[b underline magenta]{x[0]}[/]\n-{x[1]}", style=None)
                for x in command_list
            ]
        )

        await self.view.dock(self.status, size=25, edge="right")
        await self.view.dock(self.playlists_view, size=25, edge="left", name="sidebar")
        await self.view.dock(self.command_area, edge="bottom", size=3)

        self.x = Static(Button("yp"))

        await self.view.dock(self.x, edge="top")

        await self.x.update(Button("Hi"))

        # await self.view.dock(
        #     *[
        #         GridView(
        #             DockLayout(
        #                 [
        #                     Dock(
        #                         edge="left",
        #                         widgets=[
        #                             Placeholder(),
        #                             Placeholder(),
        #                         ],
        #                     )
        #                 ]
        #             )
        #         )
        #     ],
        #     edge="right",
        # )
