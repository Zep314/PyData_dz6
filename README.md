# Сбор и разметка данных (семинары)
## Урок 6. Scrapy. Парсинг фото и файлов

### Задание

1. Создайте новый проект Scrapy. Дайте ему подходящее имя и убедитесь, что ваше окружение правильно настроено для 
   работы с проектом.
2. Создайте нового паука, способного перемещаться по сайту www.unsplash.com. Ваш паук должен уметь перемещаться по 
   категориям фотографий и получать доступ к страницам отдельных фотографий.
3. Определите элемент (Item) в Scrapy, который будет представлять изображение. Ваш элемент должен включать такие 
   детали, как URL изображения, название изображения и категорию, к которой оно принадлежит.
4. Используйте Scrapy ImagesPipeline для загрузки изображений. Обязательно установите параметр IMAGES_STORE в 
   файле settings.py. Убедитесь, что ваш паук правильно выдает элементы изображений, которые может 
   обработать ImagesPipeline.
5. Сохраните дополнительные сведения об изображениях (название, категория) в CSV-файле. Каждая строка должна 
   соответствовать одному изображению и содержать URL изображения, локальный путь к файлу (после загрузки), 
   название и категорию.



### Решение

Устанавливаем scrapy, и создаем новый проект

    venv/bin/activate.bat
    pip install scrapy
    scrapy startproject unsplash

Генерируем нового паука

    cd unsplash/unsplash/spiders/
    scrapy genspider -t crawl unsplash_images "unsplash.com"

Редактируем код паука: [unsplash/unsplash/spiders/unsplash_images.py](unsplash/unsplash/spiders/unsplash_images.py)

Запускае паука в работу:

    cd jofel
    scrapy crawl unsplash_images -o output.json

#### Результат работы:

Файл с данными: [unsplash/output.json](jofel/output.json)

Вывод программы:

