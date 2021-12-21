import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"😇Hy 🙋‍♂ {message.from_user.mention} എന്തൊക്കെയുണ്ട് വിശേഷങ്ങൾ😇,  ✨ {message.from_user.mention}✨️ ഗ്രൂപ്പിലേക്ക് സ്വാഗതം🦋.ഈ ഗ്രൂപ്പിൽ നിങ്ങൾ റിക്വസ്റ്റ് ചെയ്യുന്ന മൂവീസ് bot തരുന്നതായിരിക്കും. ഗ്രൂപ്പിൽ അലമ്പ് കാണിക്കുന്നവരെ Remove ആകുന്നതായിരിക്കും.🦋",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"ഇപ്പൊ എന്താ ഇണ്ടായേ എന്ദിന ഈ ആൾക്കാരൊക്കെ പോകുന്നേ ഇതെന്താ നരകമോ 🥲🥲",chat_id=chatid)
	

