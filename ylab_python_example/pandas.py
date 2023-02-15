import pandas as pd

# CSVの読み込み
def read_csv():
    df = pd.read_csv("./example.csv")

    # Headerなし
    df = pd.read_csv("./example.csv", header=None)
    # Headerを渡す
    df = pd.read_csv("./example.csv", header=("foo", "bar", "baz"))
    # Headerの行を指定する（2行目）
    # Headerより前の行は無視される
    df = pd.read_csv("./example.csv", header=2)

    # 特定の行をスキップ（3行スキップ）
    df = pd.read_csv("./example.csv", skiprows=3)
    # 特定の行をスキップ（2,5,8行目をスキップ）
    df = pd.read_csv("./example.csv", skiprows=[2, 5, 8])
    # 特定の行のみ読み込む（0,3,4行目のみ）
    df = pd.read_csv("./example.csv", skiprows=lambda x: x not in [0, 3, 4])
    # 最初の数行を読み込む
    df = pd.read_csv("./example.csv", nrows=4)

    # 文字列として読み込み
    df = pd.read_csv("./example.csv", dtype=str)

    # どの値も欠陥値として扱わない
    # 欠陥値:
    #   "", "#N/A", "#N/A N/A", "#NA", "-1.#IND", "-1.#QNAN", "-NaN", "-nan",
    #   "1.#IND", "1.#QNAN", "N/A", "NA", "NULL", "NaN", "n/a", "nan", "null"
    df = pd.read_csv("./example.csv", na_filter=False)

    # エンコーディングを指定
    df = pd.read_csv("./example.csv", encoding="utf-8")


# TSV (Tab Separated Values)の読み込み
def read_tsv():
    df = pd.read_table("./example.tsv")

    # CSVと一緒


# DataFrameに列を追加
def add_column():
    df = pd.DataFrame(
        {"A": ["A1", "A2", "A3"], "B": ["B1", "B2", "B3"], "C": ["C1", "C2", "C3"]},
        index=["ONE", "TWO", "THREE"],
    )

    # スカラーを追加
    # 全ての列が同じ値になる
    df["A"] = 0

    # Array-likeオブジェクトを追加
    # list, np.ndarrayなど
    df["E"] = [0, 1, 2]

    # Seriesを追加
    # DataFrameの列への参照はSeriesとなっている
    df["F"] = df["B"] + df["C"]


# DataFrameやSeriesを連結する
def concat_df():
    df1 = pd.DataFrame(
        {"A": ["A1", "A2", "A3"], "B": ["B1", "B2", "B3"], "C": ["C1", "C2", "C3"]},
        index=["ONE", "TWO", "THREE"],
    )
    df2 = pd.DataFrame(
        {"C": ["C2", "C3", "C4"], "D": ["D2", "D3", "D4"]},
        index=["TWO", "THREE", "FOUR"],
    )
    s1 = pd.Series(["X1", "X2", "X3"], index=["ONE", "TWO", "THREE"], name="X")
    s2 = pd.Series(["Y2", "Y3", "Y4"], index=["TWO", "THREE", "FOUR"], name="Y")

    # DataFrameを連結する（縦方向）
    df = pd.concat([df1, df2])
    # DataFrameを連結する（横方向）
    df = pd.concat([df1, df2], axis=1)

    # 共通部分のみを残す
    df = pd.concat([df1, df2], join="inner")

    # Seriesを連結する（縦方向）
    sr = pd.concat([s1, s2])
    # Seriesを連結する（横方向）
    df = pd.concat([s1, s2], axis=1)

    # DataFrameとSeriesを連結（列）
    df = pd.concat([df1, s2], axis=1)
    # DataFrameとSeriesを連結（行）
    df = df1.append(s1)
