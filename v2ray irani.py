from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_subscription', methods=['POST'])
def generate_subscription():
    # لینک سابسکریپشن واقعی شما
    subscription_url = "https://github.com/v2rayirani/sublink/blob/main/sub.text"

    # دریافت مقادیر از درخواست JSON
    uuid = request.json.get('uuid')
    domain = request.json.get('domain')
    path = request.json.get('path')

    # جایگزینی مقادیر UUID، domain و path در لینک سابسکریپشن
    subscription_link = subscription_url.replace('domain', domain).replace('uuid', uuid).replace('path', path)

    # استخراج کانفیگ‌ها از لینک سابسکریپشن
    config_params = subscription_link.split("?")[-1].split("&")
    config = {}
    for param in config_params:
        key, value = param.split("=")
        config[key] = value

    # جایگزینی مقادیر کانفیگ با مقادیر ورودی کاربر
    for key in config.keys():
        if key != 'uuid' and key != 'domain' and key != 'path':
            config[key] = request.json.get(key)

    # ایجاد لینک نهایی با مقادیر جدید
    final_subscription_url = subscription_link.split("?")[0] + "?"
    final_subscription_url += "&".join([f"{key}={value}" for key, value in config.items()])

    return jsonify({"subscription_link": final_subscription_url})

if __name__ == '__main__':
    app.run(debug=True)
