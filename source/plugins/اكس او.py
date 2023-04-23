from pyrogram import Client, filters
from config import app, HNDLR
import asyncio

@app.on_message(filters.command("اكس او$", prefixes=f"{HNDLR}") & filters.me)
async def xo(app, msg):
	result = await app.get_inline_bot_results("xoBot", "play")
	await msg.delete()
	await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)