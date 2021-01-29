import openpyxl
import pprint

# 問題文が複数行に渡り記述してある
# 解答が問題文と列がずれているものがある
# 正解が太字になっていないものがある
# 問題文と解答には一行空白がある（逆もしかり）


class Execl:
    def __init__(self, file_path):
        self.excel_obj = None
        self.file_path = file_path
        self.excel_path = None
        self.question = []

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


class Question:
    def __init__(self):
        self.no = None
        self.q = ""
        self.a = []
        self.problem = []
        self.row = None
        self.col = None
        self.answer_flag = None  # 正解が設定されているか判定

    def _SetQuestion(self, text):
        if text is not None:
            self.q += text

    def _SetAnswer(self, text):
        if text is not None:
            self.a.append(text)

    def _SetProblem(self, text):
        if text is not None:
            self.problem.append(text)

    def _SetRow(self, row):
        if row is not None:
            self.row = row

    def _SetCol(self, col):
        if col is not None:
            self.col = col

    def _SetNo(self, no):
        if no is not None:
            self.no = no

    def _CheckAnswerCount(self):
        if len(self.a) < 1:
            self.answer_flag = False
        else:
            self.answer_flag = True


def cd():
    import os
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    cd()
    ex = Execl("../mine/path.txt")
    ex._GetFileExcelPath()
    # print(ex.excel_path)
    ex._GetExcelFile()
    ex._ExcelGetCell()
    # pprint.pprint(ex.excel_obj)
