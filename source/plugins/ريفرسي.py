from pyrogram import Client, filters
from config import app, HNDLR
import asyncio

@app.on_message(filters.command("ريفرسي$", prefixes=f"{HNDLR}") & filters.me)
async def othello(app, msg):
	result = await app.get_inline_bot_results("U5iBOT", "othello")
	await msg.delete()
	await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
