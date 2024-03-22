import requests
from datetime import datetime
from bs4 import BeautifulSoup

def save_list_to_file(lst, filename):
    with open(filename, 'a') as file:
        line = ', '.join(map(str, lst)) + '\n'
        file.write(line)


def crawling_lotto(count):
    # url에 회차를 실어 페이지 조회
    url = f'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    date = datetime.strptime(soup.find('p', class_='desc').text, '(%Y년 %m월 %d일 추첨)')
    win_number = [int(i) for i in soup.find('div', class_='num win').find('p').text.strip().split('\n')]
    bonus_number = int(soup.find('div', class_='num bonus').find('p').text.strip())
    
    save_list_to_file(win_number,'lotto_data.txt')
    return win_number


if __name__ == "__main__":
    # print(crawling_lotto(1))

    for i in range(1111):
        print(str(i+1)+"회차 : ")
        print(crawling_lotto(i+1))