#!/usr/bin/env python3
# Super Simple Cultural Greetings - Perfect for Docker!

import time
import random

# Cultural greetings from around the world
greetings = [
    "Hello! (English)",
    "¡Hola! (Spanish)", 
    "Bonjour! (French)",
    "مرحبا (Arabic)",
    "你好 (Chinese)",
    "こんにちは (Japanese)",
    "नमस्ते (Hindi)",
    "Hujambo! (Swahili)"
]

print("🌍 Welcome to Cultural Greetings!")
print("This simple Python app is running inside Docker! 🐳")
print("="*50)

# Keep the container running and show greetings
while True:
    greeting = random.choice(greetings)
    print(f"Random greeting: {greeting}")
    time.sleep(5)  # Wait 5 seconds between greetings
