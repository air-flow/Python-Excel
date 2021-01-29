import openpyxl
import pprint


class Execl:
    def __init__(self, file_path):
        self.excel_obj = None
        self.file_path = file_path
        self.excel_path = None

    def _GetFileExcelPath(self):
        with open(self.file_path, mode="r", encoding="utf-8") as f:
            self.excel_path = f.readlines()[0]

    def _GetExcelFile(self):
        self.excel_obj = openpyxl.load_workbook(self.excel_path)
        # print(self.excel_obj.sheetnames)

    def _ExcelGetCell(self):
        sheet = self.excel_obj.worksheets[0]
        for cols in sheet.iter_cols(min_row=1, min_col=3, max_row=2040):
            for cell in cols:
                if cell.value is not None:
                    print(cell.row, cell.value)


def cd():
    import os
    os.chdir(os.path.dirname(__file__))


def test():
    wb = openpyxl.load_workbook("Sample.xlsx")


if __name__ == "__main__":
    cd()
    ex = Execl("../mine/path.txt")
    ex._GetFileExcelPath()
    # print(ex.excel_path)
    ex._GetExcelFile()
    ex._ExcelGetCell()
    # pprint.pprint(ex.excel_obj)
