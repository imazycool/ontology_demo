

from models.menu import Menu


class CLIRenderer:

    def display(self, menu: Menu):
        print("=" * 50)
        print(menu.title)
        print("=" * 50)
        print(f"\n{menu.message}\n")
        for index, option in enumerate(menu.options, start=1):
            print(f"{index}. {option}")
        print("0. Exit")
        while True:
            try:
                return int(input("\nEnter your choice <number> : "))
            except ValueError:
                print("Please enter a valid number.")