from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Variáveis
nome_cl = 'Supermercado Galves'
telefone_cl = "(11) 99999-9999"


#abrindo imagem base
def image_sizing(file):
    image = Image.open(file)
    return image.size

image_base = Image.open('quadrado.png')
width_base, height_base = image_base.size

print("Largura de: " + str(width_base))
print("Altura de: " + str(height_base))

#abrindo whatsapp icon
image_whats = Image.open('whatsapp_icon.png')
width_whats, height_whats = image_whats.size

print("Largura de: " + str(width_whats))
print("Altura de: " + str(height_whats))

#ajustando tamanho do icone do whatsapp e colando na imagem base
if width_base == 1200:
    whats_basewidth = 124
    wpercent = whats_basewidth/float(width_whats)
    hsize = int((float(height_whats)*float(wpercent)))
    image_whats = image_whats.resize((whats_basewidth, hsize), Image.ANTIALIAS)
    image_base.paste(image_whats, (307,1374), image_whats.convert('RGBA'))
else:
    whats_basewidth = 90
    wpercent = whats_basewidth/float(width_whats)
    hsize = int((float(height_whats)*float(wpercent)))
    image_whats = image_whats.resize((whats_basewidth, hsize), Image.ANTIALIAS)
    image_base.paste(image_whats, (274,1475), image_whats.convert('RGBA'))

#Adicionando o nome do estabelecimento e número de telefone
I1 = ImageDraw.Draw(image_base)

if width_base == 1200:
    nameFont = ImageFont.truetype('Roboto-Bold.ttf', 36)
    I1.text((438,1374), nome_cl, font = nameFont, fill=(0, 0, 0))
    telFont = ImageFont.truetype('Roboto-Bold.ttf', 60)
    I1.text((427,1414), telefone_cl, font = telFont, fill=(0, 0, 0))
else:
    nameFont = ImageFont.truetype('Roboto-Bold.ttf', 36)
    I1.text((364,1475), nome_cl, font = nameFont, fill=(0, 0, 0))
    telFont = ImageFont.truetype('Roboto-Bold.ttf', 45)
    I1.text((364,1508), telefone_cl, font = telFont, fill=(0, 0, 0))

image_base.show()

image_base.save("teste2.png")