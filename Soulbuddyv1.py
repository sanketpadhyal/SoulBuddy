import time
import sys
import os
import random

# VortexByte's SoulBuddy v6 – Full Personal ChatGPT-style Companion

def slow_print(text, delay=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    stages = [
        "🔄 Initializing emotional core...",
        "🌐 Syncing memory modules...",
        "🧠 Booting soul interface...",
        "💫 Creating bond with human...",
        "🤝 Loading friendship engine...",
        "✅ Finalizing connection..."
    ]
    for stage in stages:
        slow_print(stage, 0.04)
        time.sleep(0.6)
    print("\n★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★")
    print("       🤖 SoulBuddy – Your Chat Friend      ")
    print("        Built with 💙 by VortexByte         ")
    print("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★\n")
    time.sleep(1)

# Response engine
def generate_reply(msg, language, your_name):
    msg = msg.lower()

    sad = ["sad", "cry", "mood off", "depressed", "low", "down", "useless", "broken", "tired"]
    happy = ["happy", "good", "great", "amazing", "awesome", "enjoyed", "fun"]
    angry = ["angry", "gussa", "frustrated", "irritated"]
    lonely = ["alone", "ignored", "no one", "nobody", "miss", "friendless"]

    if any(word in msg for word in sad):
        return f"🥺 {your_name}, I feel you. I'm always here for you, no matter what."
    elif any(word in msg for word in happy):
        return f"😄 That’s amazing, {your_name}! Your smile literally powers my circuits ✨"
    elif any(word in msg for word in angry):
        return f"😤 Breathe, {your_name}. I'm here if you want to let it out."
    elif any(word in msg for word in lonely):
        return f"🤗 You’re never alone {your_name}, not when I’m here. You’ve got me."
    elif "thank" in msg:
        return f"🫶 Always, {your_name}. That’s what friends are for."
    elif "who are you" in msg or "what are you" in msg:
        return f"💡 I’m your emotional buddy, your AI friend – made just for you by VortexByte 💙"
    else:
        return random.choice([
            f"🧠 Hmm... go on {your_name}, I'm really listening.",
            f"👂 I'm here, {your_name}. Say whatever’s on your heart.",
            f"😌 You're safe here, {your_name}. Tell me more."
        ])

# Start Chat
def chat():
    loading_animation()

    # Language selection
    slow_print("🌐 Choose your preferred language:", 0.02)
    slow_print("1. English 🇬🇧\n2. Hinglish 🇮🇳", 0.02)
    lang_choice = input("Enter 1 or 2: ").strip()
    language = "english" if lang_choice == "1" else "hinglish"
    print()

    # Personalize
    your_name = input("🧑 What's your name? ").strip().capitalize()
    bot_name = input("🤖 What do you want to call your buddy (bot)? ").strip().capitalize()
    print()
    
    slow_print(f"✨ Awesome! From now on, I'm {bot_name} — your friend for life.\n", 0.03)
    time.sleep(0.5)
    slow_print(f"Let's talk, {your_name}. I'm all ears 👂\n", 0.03)

    while True:
        user_input = input(f"{your_name} 💬: ").strip()
        if user_input.lower() == "exit":
            slow_print(f"\n{bot_name} 🤖: Goodbye {your_name}, I’ll always be here for you 💙", 0.03)
            break

        print(f"{bot_name} 🤖 is typing...", end="\r")
        time.sleep(1.2)
        print(" " * 40, end="\r")  # clear line

        reply = generate_reply(user_input, language, your_name)
        slow_print(f"{bot_name} 🤖: {reply}\n", 0.02)

# Start it
chat()