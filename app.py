from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/ads.txt')
def ads_txt():
    return send_from_directory('static', 'ads.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jpeg-to-png')
def jpeg_to_png():
    return render_template('converter.html', 
                         title='JPEG to PNG Converter',
                         from_format='JPEG',
                         to_format='PNG')

@app.route('/pdf-to-img')
def pdf_to_img():
    return render_template('converter.html',
                         title='PDF to Image Converter',
                         from_format='PDF',
                         to_format='Image')

@app.route('/img-to-pdf')
def img_to_pdf():
    return render_template('converter.html',
                         title='Image to PDF Converter',
                         from_format='Image',
                         to_format='PDF')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)