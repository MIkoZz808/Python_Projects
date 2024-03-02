import telebot
from telebot import types

# Replace 'YOUR_API_TOKEN' with your actual API token
API_TOKEN = 'API_TOKEN'

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm a simple bot. \n -> echo feature \n -> display image feature \n click on /help")

# Define a handler for the /echo command
@bot.message_handler(commands=['echo'])
def echo(message):
    # Extract the text following the /echo command
    text = ' '.join(message.text.split()[1:])
    
    # Check if the text is empty
    if not text:
        # If text is empty, send a message indicating the error
        bot.send_message(message.chat.id, "Error: Please provide text to echo.")
    else:
        # If text is not empty, send the echoed message
        bot.send_message(message.chat.id, text)

# Define a handler for the /help command
@bot.message_handler(commands=['help'])
def help(message):
    # Create a keyboard with a button for the "I want to quit" command
    keyboard = types.InlineKeyboardMarkup()
    quit_button = types.InlineKeyboardButton(text="I want to quit", callback_data="quit")
    keyboard.add(quit_button)
    
    # Send the help message with the keyboard
    help_message = "Here are some commands:\n\n"
    help_message += "/start - Start the bot\n"
    help_message += "/echo <text> - Echo the provided text\n"
    help_message += "Click the button below if you want to quit:"
    
    bot.send_message(message.chat.id, help_message, reply_markup=keyboard)

# Define a handler for the callback data
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "quit":
        # Respond to the "I want to quit" button click
        photo = open('dont_quit.jpg', 'rb')  # Replace 'path_to_your_image.jpg' with the path to your image
        bot.send_photo(call.message.chat.id, photo)

# Start the bot
print("Hey Im running...")
bot.polling()
