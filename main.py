from bot import bot
from bot.hello_message import meeting_message
from bot.corpuses import list_of_corpuses
from bot.cabinets import list_of_cabinets
from bot.cabinet_info import get_info


# commit
# bot.polling(interval=5)
bot.infinity_polling()
