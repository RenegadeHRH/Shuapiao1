
import requests
from fake_useragent import UserAgent
import socket

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


IP = get_host_ip()
def click():
    URI="https://www.ulearning.cn/eventjudge/contestant/setPraise.do"
    headers={
      "Pragma":"no-cache",
      "Cache-Control":"no-cache",
      "sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Microsoft Edge\";v=\"90\"",
      "Accept":"*/*",
      "X-Requested-With":"XMLHttpRequest",
      "sec-ch-ua-mobile":"?0",
      # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66",
      "User-Agent":UserAgent().random,
      "Origin":"https://www.ulearning.cn",
      "Sec-Fetch-Site":"same-origin",
      "Sec-Fetch-Mode":"cors",
      "Sec-Fetch-Dest":"empty",
      "Referer":"https://www.ulearning.cn/eventjudge/contestant/getProductionByID.do?productionID=777",
      "Accept-Encoding":"gzip, deflate, br",
      "Accept-Language":"zh-CN,zh;q=0.9",
      # "Cookie":"Hm_lvt_82dc9406a304f020903ac2082ddad1d8=1618191428,1619106594,1619260382,1620742025; xn_dvid_kf_20125=6B3F40-D5FEE2C4-92E8-DBC4-AA11-5BC0B65C3A1E; HWWAFSESID=9a96773df26657df23; HWWAFSESTIME=1622019054545; UMOOC_SESSION=B15BA31A1E583E9F7A42E6757BB20D6B; ALREADPRAISE_777=false"
    }
    data={
    'productionID':'777',
     'IP':IP,
    }
    respond=requests.post(url=URI,data=data,headers=headers)
    print(IP)
    print(respond.status_code)
    print(respond.text)
click()
