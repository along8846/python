from PIL import Image, ImageDraw, ImageFont, ImageFilter

# def stamp_num(img,num):
#     drawSurface = ImageDraw.Draw(img)
#     print(img.size)
#     numFont = ImageFont.truetype('ArialHB.ttc',300)
#     drawSurface.text((600,0),num,fill=(255,0,0),font=numFont)
#     img = img.resize((img.size[0]/5,img.size[1]/5))
#     img.save("/Users/apple/Desktop/along/WechatIMG11_1.jpeg")
#     img.show()

# if __name__ =='__main__':
#     img = Image.open('/Users/apple/Desktop/along/WechatIMG11.jpeg')
#     stamp_num(img,"99999999")


img = Image.open('/Users/apple/Desktop/along/WechatIMG11.jpeg')
# 获取图像尺寸
w, h = img.size
print("Original image size: {w},{h}".format(w=w,h=h))

img2 = img.filter(ImageFilter.BLUR)
img2.save("/Users/apple/Desktop/along/WechatIMG11_2.jpeg")