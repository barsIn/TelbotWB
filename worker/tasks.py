from telbot import bot
from dbcore import select_subscribers
from .celery import celery
from scripts import get_info
from worker.celery import celery_event_loop


async def snd_message_to_subscribers():
    subscribers = select_subscribers()
    if subscribers:
        for sub in subscribers:
            id = sub[0]
            good_info = get_info(int(sub[1]))
            await bot.send_message(id, f'Товар {good_info["prod_name"]}\n'
                                     f'Артикул {good_info["article"]}\n'
                                     f'Цена {good_info["price"]} руб.\n'
                                     f'Всего остатки на складах {good_info["quantity"]}\n')


@celery.task
async def hello():
    print('Hello')


@celery.task
def test_task() -> None:
    celery_event_loop.run_until_complete(snd_message_to_subscribers())