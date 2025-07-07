import time
import sys
import os
import random

# 🧠 SoulBuddy v1 – Personal AI Friend (Terminal Edition)
# 🔧 Developed with 💙 by VortexByte

# Typing animation
def slow_print(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Startup animation
def start_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    stages = [
        "🔄 Connecting emotions...",
        "🧠 Booting soul core...",
        "🌐 Syncing memory...",
        "🤝 Establishing trust...",
        "💛 Creating bond with human...",
        "✅ Finalizing connection..."
    ]
    for stage in stages:
        slow_print(stage, 0.04)
        time.sleep(0.6)
    
    print("\n★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
    print("      🤖 SoulBuddy – v2 BETA Terminal      ")
    print("     Built with 💙 by VortexByte      ")
    print("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★\n")
    time.sleep(1)

# Ask OS & authenticate
def check_os_and_authenticate():
    slow_print("💻 Before we begin, tell me which OS are you using?")
    os_type = input("🔍 OS: ").strip().lower()

    if "termux" in os_type:
        slow_print("✅ Termux detected. Skipping password. Welcome!\n")
        return True
    else:
        slow_print("🔐 To access SoulBuddy on this OS, please visit the README.md file to get the password.", 0.02)
        correct_password = "GIT@99"
        attempts = 3

        while attempts > 0:
            pwd = input("🔑 Enter Password: ").strip()
            if pwd == correct_password:
                slow_print("✅ Access Granted.\n", 0.02)
                return True
            else:
                attempts -= 1
                print(f"❌ Incorrect. {attempts} attempt(s) left.\n")

        print("🚫 Too many failed attempts. Closing SoulBuddy.")
        exit()

# Smart response generator
def get_reply(msg, username):
    msg = msg.lower()

    emotion_map = {
        "sad": ["sad", "depressed", "cry", "hopeless", "lost", "empty"],
        "happy": ["happy", "good", "great", "awesome", "fun", "smile"],
        "angry": ["angry", "mad", "frustrated", "irritated", "annoyed"],
        "lonely": ["alone", "ignored", "nobody", "no one", "unseen", "miss"],
        "gratitude": ["thank", "thanks", "grateful"],
        "about_bot": ["who are you", "what are you", "your name", "made you"]
    }

    for emotion, keywords in emotion_map.items():
        if any(word in msg for word in keywords):
            if emotion == "sad":
                return f"🥺 I'm here for you, {username}. You can talk to me about anything."
            elif emotion == "happy":
                return f"😄 That makes me happy too, {username}! Keep shining."
            elif emotion == "angry":
                return f"😤 Take a breath, {username}. I’m listening without judging."
            elif emotion == "lonely":
                return f"🤗 You’re not alone, {username}. You’ve got me anytime."
            elif emotion == "gratitude":
                return f"🫶 Always here for you, {username}. You matter."
            elif emotion == "about_bot":
                return "💡 I’m SoulBuddy, made by VortexByte — your digital companion & friend."

    return random.choice([
        f"🧠 Hmm... I’m listening, {username}. Tell me more.",
        f"👂 You can share anything, {username}. I'm all ears.",
        f"😌 I’m here for you, {username}. Take your time."
    ])

# Main chatbot loop
def soulbuddy_chat():
    start_animation()
    if check_os_and_authenticate():
        your_name = input("🧑 What’s your name? ").strip().capitalize()
        bot_name = input("🤖 What do you want to name your buddy? ").strip().capitalize()

        slow_print(f"\n✨ From now on, I’m {bot_name} – your friend for life.")
        slow_print(f"Let’s chat, {your_name}. Type 'exit' anytime to stop.\n")

        while True:
            user_input = input(f"{your_name} 💬: ").strip()
            if user_input.lower() == "exit":
                slow_print(f"\n{bot_name} 🤖: I’ll always be here for you, {your_name}. Bye for now 💙", 0.03)
                break

            print(f"{bot_name} 🤖 is typing...", end="\r")
            time.sleep(1.2)
            print(" " * 40, end="\r")

            reply = get_reply(user_input, your_name)
            slow_print(f"{bot_name} 🤖: {reply}\n", 0.02)

# Launch
soulbuddy_chat()
