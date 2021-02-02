class AWSCloudPractitioner:

    def __init__(self, text_list):
        self.untreated_text_list = text_list
        self.question_list = []
        # 出題問題オブジェクト、選択解答
        self.setting_question = []
        self.mode = True
        self.question_Definition = {"q": "", "a": "^[a-zA-Z][.]"}
        self.number_of_correct_answers = 0
        self.print_mode = 0
        # self.reorganization_list = None

    def _CheckAnswerSreach(self):
        for i in self.question_list:
            if not i.choices_flag:
                i._QuestionResultPrint()
        print(len(self.question_list))

    def _ReorganizationQuestionList(self):
        add_flag = False
        answer_flag = False
        q = Question()
        for i in self.untreated_text_list:
            # 問題文判定
            if not self._CheckProblemText(i[1]):
                if answer_flag:
                    add_flag = True
                else:
                    q.question += i[1]
            else:
                answer_flag = True
                q._CheckBold(i[2], i[1])
                q.choices.append(i[1])
            if add_flag:
                add_flag = False
                answer_flag = False
                q._SetNo(len(self.question_list))
                q._CheckAnswerCount()
                self.question_list.append(q)
                q = Question()
                q.question += i[1]

    def _CheckProblemText(self, text, juge="a"):
        pattern = self.question_Definition[juge]
        matchOB = re.match(pattern, text.strip())
        if matchOB:
            return True
        else:
            return False

    def _MockExamination(self, count=10):
        for i in range(count):
            temp = random.choice(self.question_list)
            select = {"obj": temp, "choices": None}
            if temp.choices_flag:
                temp._QuestionPrint()
                temp._AnswerPrint()
                # temp._ProblemPrint()
                select["choices"] = self._InputUserAnswer()
                self._PrintAnswerJuge(temp)
            else:
                print("answer not set error")
            self.setting_question.append(select)
        self._CheckingAnswers()

    def _InputUserAnswer(self):
        print("解答を選択してください")
        print("a, A, 1 のどれでも可")
        print("複数選択肢は「,」、「.」のどちらかで")
        user_answer = input()
        while True:
            if len(user_answer) > 0:
                break
            else:
                print("選択肢を入力してください。")
            user_answer = input()
        return user_answer

    def _PrintAnswerJuge(self, question):
        if self.mode:
            question._ProblemPrint()

    def _CheckingAnswers(self):
        for i in self.setting_question:
            answer_list = i["obj"].answer
            answer = self._ReplaceAnswerList(answer_list)
            choice = i["choices"].replace(".", "").replace(",", "")
            choice = list(self._ReplaceAlphabetString(choice))
            self._SortListAlphabet(answer)
            self._SortListAlphabet(choice)
            # print(answer, choice, " debug")
            if answer == choice:
                self.number_of_correct_answers += 1
        self._QuestionResult()

    def _QuestionResult(self):
        self.setting_question[0]["obj"]._HaihunPrint("結果")
        print(str(self.number_of_correct_answers) +
              "/" + str(len(self.setting_question)))

    def _ReplaceAnswerList(self, answer_list):
        result = ""
        for i in answer_list:
            result += i[0]
        return list(result)

    def _ReplaceAlphabetString(self, text):
        alphabet = [chr(i) for i in range(65, 65 + 26)]
        number = list(map(str, list(range(1, 10))))
        d = dict(zip(number, alphabet))
        # print(s.translate(str.maketrans(d)))
        result = []
        for i in text:
            result.append(i.translate(str.maketrans(d)))
        return result

    def _SortListAlphabet(self, sort_list):
        return sort_list.sort()
