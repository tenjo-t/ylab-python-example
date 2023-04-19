import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Y = [10.3, 11.6, 15.4, 19.0, 25.3, 25.8, 27.5, 32.8, 29.4, 23.3, 17.7, 12.6]
Z = [1.4, 3.3, 6.2, 9.2, 15.3, 18.5, 21.6, 25.2, 21.7, 16.4, 9.3, 5.2]


def plot():
    fig, ax = plt.subplots()
    ax.plot(X, Y)
    plt.show()


def plot_marker():
    fig, ax = plt.subplots()
    # markerの種類
    # "." point
    # "," pixel
    # "o" circle
    # "v" triangle_down
    # "^" triangle_up
    # "<" triangle_left
    # ">" triangle_right
    # "1" tri_down
    # "2" tri_up
    # "3" tri_left
    # "4" tri_right
    # "8" octagon
    # "s" square
    # "p" pentagon
    # "*" star
    # "h" hexagon1
    # "H" hexagon2
    # "+" plus
    # "x" x
    # "D" diamond
    # "d" thin_diamond
    # "|" vline
    # "_" hline
    # "None", None, " ", "" nothing
    ax.plot(X, Y, ".")
    plt.show()


def plot_line_and_marker():
    fig, ax = plt.subplots()
    # lineの種類
    # "-"  solid
    # "--" dashed
    # ":"  dotted
    # "-." dashdot
    ax.plot(X, Y, "o-")
    plt.show()


def plot_line_width():
    fig, ax = plt.subplots()
    ax.plot(X, Y, "o-", lw=2)
    plt.show()


def plot_color():
    fig, ax = plt.subplots()
    # 1文字
    # b (Blue), g (Green), r (Red)
    # c (Cyan), m (Magenta), y (Yellow), k (Black), w (White)
    #
    # HEX
    # #e41a1c, #377eb8, ...
    #
    # RGB
    # (1.0, 0.0, 0.0), (0.8, 0.2, 0.4), ...
    #
    # Gray scale
    # "0.0", "0.5", "1.0"
    ax.plot(X, Y, color="r")  # red
    plt.show()


def plot_subplot():
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(X, Y, "o-", color="r")
    ax2.plot(X, Z, "x-", color="b")
    plt.show()


def plot_subplot_share_x_axis():
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(X, Y, "o-", color="r")
    ax2.plot(X, Z, "x-", color="b")
    plt.show()


def plot_range():
    fig, ax = plt.subplots()
    ax.plot(X, Y)
    ax.set_xlim(1, 12)
    ax.set_ylim(0, 40)
    plt.show()


def plot_label():
    fig, ax = plt.subplots()
    ax.plot(X, Y)
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature (℃)")
    plt.show()


def plot_legend():
    fig, ax = plt.subplots()
    ax.plot(X, Y, label="Highest")
    ax.legend(loc="upper left")


def plot_size():
    # サイズはインチ
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plt(X, Y)
    plt.show()


def plot_dpi():
    fig, ax = plt.subplots(dpi=300)
    ax.plt(X, Y)
    plt.show()


## 棒グラフ ##


def bar():
    fig, ax = plt.subplots()
    ax.bar(X, Y)
    plt.show()


def bar_tick():
    fig, ax = plt.subplots()
    ax.bar(
        X,
        Y,
        tick_label=[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
    )
    plt.show()


def bar_stack():
    fig, ax = plt.subplots()
    ax.bar(X, Y)
    ax.bar(X, Z)
    plt.show()


def horizontal_bar():
    fig, ax = plt.subplots()
    ax.barh(X, Y)
    plt.show()
