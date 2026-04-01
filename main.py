import asyncio
from pyrogram import Client, filters

# بياناتك التي زودتني بها
API_ID = 18751549
API_HASH = "85527463b9f14c85740396224c412598"
MAIN_TOKEN = "8701607814:AAFM7UUUakIL0xJmjF8mxjGZkS9FiRfFZPA"

# تشغيل سورس جبروت
app = Client("JABARUT_FACTORY", api_id=API_ID, api_hash=API_HASH, bot_token=MAIN_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "welcome to **𝗝𝗔𝗕𝗔𝗥𝗨𝗧** source ⚡\n\n"
        "🏭 مصنع البوتات الخاص بك يعمل بنجاح!\n"
        "أرسل توكن بوتك الآن لتفعيله."
    )

if __name__ == "__main__":
    print("🚀 سورس جبروت يعمل الآن...")
    app.run()
