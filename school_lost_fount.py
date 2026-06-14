# 학교 분실물 파이썬 버전
# 추가
# 찾아가면 업데이트
# 검색
# 수정

'''
lost_items_db 형식
{
    1: {"이름":???, "장소":???, "상태:True"},
    2: {"이름":???, "장소":???, "상태:Flase"}
}
'''


## Srvice
# 분실물 추가 함수
def add_lost_item(lost_items_db, item_id, item, place, state):
    lost_items_db[item_id] = {"이름":item, "장소":place, "상태":state} # 분실물이름과 장소 딕셔너리로 저장한 값을 전체 분실물 딕셔너리에 추가

# 분실물 전체 검색 함수
def search_all_item(lost_items_db):
    item_box = []
    for item_id, item_info in lost_items_db.items():
        item_box.append({
                         "id":item_id,
                         "이름":item_info["이름"],
                         "장소":item_info["장소"],
                         "상태":item_info["상태"]
                        })
    return item_box

# 분실물 이름으로 검색
def search_name_item(input_item, lost_items_db):
    item_box = []
    is_in_item = False
    for item_id, item_info in lost_items_db.items():
        item_name = item_info["이름"]
        if input_item in item_name:
            item_box.append({
                             "id":item_id,
                             "이름":item_info["이름"],
                             "장소":item_info["장소"],
                             "상태":item_info["상태"]
                            })
            is_in_item = True
    return is_in_item, item_box

# 분실물 장소로 검색
# def search_place_itme():

# bool자료형으로 받은 상태를 문자로 변경
def bool_chg_str(is_in_item):
    if is_in_item:
        return "보관중"
    else:
        return "찾아감"
            
        
## Controller
# 메인함수
def main():
    lost_items_db = {}
    item_id = 1
    
    while True:
        print("=============================")
        print("1. 분실물 등록")
        print("2. 전체 분실물 검색")
        print("3. 분실물 이름으로 검색")
        print("4. 종료")
        try:
            input_num = int(input("번호 입력> "))
            if not(1 <= input_num <= 4):
                raise ValueError("1부터 4까지 사이의 숫자를 입력해주세요")
        except ValueError:
            print("잘못된 입력을 하셨습니다. 다시 입력하세요")
            continue
        # 분실물 등록
        if input_num == 1: 
            item = input("분실물 이름을 작성하세요> ")
            place = input("분실물을 습득한 장소 작성하세요> ")
            state = True
            add_lost_item(lost_items_db, item_id, item, place, state)
            item_id += 1
        
        # 전체 분실물 검색
        elif input_num == 2: 
            if len(lost_items_db) == 0: # 등록된 분실물이 있는지 검사
                print("아직 등록된 분실물이 없습니다")
            else: # 있다면 보여주기
                items_list = search_all_item(lost_items_db)
                for item in items_list:
                    print(f"{item['id']}. 이름: {item['이름']}, 찾은 장소: {item['장소']}, 상태: {bool_chg_str(item['상태'])}")
        
        # 분실물 이름으로 검색
        elif input_num == 3: 
            if len(lost_items_db) == 0: # 등록된 분실물이 있는지 검사
                print("아직 등록된 분실물이 없습니다")
            else:
                input_item = input("분실물 이름을 입력하세요> ")
                is_found, found_list = search_name_item(input_item, lost_items_db)
                if is_found:
                    print(f"{input_item}이(가) 포함된 분실물을 찾았습니다")
                    for item in found_list:
                        print(f"{item['id']}. 이름: {item['이름']}, 찾은 장소: {item['장소']}, 상태: {bool_chg_str(item['상태'])}")
                else:
                    print(f"현재 있는 분실물중 '{input_item}'은(는) 없습니다")
        
        # 종료
        elif input_num == 4: 
            print("프로그램을 종료합니다")
            break

if __name__ == "__main__":
    main()