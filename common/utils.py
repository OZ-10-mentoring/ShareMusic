from openai import OpenAI

from config.settings import CHATGPT_API_KEY

client = OpenAI(
    api_key=CHATGPT_API_KEY,
)


def generate_ai_summary(title, body):
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="너는 게시글을 요약해주는 정리하는 사람이야. 요약할 때는 형태를 '정리:' 를 무조건 붙이고 간단하게 요약해줘.",
        input= f"제목은 {title} 이고 내용은 {body}",
    )
    return response.output_text
