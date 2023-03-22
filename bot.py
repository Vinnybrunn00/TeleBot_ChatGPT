from telebot.async_telebot import AsyncTeleBot
from keys.mytokens import Token_key
import asyncio
import openai
openai.api_key = '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'

bot = AsyncTeleBot(Token_key())
print('Conected!')

@bot.message_handler(commands=['start'])
async def Start(messager):
    await bot.send_message(messager.chat.id, '[200] - Ok')

@bot.message_handler(content_types=['text'])
async def Response(messager):
    message = []
    user = messager.text
    message.append(
        {'role':'user',
        'content': user}
    )
    output = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=message)
    reply = output.choices[0].message.content

    await bot.send_message(messager.chat.id, reply, parse_mode='Markdown')

asyncio.run(bot.polling(non_stop=True))