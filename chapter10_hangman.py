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
# 正解のリストを作成
answers_list = []
# with open & "r" & encoding = "utf-8"
# fをエイリアスに設定してseasons.txtファイルを開く
with open("seasons.txt", "r", encoding = "utf-8") as f:
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
    print(answer)
