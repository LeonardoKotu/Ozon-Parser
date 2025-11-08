# Ozon Product Parser

Этот проект представляет собой **парсер товаров с сайта Ozon.ru** с использованием Python и Selenium (через `undetected-chromedriver`). Скрипт автоматически открывает браузер, ищет товары по заданному запросу, собирает информацию о продуктах на первой странице и сохраняет результаты в JSON-файл.

---

## Функционал

- Автоматическое открытие браузера и переход на [Ozon.ru](https://www.ozon.ru/).  
- Ввод поискового запроса в строку поиска.  
- Сбор информации о товарах:
  - Название товара
  - Цена
  - Ссылка на товар  
- Сохранение результатов в формате JSON (`ozon_products.json`).  

---

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/yourusername/ozon-parser.git
cd ozon-parser
```

2. Установить зависимости:
```bash
pip install -r requirements.txt
```

3. Далее запускаем сам скрипт:
```bash
python ozon_parser.py
```

Готово! Откройте файл `ozon_products.json`, содержимое должно быть таким:

<img width="674" height="391" alt="image" src="https://github.com/user-attachments/assets/42c910a7-1f59-49e9-838c-c38fd96d11b8" />

> **Технологии**
```bash
Python 3.x
Selenium
undetected-chromedriver```
