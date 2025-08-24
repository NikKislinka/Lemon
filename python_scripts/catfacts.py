import requests

cat_fact_api = 'https://catfact.ninja/fact'

translation_api = 'https://api.mymemory.translated.net/get'

try:
    resp_cat = requests.get(cat_fact_api)
    resp_cat.raise_for_status()
    data_cat = resp_cat.json()
    
    original_cat_fact = data_cat['fact']
    print("Оригинальный факт о кошке (EN):")
    print(original_cat_fact)

    resp_tr = requests.get(translation_api, params={'q': original_cat_fact, 'langpair': 'en|ru'})
    resp_tr.raise_for_status()
    data_tr = resp_tr.json()
    
    translate = data_tr['responseData']['translatedText']
    print('Перевод на русский:')
    print(translate)

except requests.exceptions.RequestException as e:
    print(f'Ошибка запроса: {e}')
except KeyError as e: 
    print(f'Ошибка при разборе данных: Не найден ключ {e}. Возможно, изменилась структура ответа API.')
except Exception as e: 
    print(f'Произошла непредвиденная ошибка: {e}')

