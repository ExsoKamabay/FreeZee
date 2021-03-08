from bs4 import BeautifulSoup;import requests,json

class Yippy:
    def yippy(self,query):
        dt = {
            'urls':[],
            'title':[],
            'decription':[],
            'datetime':[]
        }
        setattr(self,'url','http://www.yippy.com/search?query=%s'%(str(query)));
        setattr(self,'req',requests.get(getattr(self,'url')).content)
        setattr(self,'sup',BeautifulSoup(getattr(self,'req'),'html.parser'))
        setattr(self,'u&t',getattr(self,'sup').find_all('div',{'class':'field field-title'}))
        setattr(self,'dec',getattr(self,'sup').find_all('div',{'class':'field field-snippet'}))
        setattr(self,'date',getattr(self,'sup').find_all('div',{'class':'field field-date'}))
        for url,dec,dat in zip(
            getattr(self,'u&t'),
            getattr(self,'dec'),
            getattr(self,'date')):
            dt['urls'].append(url.a['href'])
            dt['datetime'].append(dat.span.text)
            dt['title'].append(url.span.text)
            dt['decription'].append(dec.span.text)

        self.dumps = json.dumps(dt,sort_keys=True,indent=2)
        return json.loads(self.dumps);


