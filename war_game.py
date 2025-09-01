# 組み込み関数
import random
#====================
# Cardクラスを定義
#====================
# クラスを作成
class Card:
    # ランクと文字列の対応表
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 11,
                    "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, 
                    "5": 5, "4": 4, "3": 3, "2": 2}
    # 初期設定
    def __init__(self, suit, rank):
        # インスタンス変数を作成
        self.suit = suit
        self.rank = rank
        # 対応表からランクの強さを取得
        #self.value = self.card_values[rank]・・クラス変数
        self.value = Card.card_values[rank]
    # カードの情報を表示
    def __repr__(self):
        return f"{self.suit} の {self.rank}"
    # カードの強さを比較する
    def __gt__(self, other):
        return self.value > other.value# gratert thanメソッド
    
    
#====================
# Deckクラスを定義
#====================
class Deck:
    # 初期設定
    def __init__(self):
        # 空のカードリストを作成
        self.cards = []
        # カードの要素であるスートとランクのリストを作成
        suits = ["スペード", "クラブ", "ダイヤ", "ハート"]
        ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]# Qが小文字だったので修正
        # ２重ループでスートとランク全ての組み合わせのリストを作成
        for suit in suits:
            for rank in ranks:
                # Cardクラスのインスタンスを作成しリストに追加
                self.cards.append(Card(suit, rank))
    # デッキをシャッフルするメソッドを作成
    def shuffle(self):# :が；だったので修正＆インデントが落ちていたので修正
        random.shuffle(self.cards)
    # カードを配るメソッドを作成
    def deal_card(self):
    # １番上のカードを取り出して、リストからは削除＆インデントが落ちていたので修正
        return self.cards.pop()
    

