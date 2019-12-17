from requests_html import HTMLSession
import sys
from bs4 import BeautifulSoup


numbers = sys.argv

session = HTMLSession()
content = session.get('http://ketqua.net')
content_tree = BeautifulSoup(content.text, 'html.parser')


def lottery():
    awards = {'Giải đặc biệt': [find_number(0, 0)],
              'Giải nhất': [find_number(1, 0)],
              'Giải nhì': [find_number(2, 0), find_number(2, 1)],
              'Giải ba': [find_number(3, n) for n in range(6)],
              'Giải tư': [find_number(4, n) for n in range(4)],
              'Giải năm': [find_number(5, n) for n in range(6)],
              'Giải sáu': [find_number(6, n) for n in range(3)],
              'Giải bảy': [find_number(7, n) for n in range(4)]
              }
    set_numbers = set(numbers)
    awards_numbers = []
    for item in list(awards):
        awards_numbers.extend(awards[item])
    set_awards_numbers = set(awards_numbers)
    if set_numbers.intersection(set_awards_numbers) != set():
        for number in numbers:
            for item in list(awards):
                if number in awards[item]:
                    print(f"Chúc mừng bạn đã được {item} với số {number}!")
    else:
        for item in list(awards):
            value = ' | '.join(awards[item])
            print(f"{item}: {value}")


def find_number(x, y):
    number_location = content_tree.find('td', attrs={'id': f'rs_{x}_{y}'})
    return number_location.text[-2:]


if __name__ == "__main__":
    lottery()
