# JD Comments Crawler Demo

------

Use Scrapy framework to crawling user comments for a jd product.
Use ElasticSearch to search comments based on key words.


## sample query

GET /scrapy-2020-05/items/_search
{
"query":{
    "match":{
        "content": "很好"
    }
  }
}
