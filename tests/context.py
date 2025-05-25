"""
テストモジュールが product_api パッケージをインポートできるようにするヘルパー。
uv pip install -e . を実行せずに、開発中のコードをテストできます。
"""
import os
import sys

# プロジェクトルートをPythonパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# アプリケーションモジュールをインポート
import product_api