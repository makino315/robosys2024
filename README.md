# plusコマンド
![test](https://github.com/makino315/robosys2024/actions/workflows/test.yml/badge.svg)

標準入力から読み込んだ数字を足す。

# Disney Anniversary Script
このスクリプトは、ディズニーの設立年からの経過年数を計算し、現在の年から設立からの周年を表示します。

# 主な機能
現在の年を入力として受け取り、ディズニーの設立からの経過年数を計算
正常な年の入力に対する結果表示
無効な入力に対するエラーメッセージ表示

# 動作環境
OS: Windows, macOS, Linux
Pythonバージョン: 3.8以上
必要なライブラリ: なし

# インストール方法
Pythonをインストール: Python 3.8以上をインストールしてください（公式サイト）。
リポジトリをクローン:git clone https://github.com/yourusername/disney_anniversary.git
cd disney_anniversary


# 使い方
スクリプトの実行: ターミナルで以下のコマンドを実行します。
echo 2024 | python3 disney_anniversary.py
これにより、ディズニーの設立年からの経過年数が出力されます。

# 実行例
ディズニーは 1923 年に設立され、今年で 101 周年です。


# テスト
スクリプトが正しく動作するかを確認するためのテストスクリプトも含まれています。テストを実行するには、以下のコマンドを使用してください
unittestを使用したテスト:python -m unittest test_disney_anniversary.py
bashスクリプトを使用したテスト:
chmod +x test_disney_anniversary.sh
./test_disney_anniversary.sh



# 権利関係
著作権: 2024 Kazuki Makino
ライセンス: このプロジェクトはBSD-3-Clauseライセンスの下でライセンスされています。
