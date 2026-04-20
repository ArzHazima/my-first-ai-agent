import os
from openai import OpenAI
from dotenv import load_dotenv

# פותח את הכספת ומושך את המפתח
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# חיבור ל-OpenAI באמצעות המפתח שנשאב
client = OpenAI(api_key=API_KEY)

video_topic = "איך ללמוד למבחנים במדעי המחשב בלי להשתגע"
print(f"Starting YouTube Producer for topic: {video_topic}...")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a professional YouTube producer. Write a viral title, a short description with hashtags, and a 1-minute script based on the given topic. Write everything in Hebrew."},
        {"role": "user", "content": f"Topic: {video_topic}"}
    ]
)

print("\n=== AI PRODUCER RESULT ===")
print(response.choices[0].message.content)