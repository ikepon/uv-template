# Example Package

example_packageはuvテンプレートプロジェクトのサンプルパッケージです。テンプレートの使い方と開発パターンを示すために作成されています。

## 📦 機能

### 主要な関数

#### `greeting(name: str) -> str`
名前を受け取って挨拶メッセージを生成します。

```python
from example_package import greeting

# 基本的な使用例
message = greeting("World")
print(message)  # "Hello, World!"

# エラーハンドリング
try:
    greeting("")  # ValueError が発生
except ValueError as e:
    print(f"エラー: {e}")
```

#### `calculate_sum(numbers: list[int | float]) -> int | float`
数値のリストの合計を計算します。

```python
from example_package import calculate_sum

# 整数のリスト
result = calculate_sum([1, 2, 3, 4, 5])
print(result)  # 15

# 小数点を含むリスト
result = calculate_sum([1.5, 2.5, 3.0])
print(result)  # 7.0

# エラーハンドリング
try:
    calculate_sum([])  # ValueError が発生
except ValueError as e:
    print(f"エラー: {e}")
```

#### `is_even(number: int) -> bool`
数値が偶数かどうかを判定します。

```python
from example_package.main import is_even

print(is_even(2))   # True
print(is_even(3))   # False
print(is_even(0))   # True
```

## 🖥️ コマンドラインインターフェース

パッケージをインストールすると、`example-cli`コマンドが使用できます。

### インストール

```bash
# 開発モードでインストール
uv sync --all-extras

# または本番用インストール
uv sync
```

### 使用方法

#### greetコマンド
指定した名前で挨拶メッセージを表示します。

```bash
# 基本的な使用例
example-cli greet "Python"
# 出力: Hello, Python!

example-cli greet "世界"  
# 出力: Hello, 世界!
```

#### sumコマンド
複数の数値の合計を計算します。

```bash
# 整数の合計
example-cli sum 1 2 3 4 5
# 出力: Sum: 15

# 小数点を含む数値
example-cli sum 1.5 2.5 3.0
# 出力: Sum: 7.0

# 単一の数値
example-cli sum 42
# 出力: Sum: 42
```

#### ヘルプの表示

```bash
# メインヘルプ
example-cli --help

# サブコマンドのヘルプ
example-cli greet --help
example-cli sum --help
```


### doctestの実行

関数のdocstringに含まれる例をテストできます：

```bash
python -m doctest src/example_package/main.py -v
```

## 🔧 カスタマイズ方法

このサンプルパッケージをベースに独自の機能を実装する場合：

1. **パッケージ名を変更**
   ```bash
   # ディレクトリ名を変更
   mv src/example_package src/your_package_name
   
   # pyproject.tomlのスクリプト設定も更新
   ```

2. **新しい関数を追加**
   ```python
   # src/your_package_name/main.py に関数を追加
   def your_function(param: str) -> str:
       """Your function description."""
       return f"Result: {param}"
   ```

3. **CLIコマンドを拡張**
   ```python
   # src/your_package_name/cli.py にサブコマンドを追加
   your_parser = subparsers.add_parser("your-command", help="Your command help")
   your_parser.add_argument("param", help="Parameter description")
   ```

4. **テストを追加**
   ```python
   # tests/ に対応するテストファイルを作成
   def test_your_function():
       result = your_function("test")
       assert result == "Result: test"
   ```

## 📚 参考資料

- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [pytest Documentation](https://docs.pytest.org/)
- [uv Documentation](https://docs.astral.sh/uv/)