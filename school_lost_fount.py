# 학교 분실물 파이썬 버전
# 추가
# 찾아가면 업데이트
# 검색
# 수정

#TODO: while문 돌아가기 기능 함수로 만들어서 추가하기, lost_items id 랑 take_students id 분리하기

'''
lost_items 형식
{
    1: {"이름":???, "장소":???, "상태":True},
    2: {"이름":???, "장소":???, "상태":Flase}
}
'''


## Srvice
# 분실물 추가 함수
def add_lost_item(lost_items, item_id, item, place, state):
    lost_items[item_id] = {"이름":item, "장소":place, "상태":state} # 분실물이름과 장소 딕셔너리로 저장한 값을 전체 분실물 딕셔너리에 추가 나중에 JSON파일 형식처럼

# 분실물 전체 검색 함수
def search_all_item(lost_items):
    item_box = []
    for item_id, item_info in lost_items.items():
        item_box.append({
                "id":item_id,
                "이름":item_info["이름"],
                "장소":item_info["장소"],
                "상태":item_info["상태"]
            })
    return item_box

# 분실물 이름 또는 장소로 검색
def search_item(input_num, input_keyword, lost_items):
    item_box = []
    is_in_item = False
    is_match = False
    for item_id, item_info in lost_items.items():
        if input_num == 3:
            item_name = item_info["이름"]
            is_match = input_keyword in item_name
        elif input_num == 4:
            item_place = item_info["장소"]
            is_match = input_keyword == item_place
        if is_match:
            item_box.append({
                "id":item_id,
                "이름":item_info["이름"],
                "장소":item_info["장소"],
                "상태":item_info["상태"]
            })
            is_in_item = True
    return is_in_item, item_box

# 분실물 가져가기
def take_lost_item(input_id, lost_items):
    lost_items[input_id]["상태"] = False

# 분실물 가져간 학생 추가
def add_take_student(student_name, student_number, student_id, lost_items):
    item_name = lost_items[student_id]["이름"]
    take_students = {
        "분실물":item_name,
        "학생이름":student_name,
        "학생학번":student_number
    }
    return take_students

# 메뉴로 돌아가기 함수 true false를 리턴해서 true면 break
def back_menu(user_input):
    if user_input == "q":
        return True
    return False

# bool자료형으로 받은 상태를 문자로 변경
def status_to_string(is_in_item):
    if is_in_item:
        return "보관중"
    else:
        return "찾아감" 
        
