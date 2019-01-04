import os
import re
import time

import feedparser
import requests
import schedule

import Logger
import OperaFile
from resources import settings
class RssDownLoad:

    def __init__(self):
        self.logger = Logger.setup_logging(name=__name__)
        self.dbmeinv='https://rsshub.app/dbmv/'
        self.last_comment = "last_comment_dbmv"

    def parse_dbmv(self):

        self.logger.info("开始解析 rss:" + self.dbmeinv)
        rss = feedparser.parse(self.dbmeinv)
        self.parse_img_rss(rss=rss)

        self.logger.info("开始解析 rss:" + self.top_ooxx_rss)
        rss = feedparser.parse(self.top_ooxx_rss)
        self.parse_img_rss(rss=rss)

    def parse_img_rss(self, rss):
        self.logger.info(rss.feed.get('title'))
        self.logger.info(rss.feed.get('subtitle'))
        if not os._exists(self.last_comment):
            with open(self.last_comment, 'wb') as file_writer:
                OperaFile.write_txt(self.last_comment, "")
        last_comment = OperaFile.read_txt(self.last_comment)

        list_type = rss.href.split('/')
        type = list_type[len(list_type) - 1]  # 图片名称
        comment_ = ''
        for entry in rss.entries:
            comment = entry.get('id').split("comment-")[1]
            if comment in last_comment.split(","):
                self.logger.debug("数据重复，跳过")
                continue
            img_urls = self.regex_img(entry.get('summary'))
            for img_url in img_urls:
                self.download_img(img_url=img_url, type=type, comment=comment[:-3])
            comment_ += comment + ","
        OperaFile.write_line(self.last_comment, comment_)

    def download_img(self, img_url, type, comment):
        self.logger.info("download : %s" % (img_url))
        dir_path = os.path.join(settings.IMAGES_STORE, type, comment)  # 存储路径
        print(dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        list_name = img_url.split('/')
        file_name = list_name[len(list_name) - 1]  # 图片名称
        # print 'filename',file_name
        file_path = os.path.join(dir_path, file_name)
        # print 'file_path',file_path
        if os.path.exists(file_name):
            return
        with open(file_path, 'wb') as file_writer:
            conn = requests.get(img_url)  # 下载图片
            file_writer.write(conn.content)
        file_writer.close()

    def regex_img(self, str):
        pattern = 'src="(?P<img>.*?)"'
        regex = re.compile(pattern=pattern)
        return regex.findall(str)


if __name__ == '__main__':
    jd = RssDownLoad()
    jd.logger.info("start jandan ...")

    jd.parse_dbmv()
