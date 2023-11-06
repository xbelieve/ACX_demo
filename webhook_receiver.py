from flask import Flask, request, jsonify, Response
import logging

app = Flask(__name__)

@app.route('/', methods=['OPTIONS', 'POST', 'GET'])
def webhook_receiver():
    # Handle HTTP OPTIONS request for CORS
    if request.method == 'OPTIONS':
        response_headers = {
            'Webhook-Allowed-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Origin': '*',
        }
        return ('', 200, response_headers)

    # Handle incoming events (assuming JSON data)
    if request.method == 'POST':
        data = request.get_data()

        # Print request data to console and log file
        logging.info(f"Received Data: {data}")
        print(f"Received Data: {data}")

        # Your processing logic here

        return 'Webhook event processed successfully', 200

    if request.method == 'GET' :
        data = request.get_data()
        logging.info(f"Received data: {data}")
        print(f"Received Data: {data}")
        return 'Get request successfully', 200
    # Handle unsupported HTTP methods
    return 'Method Not Allowed', 405

if __name__ == '__main__':
    logging.basicConfig(filename='webhook_receiver.log', level=logging.INFO)
    app.run(host='0.0.0.0', port=3000)