import schedule
import time

from JanDan import JanDan

if __name__ == '__main__':
    jd = JanDan()

    jd.parse_ooxx()
    # 每15分钟执行一次
    schedule.every(10).minutes.do(jd.parse_ooxx)

    for job in schedule.jobs:
        jd.logger.info(str(job))
    while True:
        schedule.run_pending()
        time.sleep(1)