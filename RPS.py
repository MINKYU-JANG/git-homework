import random

# 가위 바위 보 리스트 생성
choices = ['가위', '바위', '보']
# 승/패/무 카운트 할 변수
win_count = 0
lose_count = 0
draw_count = 0

while True:
    # 컴퓨터의 랜덤한 가위 바위 보
    com_choice = random.choice(choices)
    # 사용자의 가위 바위 보 선택
    user_choice = input('가위, 바위, 보 중 하나를 선택하세요: ')
    # print('사용자: ' + user_choice + ', ' + '컴퓨터: ' + com_choice)
    print(f'사용자: {user_choice}, 컴퓨터: {com_choice}')

    # 사용자의 입력값을 '가위', '바위', '보'로 제한하기 위한 조건문
    if (user_choice == '가위') or (user_choice == '바위') or (user_choice == '보'):
        if user_choice == com_choice:
            print('무승부 입니다')
            draw_count += 1

        elif (user_choice == '가위' and com_choice == '보') or (user_choice == '바위' and com_choice == '가위') or (user_choice == '보' and com_choice == '바위'):
            print('사용자 승리!')
            win_count += 1

        elif (user_choice == '가위' and com_choice == '바위') or (user_choice == '바위' and com_choice == '보') or (user_choice == '보' and com_choice == '가위'):
            print('컴퓨터 승리!')
            lose_count += 1

        # 게임 재시작 여부 묻기
        while True:

            retry = input('다시 하시겠습니까? (y/n): ')

            if (retry == 'y') or (retry == 'Y'):
                break

            elif (retry == 'n') or (retry == 'N'):
                print('게임을 종료합니다.')
                # 승, 패, 무 결과 출력
                # print('승: ' + str(win_count), ' 패: ' + str(lose_count), ' 무승부: ' + str(draw_count))
                print(f'승: {win_count} 패: {lose_count} 무승부: {draw_count}')
                break

            else:
                print('y/n 로만 입력해주세요')

        # retry == 'y' or 'Y':게임 재시작, retry == 'n' or 'Y':게임 종료
        if (retry == 'n') or (retry == 'N'):
            break
    else:
        print('유효한 입력이 아닙니다')
