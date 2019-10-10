# lesson14 課題： プロ野球チームの勝ち負け数を表示する
# memo: baseball_team.py

from baseball_team import Baseball_Team

# 表の見出し
print("team".ljust(9), "win".ljust(4), "lose".ljust(4), "draw".ljust(4), "rate".ljust(4))

# 結果の表示
Carp = Baseball_Team(name = 'Carp', win = 88, lose = 51, draw = 4)
Carp.show_team_result()

Tigers = Baseball_Team(name = 'Tigers', win = 78, lose = 61, draw = 4)
Tigers.show_team_result()

BayStars = Baseball_Team(name = 'BayStars', win = 73, lose = 65, draw = 5)
BayStars.show_team_result()

Giants = Baseball_Team(name = 'Giants', win = 72, lose = 68, draw = 3)
Giants.show_team_result()

Dragons = Baseball_Team(name = 'Dragons', win = 59, lose = 79, draw = 5)
Dragons.show_team_result()

Swallows = Baseball_Team(name = 'Swallows', win = 45, lose = 96, draw = 2)
Swallows.show_team_result()
