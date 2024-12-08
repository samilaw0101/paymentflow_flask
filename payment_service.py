from flask import Flask, session, request, jsonify
import os
app = Flask(__name__)

orders = []
app.secret_key = os.urandom(24)

@app.route('/login', methods=['POST'])
def login():
    print(request.json)
    session['user_id'] = request.json.get('user_id')
    return 'Login successful'


@app.route('/order', methods=['POST'])
def create_order():
    if 'user_id' not in session:
        return 'You are not authorized to access this page'

    order_id = len(orders) + 1
    orders.append({'id': order_id})
    return jsonify({'order_id': order_id})


@app.route('/payment', methods=['POST'])
def make_payment():
    if 'user_id' not in session:
        return 'You are not authorized to access this page'

    order_id = request.json.get('order_id')
    if not order_id:
        return jsonify({'error': 'Missing order_id'}), 400

    return jsonify({'message': 'Payment successful'})


if __name__ == '__main__':
    app.run(debug=True)
