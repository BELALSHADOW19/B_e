from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio
reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("عوده",callback_data="help"),
             ]]
             )
txx1 = """
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
• تفعيل ، تعطيل الترحيب 
• قبول ، رفض
• كتم ، الغاء كتم 
• سبام + الكلمه + الرقم (سبام هورس 22)
• ايدي + ايدي بالرد
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
"""
txx2 = """
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
• حظر ، الغاء حظر
• مسح المحظورين
• كتم ، الغاء كتم 
• مسح المكتومين
• ايدي + ايدي بالرد
• مسح رسايله (بالرد)
• تدمير (لتحظر جميع اعضاء المجموعه او القناه)
• مسح الروابط 
• مسح الصور 
• مسح + العدد
• اضف جهاتي
•فتح الكول
•قفل الكول
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
"""
txx3 = """
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
• `غ` + اسم الاغنيه
• `ف` + اسم الفيديو 
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
"""
txx4 = """
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
• `اذاعه خاص` (بالرد علي النص)
• `اذاعه للمجموعات` (بالرد علي النص)
• `اذاعه للقنوات` (بالرد علي النص)

• `توجيه للخاص (بالرد علي الرساله)`
• `توجيه للمجموعات (بالرد علي الرساله)`
• `توجيه للقنوات (بالرد علي الرساله)`
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
"""
txx5 = """
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
• زواج ، طلاق -- زوجاتي -- مسح زوجاتي
• رفع ، تنزيل خول -- الخولات -- مسح الخولات 
• رفع ، تنزيل بنتي -- بناتي -- مسح بناتي
• رفع ، تنزيل شاذ -- الشواذ -- مسح الشواذ
• رفع ، تنزيل عرص -- المعرصين -- مسح المعرصين
• رفع ، تنزيل كلب -- الكلاب -- مسح الكلاب
• رفع ، تنزيل متوحد -- المتوحدين -- مسح المتوحدين
• رفع ، تنزيل حمار -- الحمير -- مسح الحمير
• رفع ، تنزيل بقلبي -- القلوب -- مسح القلوب 
• رفع ، تنزيل ابني -- اولادي -- مسح اولادي
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
"""
txx6 = """
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
`نسبة الحب`
`نسبة الذكاء`
`نسبة الكره`
`نسبة الشذوذ`
`نسبة العفانه`
`نسبة الهطل`
`نسبة العبط`
`نسبة القوة`
`نسبة الضعف`
`نسبة الرجوله`
`نسبة الغباء`
`نسبة الانوثة`
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
"""
txx7 = """
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
• `تلجراف` (بالرد علي صوره لرفعها علي تليجراف)
• `وش يقول` (بالرد علي صوت)
• `تفعيل تعطيل الساعه` 
• `تغيير اسمي` + الاسم (تغيير اسمي HORSE )
• `سورس`
⟣=====⧼ ᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ ⧽=====⟢
"""
txx8 = """
- شرطه / بالرد علي صحبك 
- تهكير / بالرد علي صحبك
- تحميل
- مربع
- دائره
- بشره
- قياس
- يد
- العد التنازلي
- قتل
- معاكسه
- عبقري
- افعي
- ولد
- مايكرو
- فايروس
- نيكول
- موسيقي
- رسم
- نجمه
- مكعبات
- مطر
- تفريغ
- النظام الشمسي
- افكر
"""
txx9 = """
- متت
- زعلت
- ساعه
- مح
- جيم
- الارض
- اقمار
- قمور
- BELAL
- تنصيب
- كلب
- خنزير
- اعمل ليك
- اجري
- رعد
- دبابه
- انتحر
- قناص
- غبي
- قنبلة
- كبلز
- مدينة
- سبونج
- صدمه
- فيل
"""
txx10 = """
♡~ ⦙  قائـمه اوامر الزغرفه : 
♡~ ⦙  .المواليد  
♡~ ⦙  .اشهر مزغرفة 
♡~ ⦙  .البايو 
♡~ ⦙  .قنوات 
♡~ ⦙  .الرموز 
♡~ ⦙  .اسماء 
♡~ ⦙  .زخرفه
"""
@bot.on_callback_query(filters.regex("^help1$"))
async def help1(client, callback_query):
  await callback_query.edit_message_text(txx1,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help2$"))
async def help2(client, callback_query):
  await callback_query.edit_message_text(txx2,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help3$"))
async def help3(client, callback_query):
  await callback_query.edit_message_text(txx3,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help4$"))
async def help4(client, callback_query):
  await callback_query.edit_message_text(txx4,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help5$"))
async def help5(client, callback_query):
  await callback_query.edit_message_text(txx5,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help6$"))
async def help6(client, callback_query):
  await callback_query.edit_message_text(txx6,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help7$"))
async def help6(client, callback_query):
  await callback_query.edit_message_text(txx7,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help8$"))
async def help6(client, callback_query):
  await callback_query.edit_message_text(txx8,reply_markup=reply_markup)  
@bot.on_callback_query(filters.regex("^help9$"))
async def help6(client, callback_query):
  await callback_query.edit_message_text(txx9,reply_markup=reply_markup)    
@bot.on_callback_query(filters.regex("^help10$"))
async def help6(client, callback_query):
  await callback_query.edit_message_text(txx10,reply_markup=reply_markup)      
@bot.on_callback_query(filters.regex("^help$"))
async def back(client, callback_query):
  await callback_query.edit_message_text("• ⟣=====⧼[᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ](https://t.me/SOURCE_HORSE)⧽=====⟢\n◐ ① اوامر الخاص📩\n◐ ② اوامر القنوات والمجموعات 🧰 \n◐ ③ اوامر اليوتيوب 🖼\n◐ ④ اوامر الاذاعه📊\n◐ ⑤ اوامر الرفع 🪪 \n◐ ⑥ اوامر النسب🌿\n◐ ⑦ اوامر اضافية 🔑 \n◐ ⑧ اوامر تسلية1 🎲 \n◐ ⑨ اوامر تسلية2 🎮 \n◐ ⑩ اوامر الزخرفة 🖌\n• ⟣=====⧼ [᥉᥆υᖇᥴᥱ 𝗁᥆ᖇ᥉ᥱ](https://t.me/SOURCE_HORSE)⧽=====⟢",reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("①",callback_data="help1"),
             InlineKeyboardButton("②",callback_data="help2"),
             InlineKeyboardButton("③",callback_data="help3"),
             ],
             [
             InlineKeyboardButton("④",callback_data="help4"),
             InlineKeyboardButton("⑤",callback_data="help5"),
             InlineKeyboardButton("⑥",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("⑦",callback_data="help7"),
             InlineKeyboardButton("⑧",callback_data="help8"),
             InlineKeyboardButton("⑨",callback_data="help9"),
             InlineKeyboardButton("⑩",callback_data="help10"),
             ],
             [
             InlineKeyboardButton("جـࢪؤب ٵلـسـؤࢪس",url="https://t.me/BAR_HORSE"),
             ],
             [
             InlineKeyboardButton("قـنـٵة ٵلـسـؤࢪس",url="https://t.me/SOURCE_HORSE"),
             ]]
             ))
