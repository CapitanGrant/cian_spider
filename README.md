## Парсер для сбора данных объявлений о недвижимости с cian.ru.

Паук умеет собирать следующие данные из каждого объявления:
- Заголовок объявления;
- Количество комнат;
- Общая площадь квартиры;
- Этаж;
- Адрес;
- Цена;
- ID объявления;
- Номер страницы, на которой находится объявление.

<!--Установка-->
## Установка (Windows)
У вас должны быть установлены [зависимости проекта](https://github.com/CapitanGrant/cian_spider#зависимости)
```pip install -r requirements. txt```
1. Клонирование репозитория 

```git clone https://github.com/CapitanGrant/cian_spider.git```

2. Переход в директорию Cian_spider

```cd cian_spider```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Запуск скрипта для демонстрации возможностей парсера


_для создания файла в формате json, csv выполните следующую команду_

```scrapy crawl myspider -O имя_вашего_файла.json``` или
```scrapy crawl myspider -O имя_вашего_файла.csv```  



