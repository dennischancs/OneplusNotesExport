# 导入库
import sys
import io
import time
import json
import re
import requests

with open("Notes/oneplus_Notes.html","w", encoding='utf8') as f:
    # 预设 url
    urls = {
        'list_url': 'https://cloud.h2os.com/note/list', # 获取一加便签所有条目id
        'note_url': 'https://cloud.h2os.com/note/info'  # 由各条目id获取具体内容
    }

    # 预设 header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        'Host': 'cloud.h2os.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://cloud.h2os.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://cloud.h2os.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5,ja;q=0.4,de-DE;q=0.3,de;q=0.2,zh-TW;q=0.1,und;q=0.1',
        'Cookie': '**********; opcloud_token=ONEPLUS_cd**********P4ZA; NEARME_ACCOUNTNAME_COOKIE=D***n; opcloud_vcode=79a***********577; accountName=D****n'
    }

    # 采用Cookies登陆
    opcloud_token = re.split('opcloud_token=(.*?);', headers['Cookie'])[1]
    s=requests.session()

    # 获取list_id
    r_listjson = s.post(urls['list_url'], data='last=0&isinit=1&group=&token='+opcloud_token, headers=headers, verify=False)
    r_list = json.loads(r_listjson.text)
    noteall = ''

    for i in range(r_list['totalCount']-1):
      noteId = r_list['items'][i]['globalId'] # 每条note的id
      noteSubject = r_list['items'][i]['subject'] # 每条note的标题
      noteTime = time.strftime("%Y%m%d-%H:%M:%S", time.localtime(r_list['items'][i]['updated']/1000)) # 每条note的最近编辑时间
      # 获取notes
      r_notejson = s.post(urls['note_url'], data='token='+opcloud_token+'&gid='+noteId, headers=headers, verify=False)
      r_note = json.loads(r_notejson.content)
      noteContent = r_note['content']
      noteall += "<h2>{} - {}</h2><h4>updated : {}</h4>{}<hr/>\n".format(i+1, noteSubject, noteTime, noteContent) # 写入notes
   
    # dump as HTML
    html = "<!DOCTYPE html>\n<head>{}</head>\n<body>\n{}</body>\n</html>"
    # add a title
    title = "<h1>Oneplus Notes Export</h1>"

    # f.write(content)
    body = "{}\n<hr/><hr/>\n{}".format(title, noteall)
    html = html.format('', body)
    f.write(html)
