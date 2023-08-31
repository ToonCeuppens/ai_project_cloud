from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Laad het model bij het opstarten van de app
model = tf.keras.models.load_model('mnist_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    predictions = model.predict(data["input"])
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
