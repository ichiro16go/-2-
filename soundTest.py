import pyxel

pyxel.init(200, 200)

def play_sound():
    pyxel.play(0, 0)

def update():
    if pyxel.btnp(pyxel.KEY_SPACE):
        play_sound()

def draw():
    pyxel.cls(0)
    pyxel.text(50, 100, "Press SPACE to play sound", 7)

# 音声データの設定
# pyxel.sound(0).set(
#     notes="C3E3G3C4",  # ドレミファソラシド
#     tones="S",        # サイン波
#     volumes="3",      # 音量
#     effects="NNNN",   # エフェクト（指定なし）
#     speed=10          # 再生速度
# )
pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)


pyxel.run(update, draw)
