import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. טעינת המפתח (בטוח ומוסתר מהאינטרנט)
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# חיבור לשרתים האמיתיים של OpenAI
client = OpenAI(api_key=API_KEY)

# 2. קלט דינמי מהמשתמש
print("🎥 Welcome to YouTube Producer AI (LIVE MODE) 🎥")
video_topic = input("Enter your YouTube topic: ")

print(f"\n[System] Sending live request to OpenAI for: '{video_topic}'...")
print("[System] Please wait a few seconds...\n")

# 3. פנייה אמיתית ל-AI (עולה כסף)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a professional YouTube producer. Write a viral title, a short description with hashtags, and a 1-minute script based on the given topic. Write everything in Hebrew."},
        {"role": "user", "content": f"Topic: {video_topic}"}
    ]
)

# חילוץ הטקסט שה-AI ייצר
real_ai_response = response.choices[0].message.content

# 4. שמירת התוצאה האמיתית לקובץ טקסט
with open("youtube_script.txt", "w", encoding="utf-8") as file:
    file.write(real_ai_response)

print("✅ SUCCESS! The REAL script has been saved to 'youtube_script.txt'")