import os
from rembg import remove
from PIL import Image
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
TOKEN = "*****************"

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hi im a background remover bot click /start')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='hi, please send the image you wanna remove his background')

async def process_image(image_name:str):
    name,_ = os.path.splitext(image_name)
    output_image_path = f'./Cut_Background_Bot/processed/{name}.png'
    input = Image.open(f'./Cut_Background_Bot/images/{image_name}')
    output = remove(input)
    output.save(output_image_path)
    os.remove(f'./Cut_Background_Bot/images/{image_name}')
    return output_image_path

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if filters.PHOTO.check_update(update):
        file_id = update.message.photo[-1].file_id
        unique_file_id = update.message.photo[-1].file_unique_id
        image_name = f'{ unique_file_id }.jpg'
    elif filters.Document.IMAGE:
        file_id = update.message.document.file_id
        _,file_ext = os.path.splitext(update.message.document.file_name)
        unique_file_id = update.message.document.file_unique_id
        image_name = f"{ unique_file_id }.{ file_ext }"
        
    save_image = await context.bot.get_file(file_id)
    await save_image.download_to_drive(custom_path=f"./Cut_Background_Bot/images/{image_name}")
    await context.bot.send_message(chat_id=update.effective_chat.id, text='your image is on proccess now please wait...')
    processed_image = await process_image(image_name)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=processed_image)
    os.remove(processed_image)
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # command handler
    help_handler = CommandHandler('help', help)
    start_handler = CommandHandler('start', start)
    image_handler = MessageHandler(filters.PHOTO | filters.Document.IMAGE, handle_image)

    
    # register handler
    application.add_handler(help_handler)
    application.add_handler(start_handler)
    application.add_handler(image_handler)
        
    application.run_polling()