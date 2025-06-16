"""
テストモジュールが product_api パッケージをインポートできるようにするヘルパー。

srcレイアウトに対応したパス設定を行います。
"""
import os
import sys

# srcディレクトリをPythonパスに追加
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_path)

# アプリケーションモジュールをインポート
import product_api