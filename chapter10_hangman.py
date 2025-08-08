import random
"""新しいPythonファイルの作成:
hangman.py という名前で、
いよいよ本体となるファイルを作成しましょう。"""
# with open & "w" & encoding = "utf-8"
# fをエイリアスに設定
#with open("hangman.py", "w", encoding = "utf-8") as f:

# chapter10_hangman.pyを作成   

"""必要な機能の読み込み:
ランダムな選択をするために、
Pythonのrandomモジュールをimport文で読み込みます。
"""
# ファイルの冒頭にrandomモジュールをインポートするためのセルを用意

"""ファイルから単語リストを作成する:
with open() を使って、seasons.txt を 読み込みモード ("r") で開きます。
エンコーディングの指定(utf-8)も忘れないようにしましょう。
ファイルの中身を一つの文字列として読み取ります。
読み取った文字列を、改行で区切ってリストに変換します。
これには .splitlines() という便利なメソッドが使えます。
"""
# 関数を定義
def get_random_word(filename):
    # 正解のリストを作成
    #answers_list = []・・41行と重複のため不要
# with open & "r" & encoding = "utf-8"
# fをエイリアスに設定してseasons.txtファイルを開く
    with open(filename, "r", encoding = "utf-8") as f:
    # for inループでファイルから文字列を読み取りリストに格納
    #for answer in seasons_list:
    # answers_list = answers_list.append(answer)# fは（）の中に必要？AttributeErrorが出る
        # .appendメソッドの使い方を忘れている
        # 改行で区切り、作成したリストに格納
        # .splitlines()メソッドを利用
        #answers_list = answers_list.splitlines("\n")# AttributError・・わからない
    # 宝の地図を使用　ファイルの中身を一つの文字列として読み取る
        all_text = f.read()
    # 読み取った文字列を改行で区切りリストに格納・・.splitlines()メソッド
        answers_list = all_text.splitlines()# "\n"は入れなくても良い
    """リストからランダムに1つ選ぶ:"""
    answer = random.choice(answers_list)
    """結果の確認:"""
    #print(answer)→return()へ変更
    return answer

"""お題の単語を取得する
昨日完成させたget_random_word()関数を呼び出して、
seasons.txtからランダムな単語を一つ取得し、
secret_wordのような変数に保存します。
"""
# 定義した関数を使いseasons.txtからランダムに単語を選択
hangman_answer = get_random_word("seasons.txt")

"""ゲームボードを作成する
取得したsecret_wordの文字数と
同じ数のアンダースコア_を要素に持つリストを作成し、
boardという変数に保存します。
ヒント: ["_"] * len(secret_word) """
board = ["_"] * len(hangman_answer)

"""ハングマンの絵を準備する
つられた人の絵（stagesリスト）を定義します。
これは、間違えた回数に応じて表示を
切り替えるための部品になります。"""
# hangman_pictureを定義→関数ではなく変数で十分
#def hangman_picture():→コメントアウト
wrong = 0
stages = ["",
        r"___   ",
        r"|     ",
        r"|  |  ",
        r"|  O  ",
        r"| /|\ ",
        r"| / \ ",
        ]
# hangman_answerを１文字ずつ要素に分解したリスト
rletters = list(hangman_answer)

# 初期設定
win = False 

"""初期画面を表示する
最後に、以下の要素を
print()関数を使ってターミナルに表示してみましょう。
「ハングマンへようこそ！」といった歓迎メッセージ。
ハングマンの初期状態の絵（stagesリストの最初の要素）。
作成したboardリスト。見やすくするために、
" ".join(board)という書き方で、
要素の間にスペースを入れて表示するのがおすすめです。
"""
# 初期画面を用意
print("ハングマンへようこそ！")
print(stages[0])#  まだ何も描かれていない画面を表示
print(" ".join(board))
