from drawbot_skia.drawbot import rect, saveImage
x = 75 
step = 150 
for i in range(6):
    rect(450, x, 100, 100)
    x = x + step
saveImage("c:/Users/anast/Desktop/DH/питоновый dh/домашка 27 ноября/vertical.pdf")