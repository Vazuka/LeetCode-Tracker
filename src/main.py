import requests
from bs4 import BeautifulSoup

#username = 'nick-vishnoi'
#url = f'https://www.leetcode.com/u/nick-vishnoi/'

response = requests.get('https://www.leetcode.com/u/nick-vishnoi/')
if response.status_code != 200:
    raise Exception('Failed to load page')

soup = BeautifulSoup(response.content, 'html.parser')

solved_problems = soup.find('span', {'class': 'text-[30px] font-semibold leading-[32px]'})

if solved_problems:
    print(f'Number of problems solved: {solved_problems.text.strip()}')
else:
    print('Failed to find the number of solved problems on the profile page')
