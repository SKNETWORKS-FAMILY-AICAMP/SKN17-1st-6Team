# 최근 2개년도 자동차 정보 업데이트

from recent_excel import kia_recent
from recent_excel import hyundai_recent
import mysql.connector

# DB 연결
def insert_to_db(data, brand_name, brand_code):

    connection = mysql.connector.connect(
        host='localhost',
        user='sixsense',
        password='sixsense',
        database='cardb'
    )
    cursor = connection.cursor()

    sql = "INSERT IGNORE INTO CAR_info (BRAND_NAME, BRAND_CODE, CAR_NAME) VALUES (%s, %s, %s)"
    values = [(brand_name, brand_code, car_name) for car_name, sale in data]

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
    insert_to_db(kia_data, '기아자동차', 1)
    insert_to_db(hyundai_data, '현대자동차', 2)

