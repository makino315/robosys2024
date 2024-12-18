# plusコマンド
![test](https://github.com/makino315/robosys2024/actions/workflows/test.yml/badge.svg)

標準入力から読み込んだ数字を足す。

# Symbolic Integral Calculator
このソフトウェアは、与えられた関数のシンボリック定積分を計算するためのツールです。ユーザーは関数と積分区間を指定し、その区間における定積分結果を得ることができます。

# 主な機能
任意の関数の数式を入力として受け取り、シンボリック積分を実行。
指定された区間における定積分の結果を分数形式で提供。
入力エラーや数式エラーが発生した場合に適切なエラーメッセージを表示。

# 動作環境
OS: Windows, macOS, Linux
Pythonバージョン: Python 3.8 以上
必要なライブラリはsympy

# インストール方法
Pythonをインストール:
Python 3.8以上をインストールしてください（公式サイト: https://www.python.org/）。
必要なライブラリをインストール:
ターミナルで以下のコマンドを実行してください。
pip install sympy
スクリプトをダウンロード:
リポジトリからスクリプトをダウンロードします:
git clone <リポジトリのURL>
cd <ダウンロードしたフォルダ>

# 使い方
スクリプトの実行:
ターミナルで以下のコマンドを実行します。
echo -e "x**2\n0,1" | python integral.py
これにより、関数 x**2 を区間 0 から 1 で積分した結果が表示されます。

# 実行例
以下のように入力を与えるとします。
x**2
0,1
以下の結果が表示されます。
f(x) = x**2 の区間 [0.0, 1.0] における定積分の結果: 1/3

# テスト
以下の関数と区間でテストを実施し、期待される結果が得られることを確認しています。
関数x**2　区間0,1	結果1/3
関数sin(x)	区間0,pi	結果2
関数exp(x)	区間0,1	　　結果e - 1

# ライセンス
このソフトウェアはMITライセンスのもとで提供されます。

# 謝辞
このソフトウェアは、Pythonのライブラリ sympy を利用しています。
開発およびテストに協力してくれた皆様に感謝いたします。

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7〜3.10

## テスト環境
- Ubuntu 24.04 LTS

