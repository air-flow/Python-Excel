class Execl:
    # ToDo cell自動取得によるテキスト抽出
    def __init__(self, file_path):
        self.excel_obj = None
        self.file_path = file_path
        self.excel_path = None
        self.sheet_range = [["C1", "D2050"], ["A1", "B1310"]]
        # self.sheet_range = []
        self.text = []
        self.sheet_count = None

    def _GetFileExcelPath(self):
        with open(self.file_path, mode="r", encoding="utf-8") as f:
            self.excel_path = f.readlines()[0]

    def _GetExcelFile(self):
        self.excel_obj = openpyxl.load_workbook(self.excel_path)
        #  cell番号自動取得
        # for i in range(len(self.excel_obj.sheetnames)):
        #     temp = [self.excel_obj.worksheets[i].max_row,
        #             self.excel_obj.worksheets[i].max_column]
        # self.sheet_range.append(temp)
        self.sheet_count = len(self.excel_obj.sheetnames)

    def _ExcelGetCell(self, index=0):
        sheet = self.excel_obj.worksheets[index]
        cell = sheet[self.sheet_range[index][0]:self.sheet_range[index][1]]
        for i, (c, d) in enumerate(cell):
            if c.value is not None or d.value is not None:
                tc = c.value if c.value is not None else ""
                td = d.value if d.value is not None else ""
                set_cell = c if c.value is not None else d
                self.text.append([i, tc + td, set_cell])
        # print(len(self.text))
