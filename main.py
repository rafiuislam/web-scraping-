from bs4 import BeautifulSoup
import requests

print('What skills are you not familiar with? ')
unfamiliar_skill = input(":")
print(f"Filtering out {unfamiliar_skill}")

html_res = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_res, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        links = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print('')
            print('')
            
            print(f"Company Name: {company_name.strip()}")
            print('')
            print(f"Required skills: {skills.strip()}")
            print('')
            print(f"More Info: {links}")

            print('')
            print('')
