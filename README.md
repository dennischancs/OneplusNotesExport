# Oneplus Notes Export

一加手机便签APP数据导出为html文件

# 使用

1. 浏览器登陆[便签 - OnePlus Cloud Beta](https://cloud.h2os.com/#/note)；
2. 复制浏览器的Cookies，如下

```python
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
    'Cookie': '*****************************************************************'
}
```

3. 运行`python getNotes.py`，等待一会得到`Notes/oneplus_Notes.html`

# 效果
