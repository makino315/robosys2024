#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Kazuki Makino
# SPDX-License-Identifier: BSD-3-Clause

import sympy as sp
import sys

# 標準入力から関数と積分区間を一度に受け取る
data = sys.stdin.read().strip().splitlines()

# 最初の行に関数、2行目に積分区間が来ることを想定
function_input = data[0].strip()  # 関数の数式
a, b = map(float, data[1].split(','))  # 積分区間の読み取り

# シンボリック変数を定義
x = sp.symbols('x')

try:
    # 数式を解析して関数として定義
    f = sp.sympify(function_input)

    # 定積分の計算
    integral_result = sp.integrate(f, (x, a, b))

    # 結果を分数形式で表示
    integral_result_fraction = sp.nsimplify(integral_result)  # 結果を簡略化（分数形式に変換）
    
    print(f"f(x) = {function_input} の区間 [{a}, {b}] における定積分の結果: {integral_result_fraction}")

except Exception as e:
    print(f"エラー: {e}")

