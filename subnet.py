from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import ipaddress

# Replace with your bot token
TOKEN = "7861383816:AAFBgC4etNqLHs91f26z5s24zUC6ejGaxgg"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Send me an IP address with CIDR (e.g., /subnet 192.168.1.0/24) and I will calculate the subnetting details for you.")

async def subnet(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        await update.message.reply_text("Please provide an IP address with CIDR, like: /subnet 192.168.1.0/24")
        return
    
    try:
        network = ipaddress.ip_network(context.args[0], strict=False)
        response = f"📡 Network Information:\n"
        response += f"🔹 Network Address: {network.network_address}\n"
        response += f"🔹 Broadcast Address: {network.broadcast_address}\n"
        response += f"🔹 Number of Addresses: {network.num_addresses}\n"
        response += f"🔹 First Host IP: {list(network.hosts())[0]}\n"
        response += f"🔹 Last Host IP: {list(network.hosts())[-1]}\n"
        response += f"🔹 Subnet Mask: {network.netmask}\n"
        await update.message.reply_text(response)
    except ValueError:
        await update.message.reply_text("⚠️ Invalid IP address. Please enter a correct format like: 192.168.1.0/24")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("subnet", subnet))

    print("✅ Bot is now running...")
    app.run_polling()

if __name__ == "__main__":
    main()
