import requests


def get_info(number=211695539):
    url = f'https://card.wb.ru/cards/v1/detail'
    payload= {
        'appType': 1,
        'curr': 'rub',
        'dest': -1257786,
        'spp': 30,
        'nm': number
    }
    r = requests.get(url, params=payload)
    prod_name = r.json()['data']['products'][0]['name']
    prod_article = r.json()['data']['products'][0]['id']
    price = r.json()['data']['products'][0]['salePriceU']/100
    stocks = r.json()['data']['products'][0]['sizes'][0]['stocks']
    all_count = 0
    for stock in stocks:
        all_count += stock['qty']
    # all_count = sum(promotions_value)

    return {'prod_name': prod_name, 'article': prod_article, 'price': price, 'quantity': all_count}


get_info(205447945)