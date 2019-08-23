import requests
payload = {"location":"chicago","description":"python","type":""}
r = requests.get('https://jobs.github.com/positions.json', params=payload)
print(r.url)
# print(r.text)

languages = ['c++', 'ruby', 'scala', 'python', 'sql', 'javascript']
for entry in r.json():

    print('________________________________________________________________________________')
    print(entry['type'])
    print('________________________________________________________________________________')
