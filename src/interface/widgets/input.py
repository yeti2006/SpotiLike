from textual_inputs import TextInput

from textual.widget import Widget
from textual.views import GridView
from textual.widgets import Placeholder

from rich.panel import Panel


class CMD(TextInput):
    def __init__(self):
        super().__init__()
        self.title = "Command Area"
        self.placeholder = "Enter command [see help for more]"
        self.style = "yellow"
        self.border_style = "cyan"


class ShortcutInput(Widget):
    def render(self):
        view = GridView()

        return view
