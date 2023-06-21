from deckshuffle import app
import deckshuffle.cardlist as cardlist
import deckshuffle.shuffle as shuffle
from flask import render_template
from flask import request

# シャッフルするデッキの呼び出し
before_shuffle = cardlist.before_shuffle
after_shuffle = cardlist.after_shuffle


# トップページの呼び出し
@app.route("/")
def index():
    return render_template("index.html")


# トップページの呼び出し(カードリストの初期化)
@app.route("/", methods=["POST"])
def index_post():
    global before_shuffle
    global after_shuffle
    before_shuffle = after_shuffle
    return render_template("index.html")


# シャッフル結果の呼び出し
@app.route("/result", methods=["POST"])
def result_post():
    name = request.form.get("sel")
    count = request.form.get("count")
    global before_shuffle
    for i in range(int(count)):
        if name == "ヒンズーシャッフル":
            before_shuffle = shuffle.hindu(before_shuffle)
        elif name == "スライドシャッフル":
            before_shuffle = shuffle.slide(before_shuffle)
        elif name == "ディールシャッフル(標準)":
            name = "ディールシャッフル"
            before_shuffle = shuffle.deal_stand(before_shuffle)
        elif name == "ディールシャッフル(ランダム)":
            name = "ディールシャッフル"
            before_shuffle = shuffle.deal_random(before_shuffle)
        elif name == "ファローシャッフル(完全)":
            name = "ファローシャッフル"
            before_shuffle = shuffle.farrow_perfect(before_shuffle)
        elif name == "ファローシャッフル(不完全)":
            name = "ファローシャッフル"
            before_shuffle = shuffle.farrow_imperfect(before_shuffle)
        elif name == "ウォッシュシャッフル":
            before_shuffle = shuffle.wash(before_shuffle)
    return render_template(
        "result.html",
        message="{} を {} 回行いました".format(name, count),
        before_card=after_shuffle,
        after_card=before_shuffle,
    )
