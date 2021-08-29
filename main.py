from bs4 import BeautifulSoup
import requests
import time

print('What skills are you not familiar with? ')
unfamiliar_skill = input(":")
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_res = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_res, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            links = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'store/{index}.txt', 'w') as t:
                    t.write(f"Company Name: {company_name.strip()} \n")
                    t.write(f"Required skills: {skills.strip()} \n")
                    t.write(f"More Info: {links} ")

                print(f'File saved in: {index}')

if __name__ == "__main__":
    while True:
        find_jobs()
        minute_wait = 5
        print(f'Waiting {minute_wait} minutes')
        time.sleep(minute_wait * 60)