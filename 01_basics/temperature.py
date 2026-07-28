import random

温度 = random.randint(-30, 40)

if 温度 >= 30:
    print("暑いですクーラーつけろ")
elif 温度 >= 25:
    print("ちょうどいい温度です")
elif 温度 >= 20:
    print("少し寒いです")
elif 温度 >= 15:
    print("寒い暖房つけろ")
elif 温度 >= 5:
    print("凍結☆")
elif 温度 >= -5:
    print("寒すぎるだろ")
elif 温度 >= -30:
    print("北極")
else:
    print("それ以下は地獄")

print(f"今日の気温は{温度}℃です")
