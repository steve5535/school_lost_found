# 학교 분실물 파이썬 버전
# 추가
# 찾아가면 업데이트
# 검색
# 수정

def add_lost_item(lost_items_db, id, item, place):
    lost_items_db[id] = {"이름":item, "장소":place} # 분실물이름과 장소 딕셔너리로 저장한 값을 전체 분실물 딕셔너리에 추가


def main():
    lost_items_db = {}
    id = 1
    
    item = input("분실물 이름을 작성하세요> ")
    place = input("분실물을 습득한 장소 작성하세요> ")
    add_lost_item(lost_items_db, id, item, place)
    id += 1
    
    
    print(lost_items_db)

if __name__ == "__main__":
    main()