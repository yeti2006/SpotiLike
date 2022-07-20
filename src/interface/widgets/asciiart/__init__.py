from pyfiglet import Figlet
from rich.text import Text

f = Figlet(font='slant')

logo_art = Text(f"{f.renderText('SpotiLike')}", style="green_yellow")
