# 🎥 YouTube Producer AI Agent

A smart Python agent that acts as a professional YouTube producer. 
You provide a topic, and the AI generates a viral title, a description with hashtags, and a complete 1-minute video script.

## 🚀 Features
- **Dynamic Input**: Prompts the user for a video topic.
- **Secure API Connection**: Uses `.env` to protect OpenAI API keys.
- **File I/O**: Automatically saves the generated script to a local text file (`youtube_script.txt`).
- **Mocking Ready**: Built with decoupled architecture, allowing for local testing without incurring API costs.

## 🛠️ Technologies
- Python 3
- OpenAI API (gpt-4o-mini)
- `python-dotenv` for security

## 💡 How to Run
1. Clone the repository.
2. Create a `.env` file and add your key: `OPENAI_API_KEY=your_key_here`
3. Run the agent: `python agent.py`
4. Enter your topic and check the generated text file!
