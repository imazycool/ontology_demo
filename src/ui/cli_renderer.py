
from models.menu import Menu
from ui.renderer import Renderer
from ui.terminal import Terminal


class CLIRenderer(Renderer):

    def __init__(self):
        self.terminal = Terminal()
        
    def show_message(self, message: str):
        self.terminal.write(message)

    def display(self, menu: Menu) -> int:
        self.terminal.write(" " * 50)
        self.terminal.write("=" * 50)
        self.terminal.write(f"{' ' * 10}{menu.title}")
        self.terminal.write("=" * 50)
        self.terminal.write(f"\n{menu.message}\n")
        for index, option in enumerate(menu.options, start=1):
            self.terminal.write(f"{index}. {option}")
        self.terminal.write("0. Exit")
        while True:
            try:
                return int(input("\nEnter your choice <number> : "))
            except ValueError:
                self.terminal.write("Please enter a valid number.")