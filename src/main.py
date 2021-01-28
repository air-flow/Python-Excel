import openpyxl


class execl:
    def __init__(self):
        self.file_obj = None
        self.file_path = None

    def _GetFileExcelPath(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as f:
            self.file_path = f.readlines()


def cd():
    import os
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    cd()
