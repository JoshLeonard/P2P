from services.fileservice import FileService


class UserInterface:

    def __init__(self, file_service):
        self.options = (self.load_file_request, self.view_files, self.exit)
        self.file_service = file_service

    def run(self):
        self.print_options()
        self.handle_menu_selection()

    def print_options(self):
        print('1. File request')
        print('2. View my files')
        print('3. Exit')

    def handle_menu_selection(self):
        selected_item = input()
        selected_item_int = int(selected_item)
        option_method = self.options[selected_item_int - 1]
        print('selected ' + selected_item)
        option_method()

    def load_file_request(self):
        print('load file')
        path = input('Enter the path to file manifest:')
        self.file_service.file_request(path)

    def view_files(self):
        print('view files')

    def exit(self):
        print('exit')


if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
