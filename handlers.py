from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    photo = FSInputFile("Flux_Dev_The_image_depicts_a_spacethemed_scene_with_a_view_of__2.jpg")  # պատկերի տեղադրությունը
    await message.answer_photo(
    photo, 
    caption=f" Hey👋 @{message.from_user.username} Welcome to the HyperVerse", 
    reply_markup=kb.main
)

