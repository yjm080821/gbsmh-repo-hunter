import json
import subprocess
from colorama import Fore, Style, init
init()

with open("github_projects.json", encoding="utf-8") as f:
    data = json.load(f)

# 유저 및 프로젝트 목록 출력
print("\n🗂️  사용 가능한 GitHub 프로젝트:\n")

user_map = {}  # 번호 기반 선택용

idx = 1
for user_info in data:
    user = user_info['user']
    url = user_info['url']
    projects = user_info['projects']

    print(f"{Fore.CYAN}{user}{Style.RESET_ALL} ({url})")
    for proj in projects:
        print(f"  {Fore.YELLOW}[{idx}]{Style.RESET_ALL} {proj}")
        user_map[str(idx)] = (url, proj)
        idx += 1
    print()

# 사용자 입력받기
choice = input(f"\n👉 복사할 프로젝트 번호 입력: ")

if choice not in user_map:
    print("❌ 잘못된 선택입니다.")
else:
    base_url, repo = user_map[choice]
    username = base_url.strip("/").split("/")[-1]
    clone_url = f"https://github.com/{username}/{repo}.git"

    print(f"\n📦 복제 중: {Fore.GREEN}{clone_url}{Style.RESET_ALL}")
    subprocess.run(["git", "clone", clone_url])
