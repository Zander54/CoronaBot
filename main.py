import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from bs4 import BeautifulSoup


token = "26a1c4b052f5cbee679a7ce920131f6b694aaa567e48855bbace0822dfd791eb128e996ec19fb1fb26a2f"
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


facts = ["Covid-19 и SARS-CoV-2 - не одно и то же. Covid-19 - это заболевание (D - сокращение от 'disease'), вызванное новым коронавирусом. SARS-CoV-2 - название самого вируса.",
"CoV - сокращение от CoronaVirus, коронавирус. Так называется семейство вирусов (всего их около 40), которые внешне напоминают солнечную корону из-за шиповидных отростков.",
"Коронавирусы - самозванцы от биологии. Наконечник каждого шипа 'имитирует' молекулу полезного вещества, так что клеточные рецепторы с радостью сами затягивают ее в себя - а за шипом в клетку продавливается весь вирус. Так происходит заражение.",
"Термин 'новый коронавирус'' (novel или nCoV) означает, что раньше он не встречался не только ученым, но и нашим клеткам.",
"За 2 млн лет эволюции наша иммунная система научилась бороться с большинством известных инфекций, но новый коронавирус застает ее врасплох - поэтому с ним так тяжело справиться и так легко заразиться.",
"Попав в клетку, вирус 'захватывает'' над ней контроль и заставляет бесконечно производить собственные копии - вместо привычных ей белков. Начинается цепная реакция. В итоге клетка погибает, но носитель инфекции становится заразным.",
"На начальном этапе заражения новый коронавирус активно размножается в горле и верхних дыхательных путях. Потом инфекция опускается ниже и может добраться до легких, вызывая воспаление.",
"Именно поэтому первый симптом заражения - кашель. Уже потом начинает повышаться температура.",
"Или не начинает - у 30% пациентов в Ухане температура на момент прибытия в больницу была не выше нормы.",
"У многих заразившихся (18% или почти каждого пятого) нет даже кашля. Болезнь протекает вообще без симптомов - человек может даже не подозревать, что болен.",
"При этом такой бессимптомный больной всё равно является активным носителем инфекции и может заражать других.",
"Если Covid-19 протекает в легкой форме, его симптомы очень похожи на обычный сезонный грипп: сухой кашель, температура, общая слабость, иногда боль в мышцах или головная боль.",
"Лечится он тоже точно так же, как обычный грипп - в домашних условиях, симптоматически.",
"Один из самых необычных симптомов коронавируса - потеря чувства вкуса и/или обоняния.",
"Он встречается не у всех инфицированных, но может быть и единственным симптомом.",
"Так что если вы вдруг перестали чувствовать запахи или вкусы, это повод насторожиться и принять меры.",
"Важно: носитель нового коронавируса становится опасен для окружающих сразу после заражения - задолго до того, как у него появятся или не появятся первые симптомы.",
"Хорошая новость: чем более смертоносен опасный вирус, тем хуже он распространяется. Убив своего хозяина, вирус больше не может заражать других. Поэтому вирус редко мутирует в более смертоносную форму - это не в его интересах.",
"Плохая новость: SARS-CoV-2 - как раз из другой категории. Этот вирус делает хозяина разносчиком заразы, но проявляется не сразу или не проявляется вообще, так что носитель успевает заразить еще нескольких человек.",
"В среднем каждый носитель нового коронавируса успевает заразить от 2 до 4 здоровых людей. Это число выше, чем у сезонного гриппа (1,3), но ниже, чем у кори (12+)."]

photos = ['photo-194380991_457239022', 'photo-194380991_457239023',
'photo-194380991_457239024', 'photo-194380991_457239025',
'photo-194380991_457239026', 'photo-194380991_457239027',
'photo-194380991_457239028', 'photo-194380991_457239029',
'photo-194380991_457239030', 'photo-194380991_457239031',
'photo-194380991_457239032', 'photo-194380991_457239033',
'photo-194380991_457239034', 'photo-194380991_457239035',
'photo-194380991_457239036', 'photo-194380991_457239037',
'photo-194380991_457239038', 'photo-194380991_457239039',
'photo-194380991_457239040', 'photo-194380991_457239041',
'photo-194380991_457239042', 'photo-194380991_457239043',
'photo-194380991_457239044', 'photo-194380991_457239045',
'photo-194380991_457239046', 'photo-194380991_457239047',
'photo-194380991_457239048', 'photo-194380991_457239049',
'photo-194380991_457239050', 'photo-194380991_457239051',
'photo-194380991_457239052', 'photo-194380991_457239053',
'photo-194380991_457239054', 'photo-194380991_457239055',
'photo-194380991_457239056','photo-194380991_457239057',
'photo-194380991_457239058']

nums = []

for _ in range(len(photos)):
    nums.append(int(_))