## Controller
# 메인함수
def main():
    lost_items = {
        1:{"이름":"연필", "장소":"교실", "상태":False},
        2:{"이름":"시계", "장소":"운동장", "상태":True},
        3:{"이름":"에어팟", "장소":"운동장", "상태":True},
        4:{"이름":"연필", "장소":"교무실", "상태":True}
    }
    take_students = {
        1:{"분실물":"연필", "학생이름":"성선혁", "학생학번":"20713"}
    }
    item_id = len(lost_items) + 1
    student_id = len(take_students) + 1
    
    while True:
        print("=============================")
        print("1. 분실물 등록")
        print("2. 전체 분실물 검색")
        print("3. 분실물 이름으로 검색")
        print("4. 분실한 장소로 검색")
        print("5. 분실물 찾아가기")
        print("6. 종료")
        try:
            input_num = int(input("번호 입력> "))
            if not(1 <= input_num <= 6):
                raise ValueError("1부터 5까지 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("잘못된 입력을 하셨습니다. 다시 입력하세요.")
            continue
        # 분실물 등록
        if input_num == 1: 
            item = input("분실물 이름을 작성하세요> ")
            place = input("분실물을 습득한 장소 작성하세요> ")
            state = True
            add_lost_item(lost_items, item_id, item, place, state)
            item_id += 1
        
        # 전체 분실물 검색
        elif input_num == 2: 
            if len(lost_items) == 0: # 등록된 분실물이 있는지 검사
                print("아직 등록된 분실물이 없습니다.")
            else: # 있다면 보여주기
                items_list = search_all_item(lost_items)
                for item in items_list:
                    print(f"{item['id']}. 이름: {item['이름']}, 찾은 장소: {item['장소']}, 상태: {status_to_string(item['상태'])}")
        
        # 분실물 이름으로 검색
        elif input_num == 3: 
            if len(lost_items) == 0: # 분실물이 저장되어 있는지 검사
                print("아직 등록된 분실물이 없습니다.")
                continue
            while True:
                input_item = input("분실물 이름을 입력하세요(메뉴로 돌아가기 'q')> ")
                if back_menu(input_item):
                    print("메뉴로 돌아갑니다.")
                    break
                is_found, found_list = search_item(input_num, input_item, lost_items)
                if is_found: # 입력한 분실물 이름을 포함한 분실물이 저장되어 있다면
                    print(f"{input_item}이(가) 포함된 분실물을 찾았습니다")
                    for item in found_list:
                        print(f"{item['id']}. 이름: {item['이름']}, 찾은 장소: {item['장소']}, 상태: {status_to_string(item['상태'])}")
                else: # 입력한 분실물 이름을 포함한 분실물이 없다면
                    print(f"현재 있는 분실물 중 '{input_item}'이(가) 포함되어있는 분실물은 없습니다. 다시 입력하세요.")
        
        # 분실한 장소로 검색
        elif  input_num == 4:
            if len(lost_items) == 0: # 분실물이 저장되어 있는지 검사
                print("아직 등록된 분실물이 없습니다.")
                continue
            while True:
                input_place = input("분실한 장소를 입력하세요(메뉴로 돌아가기 'q')> ")
                if back_menu(input_place):
                    print("메뉴로 돌아갑니다.")
                    break
                is_found, found_list = search_item(input_num, input_place, lost_items)
                if is_found: # 입력한 장소에 대한 분실물이 있다면
                    print(f"{input_place}에서 찾은 분실물을 찾았습니다")
                    for item in found_list:
                        print(f"{item['id']}. 이름: {item['이름']}, 찾은 장소: {item['장소']}, 상태: {status_to_string(item['상태'])}")
                else: # 입력한 장소에서 찾은 분실물이 없다면
                    print(f"현재 있는 분실물 중 '{input_place}'에서 찾은 분실물은 없습니다. 다시 입력하세요")
        
        # 분실물 찾아가기
        elif input_num == 5:
            if len(lost_items) == 0:
                print("아직 등록된 분실물이 없습니다.")
                continue
            while True:
                input_id = input("찾아가려는 분실물의 번호를 입력하세요(메뉴로 돌아가기 'q')> ")
                if back_menu(input_id):
                    print("메뉴로 돌아갑니다.")
                    break
                try:
                    input_id = int(input_id)
                except ValueError:
                    print("분실물 번호로 다시 입력해주세요.")
                    continue
                if input_id not in lost_items.keys():
                    print(f"'{input_id}'번은 존재하지 않는 분실물 번호입니다. 다시 입력하세요.")
                    continue
                take_item_name = lost_items[input_id]["이름"]
                take_item_place = lost_items[input_id]["장소"]
                if lost_items[input_id]["상태"] == False: # 이미 가져갔다면
                    take_student_name_masked = (take_students[input_id]["학생이름"])[0] + "*" + (take_students[input_id]["학생이름"])[2:] # 가져간 학생이름 2번째 이름 *으로 마스킹 하기
                    take_student_number = take_students[input_id]["학생학번"]
                    print(f"{take_item_place}에서 찾은 {take_item_name}은(는) {take_student_number} {take_student_name_masked}이(가) 가져갔습니다.")
                    continue
                while True:
                    is_take = input(f"{take_item_place}에서 찾은 {take_item_name}을(를) 가져가겠습니까? (y,n)> ")
                    if is_take == "y" or is_take == "n":
                        break
                    else:
                        print("'y'또는 'n'을 입력해주세요.")
                if is_take == "y":
                    input_student_name = input("이름을 입력해주세요> ")
                    input_student_number= input("학번을 입력해주세요> ")
                    take_students[student_id] = add_take_student(input_student_name, input_student_number, student_id, lost_items)
                    take_lost_item(input_id, lost_items)
                    print("분실물을 가져가셨습니다.")
                    break
                else:
                    print("가져가지 않으셨습니다.")
                    break
        
        # 종료
        elif input_num == 6: 
            print("프로그램을 종료합니다")
            break

if __name__ == "__main__":
    main()