# AWSCloudPractitioner Class Documents

create date :2021-02-04

Excel 読み込みデータを一行識別して Question Class に格納して question_list に格納する。

## \_\_init\_\_

self.untreated_text_list 未整形のデータ
self.question_list = 出題問題オブジェクト
self.setting_question = 出題した問題格納
self.mode 出題後解答を出力するかのフラグ
self.question_Definition 正規表現判定
self.number_of_correct_answers 正解数
self.print_mode 現在未使用変数　出力形式を分けようと用意した

## \_CheckAnswerSreach

正解が正しくセットされていない問題を出力する関数

## \_ReorganizationQuestionList

テキストリストから問題と選択肢を区別して Question Class にセットする。

## \_CheckProblemText

正規表現で問題文と選択肢を判定している。

## \_MockExamination

模擬試験実行関数

ランダムに問題リストから Question Class から問題文を出力している。

## \_InputUserAnswer

選択肢をターミナルから入力させる関数

## \_PrintAnswerJuge

答えを出力するかを判定関数

## \_CheckingAnswers

答え合わせをする関数

## \_QuestionResult

正解数出力関数

## \_ReplaceAnswerList

選択肢を「A」などの単位で変換するための関数

## \_ReplaceAlphabetString

ターミナルからの入力を変換する関数

## \_SortListAlphabet

正解と選択肢をリスト比較するためにソートする関数
