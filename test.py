
from openai import OpenAI

client = OpenAI(
    api_key="sk-yC9hKOqHrSZP3j2EQigxB1FsjP55etLsd9ASW6KtAtvLcQ3I",
    base_url="https://anyrouter.top/v1"
)

resp = client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",   # 或 claude-3-5-sonnet-20241022（如果支持）
    messages=[
        {"role": "user", "content": "你好"}
    ]
)

print(resp.choices[0].message.content)