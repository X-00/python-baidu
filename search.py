from bs4 import BeautifulSoup
import requests

word=input("请输入搜索的关键词:");
page=input("请输入要爬取的页数:")
START_URL="http://www.baidu.com/s?wd={0}&pn={1}"
# HEADERS={"Accept": "text/html, application/xhtml+xml, image/jxr, */*",

         # "Accept - Encoding": "gzip, deflate, br",

         # "Accept - Language": "zh - CN",

         # "Connection": "Keep - Alive",
         # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
         # "referer":"baidu.com"};
HEADERS={
 "X-Requested-With":"XMLHttpRequest",
 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; ServiceUI 13.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"  
}
num=int(page)
for i in range(0,num):
    if i==0:
        nums=0
    else:
        # if i==1:
            # nums=10
        # else:	 
        nums=int(i*10)
    print('-----------------------------------------第'+str(i+1)+'页---------------------------------------------------------')
    url=START_URL.format(word,nums)
    html=requests.get(url,headers=HEADERS).content.decode("utf-8") 
    pages=BeautifulSoup(html,'html.parser').find_all('h3',class_='t')
    for result_table in pages:
        a_click = result_table.find("a");
        print( "-----标题----\n" + a_click.get_text())  # 标题
        print("----链接----\n" + str(a_click.get("href")))  # 链接
