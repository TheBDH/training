import requests

cookies = {
    '_ga': 'GA1.2.457204887.1470587010',
    '__utma': '117564634.457204887.1470587010.1472083386.1472087084.9',
    '__utmc': '117564634',
    '__utmz': '117564634.1472087084.9.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'IDMSESSID': '100605285',
    'TS01c30e41': '014b44e76b4319048068fa9c15aecf017eac3f6b5531ce6a0487161c60926bf1ea271dc1c6ebc54059b16808529f7180160bba521dc4ccde2c2dfddef845c2c8217b09dd50',
}

headers = {
    'Origin': 'https://cab.brown.edu',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,es;q=0.6,fr;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://cab.brown.edu/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = 'criteria=%255B%257B%2522field%2522%253A%2522course.level%2522%252C%2522value%2522%253A%2522u%2522%257D%252C%257B%2522field%2522%253A%2522course.dept%2522%252C%2522value%2522%253A%2522AFRI%2522%257D%255D'

r = requests.post('https://cab.brown.edu/asoc-api/?output=json&page=asoc.rjs&route=search&term=201610', headers=headers, cookies=cookies, data=data)

response = r.json()

classes = response["courses"]

to_print = []

for c in classes:
    to_print.append(c["title"])

f = open("output.txt", "w")

f.truncate()

for c in to_print:
    f.write(c + "\n")