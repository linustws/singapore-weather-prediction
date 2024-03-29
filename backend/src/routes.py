from flask import Blueprint
from flask import jsonify
from flask import request

from models import cache
from models import start_thread

routes = Blueprint('routes', __name__)


@routes.route('/', methods=['GET'])
def get_data():
    model = cache.get('lstm_model')

    if model is None:
        # Model not setup, setup model and return an error response with 500 status code
        start_thread()
        return jsonify({'error': 'Model not setup'}), 500

    else:
        try:
            data = model.get_data()
        except Exception as e:
            return jsonify({'error': 'Prediction error: {}'.format(str(e))}), 500

    # Return the prediction as a JSON response
    return jsonify({'data': data})


@routes.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Parse JSON data from the request body
        print('Received data:', data)

        input_data = data['value']
        selected_option = data['type']

        # Log a message to indicate that the endpoint is called
        print('Prediction endpoint called. Input:', input_data, 'Type:', selected_option)

    except Exception as e:
        # An error occurred, return an error response with 400 status code
        return jsonify({'error': 'Invalid JSON format'}), 400

    if selected_option == 'year':
        num_months = int(input_data) * 12
    else:
        num_months = int(input_data)

    model = cache.get('lstm_model')

    if model is None:
        # Model not setup, setup model and return an error response with 500 status code
        start_thread()
        return jsonify({'error': 'Model not setup'}), 500

    else:
        try:
            # Perform prediction using the model
            prediction = model.predict(num_months)
        except Exception as e:
            # An error occurred during prediction, return an error response with 500 status code
            return jsonify({'error': 'Prediction error: {}'.format(str(e))}), 500

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})
