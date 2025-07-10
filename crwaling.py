from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
import json
import time

service = Service('geckodriver.exe')
driver = webdriver.Firefox(service=service)
driver.get("https://github.com/orgs/GBSWHS/people")
time.sleep(3)

member_links = []
members = driver.find_elements(By.CSS_SELECTOR, 'a.f4.d-block')
for member in members:
    name = member.text.strip()
    url = member.get_attribute('href')
    member_links.append((name, url))

data = []

data = []

for name, profile_url in member_links:
    all_repos = []
    page = 1

    while True:
        driver.get(f"{profile_url}?page={page}&tab=repositories")
        time.sleep(2)

        repos = driver.find_elements(By.CSS_SELECTOR, 'div#user-repositories-list ul li h3 a')
        if not repos:
            break

        repo_names = [repo.text.strip() for repo in repos]
        all_repos.extend(repo_names)
        page += 1

    data.append({
        "user": name,
        "url": profile_url,
        "projects": all_repos
    })


driver.quit()

with open("github_projects.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ JSON 저장 완료: github_projects.json")
