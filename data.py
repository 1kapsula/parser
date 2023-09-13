import json
import datetime
import operator
import copy

class NewsStats:
    news_info = []

    def __init__(self, info_path=None):
        with open(info_path, 'r') as f:
            self.news_info = json.loads(f.read())
            for i in self.news_info:
                i['date'] = datetime.datetime.strptime(i['date'], '%d.%m.%Y,%H:%M')

    def GetShortest(self,max=-1):
        data = copy.deepcopy(self.news_info)
        data = sorted(data, key=lambda d: d['time to read'])
        if max != -1:
            data = data[:max]
        return data

    def GetLongest(self,max=-1):
        data = copy.deepcopy(self.news_info)
        data = sorted(data, key=lambda d: d['time to read'], reverse=True)
        if max != -1:
            data = data[:max]
        return data

    def GetNewsOfOneDay(self, one_day, max=-1):
        data = copy.deepcopy(self.news_info)
        rtn_list = [i for i in data if i['date'].strftime('%d.%m.%Y') == one_day.strftime('%d.%m.%Y')]
        if max != -1:
            rtn_list = rtn_list[:max]
        return rtn_list

    def FindArticleByName(self, name, max=-1):
        data = copy.deepcopy(self.news_info)
        rtn_list = [i for i in data if name in i['header']]
        if max != -1:
            rtn_list = rtn_list[:max]
        return rtn_list

    def GetLeastPopular(self, max=-1):
        data = copy.deepcopy(self.news_info)
        data = sorted(data, key=lambda d: d['comments count'])
        if max != -1:
            data = data[:max]
        return data

    def GetMostPopular(self,max=-1):
        data = copy.deepcopy(self.news_info)
        data = sorted(data, key=lambda d: d['comments count'], reverse=True)
        if max != -1:
            data = data[:max]
        return data