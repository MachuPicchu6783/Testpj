# lesson14 課題： プロ野球チームの勝ち負け数を表示する
# memo: use_baseball_team.py; 継承

# クラス
class Baseball_Team:  
    
    # 初期化する特殊メソッド
    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw
    
    # 表示するメソッド
    def show_team_result(self):
        print("{:<10}".format(self.name), end="")
        print("{:<5}".format(self.win), end="")
        print("{:<5}".format(self.lose), end="")
        print("{:<5}".format(self.draw), end="")
        #勝率
        rate = self.calc_win_rate()
        print(round(rate, 3))
    
    # 計算メソッド
    def calc_win_rate(self):  # selfはクラスBaseball_Teamを指す
        rlt = self.win / (self.win + self.lose)
        return rlt