def getRegionInfo(Region_name):
    page = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/#")
    soup = BeautifulSoup(page.text, features="html.parser")
    ill, healed, dead = 0, 0, 0

    data = soup.find_all('tr')

    for reg in data:
        if 'откуда' in reg.text.lower():
            break
        region = reg.find('th').text.lower()
        
        if region == Region_name or Region_name in region:
            nums = reg.find_all('td')
            ill = nums[0].text
            healed = nums[1].text
            dead = nums[2].text
            info = "В связи с коронавирусной инфекцией в данном регионе сейчас:\n"\
            "Случаев заболевания: {}\n"\
            "Выздоровлений: {}\n"\
            "Смертей: {}\n"\
            "Информация взята с сайта стопкоронавирус.рф".format(ill, healed, dead)
            return info
    return "Не нашел такого региона... Попробуйте ввести укореченное название."     


def getMeme():
    num = random.randint(0, len(nums) - 1)
    memenum = nums[num]
    nums.remove(nums[num])
    if len(nums) <= 1:
        nums.clear()
        for _ in range(len(photos)):
            nums.append(int(_))
    return photos[memenum]


def getInfo():
    site = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/")

    if site.status_code != 200:
        return "Извините, в данный момент информация недоступна."
    html = site.text

    soup = BeautifulSoup(html, features="html.parser")

    all = soup.find_all('div', class_="cv-countdown__item-value")
    # all = soup.find_all('div', class_="cv-countdown__item-value _accent")

    tests = all[0].text
    ill = all[1].text
    day_ill = all[2].text
    heal = all[3].text
    dead = all[4].text
    info = "На данный момент в России по коронавирусу ситуация следующая:\n" \
           "Проведено тестов: {}\n" \
           "Случаев заболевания: {}\n" \
           "Случаев заболевания за последние сутки: {}\n" \
           "Выздоровевших: {}\n" \
           "Умерших: {}.\n" \
           "Информация взята с сайта стопкоронавирус.рф".format(tests, ill, day_ill, heal, dead)
    return info


def random_id():
    return random.randint(0, 10000000000000)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.text.lower() == 'начать':
            vk.messages.send(
                user_id = event.user_id,
                message = "Здравствуй! Я являюсь ВК-ботом, способным поставлять актуальную и свежую " +
                "информацию о заболевании Covid-19 в Российской Федерации.\n" +
                "Все факты, которые я использую, взяты с https://www.bbc.com/russian/features-52065978\n"
                "Приятной самоизоляции!",
                keyboard = open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id = random_id()
            )
        elif event.text.lower() == 'привет':
            vk.messages.send(
                user_id = event.user_id,
                message = "Привет!",
                keyboard = open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id = random_id()
            )
        elif event.text.lower() == 'ситуация в стране':
            vk.messages.send(
                user_id=event.user_id,
                message=getInfo(),
                keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id=random_id()
            )
        elif event.text.lower() == 'мемы':
            vk.messages.send(
                user_id=event.user_id,
                message="",
                keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id=random_id(),
                attachment = getMeme()
            )
        elif event.text.lower() == 'мифы':
            vk.messages.send(
                user_id=event.user_id,
                message='''Мифы о коронавирусе:\n-новым коронавирусом нельзя заразиться через письма и посылки
-нет никаких доказательств, что домашние животные, как собаки или кошки, могут быть переносчиками нового коронавируса
-вакцины против пневмонии не защищают от нового коронавируса
-высокая и низкая температура не убивает новый коронавирус
-новый коронавирус не лечится антибиотиками
-на данный момент лекарств для профилактики или лечения нового коронавируса нет. Тем не менее обращаться к врачу необхожимо каждому пациенту. Медицинская помощь поможет облегчить симптомы и не допустить дальнейшего развития заболевания''',
                keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id=random_id()
            )
        elif event.text.lower() == 'симптомы':
            vk.messages.send(
                user_id=event.user_id,
                message='''Симптомы коронавируса:\nповышение температуры тела;
утомляемость;
сухой кашель.
У некоторых инфицированных могут также наблюдаться:
боли в мышцах и суставах;
заложенность носа;
выделения из носа;
боль в горле;
диарея.
В среднем с момента заражения до возникновения симптомов проходит 5-6 дней, хотя в отдельных случаях этот период может продолжаться до 14 дней.''',
                keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id=random_id()
            )
        elif event.text.lower() == 'факты':
            vk.messages.send(
                user_id=event.user_id,
                message=random.choice(facts),
                keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id=random_id()
            )
        elif event.text.lower() == 'ситуация в конкретном регионе':
            vk.messages.send(
                user_id=event.user_id,
                message="Введите название региона.",
                keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id=random_id()
            )
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    vk.messages.send(
                        user_id=event.user_id,
                        message=getRegionInfo(event.text.lower()),
                        keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                        random_id=random_id()
                    )
                    break
        else:
            vk.messages.send(
                user_id=event.user_id,
                message="Не понял ваше сообщение...",
                keyboard=open('keyboard.json', 'r', encoding='UTF-8').read(),
                random_id=random_id()
            )


