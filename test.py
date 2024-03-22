import random
from collections import Counter

def generate_lotto_numbers():
    past_results = [
        [1, 3, 11, 20, 25, 31],  # 예시: 과거 로또 당첨 번호 100회
        # 여기에 실제 과거 로또 당첨 번호 데이터를 입력합니다.
    ]

    # 모든 당첨 번호를 하나의 리스트로 펼칩니다.
    all_numbers = [number for result in past_results for number in result]

    # 각 번호의 출현 빈도를 카운트합니다.
    number_counts = Counter(all_numbers)

    # 출현 빈도가 높은 순으로 정렬합니다.
    sorted_numbers = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)

    # 출현 빈도가 높은 번호일수록 선택 확률을 높게 설정합니다.
    probabilities = {num: (count / len(past_results)) for num, count in sorted_numbers}

    # 선택 확률을 기반으로 번호를 선택합니다.
    selected_numbers = random.choices(list(probabilities.keys()), weights=list(probabilities.values()), k=6)

    return sorted(selected_numbers)

if __name__ == "__main__":
    numbers = generate_lotto_numbers()
    print("로또 번호:", numbers)
