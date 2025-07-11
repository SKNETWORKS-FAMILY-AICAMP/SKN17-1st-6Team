# 최근 2개년도 자동차 등록현황 업데이트
from recent_excel import kia_recent
from recent_excel import hyundai_recent
import mysql.connector

# DB 연결
def insert_to_db(data, brand_code, year):

    connection = mysql.connector.connect(
        host='localhost',
        user='sixsense',
        password='sixsense',
        database='cardb'
    )
    cursor = connection.cursor() 

    sql = """
    INSERT IGNORE INTO registed_info (BRAND_CODE, CAR_NAME, YEAR, REGISTED_COUNT) 
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE registed_count = VALUES(registed_count)
    """

    values = [(brand_code, car_name, year, registed_count) for car_name, registed_count in data]
# INSERT
    cursor.executemany(sql, values)

# 커밋 및 종료
    connection.commit()

    cursor.close()
    connection.close()
    print('저장완료')


# 브랜드코드 수기 입력
if __name__ == "__main__":
    kia_data = kia_recent()
    hyundai_data = hyundai_recent()

    year = "최신"

    insert_to_db(kia_data, 1, year)
    insert_to_db(hyundai_data, 2, year)

