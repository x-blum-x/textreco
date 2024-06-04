from flask import Flask, request
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/api/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return 'Image file is not provided', 400
    file = request.files['image']
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == '__main__':
    app.run(port=3000,debug=True)##mudar conforme necessidades de hospedagem
