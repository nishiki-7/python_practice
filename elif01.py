score = int(input('テストの点数を入力してください >>'))

if score < 0 or score > 100:
    print('異常な得点です')
    print('100点満点で入力し直してください')
elif score >= 80:
    print('高得点ですね！よく頑張りました！')
elif score >= 70:
    print('いい点数です！お疲れ様！')
elif score >= 60:
    print('ギリギリ合格！あぶなかったね。')
else:
    print('不合格！')
    print('何やってんじゃ！')
