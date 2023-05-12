from pyrogram import Client, filters, enums
from config import *
import asyncio
from pyrogram.types import Message, ChatPrivileges


def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False


@Client.on_message(filters.command("كتم$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def mute(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    chek = await is_Admin(msg.chat.id, msg.from_user.id)
    if chek == False:
        await message.reply("• يجب ان تكون مشرف بالمجموعه لاستخدام الاوامر")
        return False
    try:
        if msg.reply_to_message.from_user.id == sudo_id:
            return await msg.edit("• لا يمكنك كتم نفسك")
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم كتمه بنجاح"
        await msg.edit(txx)
    except:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")


@Client.on_message(filters.command("الغاء كتم$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_mute(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    try:
        if msg.reply_to_message.from_user.id == sudo_id:
            return await msg.edit("• لا يمكنك  الغاء كتم نفسك")
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم الغاء كتمه بنجاح"
        await msg.edit(txx)
    except:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم الغاء كتم القناه في المجموعه")


@Client.on_message(filters.command("مسح المكتومين", prefixes=f".") & filters.me & filters.group)
async def un_mute_all(c, msg):
    r.delete(f"{sudo_id}mute{msg.chat.id}")
    txx = f"• تم مسح المكتومين بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("حظر$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def bann(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    chek = await is_Admin(msg.chat.id, msg.from_user.id)
    if chek == False:
        await message.reply("• يجب ان تكون مشرف بالمجموعه لاستخدام الاوامر")
        return False
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك حظر نفسك")
    try:
        await c.ban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم حظره بنجاح"
        await msg.edit(txx)
    except Exception as e:
        await msg.edit(f"• ليس لديك صلاحيات الحظر في المجموعه")


@Client.on_message(filters.command("الغاء حظر$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_ban(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم الغاء كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك  الغاء حظر نفسك")
    try:
        await c.unban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم الغاء حظره بنجاح"
        await msg.edit(txx)
    except:
        await msg.edit("• العضو ليس محظور \n• او ليس لديك صلاحيات الحظر في المجموعه")


@Client.on_message(filters.command(["مسح المحظورين$", "مسح المطرودين$"], prefixes=f".") & filters.me & ~filters.private)
async def un_ban_all(c, msg):
    xxx = 0
    async for m in c.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.BANNED):
        try:
            await c.unban_chat_member(msg.chat.id, m.user.id)
            xxx += 1
        except:
            pass
    await msg.edit(f"• تم الغاء حظر {xxx} عضو")


@Client.on_message(filters.command("تدمير$", prefixes=f".") & filters.me & ~filters.private)
async def ban_all_members(c, msg):
    xxx = 0
    un = 0
    async for m in c.get_chat_members(msg.chat.id):
        try:
            if m.user.id == sudo_id:
                continue
            await c.ban_chat_member(msg.chat.id, m.user.id)
            if xxx % 10 == 0:
                await msg.edit(f"• تم حظر {xxx}")
            xxx += 1
        except:
            un += 1
    await msg.edit(f"• تم حظر {xxx} عضو\n• لم استطيع حظر {un} عضو")


@Client.on_message(filters.command("كتم عام$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def mute_all(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك كتم نفسك")
    r.sadd(f"{sudo_id}mute", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم كتمه عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command(
    ["الغاء كتم عام$", "الغاء كتم العام$", "الغاء الكتم العام$", "الغاء العام$", "الغاء الحظر العام$", "الغاء حظر عام$",
     "الغاء حظر العام$"], prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_mute_all_user(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم الغاء كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك  الغاء كتم نفسك")
    r.srem(f"{sudo_id}mute", msg.reply_to_message.from_user.id)
    r.srem(f"{sudo_id}ban", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم الغاء كتمه/حظره عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح قائمه العام$", prefixes=f".") & filters.me & filters.group)
async def un_mute_all_3am(c, msg):
    r.delete(f"{sudo_id}mute")
    r.delete(f"{sudo_id}ban")
    txx = f"• تم مسح المكتومين/المحظورين عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("حظر عام$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def ban_all(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك حظر نفسك")
    r.sadd(f"{sudo_id}ban", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم حظره عام بنجاح"
    await msg.edit(txx)
    
@Client.on_message(filters.command("مغادرة$", prefixes=f".") & filters.me )
async def leave_group(c,msg):
  await msg.edit("• يتم مغادرة المجموعه ....🕷")
  await asyncio.sleep(.5)
  await msg.edit("• تم مغادرة المجموعه بنجاح.🕷")
  await c.leave_chat(msg.chat.id)
@Client.on_message(filters.command("الغاء تثبيت الكل$", prefixes=f".") & filters.me)
async def unpin_allm(c,msg):
  try:
     await c.unpin_all_chat_messages(msg.chat.id)
     await msg.edit("• تم الغاء تثبيت كل الماسدجات بنجاح.🕷")
  except:
    await msg.edit("• م معاك صلاحية التثبيت يصاحبي.🕷")
@Client.on_message(filters.command("تثبيت$", prefixes=f".") & filters.me)
async def pin_msg(c,msg):
  if msg.reply_to_message:
    await c.pin_chat_message(
            msg.chat.id,
            msg.reply_to_message.id,
            disable_notification=False,
            both_sides=True
        )
    await msg.edit("• تم تثبيت الماسدج بنجاح.🕷")
  else:
    await msg.edit("• اعمل ريبلاي ع الماسدج الاول يصاحبي وجرب تاني.🕷")
@Client.on_message(filters.command("الغاء تثبيت$", prefixes=f".") & filters.me)
async def unpin_msg(c,msg):
  if msg.reply_to_message:
       await c.unpin_chat_message(
             msg.chat.id,
             msg.reply_to_message.id,
         )    
       await msg.edit("• تم الغاء تثبيت الماسدج بنجاح.🕷")
  else:
    await msg.edit("• اعمل ريبلاي ع الماسدج الاول يصاحبي وجرب تاني.🕷")    
@Client.on_message(filters.command("موافقة على الكل$", prefixes=f".") & filters.me)
async def app_allreq(c,msg):
  try:
    await c.approve_all_chat_join_requests(msg.chat.id)
    await msg.edit("• تمت موافقة على كل طلبات الانضمام")
  except:
    await msg.edit("• انت م ادمن اصلا يصاحبي")
@Client.on_message(filters.group & filters.me, group=9)
async def promote_admin(c,msg):
   if ".رفع مشرف" in msg.text:
    if msg.reply_to_message:  
     user_id = msg.reply_to_message.from_user.id 
     me = msg.from_user.id
     bot = await app.get_chat_member(msg.chat.id, "me")
     if user_id == me:
       return await msg.reply_text("ازاي هترفع نفسك يصاحبي")
     if not bot.privileges.can_promote_members:
       return await msg.reply_text("ممعكش صلاحية الرفع يصاحبي")
     await c.promote_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
             ),
         )
     a = msg.text.split(" ")
     if len(a)  > 2:
        mas = msg.text 
        title = mas.replace(".رفع مشرف","")
        await c.set_administrator_title(msg.chat.id, msg.reply_to_message.from_user.id, title)
        await msg.edit(f"تم رفع {msg.reply_to_message.from_user.mention} مشرف و لقبه {title}")
     else:
      await msg.edit(f"تم رفع {msg.reply_to_message.from_user.mention} مشرف")
    else:
          await msg.edit("اعمل ريب ع الشخص يصاحبي")
   elif ".تنزيل مشرف" in msg.text:
    if msg.reply_to_message:
      user_id = msg.reply_to_message.from_user.id 
      me = msg.from_user.id
      bot = await app.get_chat_member(msg.chat.id, "me")
      if user_id == me:
        return await msg.reply_text("ازاي هترفع نفسك يصاحبي")
      if not bot.privileges.can_promote_members:
        return await msg.reply_text("ممعكش صلاحية الرفع يصاحبي")
      await c.promote_chat_member(msg.chat.id, msg.reply_to_message.from_user.id, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=False,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
             ),
         )
      await msg.edit(f"تم تنزيل {msg.reply_to_message.from_user.mention} من الاشراف")
    else:
          await msg.edit("اعمل ريب ع الشخص يصاحبي")
   else:
    return
