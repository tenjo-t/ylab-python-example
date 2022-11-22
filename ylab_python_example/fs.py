from pathlib import Path

# テキストファイルを読み込む
def read_text_file():
    path = Path.cwd()

    # 1行ずつ読み込む
    with path.open(mode="r", encoding="utf-8") as f:
        for l in f:
            pass

    # 1度に読み込む
    with path.open(mode="r", encoding="utf-8") as f:
        text = f.read()


# テキストファイルに書き込む
def write_text_file():
    path = Path.cwd()

    # mode="w" 上書きモード
    # mode="a" 追記モード
    # mode="x" ファイルが存在しないときに新規作成して書き込み
    with path.open(mode="w", encoding="utf-8") as f:
        # 書き込む
        # writeメソッドは改行を自動で入れない
        f.write("foo\n")

        # witelinesメソッドは改行を自動で入れる
        f.writelines(["foo", "bar"])


# 実行したディレクトリにあるファイル・フォルダのパスを得る
def walk_dir():
    for path in Path.cwd().glob("*"):
        pass


# 実行したディレクトリにあるCSVファイルのパスを得る
def walk_csv():
    for path in Path.cwd().glob("*.csv"):
        pass


# 実行したディレクトリ以下にある全てのファイル・フォルダのパスを得る
def walk_dir_all():
    for path in Path.cwd().glob("**/*"):
        pass


# 実行したディレクトリ以下にある全てのCSVファイルのパスを得る
def walk_csv_all():
    for path in Path.cwd().glob("**/*.csv"):
        pass
