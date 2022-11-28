import random

random_number = random.randint(1,100) #1~100사이의 숫자를 랜덤으로 생성

#print(random_number)

game_count = 1 #사용자 입력 횟수
while True :
    try:    
        my_number = int(input("1~100 사이의 숫자를 입력하세요 :")) # 사용자 숫자 입력  
        
        if my_number > random_number :  #사용사 숫자가 생성된 숫자보다 크면 아래 텍스트 출력
            print("다운")
        elif my_number < random_number :    #사용자 숫자가 생성된 숫자보다 작으면 아래 텍스트 출력
            print("업")
        elif my_number == random_number :   #사용자 숫자가 생성된 숫자와 같으면 아래 텍스트 출력후 반복문(While) 종료
            print(f"축하합니다.{game_count}회 만에 맞췃습니다")
            break
    
        game_count = game_count + 1 #맞추지못하면 입력 횟수 1 증가
    except :
        print("에러가 발생하였습니다. 숫자를 입력하세요")
 
