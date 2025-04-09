from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='HyperVerse Community📢', url="https://t.me/HyperrVersee")],
    [InlineKeyboardButton(
        text='Play▶ ',
        web_app=WebAppInfo(url="https://haykoo707.github.io/hyperversee/")  # Mini App-ի հղումը
    ),
     ]
])
