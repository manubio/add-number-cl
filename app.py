from typing import final
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        nome_cl = request.form['nameCL']
        telefone_cl = request.form['telCL']

        #abrindo imagem base
        image_base = Image.open(f)
        width_base, height_base = image_base.size

        #abrindo WhatsApp
        image_whats = Image.open('whatsapp_icon.png')
        width_whats, height_whats = image_whats.size

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

        final_image = image_base
        final_image.save(app.config['UPLOAD_FOLDER'] + filename)

        content = os.path.join(app.config['UPLOAD_FOLDER'] + filename)
        
    return render_template('content.html', cl_image=content) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)