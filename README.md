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
    pip install pillow
    scrapy startproject unsplash

Генерируем нового паука

    cd unsplash/unsplash/spiders/
    scrapy genspider -t crawl unsplash_images "unsplash.com"

Редактируем код паука: [unsplash/unsplash/spiders/unsplash_images.py](unsplash/unsplash/spiders/unsplash_images.py)

Настраиваем обработку дополнительных полей [unsplash/unsplash/items.py](unsplash/unsplash/items.py)

Настраиваем промежуточную обработку [unsplash/unsplash/pipelines.py](unsplash/unsplash/pipelines.py)

Корректируем настройки [unsplash/unsplash/settings.py](unsplash/unsplash/settings.py)

Запускаем паука в работу:

    cd unsplash
    scrapy crawl unsplash_images --set FEED_URI=scraped_data.csv --set FEED_FORMAT=csv

#### Результат работы:

Файл с данными: [unsplash/scraped_data.csv ](unsplash/scraped_data.csv)

Вывод программы:

    (venv) C:\Work\python\Data\PyData_dz6\unsplash>scrapy crawl unsplash_images --set FEED_URI=scraped_data.csv --set FEED_FORMAT=csv
    2024-01-19 09:42:11 [scrapy.utils.log] INFO: Scrapy 2.11.0 started (bot: unsplash)
    2024-01-19 09:42:11 [scrapy.utils.log] INFO: Versions: lxml 5.1.0.0, libxml2 2.10.3, cssselect 1.2.0, parsel 1.8.1, w3lib 2.1.2, Twisted 22.10.0, Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)], pyOpenSSL 23.3.0 (OpenSSL 3.1.4 24 Oct 2023), cryptography 41.0.7, Platform Windows-10-10.0.22621-SP0
    2024-01-19 09:42:11 [scrapy.addons] INFO: Enabled addons:
    []
    2024-01-19 09:42:11 [asyncio] DEBUG: Using selector: SelectSelector
    2024-01-19 09:42:11 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
    2024-01-19 09:42:11 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
    2024-01-19 09:42:11 [scrapy.extensions.telnet] INFO: Telnet Password: 7e049f0615627484
    2024-01-19 09:42:11 [py.warnings] WARNING: C:\Work\python\Data\PyData_dz6\venv\lib\site-packages\scrapy\extensions\feedexport.py:406: ScrapyDeprecationWarning: The `FEED_URI` and `FEED_FORMAT` settings have been deprecated in favor of the `FEEDS` setting. Please see the `FEEDS` setting docs for more details
      exporter = cls(crawler)
    
    2024-01-19 09:42:11 [scrapy.middleware] INFO: Enabled extensions:
    ['scrapy.extensions.corestats.CoreStats',
     'scrapy.extensions.telnet.TelnetConsole',
     'scrapy.extensions.feedexport.FeedExporter',
     'scrapy.extensions.logstats.LogStats']
    2024-01-19 09:42:11 [scrapy.crawler] INFO: Overridden settings:
    {'BOT_NAME': 'unsplash',
     'FEED_EXPORT_ENCODING': 'utf-8',
     'FEED_EXPORT_FIELDS': ['category', 'name', 'file_path', 'image_urls'],
     'NEWSPIDER_MODULE': 'unsplash.spiders',
     'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
     'ROBOTSTXT_OBEY': True,
     'SPIDER_MODULES': ['unsplash.spiders'],
     'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
    2024-01-19 09:42:11 [scrapy.middleware] INFO: Enabled downloader middlewares:
    ['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
     'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
     'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
     'scrapy.downloadermiddlewares.retry.RetryMiddleware',
     'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
     'scrapy.downloadermiddlewares.stats.DownloaderStats']
    2024-01-19 09:42:11 [scrapy.middleware] INFO: Enabled spider middlewares:
    ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
     'scrapy.spidermiddlewares.referer.RefererMiddleware',
     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
     'scrapy.spidermiddlewares.depth.DepthMiddleware']
    2024-01-19 09:42:11 [scrapy.middleware] INFO: Enabled item pipelines:
    ['unsplash.pipelines.CustomImagesPipeline']
    2024-01-19 09:42:11 [scrapy.core.engine] INFO: Spider opened
    2024-01-19 09:42:11 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
    2024-01-19 09:42:11 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/robots.txt> (referer: None)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com> (referer: None)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/textures-patterns> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.dupefilters] DEBUG: Filtered duplicate request: <GET https://unsplash.com/> - no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/film> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/travel> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/nature> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/experimental> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/architecture-interior> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/wallpapers> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/3d-renders> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/animals> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-room-that-has-some-shelves-in-it-8vhLqlalUjg> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/health> (referer: https://unsplash.com)
    2024-01-19 09:42:12 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/people> (referer: https://unsplash.com)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/street-photography> (referer: https://unsplash.com)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/food-drink> (referer: https://unsplash.com)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-woman-in-a-white-dress-with-branches-on-her-head-J48L5RQmArI> (referer: https://unsplash.com)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/plus/new> (referer: https://unsplash.com)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-man-and-a-woman-standing-next-to-each-other-AjE6FYGOgas> (referer: https://unsplash.com)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-large-body-of-water-covered-in-lots-of-water-1aZc3aXaLsg> (referer: https://unsplash.com/t/textures-patterns)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-close-up-of-a-building-made-out-of-bricks-ehTjAGnylco> (referer: https://unsplash.com/t/textures-patterns)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-close-up-of-a-white-object-with-wavy-lines-T-PEDySKIMU> (referer: https://unsplash.com/t/textures-patterns)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-painting-of-a-tree-in-the-snow-L9b3xMjqmZk> (referer: https://unsplash.com/t/textures-patterns)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/an-aerial-view-of-a-beach-and-a-body-of-water-ZZKx0PgjYRY> (referer: https://unsplash.com/t/textures-patterns)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/t/minimalism> (referer: https://unsplash.com)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/an-aerial-view-of-a-snow-covered-forest-6Picwb_Pj6o> (referer: https://unsplash.com/t/textures-patterns)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-fern-is-growing-in-the-middle-of-a-forest-Jga5B6d_2so> (referer: https://unsplash.com/t/film)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-basketball-hoop-hanging-from-the-side-of-a-house-UnGWUTu6k-g> (referer: https://unsplash.com/t/film)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-cup-of-cereal-and-a-bottle-of-milk-GYTvV5NK93M> (referer: https://unsplash.com/t/food-drink)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-man-standing-in-a-dark-room-with-a-red-light-on-his-face-_fxKIVbafQc> (referer: https://unsplash.com/t/people)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/cars-parked-on-side-of-the-road-BU1abAe76Vg> (referer: https://unsplash.com/t/street-photography)
    2024-01-19 09:42:13 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://images.unsplash.com/robots.txt> (referer: None)
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/assorted-color-of-fruits-and-vegetables-Cngzg6CiEU8> (referer: https://unsplash.com/t/health)
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-couple-of-large-wooden-doors-in-front-of-a-building-O934zeWwpUM> (referer: https://unsplash.com/plus/new)
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-man-in-a-space-suit-with-a-skull-on-his-back-zHKSobrhxBM> (referer: https://unsplash.com/plus/new)
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1705462311424-d66b507d5921?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1705462311424-d66b507d5921?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-bird-sitting-on-top-of-a-tree-branch-IyR2NwOup10> (referer: https://unsplash.com/t/animals)
    2024-01-19 09:42:14 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/a-room-that-has-some-shelves-in-it-8vhLqlalUjg>
    {'category': ['None'],
     'file_path': ['None\\a room that has some shelves in it.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1705462311424-d66b507d5921?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': 'a6cbefe3ad10538bc06ba9f43dcca97c',
                 'path': 'None\\a room that has some shelves in it.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1705462311424-d66b507d5921?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['a room that has some shelves in it']}
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-close-up-of-a-bunch-of-candy-hearts-to0WKIPEeHQ> (referer: https://unsplash.com/plus/new)
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-shadow-of-a-person-on-a-wall-SOFq8gkIm2s> (referer: https://unsplash.com/t/street-photography)
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://unsplash.com/photos/a-group-of-people-standing-on-top-of-a-beach-next-to-the-ocean-RWCtRDq5xW0> (referer: https://unsplash.com/t/minimalism)
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1705350836117-e117aa1d315b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1705350836117-e117aa1d315b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1704774801340-7d23d2d3868b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1704774801340-7d23d2d3868b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1704807395127-898b64191a16?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1704807395127-898b64191a16?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1704774799224-eddb8593b065?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1704774799224-eddb8593b065?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/a-man-and-a-woman-standing-next-to-each-other-AjE6FYGOgas>
    {'category': ['None'],
     'file_path': ['None\\a man and a woman standing next to each other.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1705350836117-e117aa1d315b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': '68afbe59d4cdafb607ee9104967a1029',
                 'path': 'None\\a man and a woman standing next to each other.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1705350836117-e117aa1d315b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['a man and a woman standing next to each other']}
    2024-01-19 09:42:14 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/an-aerial-view-of-a-beach-and-a-body-of-water-ZZKx0PgjYRY>
    {'category': ['Textures & Patterns'],
     'file_path': ['Textures & Patterns\\an aerial view of a beach and a body of '
                   'water.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1704774801340-7d23d2d3868b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': '0bbcf21ca2a4348274aff0fed42d6348',
                 'path': 'Textures & Patterns\\an aerial view of a beach and a '
                         'body of water.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1704774801340-7d23d2d3868b?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['an aerial view of a beach and a body of water']}
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1705518648497-e4ea72bcb27d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1705518648497-e4ea72bcb27d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1705113165376-b14041df2059?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1705113165376-b14041df2059?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/a-close-up-of-a-white-object-with-wavy-lines-T-PEDySKIMU>
    {'category': ['Textures & Patterns'],
     'file_path': ['Textures & Patterns\\a close up of a white object with wavy '
                   'lines.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1704807395127-898b64191a16?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': 'fb554f7d1a70c53ce59509d8c40c0ec3',
                 'path': 'Textures & Patterns\\a close up of a white object with '
                         'wavy lines.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1704807395127-898b64191a16?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['a close up of a white object with wavy lines']}
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1705131816850-58f5bbca1449?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1705131816850-58f5bbca1449?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/an-aerial-view-of-a-snow-covered-forest-6Picwb_Pj6o>
    {'category': ['Textures & Patterns'],
     'file_path': ['Textures & Patterns\\an aerial view of a snow covered '
                   'forest.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1704774799224-eddb8593b065?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': '7aebdfcb50bbfebe7c1f058b7d3affc8',
                 'path': 'Textures & Patterns\\an aerial view of a snow covered '
                         'forest.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1704774799224-eddb8593b065?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['an aerial view of a snow covered forest']}
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1696075514266-3ec98fcd0d68?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1696075514266-3ec98fcd0d68?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1692839929461-b3b30e36ef70?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1692839929461-b3b30e36ef70?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1704369354376-a6defd8e840d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:14 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1704369354376-a6defd8e840d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:14 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/a-woman-in-a-white-dress-with-branches-on-her-head-J48L5RQmArI>
    {'category': ['Experimental'],
     'file_path': ['Experimental\\a woman in a white dress with branches on her '
                   'head.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1705518648497-e4ea72bcb27d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': 'd3ceee6f950a903e0f6b58ee34e6048b',
                 'path': 'Experimental\\a woman in a white dress with branches on '
                         'her head.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1705518648497-e4ea72bcb27d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['a woman in a white dress with branches on her head']}
    2024-01-19 09:42:14 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/a-close-up-of-a-building-made-out-of-bricks-ehTjAGnylco>
    {'category': ['Textures & Patterns'],
     'file_path': ['Textures & Patterns\\a close up of a building made out of '
                   'bricks.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1705113165376-b14041df2059?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': 'beaedd6346497582b2e9a34b2088dec3',
                 'path': 'Textures & Patterns\\a close up of a building made out '
                         'of bricks.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1705113165376-b14041df2059?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['a close up of a building made out of bricks']}
    
    .......
    
    2024-01-19 09:42:18 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1704292672006-4e7d032e7fd1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:18 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1704292672006-4e7d032e7fd1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:18 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/an-aerial-view-of-a-body-of-water-t2KDsrTfBZ0>
    {'category': ['Nature'],
     'file_path': ['Nature\\an aerial view of a body of water.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1705133847476-d05dc384e2bf?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': '332bb2b3118df036a120d90423253055',
                 'path': 'Nature\\an aerial view of a body of water.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1705133847476-d05dc384e2bf?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['an aerial view of a body of water']}
    2024-01-19 09:42:18 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/a-pile-of-oranges-sitting-on-top-of-each-other-7idGftc2HYo>
    {'category': ['Food & Drink'],
     'file_path': ['Food & Drink\\a pile of oranges sitting on top of each '
                   'other.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1704292672006-4e7d032e7fd1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': '183c6d6a483f9a03bac1b505151a23ed',
                 'path': 'Food & Drink\\a pile of oranges sitting on top of each '
                         'other.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1704292672006-4e7d032e7fd1?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['a pile of oranges sitting on top of each other']}
    2024-01-19 09:42:19 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://images.unsplash.com/photo-1705256978713-d51de443130d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> (referer: None)
    2024-01-19 09:42:19 [scrapy.pipelines.files] DEBUG: File (downloaded): Downloaded file from <GET https://images.unsplash.com/photo-1705256978713-d51de443130d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D> referred in <None>
    2024-01-19 09:42:19 [scrapy.core.scraper] DEBUG: Scraped from <200 https://unsplash.com/photos/a-person-standing-on-top-of-a-mountain-holding-an-umbrella-tXbfVgLRc5g>
    {'category': ['Experimental'],
     'file_path': ['Experimental\\a person standing on top of a mountain holding '
                   'an umbrella.jpg'],
     'image_urls': ['https://images.unsplash.com/photo-1705256978713-d51de443130d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'],
     'images': [{'checksum': '689065da1ae5fbbe3aa506cc8906b631',
                 'path': 'Experimental\\a person standing on top of a mountain '
                         'holding an umbrella.jpg',
                 'status': 'downloaded',
                 'url': 'https://images.unsplash.com/photo-1705256978713-d51de443130d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'}],
     'name': ['a person standing on top of a mountain holding an umbrella']}
    2024-01-19 09:42:19 [scrapy.extensions.feedexport] INFO: Stored csv feed (93 items) in: scraped_data.csv
    2024-01-19 09:42:19 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 79209,
     'downloader/request_count': 206,
     'downloader/request_method_count/GET': 206,
     'downloader/response_bytes': 21673945,
     'downloader/response_count': 206,
     'downloader/response_status_count/200': 204,
     'downloader/response_status_count/404': 2,
     'dupefilter/filtered': 398,
     'elapsed_time_seconds': 8.393204,
     'feedexport/success_count/FileFeedStorage': 1,
     'file_count': 93,
     'file_status_count/downloaded': 93,
     'finish_reason': 'shutdown',
     'finish_time': datetime.datetime(2024, 1, 19, 6, 42, 19, 959992, tzinfo=datetime.timezone.utc),
     'httpcompression/response_bytes': 30783044,
     'httpcompression/response_count': 111,
     'item_scraped_count': 93,
     'log_count/DEBUG': 396,
     'log_count/INFO': 12,
     'log_count/WARNING': 1,
     'request_depth_max': 2,
     'response_received_count': 206,
     'robotstxt/request_count': 3,
     'robotstxt/response_count': 3,
     'robotstxt/response_status_count/200': 1,
     'robotstxt/response_status_count/404': 2,
     'scheduler/dequeued': 110,
     'scheduler/dequeued/memory': 110,
     'scheduler/enqueued': 329,
     'scheduler/enqueued/memory': 329,
     'start_time': datetime.datetime(2024, 1, 19, 6, 42, 11, 566788, tzinfo=datetime.timezone.utc)}
    2024-01-19 09:42:19 [scrapy.core.engine] INFO: Spider closed (shutdown)
    
    (venv) C:\Work\python\Data\PyData_dz6\unsplash>

Структура файлов после обработки

    (venv) C:\Work\python\Data\PyData_dz6\unsplash\scraped_images>tree /F
    Структура папок тома Windows-SSD
    Серийный номер тома: 1A38-9DB5
    C:.
    ├───3D Renders
    │       a black and white photo of a circular object.jpg
    │       a couple of people that are standing in the dark.jpg
    │       a white x-ray of a person's face.jpg
    │
    ├───Animals
    │       a close up of a bird with a blurry background.jpg
    │       a close up of a green parrot with a red beak.jpg
    │       a small bird perched on a tree branch.jpg
    │       a small white dog standing in the snow.jpg
    │
    ├───Architecture & Interiors
    │       a living room filled with furniture and a staircase.jpg
    │       a very tall building with a lot of windows.jpg
    │
    ├───Arts & Culture
    │       a woman in a kimono holding a bouquet of flowers.jpg
    │
    ├───Experimental
    │       a blue window on a yellow wall with a shadow of a palm tree.jpg
    │       a person standing on top of a mountain holding an umbrella.jpg
    │       a woman in a white dress with branches on her head.jpg
    │
    ├───Fashion & Beauty
    │       a man standing in a dark room with a red light on his face.jpg
    │       a man with no shirt on posing for a picture.jpg
    │
    ├───Film
    │       a basketball hoop hanging from the side of a house.jpg
    │       a fern is growing in the middle of a forest.jpg
    │
    ├───Food & Drink
    │       a bowl of gummy bears sitting on top of a wooden table.jpg
    │       a bunch of lemons sitting on top of a table.jpg
    │       a cup of cereal and a bottle of milk.jpg
    │       a hand holding a drink in a pool.jpg
    │       a person holding a cup of coffee with a toothbrush in it.jpg
    │       a pile of oranges sitting on top of each other.jpg
    │       clear drinking glass with red liquid.jpg
    │       cookies on top of white ceramic footed tray.jpg
    │       sliced lemon on white ceramic plate.jpg
    │       three slices of orange sitting on top of a blue surface.jpg
    │
    ├───Health & Wellness
    │       a glass of yogurt and a cup of coffee on a tray.jpg
    │       assorted-color of fruits and vegetables.jpg
    │       man in gray long sleeve shirt holding black smartphone.jpg
    │       person wearing silver watch holding black bicycle handle bar.jpg
    │       sliced avocado fruit on white ceramic saucer beside stainless steel spoon.jpg
    │       white shower head on white wall tiles.jpg
    │
    ├───Minimalism
    │       a black and white photo of a cat sitting on a window sill.jpg
    │       a black and white photo of a white wall.jpg
    │       a close up view of a wavy white surface.jpg
    │       a group of people standing on top of a beach next to the ocean.jpg
    │       a group of three white vases sitting on top of a table.jpg
    │       a group of white vases sitting on top of a table.jpg
    │       a person standing on a beach next to the ocean.jpg
    │       a woman in a white dress walking across a desert.jpg
    │       a woman in a white dress walking up a flight of stairs.jpg
    │       black and brown leather padded tub sofa.jpg
    │       black denim jeans.jpg
    │       brown ceramic teacup.jpg
    │       landscape photography of sand dunes.jpg
    │       painting of stairs with white wooden frame.jpg
    │       white cloth.jpg
    │       white cluster petaled flower in close up photography.jpg
    │       white concrete wall.jpg
    │       white flower graphic wallpaper.jpg
    │       white notebook.jpg
    │       white wooden table near brown chair.jpg
    │
    ├───Monochromatic
    │       a close up of a banana plant with green leaves.jpg
    │
    ├───Nature
    │       a bird sitting on top of a tree branch.jpg
    │       an aerial view of a body of water.jpg
    │
    ├───None
    │       a bunch of bubbles floating in the air.jpg
    │       a close up of a bunch of candy hearts.jpg
    │       a close up of a flower with a blurry background.jpg
    │       a couple of large wooden doors in front of a building.jpg
    │       a group of people sitting on top of a couch.jpg
    │       a group of young people standing next to each other.jpg
    │       a laptop computer sitting on top of a wooden desk.jpg
    │       a large wave crashing into the shore with houses in the background.jpg
    │       a man and a woman standing next to each other.jpg
    │       a man in a space suit with a skull on his back.jpg
    │       a man riding skis on top of a snow covered slope.jpg
    │       a man sitting on a bench using a laptop computer.jpg
    │       a narrow alleyway with blue buildings and steps.jpg
    │       a person holding a cat's paw while sitting on a couch.jpg
    │       a room that has some shelves in it.jpg
    │       a small house in the middle of a forest.jpg
    │       a table topped with bowls of food and pickles.jpg
    │       an aerial view of a river running through a rocky landscape.jpg
    │       two women sitting on a couch looking at a book.jpg
    │
    ├───People
    │       a man in a black jacket is posing for a picture.jpg
    │       a man standing outside.jpg
    │       man doing a cross hand sign with his arms.jpg
    │       None.jpg
    │
    ├───Street Photography
    │       a coffee shop with people sitting in the window.jpg
    │       a couple of women walking down a street next to a dog.jpg
    │       a shadow of a person on a wall.jpg
    │       an escalator in a building with a mural on the wall.jpg
    │       cars parked on side of the road.jpg
    │       None.jpg
    │
    ├───Textures & Patterns
    │       a close up of a building made out of bricks.jpg
    │       a close up of a white object with wavy lines.jpg
    │       a large body of water covered in lots of water.jpg
    │       a painting of a tree in the snow.jpg
    │       an aerial view of a beach and a body of water.jpg
    │       an aerial view of a snow covered forest.jpg
    │
    ├───Travel
    │       a couple of tall buildings.jpg
    │
    └───Wallpapers
            a snow covered mountain with clouds in the foreground.jpg
    
    
    (venv) C:\Work\python\Data\PyData_dz6\unsplash\scraped_images>
    