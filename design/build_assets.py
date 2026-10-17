from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
A=ROOT/'profile/assets'
FONT='/System/Library/Fonts/HelveticaNeue.ttc'
CN='/System/Library/Fonts/STHeiti Medium.ttc'
def font(size,bold=False,cn=False):
    return ImageFont.truetype(CN if cn else FONT,size,index=0 if cn else (1 if bold else 0))
def text(d,xy,s,size=24,color='#171918',bold=False,cn=False):
    d.text(xy,s,font=font(size,bold,cn),fill=color)
def contain(im,box):
    im.thumbnail(box,Image.Resampling.LANCZOS); return im
im=Image.new('RGB',(1800,790),'#f5f3ec');d=ImageDraw.Draw(im)
# Quiet grid and framing give the real product room to breathe.
for x in range(960,1800,55):d.line((x,0,x,700),fill='#e7e5dd')
for y in range(0,700,55):d.line((960,y,1800,y),fill='#e7e5dd')
d.ellipse((1080,95,1725,740),fill='#edebe2')
logo=Image.open(A/'wordmark.png').convert('RGBA'); logo=contain(logo,(280,80));im.paste(logo,(74,60),logo)
text(d,(76,190),'MAKE AI',106,bold=True)
text(d,(76,310),'SOMETHING',106,bold=True)
text(d,(76,430),'REAL.',106,color='#f36a35',bold=True)
text(d,(81,572),'让 AI 走进真实世界。',40,cn=True)
product=Image.open(A/'ai-passport.png').convert('RGBA')
product=product.crop(product.getbbox());product=contain(product,(820,650));im.paste(product,(935+(820-product.width)//2,38),product)
d.rounded_rectangle((1303,620,1684,666),radius=23,fill='#171918')
text(d,(1333,629),'AI PASSPORT / OPEN TO CREATE',18,color='#ffffff')
d.rectangle((0,708,1800,790),fill='#f36a35')
text(d,(78,735),'OPEN HARDWARE',23,bold=True)
text(d,(552,735),'AI COMPANIONS',23,bold=True)
text(d,(1065,735),'MADE BY YOU',23,bold=True)
d.line((1668,765,1690,743),fill='#171918',width=3)
d.line((1671,743,1690,743,1690,762),fill='#171918',width=3)
im.save(A/'hero.png',optimize=True)
# Consistent product-card canvases; preserve source photographs and aspect ratio.
for name,title,subtitle in [('ai-passport','AI PASSPORT','Wear it. Flash it. Make it anything.'),('magicbox','MAGICBOX','Shape a character. Give it a voice.')]:
    card=Image.new('RGB',(1000,740),'#f5f3ec');cd=ImageDraw.Draw(card)
    text(cd,(46,35),title,36,bold=True);text(cd,(46,89),subtitle,22,color='#64665e')
    src=Image.open(A/('ai-passport.png' if name=='ai-passport' else 'magicbox.png')).convert('RGBA')
    if name=='ai-passport':src=src.crop(src.getbbox())
    src=contain(src,(920,540));card.paste(src,((1000-src.width)//2,157+(540-src.height)//2),src)
    card.save(A/(name+'-card.png'),optimize=True)
