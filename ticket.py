from PIL import Image, ImageDraw, ImageFont

f = ImageFont.truetype('V:\Pictures\TRAINS\FONT\Dubai.ttf', 60)

for x in range(0,100):
    number = str(x).zfill(4)
    base = Image.open('V:/Pictures/TRAINS/TICKETS/blank.png')
    
    ltext = Image.new('RGBA', (1000,1000),(0,0,0,0))
    left = ImageDraw.Draw(ltext)
    left.text((420,180), '#'+ number, font=f, fill=(0,200,0))
    l=ltext.rotate(90, expand=1)
    
    layer = Image.alpha_composite(base, l)
    
    rtext = Image.new('RGBA', (1000,1000),(0,0,0,0))
    right = ImageDraw.Draw(rtext)
    right.text((420,170), '#'+ number, font=f, fill=(0,200,0))
    r=rtext.rotate(270, expand=1)
    
    ticket = Image.alpha_composite(layer, r)
    
    ticket.save("V:/Pictures/TRAINS/TICKETS/"+number+".png")
    #ticket.show()