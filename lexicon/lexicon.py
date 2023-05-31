LEXICON: dict[str, str] = {'/start': 'Привет!\n\nЯ - бот, который отслеживает цены в интернет-магазине Wildberries.\n\n'
                                     'Как это работает?\n'
                                     '- Ты отправляешь мне артикул товара\n'
                                     '- Когда цена товара уменьшится я пришлю тебе уведомление\n\n'
                                     'Чтобы узнать подробнее о работе бота нажми /help\n'
                                     'техподдержка: @help_enot_kufar',
                           '/help': 'Ты можешь добавлять товары для отслеживаня цены просто отправляя боту артикулы товаров\n\n'
                                    'чтобы просмотреть список отслеживаемых товаров  и удалить неактуальные выбери в меню соответствующий пункт (/list)\n\n'
                                    'чтобы удалить все товары из списка отслеживания или изменить валюту цен выбери в меню пункт "перезапустить бота!"\n\n'
                                    'техподдержка: @help_enot_kufar',
                           'max_items': 'К сожалению достигнуто максимальное количество '
                                        'отслеживаемых товаров\n\n'
                                        'Вы можете удалить неактуальные товары из списка отслеживания.\n\n'
                                        'Просмотреть список: /list'}


LEXICON_COMMANDS: dict[str, str] = {'/start': "🔄Перезапуск бота!🔄",
                                    '/help': '🆘Описание работы бота🆘',
                                    '/list': '📝список отслеживаемых товаров📝'}


LEXICON_CURRENCY: dict[str, str] = {'rub': 'RUB 🇷🇺 Росс. рубль',
                                    'byn': 'BYN 🇧🇾 Бел. рубль',
                                    'kzt': 'KZT 🇰🇿 Казахский тенге',
                                    'kgs': 'KGS 🇰🇬 Киргизский сом',
                                    'uzs': 'UZS 🇺🇿 Узбекский сум',
                                    'usd': 'USD 🇺🇸 Доллар США',
                                    'amd': 'AMD 🇦🇲 Армянский драм'}