# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdcommentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    guid = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    isDelete = scrapy.Field()
    isTop = scrapy.Field()
    userImageUrl = scrapy.Field()
    topped = scrapy.Field()
    replyCount = scrapy.Field()
    score = scrapy.Field()
    title = scrapy.Field()
    usefulVoteCount = scrapy.Field()
    userClient = scrapy.Field()
    anonymousFlag = scrapy.Field()
    plusAvailable = scrapy.Field()
    mobileVersion = scrapy.Field()
    productColor = scrapy.Field()
    productSize = scrapy.Field()
    textIntegral = scrapy.Field()
    status = scrapy.Field()
    referenceId = scrapy.Field()
    referenceTime = scrapy.Field()
    nickname = scrapy.Field()
    replyCount2 = scrapy.Field()
    userImage = scrapy.Field()
    orderId = scrapy.Field()
    integral = scrapy.Field()
    productSales = scrapy.Field()
    referenceImage = scrapy.Field()
    referenceName = scrapy.Field()
    firstCategory = scrapy.Field()
    secondCategory = scrapy.Field()
    thirdCategory = scrapy.Field()
    aesPin = scrapy.Field()
    days = scrapy.Field()
    afterDays = scrapy.Field()
