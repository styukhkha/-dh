from drawbot_skia.drawbot import rect, saveImage, polygon, fill, stroke, strokeWidth
fill(1, 0, 0)
rect(500, 50, 100, 100)

fill(None)
stroke(0, 0, 1)
strokeWidth(100)
polygon((10, 90), (50, 370), (400, 600), (20, 5))
saveImage('hello_drawbot.pdf')

