# test_disney_anniversary.py
import unittest
from io import StringIO
import sys

# テスト対象のスクリプトをインポート
from disney_anniversary import main

class TestDisneyAnniversary(unittest.TestCase):

    def test_disney_anniversary(self):
        # テスト用の入力
        test_input = "2024\n"
        
        # 標準入力をモック
        sys.stdin = StringIO(test_input)
        
        # 期待する出力
        expected_output = "ディズニーは 1923 年に設立され、今年で 101 周年です。\n"
        
        # 標準出力をキャプチャ
        output = StringIO()
        sys.stdout = output
        
        # スクリプトのメイン部分を実行
        try:
            main()
        except SystemExit:
            pass
        
        # 結果を取得
        result = output.getvalue()
        
        # アサーション
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()

