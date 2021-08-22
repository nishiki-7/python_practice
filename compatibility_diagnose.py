player1 = []
player2 = []

print('1人目: 趣味を3つ入力してください')
player1.append(str(input('1つ目の趣味 >>')))
player1.append(str(input('2つ目の趣味 >>')))
player1.append(str(input('3つ目の趣味 >>')))

print('2人目: 趣味を3つ入力してください')
player2.append(str(input('1つ目の趣味 >>')))
player2.append(str(input('2つ目の趣味 >>')))
player2.append(str(input('3つ目の趣味 >>')))

input('心の準備ができたらEnterキーを押してください')

common = set(player1) & set(player2)
total = set(player1) | set(player2)

compatibility_rate = len(common) / len(total) * 100
print(f'相性度は{compatibility_rate}パーセントでした')
