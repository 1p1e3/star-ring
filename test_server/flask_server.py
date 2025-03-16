"""
测试使用
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

user_list = []

@app.route("/login", methods=["POST"])
def login():
    request_data = request.get_json()
    email = request_data["email"]
    password = request_data["password"]

    for user in user_list:
        if user["email"] == email and user["password"] == password:
            return jsonify({"msg": "登录成功", "token": "1a2b3c"})

    if email is None or password is None:
        return jsonify({"msg": "用户名或密码不能为空"})
    elif email != "test@gmail.com" or password != "00000":
        return jsonify({"msg": "用户名或密码错误"})
    elif email.split("@")[1] not in ["gmail.com", "outlook.com", "qq.com"]:
        return jsonify({"msg": "暂不支持该邮箱"})
    else:
        return jsonify({"msg": "未知错误"})




@app.route("/register", methods=["POST"])
def register():
    request_data = request.get_json()
    email = request_data["email"]
    password = request_data["password"]
    re_password = request_data["repassword"]

    for user in user_list:
        if user["email"] == email:
            return jsonify({"msg": "用户已存在"})

    if email is None or password is None or re_password is None:
        return jsonify({"msg": "用户名或密码不能为空"})

    if "@" not in email:
        return jsonify({"msg": "请输入邮箱"})

    if email.split("@")[1] not in ["gmail.com", "outlook.com", "qq.com"]:
        return jsonify({"msg": "暂不支持该邮箱"})

    if password != re_password:
        return jsonify({"msg": "两次密码不一致"})

    if len(password) < 8 or len(password) > 16:
        return jsonify({"msg": "密码长度要在 8 - 16 之间"})
    else:
        user_list.append({"email": email, "password": password })
        return jsonify({"msg": "注册成功"})

if __name__ == '__main__':
    app.run(debug=True)