from flask import Flask, request, jsonify
from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model # Tensorflow 2.14.0
from flask_cors import CORS

np.set_printoptions(suppress=True)

# Faz o model
def make_model():
    model = load_model('keras_model.h5')

    class_names = open("labels.txt", "r").readlines()
    return model, class_names

app = Flask(__name__)

CORS(app)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' in request.files:
        image = request.files['image']

        try:
            image = request.files['image'].read()
            with open('imagem.jpg', 'wb') as f:
                f.write(image)
        except Exception as e:
            return jsonify('Erro ao abrir a imagem: {}'.format(str(e)), 400)

        model, class_names = make_model()

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image  = Image.open("imagem.jpg").convert("RGB")

        size = (224, 224)

        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        data[0] = normalized_image_array

        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        result_dict = {
            "identifiedClass": str(class_name[2:]).strip(),
            "confidence": str(confidence_score).strip()
        }

        return jsonify(result_dict)
    else:
        return jsonify('Nenhuma imagem foi encontrada na requisição.', 400)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)
