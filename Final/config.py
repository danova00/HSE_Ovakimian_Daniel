from lxml import etree
import urllib.request

class Config:

    web = urllib.request.urlopen('https://www.cbr.ru/currency_base/daily/')
    s = web.read()
    table_headers = []
    html = etree.HTML(s)
    tr_nodes = html.xpath('//table[@class="data"]/tbody/tr')
    header = html.xpath('//table[@class="data"]/tbody/tr/th')

    td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]
