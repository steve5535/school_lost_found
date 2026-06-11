# 학교 분실물 파이썬 버전
# 추가
# 찾아가면 업데이트
# 검색
# 수정

def add_lost_item(storage, id, item, time):
    storage[id] = {"이름":item, "시간":time} # 분실물이름과 시간을 딕셔너리로 저장한 값을 전체 분실물 딕셔너리에 추가


def main():
    lost_items_db = {}
    id = 1
    
    name = input("분실물 이름을 작성하세요> ")
    time = input("분실물을 습득한 시간을 작성하세요> ")
    add_lost_item(lost_items_db, id, name, time)
    id += 1
    
    
    print(lost_items_db)

if __name__ == "__main__":
    main()