from pyrogram import Client, filters
from config import *
import os, time

os.environ['TZ'] = 'Africa/Cairo'
time.tzset()


@Client.on_message(filters.private & ~filters.bot)
async def pv_cmd(c, msg):
    if msg.from_user.id != sudo_id:
        try:
            await bot.send_message(pm,
                                   msg.text + '\n' + f'FROM: [{msg.from_user.first_name}](tg://user?id={msg.from_user.id})')
        except:
            # await msg.download("./Ttl.jpg")
            # await app.send_photo("me", "Ttl.jpg")
            pass
        if r.sismember(f"{sudo_id}mute_pv", msg.chat.id):
            await msg.delete(revoke=True)
            return
        if r.get(f"{sudo_id}welcome"):
            if not r.sismember(f"{sudo_id}accept", msg.chat.id):
                # r.delete(f"{sudo_id}waiting{msg.chat.id}")
                welcometxt = r.get(f"{sudo_id}addwelcome{msg.chat.id}")
                welcomephoto = r.get(f"{sudo_id}addwelcomephoto{msg.chat.id}")
                if not welcometxt:
                    if not welcomephoto:
                        async for photo in c.get_chat_photos("me"):
                            if photo:
                                txx = "• ان مطوري مشغول الان \n• ارسل رسالتك وسوف يتم الرد عليك قريبا"
                                await msg.reply_photo(photo.file_id, caption=txx)
                                break
                            else:
                                await msg.reply("• ان مطوري مشغول الان \n• ارسل رسالتك وسوف يتم الرد عليك قريبا")
                                break
                        r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                        r.delete(f"{sudo_id}waiting{msg.chat.id}")
                        return
                    else:
                        await msg.reply_photo(welcomephoto,
                                              caption='• تم ارسال رسالتك بنجاح \n• انتظر حتى يتم الرد عليك')
                        r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                        r.delete(f"{sudo_id}waiting{msg.chat.id}")
                        return

                else:
                    if not welcomephoto:
                        async for photo in c.get_chat_photos("me"):
                            if photo:
                                await msg.reply_photo(photo.file_id, caption=welcometxt)
                                break
                            else:
                                await msg.reply(welcometxt)
                                break
                        r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                        r.delete(f"{sudo_id}waiting{msg.chat.id}")
                        return
                    else:
                        await msg.reply_photo(welcomephoto, caption=welcometxt)
                        r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                        r.delete(f"{sudo_id}waiting{msg.chat.id}")
                        return

            # r.set(f"{sudo_id}waiting{msg.chat.id}", "on")
            return
    else:
        if msg.text == ".قبول" or msg.text == ".الغاء كتم":
            r.srem(f"{sudo_id}mute_pv", msg.chat.id)
            r.sadd(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("• تم السماح له بالتحدث")
        if msg.text == ".رفض":
            r.srem(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("• تم رفض العضو")
        if msg.text == ".كتم":
            r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
            await msg.edit("• تم كتم العضو")


@Client.on_message(filters.group)
async def gp(client, msg):
    current_time = time.strftime('%H:%M')
    chatt = str(msg.chat.id)
    chat = chatt.replace("-100", "").replace("-", "")
    msg_link = f"[• اضغط هنا لعرض الرساله](https://t.me/c/{chat}/{msg.id})"
    if msg.mentioned:
        if msg.from_user:
            try:
                txt = f"• لديك منشن من العضو [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) \n• اسم الجروب {msg.chat.title} \n• الوقت {current_time} \n{msg_link}"
                await bot.send_message(pm, txt)
                await bot.send_message(pm, msg.text)
            except:
                pass
        else:
            txt = f"• لديك منشن من القناه {msg.sender_chat.title} \n• اسم الجروب {msg.chat.title} \n• الوقت {current_time} \n{msg_link}"
            await bot.send_message(pm, txt)
            await bot.send_message(pm, msg.text)
    if msg.from_user:
        sender_id = msg.from_user.id
    elif msg.sender_chat:
        sender_id = msg.sender_chat.id
    if r.sismember(f"{sudo_id}mute", sender_id) or r.sismember(f"{sudo_id}mute{msg.chat.id}", sender_id):
        try:
            await msg.delete()
        except:
            pass
    if r.sismember(f"{sudo_id}ban", sender_id):
        try:
            await msg.delete()
            await client.ban_chat_member(msg.chat.id, msg.from_user.id)
        except:
            pass
