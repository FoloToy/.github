from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
A=ROOT/'profile/assets'
FONT='/System/Library/Fonts/HelveticaNeue.ttc'
CN='/System/Library/Fonts/STHeiti Medium.ttc'
# Theme tokens read from the live AI Passport website.
BG='#0c0c0d'
GREEN='#20e47c'
TEXT='#f5f6f2'
MUTED='#b0b5b2'
PANEL='#17181b'
LINE='#353a37'
def font(size,bold=False,cn=False):
    return ImageFont.truetype(CN if cn else FONT,size,index=0 if cn else (1 if bold else 0))
def text(d,xy,s,size=24,color=TEXT,bold=False,cn=False):
    d.text(xy,s,font=font(size,bold,cn),fill=color)
def contain(im,box):
    im.thumbnail(box,Image.Resampling.LANCZOS); return im
im=Image.new('RGB',(1800,790),BG);d=ImageDraw.Draw(im)
for x in range(960,1800,55):d.line((x,0,x,700),fill='#202321')
for y in range(0,700,55):d.line((960,y,1800,y),fill='#202321')
d.ellipse((1050,65,1740,755),fill='#122a1e',outline='#244a35',width=2)
logo=Image.open(A/'wordmark-white.png').convert('RGBA');logo=logo.crop(logo.getbbox());logo=contain(logo,(280,80));im.paste(logo,(74,60),logo)
text(d,(76,207),'make it',124,bold=True)
text(d,(70,335),'anything.',146,color=GREEN,bold=True)
text(d,(81,540),'简单开放，人人可造。',40,cn=True)
text(d,(83,610),'WEAR.  PLAY.  CREATE.',23,color=MUTED)
product=Image.open(A/'ai-passport.png').convert('RGBA')
product=product.crop(product.getbbox());product=contain(product,(820,650));im.paste(product,(935+(820-product.width)//2,38),product)
d.rounded_rectangle((1303,620,1684,666),radius=23,fill=BG,outline=LINE,width=1)
text(d,(1333,629),'AI PASSPORT / OPEN TO CREATE',18,color=GREEN)
d.rectangle((0,708,1800,790),fill=GREEN)
text(d,(78,735),'OPEN HARDWARE',23,color=BG,bold=True)
text(d,(552,735),'AI COMPANIONS',23,color=BG,bold=True)
text(d,(1065,735),'MADE BY YOU',23,color=BG,bold=True)
d.line((1668,765,1690,743),fill=BG,width=3)
d.line((1671,743,1690,743,1690,762),fill=BG,width=3)
im.save(A/'hero.png',optimize=True)
for name,title,subtitle in [('ai-passport','AI PASSPORT','Wear it. Flash it. Make it anything.'),('magicbox','MAGICBOX','Shape it. Voice it. Make it anything.')]:
    card=Image.new('RGB',(1000,740),PANEL);cd=ImageDraw.Draw(card)
    cd.rectangle((0,0,1000,6),fill=GREEN)
    text(cd,(46,35),title,36,color=GREEN,bold=True)
    text(cd,(46,89),subtitle,22,color=MUTED)
    src=Image.open(A/('ai-passport.png' if name=='ai-passport' else 'magicbox.png')).convert('RGBA')
    if name=='ai-passport':src=src.crop(src.getbbox())
    src=contain(src,(920,540));card.paste(src,((1000-src.width)//2,157+(540-src.height)//2),src)
    card.save(A/(name+'-card.png'),optimize=True)
