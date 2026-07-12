


class Terminal:

    def write(self, message: str):
        print(message)



    def read(self) -> str:
        return input()



    def show_header(self, title: str):

        print()
        print("=" * 50)
        print(f"{title:^50}")
        print("=" * 50)
        print()



    def show_table(self, headers, rows):
        # Header
        print(f"{headers[0]:<25}{headers[1]:>20}")
        print("-" * 45)
        # Data
        for row in rows:
            print(f"{str(row[0]):<25}{row[1]:>20}")
        print()