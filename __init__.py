from download import Downloader
from data import NewsStats
from parse import Parser
import datetime
import json
import copy

PARAMS = {
    'rubric': 8,
    'range': 'month',
    'date': datetime.date(2023, 7, 4)
}
URL = 'https://www.kommersant.ru/archive/rubric/'

def process(url, web_page_path=None, data_path=None):
    downloader = Downloader(url,PARAMS)
    downloader.get_html()
    downloader.save(web_page_path)

    prser = Parser(web_page_path)
    prser.parse()
    prser.save(data_path)

    data_analise = NewsStats(data_path)

    response = []
    rtn_val = {'test name': '', 'response': []}
    max = 10
    subtext = 'Названы'

    rtn_val['test name'] = 'Find article by name "' + subtext + '" ' + str(max)
    rtn_val['response'] = copy.deepcopy(data_analise.FindArticleByName(subtext))
    if rtn_val['response'] is not None:
        for i in rtn_val['response']:
            i['date'] = i['date'].strftime('%d.%m.%Y,%H:%M')
    response.append(rtn_val)
    print('готово')

    rtn_val = {'test name': '','response': []}
    max = 2

    rtn_val['test name'] = 'Get least popular ' + str(max)
    rtn_val['response'] = copy.deepcopy(data_analise.GetLeastPopular(max))
    if rtn_val['response'] is not None:
        for i in rtn_val['response']:
            i['date'] = i['date'].strftime('%d.%m.%Y,%H:%M')
    response.append(rtn_val)
    print(rtn_val)

    rtn_val = {'test name': '', 'response': []}
    max = 1

    rtn_val['test name'] = 'Get most popular ' + str(max)
    rtn_val['response'] = copy.deepcopy(data_analise.GetMostPopular(1))
    if rtn_val['response'] is not None:
        for i in rtn_val['response']:
            i['date'] = i['date'].strftime('%d.%m.%Y,%H:%M')
    response.append(copy.deepcopy(rtn_val))
    print('готово')

    rtn_val = {'test name': '', 'response': []}
    max = 1

    rtn_val['test name'] = 'Get longest ' + str(max)
    rtn_val['response'] = copy.deepcopy(data_analise.GetLongest(1))
    if rtn_val['response'] is not None:
        for i in rtn_val['response']:
            i['date'] = i['date'].strftime('%d.%m.%Y,%H:%M')
    response.append(rtn_val)
    print('готово')

    rtn_val = {'test name': '', 'response': []}
    max = 1

    rtn_val['test name'] = 'Get shortest ' + str(max)
    rtn_val['response'] = copy.deepcopy(data_analise.GetShortest(1))
    if rtn_val['response'] is not None:
        for i in rtn_val['response']:
            i['date'] = i['date'].strftime('%d.%m.%Y,%H:%M')
    response.append(rtn_val)
    print('готово')

    rtn_val = {'test name': '', 'response': []}
    day_datetime = datetime.date(2023, 4, 7)
    day = day_datetime.strftime('%d.%m.%Y')
    max = 10

    rtn_val['test name'] = 'Get news of a day ' + day + ' ' + str(max)
    rtn_val['response'] = copy.deepcopy(data_analise.GetNewsOfOneDay(day_datetime, max))
    if rtn_val['response'] is not None:
        for i in rtn_val['response']:
            i['date'] = i['date'].strftime('%d.%m.%Y,%H:%M')
    response.append(rtn_val)
    print('готово')

    with open('output1.json', 'w') as f:
        f.write(json.dumps(response, indent=4, ensure_ascii=False))
    return

process(URL, 'news.html', 'output.json')