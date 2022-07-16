from textual.app import App
from textual.widgets import Footer, Placeholder

from loguru import logger

class SpotiLike(App):
    
    async def on_bind(self):
        await self.bind("b", "view.toggle('sidebar')", "Show/Hide sidebar")

    
    async def on_mount(self):
        # await self.view.dock(Footer(), edge="bottom")
        
        await self.view.dock(Placeholder(), edge="left", size=20, name="sidebar")
        await self.view.dock(Placeholder(), edge="bottom", size=10)
        await self.view.dock(Placeholder(), edge="top")
        
        
SpotiLike.run(log="spotilike.log")