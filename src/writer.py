import os
import colorama


colorama.init(autoreset=True)


class Writer:
    @staticmethod
    def get_path(path):
        while True:
            if os.path.exists(path):
                break
            else:
                path = input(f'{colorama.Fore.RED}Enter the correct path: ')
        if path[-1] == '/':
            path = path[:-1]
        return path

    def writing_to_file(self, path, data, count):
        path = self.get_path(path)
        with open(f'{path}/result.txt', 'w') as writer:
            for i in range(count):
                writer.write(f'{data[i]}\n')
        print(f'{colorama.Fore.GREEN}Good... Your file in:\n{path}/result.txt')
