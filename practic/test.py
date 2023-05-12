from captcha.image import ImageCaptcha
from random import choice

a = 6

alphabet = ['1','2','3','4','5','6','7','8','9','a','f','g','h','r','e','k','z','i']

pattern = []

for i in range(a):
    pattern.append(choice(alphabet))

image_captcha = ImageCaptcha(width=300, height=200)
captc = [print(end=''.join(i)) for i in pattern] 
image_captcha.write(pattern, 'capctha.jpg')