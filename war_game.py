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
    
#====================
# Playerクラスの定義
#====================
# クラスを作成
class Player:
    # 初期設定のコンストラクタ
    def __init__(self, name):
        # インスタンス変数を作成
        # 名前
        self.name = name
        # 手札
        self.hand = []
    # カードを追加するメソッド
    def add_cards(self, new_card):
        self.hand.extend(new_card)
    # 手札の枚数を確認
    def check_hand_size(self):
        return len(self.hand)
    # 場に手札を出すメソッド
    def play_card(self):
        return self.hand.pop()
    
#====================
# Gameクラスの定義
#====================
# クラスを作成
class Game:
    # 初期設定のコンストラクタ
    def __init__(self):
        # player２人を作る
        self.player1 = Player("プレイヤー１")
        self.player2 = Player("プレイヤー２")
        # Deckを１つ作る
        self.deck = Deck()
        # 作ったself.deckをshuffle
        self.deck.shuffle()
        # ループを２６回づつ回してプレイヤー２人にカードを配る
        for _ in range(26):
            # デッキからカードを引いてcard変数に保存
            card = self.deck.deal_card()
            # 引いたカードをプレイヤーに渡す
            self.player1.add_cards([card])
        for _ in range(26):
            # デッキからカードをcard変数に保存
            card = self.deck.deal_card()
            # 引いたカードをプレイヤ２に渡す
            self.player2.add_cards([card])
    # ゲームのメソッドを作成
    def play_game(self):
        # ゲームの開始を宣言
        print("War Gameを始めます。")  
        # whileループでcheck_hand_sizeを利用
        while self.player1.check_hand_size() > 0 and self.player2.check_hand_size() > 0:
            # 現在の各プレイヤーの手札の枚数を表示
            print(f"プレイヤー１の手札の枚数：{self.player1.check_hand_size()} 枚 vs プレイヤー２の手札：{self.player2.check_hand_size()} 枚")
            # 場に出したカードをp1_card変数に格納
            p1_card = self.player1.play_card()
            # 場に出したカードをp2_card変数に格納
            p2_card = self.player2.play_card()
            # プレイヤーが場に出したカードを表示    
            print(f"プレイヤー１が出したカード：{p1_card}")
            print(f"プレイヤー２が出したカード：{p2_card}")
            # 場に出したカードの勝敗を判定する
            # プレイヤー１が勝った場合
            if p1_card > p2_card:
                # プレイヤー１の名前を表示
                print(f"このラウンドは {self.player1.name} の勝ちです。")
                #　プレイヤー１のself.handにカードを追加
                self.player1.add_cards([p1_card, p2_card])
            # プレイヤー２が勝った場合
            elif p1_card < p2_card:
                # プレイヤー２の名前を表示
                print(f"このラウンドは {self.player2.name} の勝ちです。")
                # プレイヤー２のself.handにカードを追加
                self.player2.add_cards([p1_card, p2_card])
            # 引き分けた場合
            else:
                print("引き分けです。")
if __name__ == "__main__":
    game = Game()
    game.play_game()