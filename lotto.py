import random
from collections import Counter
from scipy.stats import pearsonr

def generate_lotto_numbers(past_results):
    # past_results = [
    #     [10,23,29,33,37,40],[9,13,21,25,32,42],[11,16,19,21,27,31],[14,27,30,31,40,42],[16,24,29,40,41,42],[14,15,26,27,40,42],[2,9,16,25,26,40],[8,19,25,34,37,39],[2,4,16,17,36,39],[9,25,30,33,41,44],[1,7,36,37,41,42],[2,11,21,25,39,45,44],[22,23,25,37,38,42],[2,6,12,1,33,40],[3,4,16,30,31,37],[6,7,24,37,38,40],[3,4,9,17,32,37],[3,12,13,19,32,35]  # 예시: 과거 로또 당첨 번호 100회
    #     # 여기에 실제 과거 로또 당첨 번호 데이터를 입력합니다.
    # ]
   
    testvalue = 55545445

    # 모든 당첨 번호를 하나의 리스트로 펼칩니다.
    # 리스트 컴프리헨젼 : [expression for item in iterable]
    # for result in past_results 가 한묶음(외부), for number in result가 한 묶음(내부)
    # 2차원 리스트의 모든 요소를 하나의 평평한 리스트로 변환
    all_numbers = [number for result in past_results for number in result]

    # 각 번호의 출현 빈도를 카운트합니다.
    # 딕셔너리같은 카운트 객체를 반환 Counter({1: 1, 2: 2, 3: 3})  number_counts[1] 이렇게 출력 가능
    number_counts = Counter(all_numbers)

    # 출현 빈도가 높은 순으로 정렬합니다.
    # items()는 [(1,1), (2,2), (3,3)] 의 리스트(키-값으로 이루어진 튜플) 형태로 반환
    # key:lambda는 정렬기준 x(키-값)중 x[1] 값에 대한 정렬을 한다는 의미 
    # 구체적으로는 lambda는 익명함수 => x라는 입력을 받아 x[1]을 반환하는 익명함수lambda가 key다
    sorted_numbers = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)

    # numbers_count = number_counts.items()


    # 출현 빈도가 높은 번호일수록 선택 확률을 높게 설정합니다.
    # 딕셔너리 컴프리헨젼 : {key_expr: value_expr for item in iterable}
    # num: (count / len(past_results)) => 딕셔너리의 key : value
    # for num, count in sorted_numbers => 각 튜플의 첫번째,두번째요소
    probabilities = {num: (count / len(past_results)) for num, count in sorted_numbers}

    print(probabilities)

    # 중복되지 않는 번호 6개를 선택합니다.
    selected_numbers = set()
    while len(selected_numbers) < 6:
        # print(random.choices(list(probabilities.keys()), weights=list(probabilities.values()))[0])
        number = random.choices(list(probabilities.keys()), weights=list(probabilities.values()))[0]
        selected_numbers.add(number)

    # print(probabilities)
    return sorted(selected_numbers)

def pair_probabilities(past_results):
    pair_counts = Counter()

    # 각 리스트에서 숫자 쌍의 빈도를 카운트
    for lst in past_results:
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                pair = tuple(sorted([lst[i], lst[j]]))
                pair_counts[pair] += 1

    # 전체 숫자의 총 개수
    total_numbers = len(past_results)

    print(total_numbers)
    # 각 숫자 쌍의 확률 계산
    probabilities = {pair: count / total_numbers for pair, count in pair_counts.items()}

    sorted_numbers = sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)

    print(probabilities.get((8,12),0))
    # 결과 출력
    # for pair, prob in probabilities.items():
    #     print(f"{pair}는 함께 나올 확률 {prob * 100:.2f}% 입니다.")

if __name__ == "__main__":

    past_results = []
    with open('lotto_data.txt', 'r') as file:
        for line in file:
            row = line.strip().split(',')  # 콤마로 구분된 문자열을 리스트로 분할
            row = [int(number) for number in row]  # 각 숫자를 정수로 변환
            past_results.append(row)  # 변환된 행을 데이터 리스트에 추가

    # numbers = generate_lotto_numbers(past_results)

    print(pair_probabilities(past_results))
    # print("로또 번호:", numbers)
