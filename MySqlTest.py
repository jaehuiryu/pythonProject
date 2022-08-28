import pymysql

print("TEST STEP 2")

conn = pymysql.connect(host='ryudata.cosnvljfn8l6.ap-northeast-2.rds.amazonaws.com', user='admin', password='캐나다m011', db='coindata')

cur = conn.cursor()

cur.execute("INSERT INTO coincond VALUES( 'COINB', '20220810', '140101', 'KRW',  31203)")

conn.commit()

conn.close()
