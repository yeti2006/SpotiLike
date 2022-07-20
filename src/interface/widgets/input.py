from textual_inputs import TextInput
from rich.padding import Padding
from textual.widget import Widget

class CMD(TextInput):
    def __init__(self):
        super().__init__()
        self.title = "Command Area"
        self.placeholder = "Enter command [see help for more]"
        self.style = "yellow"
        self.border_style = "cyan"
        
    
class hotkeyInput(TextInput):
    def __init__(self):
        super().__init__()
        self.value = "ctrl+?"
        self.title = "Enter hotkey"
        
    def render(self):
        return Padding(super().render(), (10, 5))

        