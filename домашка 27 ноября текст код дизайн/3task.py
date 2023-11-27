from drawbot_skia.drawbot import rect, saveImage, fill
x = 75 
y = 75
step = 150 
for i in range(6):
    rect(y, x, 100, 100)
    x = x + step
    y = y + step 
saveImage("c:/Users/anast/Desktop/DH/питоновый dh/домашка 27 ноября/diagonal.pdf")