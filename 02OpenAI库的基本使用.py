# 1. 获取client对象
from openai import OpenAI
import os

print("=== 开始测试 API Key ===")
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3.7-max",
    messages=[{"role": "system", "content": "你是一个Python编程专家,并且不说废话简单回答"},
    {"role": "assistant", "content": "你好,我是Python编程专家,很高兴为你服务"},
    {"role": "user", "content": "输出1-10的数字,使用python代码"}]
)

# 3. 打印结果
print(response.choices[0].message.content)