import os
from dotenv import load_dotenv

# שלב 1: טעינת המפתח (עדיין עובד מאובטח, למרות שאנחנו במצב טיסה)
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# שלב 2: קלט דינמי מהמשתמש
print("🎥 Welcome to YouTube Producer AI 🎥")
video_topic = input("Enter your YouTube topic: ")

print(f"\n[System] Producing content for: '{video_topic}'...")
print("[System] API connection blocked by billing. Using MOCK response...\n")

# --- החלק של ה-Mocking (חיקוי התשובה מ-OpenAI) ---
# במקום לפנות לשרת שעולה כסף, אנחנו שומרים תשובת דמה לתוך משתנה
mock_ai_response = f"""
כותרת ויראלית: הסוד המטורף מאחורי {video_topic} (לא תאמינו!)

תיאור:
בסרטון של היום נגלה את כל מה שצריך לדעת על {video_topic}. אל תשכחו לעשות לייק וסאב!
#ויראלי #טיפים #{video_topic.replace(' ', '')}

תסריט:
(פתיח) היי כולם! היום אנחנו הולכים לדבר על משהו שישנה לכם את החיים...
(גוף הסרטון) הרבה אנשים חושבים שזה קשה, אבל הנה 3 שלבים פשוטים...
(סיום) תודה שצפיתם, נתראה בסרטון הבא!
"""
# --------------------------------------------------

# שלב 3: שמירת התוצאה לקובץ טקסט חדש (File I/O)
# הפקודה הזו מייצרת קובץ אמיתי על המחשב שלך וכותבת לתוכו את התוצאה
with open("youtube_script.txt", "w", encoding="utf-8") as file:
    file.write(mock_ai_response)

print("✅ SUCCESS! The script has been saved to 'youtube_script.txt'")