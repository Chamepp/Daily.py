from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import telegram
import shutil

# Log Data
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Authorized Users
username_list = []

# Introduction
def start(bot, update):
    reply = "Welcome to World of Automation. \nI am a bot developed by a Ashkan.\nSend /help command to see what i can do."
    update.message.reply_text(reply)

# Help
def help(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        reply = '''Send /get folder_name/file_name.extension to receive a file. 
                \nSend /ls folder_name to show list of files.
                \nSend /put folder_name/file_name.extension to upload last sent file.
                \nSend /mkdir folder_name to create a Folder.
                \nSend /remove folder_name/filename.extension to delete a file.
                \nSend /adduser username to give access.
                \nSend /removeuser username to revoke access.
                \nSend /showuser to show list of users
                '''    
    else:
        reply = '''Send /get folder_name/file_name.extension to receive a file. 
                \nSend /ls folder_name to show list of files.
                \nSend /put folder_name/file_name.extension to upload last sent file.
                \nSend /mkdir folder_name to create a Folder.
                '''
    update.message.reply_text(reply)


# Send
def get(bot, update):
    username = update.message.from_user.username
    if(username not in username_list):
        update.message.reply_text("You are not Authorized.")
        return
    file = update.message.text.split(" ")[-1]
    if(file == "/send"):
        update.message.reply_text("Invalid File name.")
    else:
        reply = "Findind and Sending a requested file to you. Hold on..."
        update.message.reply_text(reply)
        path = os.getcwd()+'/'+file
        if (os.path.exists(path)):
            bot.send_document(chat_id=update.message.chat_id,document=open(path, 'rb'), timeout = 100)
        else:
            update.message.reply_text("File not Found.")

# Show
def ls(bot, update):
    username = update.message.from_user.username
    if(username not in username_list):
        update.message.reply_text("You are not Authorized.")
        return
    file = update.message.text.split(" ")[-1]
    if(file == "/show"):
        update.message.reply_text("Invalid Directory name.")
    else:
        reply = "Findind and Sending a list of files to you. Hold on..."
        update.message.reply_text(reply)
        path = os.getcwd()+'/'+file
        if (os.path.exists(path)):
            update.message.reply_text(os.listdir(path))
        else:
            update.message.reply_text("Directory not Found.")

# Put
def put(bot, update):
    f = open(str(os.getcwd())+"/file", "r")
    file_id = f.read()
    f.close
    if file_id == "":
        update.message.reply_text("You didn't upload file.")
    else:
        new_file = bot.get_file(file_id)
        message = update.message.text.split(" ")
        path = message[-1]
        if len(path) < 1:
            update.message.reply_text("Enter Path correctly.")
        else:
            new_file.download(os.getcwd()+'/'+path)
            update.message.reply_text("File Stored.")

# Make Directory
def mkdir(bot, update):
    message = update.message.text.split(" ")
    if len(message) < 1 or message[-1] == "/mkdir":
        update.message.reply_text("Invalid Syntax. Refer syntax in help section.")
        return
    path = os.getcwd() + "/" + message[-1]
    os.mkdir(path)
    update.message.reply_text("Folder Created.")

# Echo
def echo(bot, update):
    if update.message.document:
        file_id = update.message.document.file_id
        f = open(str(os.getcwd())+"/file", "w")
        f.write(file_id)
        f.close
        update.message.reply_text("Received.Now send file name and location to store. using /put command")
    else:
        reply = "Invalid Input."
        update.message.reply_text(reply)
# Error
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

# Add User
def add_user(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        username = update.message.text.split(" ")[-1]
        username_list.append(username)
        update.message.reply_text("User added.")
    else:
        update.message.reply_text("You are not Authorized.")

# Show User
def show_user(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        update.message.reply_text(username_list)
    else:
        update.message.reply_text("You are not Authorized.")

# Remove User
def remove_user(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        username = update.message.text.split(" ")[-1]
        username_list.remove(username)
        update.message.reply_text("User Removed.")
    else:
        update.message.reply_text("You are not Authorized.")

# Remove File
def remove(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        filename = update.message.text.split(" ")[-1]
        os.remove(os.getcwd()+ "/" + filename)
        update.message.reply_text("File Removed.")
    else:
        update.message.reply_text("You are not Authorized.")

# Remove Directory
def rmdir(bot, update):
    admin = update.message.from_user.username
    if admin == username_list[0]:
        filename = update.message.text.split(" ")[-1]
        shutil.rmtree(os.getcwd()+ "/" + filename)
        update.message.reply_text("Folder Removed.")
    else:
        update.message.reply_text("You are not Authorized.")

def main():
    # Data and Token
    TOKEN = os.environ['TOKEN']
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Command Handler
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("get", get))
    dp.add_handler(CommandHandler("ls", ls))
    dp.add_handler(CommandHandler("put", put))
    dp.add_handler(CommandHandler("mkdir", mkdir))

    # Admin Handlers
    dp.add_handler(CommandHandler("adduser", add_user))
    dp.add_handler(CommandHandler("showuser", show_user))
    dp.add_handler(CommandHandler("removeUser", remove_user))
    dp.add_handler(CommandHandler("remove", remove))
    dp.add_handler(CommandHandler("rmdir", rmdir))

    # Echo handler
    dp.add_handler(MessageHandler(Filters.document, echo))

    # Error Handler
    dp.add_error_handler(error)

    # Start Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()