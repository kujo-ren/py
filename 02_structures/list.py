import random

fortunes = {
    "大吉": "最高の運勢。何をやってもうまくいく日",
    "中吉": "良い運勢。計画を進めるのに適してる",
    "小吉": "まあまあの運勢。無理しなければ大丈夫",
    "末吉": "ちょっと注意。焦らず進めようね",
    "凶": "今日は慎重に行動しよう",
    "大凶": "何もしない日と思うくらいが吉。ゆっくり過ごそう"
}

result = random.choice(list(fortunes.keys()))

print(f"おみくじ結果: {result}")
print(f"説明: {fortunes[result]}")
