import requests

API_KEY = ""  # 记得换成你新建的！
url = ""
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 这就是 AI 的脑子（记忆列表）
messages = [
    {"role": "system", "content": "你是一个幽默的编程助手，回答尽量简短。"}
]

print("=== 聊天机器人已启动（输入 '退出' 结束） ===")

# 开启无限循环，一直跟你聊天
while True:
    user_input = input("\n你: ")

    if user_input == "退出":
        print("再见！")
        break

    # 1. 把你说的话存进记忆
    messages.append({"role": "user", "content": user_input})

    data = {
        "model": "kimi-k3",
        "messages": messages  # 注意看，这里把带记忆的列表传进去了
    }

    print("AI 正在思考...")

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            answer = response.json()['choices'][0]['message']['content']
            print(f"\nAI: {answer}")

            # 2. 把 AI 的回答也存进记忆
            messages.append({"role": "assistant", "content": answer})
        else:
            print(f"\n服务器拒绝了。错误码：{response.status_code}")
            messages.pop()

    except requests.exceptions.RequestException as e:
        print("\n哎呀，网络断开了，请检查你的 WiFi！")
        messages.pop()
