# 학교 분실물 파이썬 버전
# 추가
# 찾아가면 업데이트
# 검색
# 수정

# 분실물 추가 함수
def add_lost_item(lost_items_db, id, item, place):
    lost_items_db[id] = {"이름":item, "장소":place} # 분실물이름과 장소 딕셔너리로 저장한 값을 전체 분실물 딕셔너리에 추가
'''
{
    1: {"이름":???, "장소":???},
    2: {"이름":???, "장소":???}
}
'''


# 분실물 전체 검색 함수
def search_all_item(lost_items_db):
    item_box = []
    for i in range(len(lost_items_db)):
        item_name = lost_items_db[i+1]["이름"]
        item_place = lost_items_db[i+1]["장소"]
        item_box.append([i+1, item_name, item_place])
    return item_box

# 분실물 이름으로 검색
def search_name_item(input_item, lost_items_db):
    for i in range(len(lost_items_db)):
        item_name = lost_items_db[i+1]["이름"]
        if input_item == item_name:
            lost_items_db[i+1]
            
        

# 메인함수
def main():
    lost_items_db = {}
    id = 1
    
    while True:
        print("=============================")
        print("1. 분실물 등록")
        print("2. 전체 분실물 검색")
        print("3. 분실물 이름으로 검색")
        print("4. 종료")
        input_num = int(input("번호 입력> "))
        
        # 분실물 등록
        if input_num == 1: 
            item = input("분실물 이름을 작성하세요> ")
            place = input("분실물을 습득한 장소 작성하세요> ")
            add_lost_item(lost_items_db, id, item, place)
            id += 1
        
        # 전체 분실물 검색
        if input_num == 2: 
            if len(lost_items_db) == 0: # 등록된 분실물이 있는지 검사
                print("아직 등록된 분실물이 없습니다")
            else: # 있다면 보여주기
                items_list = search_all_item(lost_items_db)
                for req_id, req_name, req_place in items_list:
                    print(f"{req_id}. 이름: {req_name}, 찾은 장소: {req_place}")
        
        # 분실물 이름으로 검색
        if input_num == 3: 
            input_item = input("분실물 이름을 입력하세요> ")
            if len(lost_items_db) == 0: # 등록된 분실물이 있는지 검사
                print("아직 등록된 분실물이 없습니다")
            else:
                search_name_item(input_item, lost_items_db)
        
        # 종료
        if input_num == 4: 
            print("프로그램을 종료합니다")
            break

if __name__ == "__main__":
    main()