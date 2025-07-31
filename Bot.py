from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

BOT_TOKEN = "8358410115:AAF6mtD7Mw1YEn6LNWdEJr6toCubTOz3NLg"
ADMINS = [6998916494, 987654321]

async def add_deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("❌ Aap is command ka use nahi kar sakte.")
        return

    if len(context.args) < 1:
        await update.message.reply_text("Use: /add <amount>")
        return

    try:
        amount = float(context.args[0])
    except:
        await update.message.reply_text("Amount number me likho!")
        return

    fee = round(amount * 0.05, 2)
    release_amount = round(amount - fee, 2)
    trade_id = f"#TID{random.randint(100000,999999)}"

    message = (
        f"Recived Amount : ₹{amount}\n"
        f"Release Amount : ₹{release_amount}\n"
        f"Fee : ₹{fee}\n"
        f"Trade ID : {trade_id}\n\n"
        f"Escrowed By : 𝐌𝐑."
    )

    await update.message.reply_text(message)

if name == "main":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("add", add_deal))
    app.run_polling()
