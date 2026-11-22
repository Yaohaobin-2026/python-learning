import requests
import json

# 1. 填上你刚才申请的通行证（注意保留引号，把中间的字换掉）
API_KEY = "sk-ms-SW63dcoVUzXPVs4i726BK023McIW5bTKmL9VE5EhELwklZU8Ffrfvhqs"

# 2. 告诉大模型你要问的问题
question = "我想知道5+4=多少"

# 3. 准备发送给 DeepSeek 的“包裹”
url = "https://api.moonshot.cn/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
data = {
    "model":"kimi-k3",
    "messages": [
        {"role": "user", "content": question}
    ]
}

# 4. 发送包裹，并接收回复
print("正在呼叫 AI，请稍等...")
response = requests.post(url, headers=headers, json=data)

# 5. 把 AI 的回答提取出来并打印
if response.status_code == 200:
    result = response.json()
    answer = result['choices'][0]['message']['content']
    print("\n=== AI 老板的回复 ===")
    print(answer)
else:
    print(f"\n呼叫失败，错误码：{response.status_code}")
    print(response.text)
#错误判断
try:
    response=requests.post(url,headers=headers,json=data)
    if response.status_code == 200:
        result = response.json()
        answer = result['choices'][0]['message']['content']
        print('ai回复')
        print(answer)
    else:
     print(f'服务器错误{response.status_code}')

except requests.exceptions.RequestException as e:
    print('网络断开，请检查wifi')
    print(e)

