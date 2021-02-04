# import openpyxl
# import pprint
# import re
# import random


class Question:
    def __init__(self):
        self.no = None
        self.question = ""
        self.choices = []
        self.answer = []
        self.row = None
        self.col = None
        self.choices_flag = False  # 正解が設定されているか判定

    def _SetQuestion(self, text):
        if text is not None:
            self.question += text

    def _SetAnswer(self, text):
        if text is not None:
            self.choices.append(text)

    def _SetProblem(self, text):
        if text is not None:
            self.answer.append(text)

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
        if len(self.answer) >= 1:
            self.choices_flag = True
        else:
            self.choices_flag = False

    def _CheckBold(self, cell, text):
        flag = cell.font.bold
        flag = False if flag is None else flag
        if flag:
            self._SetProblem(text)

    def _QuestionResultPrint(self):
        print("-" * 10)
        print(self.no + 1, "問")
        print(self.question)
        # pprint.pprint(self.choices)
        print("選択肢")
        for i in self.choices:
            print(i)
        print("正解")
        # for i in self.answer:
        #     print(i)
        print("-" * 10)

    def _QuestionPrint(self):
        self._HaihunPrint(str(self.no + 1) + "問")
        print(self.question)
        # print("\n")

    def _AnswerPrint(self):
        self._HaihunPrint("選択肢")
        for i in self.choices:
            print(i.replace("\n", ""))
        self._HaihunPrint("解答入力")

    def _ProblemPrint(self):
        self._HaihunPrint("正解")
        for i in self.answer:
            print(i)
        self._HaihunPrint("")

    def _HaihunPrint(self, text="問題"):
        # print("\n")
        temp = "-" * 5
        print(temp, text, temp)
