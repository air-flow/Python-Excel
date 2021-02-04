# Excel class Documents

create date :2021-02-02

Excel からデータを読み込むためのクラス

## \_\_init\_\_

self.excel_obj 読み込んだ excel オブジェクト
self.file_path Excel ファイルの path が書かれているファイル
self.excel_path EXCEL path
self.sheet_range 明示的にセル範囲を選択するときに使用
self.sheet_range 未使用変数　セル自動取得用の変数
self.text 読み込んだテキストリスト
self.sheet_count 読み込んだ Excel のシート数

**sheet_range**で読み込む範囲を明示的に記述している。

## \_GetFileExcelPath

別テキストファイルから Excel ファイルの path を読み込む。

/mine github に上がらないファイルに path を記述している。

## \_GetExcelFile

Excel のファイル読み込みを行っている。

セル番号を自動取得も行っている。

範囲の問題上今回はコメントアウトしている。

## \_ExcelGetCell

複数のセルにまたがっている値を判定して結合して格納している。

太字を後に判定するため cell を格納している。
