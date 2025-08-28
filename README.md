# uv Python プロジェクトテンプレート

[uv](https://github.com/astral-sh/uv)を使った高速で信頼性の高い依存関係管理とプロジェクトツーリングを備えたモダンなPythonプロジェクトテンプレートです。

## 🚀 特徴

- **高速な依存関係管理**: uvによる超高速パッケージインストール
- **モダンなPythonツール**: Ruff（リンター/フォーマッター）とmypy（型チェック）が事前設定済み
- **テスト環境**: カバレッジレポート付きpytestがすぐに使える
- **Pre-commitフック**: コミット前の自動コード品質チェック
- **CI/CD対応**: GitHub Actionsワークフローでテストとリンティング
- **Python 3.13+**: 最新のPythonバージョンに対応
- **開発ツール**: IPythonとipdbによるインタラクティブデバッグツール同梱

## 📋 必要要件

- Python 3.13以上
- [uv](https://github.com/astral-sh/uv) （インストール: `curl -LsSf https://astral.sh/uv/install.sh | sh` または `brew install uv`）

## 🏁 使い始める

### このテンプレートを使う

1. このリポジトリの **「Use this template」** ボタン（緑色）をクリック
2. 「Create a new repository」を選択
3. リポジトリ名とオーナーを設定して「Create repository from template」をクリック
4. 作成したリポジトリをクローン:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git
cd YOUR_PROJECT_NAME
```

### プロジェクトのセットアップ

1. **プロジェクトをカスタマイズ**:
   - `pyproject.toml`のプロジェクトメタデータを更新:
     - `name = "project-name"` をあなたのプロジェクト名に変更
     - `description` を更新
     - 必要に応じてPythonバージョンを調整
   - `LICENSE`ファイルの著者名を変更
   - `src/example_package/`をあなたのパッケージ名にリネーム

2. **プロジェクトの初期化**:
```bash
# 仮想環境を作成して依存関係をインストール
uv venv
source .venv/bin/activate  # Windowsの場合: .venv\Scripts\activate

# 開発モードでプロジェクトをインストール
uv sync --all-extras

# pre-commitフックをインストール
pre-commit install

# 初回テストとリンティングを実行して動作確認
pytest
ruff check .
mypy src/
```

## 📁 プロジェクト構造

```
YOUR_PROJECT/
├── src/                    # ソースコードディレクトリ
│   └── your_package/       # メインパッケージ
├── tests/                  # テストファイル
├── .github/                # GitHub関連ファイル
│   └── workflows/          # GitHub Actionsワークフロー
├── .gitignore             # Git無視ルール
├── .pre-commit-config.yaml # Pre-commitフック設定
├── pyproject.toml         # プロジェクト設定と依存関係
├── README.md              # プロジェクトドキュメント
└── LICENSE                # ライセンスファイル
```

## 🛠️ 開発ワークフロー

### 依存関係の追加

```bash
# プロダクション依存関係を追加
uv add requests

# 開発用依存関係を追加
uv add --dev pytest-mock

# すべての依存関係をインストール（uv.lockから）
uv sync
```

### テストの実行

```bash
# すべてのテストを実行
pytest

# カバレッジ付きで実行
pytest --cov

# 特定のテストファイルを実行
pytest tests/test_specific.py
```

### コード品質

```bash
# Ruffでコードをフォーマット
ruff format .

# コードをリント
ruff check .

# 型チェック
mypy src/

# すべてのpre-commitフックを実行
pre-commit run --all-files
```

### パッケージの作成

1. `src/`内にパッケージディレクトリを作成:
```bash
mkdir -p src/your_package_name
touch src/your_package_name/__init__.py
```

2. `src/your_package_name/`内にコードモジュールを追加

3. `tests/`ディレクトリにテストを記述

## 🧪 テスト

pytestとカバレッジレポートが設定済み:

- テストファイルは`tests/`ディレクトリに配置
- テストファイル名は`test_`プレフィックスを付ける
- カバレッジレポートは`htmlcov/`にHTML形式で生成

## 🔧 設定

### Ruff（リンティング＆フォーマット）
- 設定は`pyproject.toml`の`[tool.ruff]`セクション
- 行長: 120文字
- モダンなPythonリンティングルールを含む

### Mypy（型チェック）
- 設定は`pyproject.toml`の`[tool.mypy]`セクション
- 厳格な型チェックを有効化
- Python 3.13ターゲット

### Pre-commit
- フックは`.pre-commit-config.yaml`で定義
- git commit時に自動実行
- 含まれるもの: 末尾空白、ファイル終端修正、ruff、mypy

## 📦 ビルドと配布

パッケージのビルド方法:

```bash
# パッケージをビルド
uv build

# ビルドされたファイルはdist/に出力
ls dist/
```

## 🤝 コントリビューション

1. リポジトリをフォーク
2. フィーチャーブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📄 ライセンス

このテンプレートはMITライセンスで提供されています。使用時は:
1. LICENSEファイルの情報を更新
2. プロジェクトに適切なライセンスを選択

## 🔗 参考資料

- [uvドキュメント](https://github.com/astral-sh/uv)
- [Pythonパッケージングガイド](https://packaging.python.org/)
- [Ruffドキュメント](https://docs.astral.sh/ruff/)
- [pytestドキュメント](https://docs.pytest.org/)
- [mypyドキュメント](https://mypy-lang.org/)

## 💡 Tips

- `uv lock --upgrade`で依存関係を最新に保つ
- `uv tree`でインストール済みパッケージの依存関係ツリーを確認
- `uv sync`でuv.lockファイルと環境を同期
- プロジェクト間の分離のため仮想環境を使用

---

*[uv-template](https://github.com/ikepon/uv-template)から生成*
