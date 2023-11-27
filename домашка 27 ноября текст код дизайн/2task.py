from drawbot_skia.drawbot import rect, saveImage
y = 75
step = 50 
for i in range(18):
    x = 75 
    for j in range(18):
        rect(y, x, 30, 30)
        x = x + step
    y = y + step
saveImage("c:/Users/anast/Desktop/DH/питоновый dh/домашка 27 ноября/verticalandhorizontal.pdf")