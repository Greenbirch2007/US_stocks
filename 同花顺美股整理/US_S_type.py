# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql
import requests

from lxml import etree
from selenium import webdriver
from requests.exceptions import RequestException
driver = webdriver.Chrome()


def get_first_page(url):

    driver.get(url)
    html = driver.page_source
    return html















def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,5967):
        sql = 'select code from us_stock where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        s_code = data['code']

        yield s_code



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='us_stock',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into us_Types (code,name,industry) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






#
if __name__ == '__main__':


    nasdap100 = 'AAPL,MSFT,AMZN,GOOG,GOOGL,FB,INTC,CMCSA,PEP,CSCO,ADBE,NVDA,NFLX,TSLA,COST,PYPL,AMGN,AVGO,TXN,CHTR,SBUX,QCOM,GILD,MDLZ,TMUS,FISV,BKNG,INTU,ADP,ISRG,VRTX,MU,CSX,BIIB,AMAT,AMD,ATVI,EXC,MAR,LRCX,WBA,ADI,ROST,ADSK,REGN,ILMN,CTSH,XEL,JD,MNST,MELI,NXPI,BIDU,KHC,SIRI,PAYX,EA,LULU,EBAY,CTAS,WDAY,ORLY,VRSK,WLTW,CSGP,PCAR,KLAC,SPLK,NTES,MCHP,VRSN,ANSS,IDXX,CERN,ALXN,ASML,SNPS,FAST,DLTR,CPRT,XLNX,CDNS,ALGN,SGEN,WDC,UAL,SWKS,CDW,CHKP,ULTA,INCY,TCOM,BMRN,EXPE,MXIM,CTXS,TTWO,FOXA,AAL,NTAP,FOX,LBTYK,LBTYA'
    # f_nasdap100 = [x for x in nasdap100 if x != ","]
    f_nasdap100 = nasdap100.split(",")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=options)


    for url_code in f_nasdap100:


        url_str = 'http://stockpage.10jqka.com.cn/'+str(url_code)+'/company/'
        bl =[]
        html = get_first_page(url_str)
        big_list = []
        bl.append(url_code)
        selector = etree.HTML(html)
        name = selector.xpath('//*[@id="produce"]/div[2]/table/tbody/tr[1]/td[3]/text()')
        type = selector.xpath('//*[@id="produce"]/div[2]/table/tbody/tr[2]/td[2]/text()')
        f_l = bl+name+type
        ff=[]

        f_tuple= tuple(f_l)
        ff.append(f_tuple)



        insertDB(ff)
        time.sleep(0.5)
        print(datetime.datetime.now())



# #
# create table us_Types(
# id int not null primary key auto_increment,
# code varchar(20) ,
# name varchar(80),
# industry varchar(80)
#  ) engine=InnoDB default charset=utf8;

#
# drop table us_Types;





# a= ['6亿','6万','8亿']
# t = []
# for i in a:
#     b = "".join(re.split(r'亿|万|\s',a))
#     t.append(b)
#
# print(t)  # t = [6,6,8]