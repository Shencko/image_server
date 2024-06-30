import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from load import load_image, meat
from upload import upload_to_gcs
from werkzeug.utils import secure_filename

load_dotenv()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



@app.route('/', methods=['GET'])
def homepage():
        return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Upload the file to GCS with metadata
       
        destination_blob_name = request.form.get('tag') 
        upload_to_gcs(file_path, destination_blob_name)
        
        return redirect(url_for('upload_success'))
    
@app.route('/upload')
def upload_success():
    return render_template('upload.html')


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        name = request.form['tag']
        print(name)
        metadata = meat(name)        
        image_link = f"https://storage.googleapis.com/{os.environ.get('GOOGLE_CLOUD_STORAGE_BUCKET')}/{name}"
        return render_template('search.html', metadata= metadata, image_link= image_link)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
    