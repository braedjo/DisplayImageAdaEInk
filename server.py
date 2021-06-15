from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

#import mainn as mad

app = Flask(__name__)


@app.route('/upload')
def upload_filer():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename('CurDis.png'))
        mad.display.image(f)
        mad.display.display()
        return 'file uploaded successfully'


app.run(debug=True, port=443, host='0.0.0.0')
