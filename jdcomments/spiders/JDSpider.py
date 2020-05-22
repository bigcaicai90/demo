import scrapy
import math
import chardet
from jdcomments.items import JdcommentsItem
import json


class JDSpider(scrapy.Spider):
    name = "JDComments"
    productId = "1384071"
    commentCount = 804882
    # commentCount = 60
    pageSize = 10
    start_urls = []

    for page in range(1, math.ceil(commentCount / pageSize) + 1):
        start_urls.append(
            "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}" \
            "&score=0&sortType=6&page={}&pageSize={}&isShadowSku=0&rid=0&fold=1".format(productId, page, pageSize))

    def parse(self, response):
        text = response.body.decode("GB2312")
        # print(chardet.detect(response.body))
        start = text.find("comments")
        end = -3
        if start > 0:
            start += 10
        print(text[start:end])

        commentsList = json.loads(text[start:end])
        for comment in commentsList:
            item = JdcommentsItem(id=str(comment['id']), guid=comment['guid'], content=comment['content'],
                                  creationTime=comment['creationTime'], isDelete=comment['isDelete'],
                                  isTop=comment['isTop'], userImageUrl=comment['userImageUrl'],
                                  topped=comment['topped'], replyCount=comment['replyCount'], score=comment['score'],
                                  title=comment['title'], usefulVoteCount=comment['usefulVoteCount'],
                                  userClient=comment['userClient'], anonymousFlag=comment['anonymousFlag'],
                                  plusAvailable=comment['plusAvailable'], mobileVersion=comment['mobileVersion'],
                                  productColor=comment['productColor'], productSize=comment['productSize'],
                                  textIntegral=comment['textIntegral'], status=comment['status'],
                                  referenceId=comment['referenceId'], referenceTime=comment['referenceTime'],
                                  nickname=comment['nickname'], replyCount2=comment['replyCount2'], userImage=comment['userImage'],
                                  orderId=comment['orderId'], integral=comment['integral'], productSales=comment['productSales'],
                                  referenceImage=comment['referenceImage'], referenceName=comment['referenceName'],
                                  firstCategory=comment['firstCategory'], secondCategory=comment['secondCategory'],
                                  thirdCategory=comment['thirdCategory'], aesPin=comment['aesPin'], days=comment['days'],
                                  afterDays=comment['afterDays'])
            yield item



