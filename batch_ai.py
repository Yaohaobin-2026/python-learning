import pandas as pd
import requests
import time

# 1. 填上你的通行证
API_KEY = ""
url = ""
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 2. 用 pandas 读取刚才的表格
df = pd.read_csv('reviews.csv')
print(f"成功读取数据，共 {len(df)} 条评价。开始让 AI 分析...")

# 准备一个空列表，用来装 AI 分析后的结果
results = []

# 3. 开启循环，一行一行处理表格里的数据
for index, row in df.iterrows():
    comment = row['comment']

    # 给 AI 设定一个任务（Prompt）
    question = f"请判断以下用户评价是【好评】、【中评】还是【差评】，直接回答这四个字，不要多余的话。评价内容：{comment}"

    data = {
        "model": "kimi-k3",
        "messages": [{"role": "user", "content": question}]
    }

    # 开始请求
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            answer = response.json()['choices'][0]['message']['content']
            # 把 AI 的回答清理一下（去掉可能带的空格或换行）
            ai_sentiment = answer.strip()
            print(f"第 {row['id']} 条评价 -> AI 判定结果：{ai_sentiment}")
        else:
            ai_sentiment = "分析失败"
            print(f"第 {row['id']} 条请求失败，错误码：{response.status_code}")

    except Exception as e:
        ai_sentiment = "网络错误"
        print(f"第 {row['id']} 条网络断开了。")

    # 把结果存进列表
    results.append(ai_sentiment)

    # 极其重要：防止请求太快被服务器封禁，每次休息 1 秒钟
    time.sleep(20)

# 4. 把结果作为新的一列，加到原来的表格里
df['AI判定'] = results

# 5. 把带有 AI 判定结果的新表格保存下来！
df.to_csv('reviews_result.csv', index=False, encoding='utf-8-sig')
print("\n太棒了！所有数据分析完毕，已保存到 reviews_result.csv 文件中。")