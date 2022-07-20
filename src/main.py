from interface.SpotiLike import SpotiLike
from rich.console import Console


SpotiLike.run(
    log="spotilike.log", title="SpotiLike <3", console=Console(height=120, width=35)
)
