
from transload import trans


from telegram import ParseMode

def start(update,context):
    name = update.message.chat.first_name
    chat_id = update.message.chat.id

    context.bot.send_message(chat_id = chat_id,
                            text = '''HI {} This is File Transloader Created by @A_b_r_i_s_h_B\n
                                      /help To get more Info'''.format(name),
                                      parse_mode=ParseMode.HTML)
def help(u,c):
    u.message.reply_text("Just send the Url you want To be transloaded")

def dl(update, context):
    """Echo the user message."""
    c_id = update.message.chat.id

    url = update.message.text
    if url.startswith('http'):
        The_link =  trans(url)

    if The_link == "https://rapidleech.hashhackers.com//telegram.dog/BhadooCloud":
        context.bot.send_message(chat_id=c_id,
            text ="An Error occured")
        return
    context.bot.send_message(chat_id=c_id,
            text =The_link )




