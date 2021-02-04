# Question Class Documents

create date :2021-02-04

問題情報を格納する class

## \_\_init\_\_

self.no 問題番号
self.question 問題
self.choices 選択肢
self.answer 答え
self.row 行
self.col 列
self.choices_flag 正解が設定されているか判定

## \_Set\*

値を格納する関数

## \_CheckAnswerCount

正解があるを判定している。

たまに正解の印である太字がないものが存在する。

## \_CheckBold

正解の太字を判定している。

true false の 2 択で返すようにしている。

## \_QuestionResultPrint

簡易的な問題を出力するための関数。

## \_QuestionPrint

問題の出力

## \_AnswerPrint

選択肢の出力

## \_ProblemPrint

答えの出力

## \_HaihunPrint

区分をわかりやすくするために区切り文字を出力する。
