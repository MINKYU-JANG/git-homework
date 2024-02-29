import random

# 이전 게임에서 최고 시도 횟수를 기록하기 위한 변수
best_try_count = 0

# n 입력 전까지 무한 반복
while True:

    # 1 부터 100까지 랜덤한 수 생성
    random_number = random.randint(1, 100)
    user_input = int(input('숫자를 입력하세요: '))

    # 1 ~ 100 숫자 입력
    if 1 <= user_input <= 100:

        # 첫번째 입력
        count = 1

        # 같은 수가 나올 때 까지 반복
        while user_input != random_number:

            # 시도 횟수 카운트
            count += 1

            if user_input > random_number:
                print('다운')

            elif user_input < random_number:
                print('업')

            user_input = int(input('다시 입력하세요: '))

        print('맞았습니다!')
        print('시도한 횟수:', count)

        # 시도한 횟수가 최고 시도 횟수 보다 높으면 갱신
        if count > best_try_count:
            best_try_count = count

        # 게임 재시작 여부 묻기
        while True:

            retry = input('다시 하시겠습니까? (y/n): ')

            if retry == 'y':
                print('이전 게임 플레이어 최고 시도 횟수:', best_try_count)
                break

            elif retry == 'n':
                print('게임을 종료합니다.')
                break

            else:
                print('y/n 로만 입력해주세요')

        # retry == 'y':게임 재시작, retry == 'n':게임 종료
        if retry == 'n':
            break

    else:
        print('유효한 범위 내의 숫자를 입력하세요')
