from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_subscription', methods=['POST'])
def generate_subscription():
    # لینک سابسکریپشن به عنوان الگو
    subscription_url = "https://github.com/v2rayirani/sublink/blob/main/sub.text"

    # دریافت مقادیر از لینک سابسکریپشن
    uuid = request.json.get('uuid')
    domain = request.json.get('domain')
    path = request.json.get('path')

    # جایگزینی مقادیر UUID، domain و path در لینک سابسکریپشن
    subscription_link = subscription_url.replace('domain', domain).replace('uuid', uuid).replace('path', path)

    return jsonify({"subscription_link": subscription_link})

if __name__ == '__main__':
    app.run(debug=True)
