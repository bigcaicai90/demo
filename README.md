# JD Comments Crawler Demo

------

Use Scrapy framework to crawling user comments for a jd product.
Use ElasticSearch to search comments based on key words.

## TODO:
JD's anti crawler system blocks the huge amount requests to get comments.
So I think I need to add a proxy. 


## sample query

GET /scrapy-2020-05/items/_search
{
"query":{
    "match":{
        "content": "很好"
    }
  }
}

## sample output (show 10 results as default)
{"took":2,"timed_out":false,"_shards":{"total":1,"successful":1,"skipped":0,"failed":0},"hits":{"total":{"value":350,"relation":"eq"},"max_score":2.5874794,"hits":[{"_index":"scrapy-2020-05","_type":"items","_id":"d89f9080d57c6c6fc4c4b33db4f69954c99c7881","_score":2.5874794,"_source":{"id":"14001518707","guid":"e460084b-272a-4a5b-9452-2dc861e9c62a","content":"很好很好！物流很快！没毛病！","creationTime":"2020-04-06 11:24:57","isDelete":false,"isTop":false,"userImageUrl":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":2,"anonymousFlag":1,"plusAvailable":201,"mobileVersion":"","productColor":"500ml整箱","productSize":"","textIntegral":20,"status":1,"referenceId":"1384058","referenceTime":"2020-04-01 10:05:42","nickname":"j***j","replyCount2":0,"userImage":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","orderId":0,"integral":40,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":null,"days":5,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"0001daf0259185bfa1ab6a27bae0f46a94d7b113","_score":2.4947948,"_source":{"id":"13677873774","guid":"c6d78e05-1116-4760-8c5e-589360a771dc","content":"水很好，物流也很快，好评。","creationTime":"2020-01-03 12:11:18","isDelete":false,"isTop":false,"userImageUrl":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":2,"anonymousFlag":0,"plusAvailable":0,"mobileVersion":"","productColor":"750ml玻璃瓶整箱","productSize":"","textIntegral":20,"status":1,"referenceId":"1384071","referenceTime":"2020-01-02 15:59:18","nickname":"jd_139460hin","replyCount2":0,"userImage":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","orderId":0,"integral":20,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"mH0HuR6AikvKuTbpwB_S0mHn90Okd9mYOuvmSm3Bx4KftcWvEMRLk1SMH8pYocJISCthdWVdGeA7V-r3pyIXfg","days":1,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"d5c1c422827a0a52bd521c4299a4230cc3772ada","_score":2.448605,"_source":{"id":"14173752387","guid":"fa3c49ad-f7a4-415e-9062-3a9c838d528a","content":"很喜欢，一直都这里买，很好喝，包装也很好看哦","creationTime":"2020-05-20 09:35:34","isDelete":false,"isTop":false,"userImageUrl":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":2,"anonymousFlag":0,"plusAvailable":0,"mobileVersion":"","productColor":"330ml整箱","productSize":"","textIntegral":20,"status":1,"referenceId":"1384057","referenceTime":"2020-05-11 10:43:48","nickname":"w***8","replyCount2":0,"userImage":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","orderId":0,"integral":40,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"bbBoF_Wp51SWLr0vBDmXbrIzed-evq6A_Y3PPXRPl5ciowz23L2SEU0f2VFqy5mjYTLnrFrCvIG6RgPODds8rg","days":9,"afterDays":9}},{"_index":"scrapy-2020-05","_type":"items","_id":"0be63f85b49fb32ecf279aafe822beb12f71a320","_score":2.3535986,"_source":{"id":"14165451681","guid":"9fd2d1cc-61dc-409f-9aaa-d3be5f74a197","content":"很好喝，很甜很舒服，下次还会光顾","creationTime":"2020-05-18 08:59:31","isDelete":false,"isTop":false,"userImageUrl":"storage.360buyimg.com/i.imageUpload/6a645f3764343631393536643334383931343931323034343630393634_sma.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":2,"anonymousFlag":0,"plusAvailable":201,"mobileVersion":"","productColor":"330ml单组","productSize":"","textIntegral":10,"status":1,"referenceId":"2952604","referenceTime":"2020-04-30 11:03:34","nickname":"牛仔与甜甜圈","replyCount2":0,"userImage":"storage.360buyimg.com/i.imageUpload/6a645f3764343631393536643334383931343931323034343630393634_sma.jpg","orderId":0,"integral":10,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"Dvsw7kikk6CH0wJc59J_DHJTUZ51DgfQnvjoDsaBe0_qUi49mtvlXbL8qA9IRM7x2akkkXK9DeZOPqFQOSbNOw","days":18,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"3224d23a802f9823735aa6187ddc0a2be7451d8c","_score":2.351772,"_source":{"id":"14133574242","guid":"f5197431-41ab-4463-a42c-35983d8948c4","content":"不错哦，很好喝，发货快送货也很快，挺好的","creationTime":"2020-05-10 06:41:09","isDelete":false,"isTop":false,"userImageUrl":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":2,"anonymousFlag":0,"plusAvailable":0,"mobileVersion":"","productColor":"500ml整箱","productSize":"","textIntegral":20,"status":1,"referenceId":"1384058","referenceTime":"2020-05-05 05:38:30","nickname":"迈步向前进","replyCount2":0,"userImage":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","orderId":0,"integral":40,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"ZXIJcswktVXmKetRQFMSRIrhvNRXfy4fL-zAWgsfQcBw2Fha0-eERnU067b4HmaSjmkGd3h6dWh5rCVgfqPIMQ","days":5,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"ec96f42fd047925786d6a23ce130d7f18ab81237","_score":2.3381925,"_source":{"id":"14178749919","guid":"8f2f0eb6-ab07-4d73-9a20-64b2b361a630","content":"很好?","creationTime":"2020-05-21 13:55:05","isDelete":false,"isTop":false,"userImageUrl":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":2,"anonymousFlag":0,"plusAvailable":201,"mobileVersion":"","productColor":"330ml玻璃瓶整箱","productSize":"","textIntegral":0,"status":1,"referenceId":"1384067","referenceTime":"2020-05-20 14:01:18","nickname":"j***d","replyCount2":0,"userImage":"misc.360buyimg.com/user/myjd-2015/css/i/peisong.jpg","orderId":0,"integral":0,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"Asp-hi0m6iKRudkN4AVW1xWx308ACWdmxAGvai2YfkHzR6mxYNqLNRYsDULwqMqz4yL-iHEiXLOSL6kShWKbDw","days":1,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"b3d78b3d90044a2c4fc88c2fe1e86c74512486a8","_score":2.3381925,"_source":{"id":"14169039366","guid":"a83bcfa8-0dff-4b57-a4ec-2da77e8de992","content":"很好","creationTime":"2020-05-19 00:24:55","isDelete":false,"isTop":false,"userImageUrl":"storage.360buyimg.com/i.imageUpload/6a645f3730363263353932613633383231353031363631393338363131_sma.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":2,"anonymousFlag":0,"plusAvailable":0,"mobileVersion":"","productColor":"330ml玻璃瓶整箱","productSize":"","textIntegral":0,"status":1,"referenceId":"1384067","referenceTime":"2020-05-17 23:47:22","nickname":"jd_138218llc","replyCount2":0,"userImage":"storage.360buyimg.com/i.imageUpload/6a645f3730363263353932613633383231353031363631393338363131_sma.jpg","orderId":0,"integral":0,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"mrtFhj7jyBFY-_od62KLP5SEXxcwCMZ9thu1eAwCOU-2E2zVWvq2Cxfdtz3fjgDKERX4X9CSoeeX54ue85Z72w","days":2,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"6f5bec92be94be1b4fc6c9a6bde6fbaa24af84ab","_score":2.335236,"_source":{"id":"14088322367","guid":"29584beb-81ca-4770-a285-9a0498fcab03","content":"东西很好，味道很好，总之给你五星好评，一次性付清那种","creationTime":"2020-04-28 12:51:10","isDelete":false,"isTop":false,"userImageUrl":"storage.360buyimg.com/i.imageUpload/3435323231323032375f6d31343436373935393330363435_sma.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":0,"anonymousFlag":0,"plusAvailable":201,"mobileVersion":"","productColor":"750ml玻璃瓶整箱","productSize":"","textIntegral":20,"status":1,"referenceId":"1384071","referenceTime":"2020-04-01 15:11:56","nickname":"布拉德-刘能","replyCount2":0,"userImage":"storage.360buyimg.com/i.imageUpload/3435323231323032375f6d31343436373935393330363435_sma.jpg","orderId":0,"integral":20,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"H5OQXftbzJJKw43m62Dw1ap8IcJ620fqeu0kqEANuDsjhmci8qQVB_6NSDUAAyrGhjLXwOy36vYFkCAm5oGH9Q","days":27,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"d7c391ba9e27cb824142edea12f8aa6800333fe6","_score":2.2856092,"_source":{"id":"14120863136","guid":"be60bb2d-fd45-48a1-afd9-f6979e4eab8b","content":"好，很好，非常好，我非常满意","creationTime":"2020-05-06 20:57:21","isDelete":false,"isTop":false,"userImageUrl":"storage.360buyimg.com/i.imageUpload/6a645f7a526b63647848484446617931353632313330343332393730_sma.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":4,"anonymousFlag":0,"plusAvailable":201,"mobileVersion":"","productColor":"750ml玻璃瓶整箱","productSize":"","textIntegral":20,"status":1,"referenceId":"1384071","referenceTime":"2020-03-16 14:50:37","nickname":"j***y","replyCount2":0,"userImage":"storage.360buyimg.com/i.imageUpload/6a645f7a526b63647848484446617931353632313330343332393730_sma.jpg","orderId":0,"integral":20,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":"OCRKTa_zvJFwYN86qC4Vpop4FSmh5NyxCxnEbJzmn0POxUvhpZOQlRIxZDVzG0dUuoq8I2Bx-3PMszw6mjDnYA","days":51,"afterDays":0}},{"_index":"scrapy-2020-05","_type":"items","_id":"5a1214535d22aedf54fc247d5fb3aa42bcb6f122","_score":2.2310615,"_source":{"id":"14179105353","guid":"5942f3e7-014d-4694-8bac-8fcb23b21ca8","content":"这东西看起来很好，用起来很不错","creationTime":"2020-05-21 15:27:24","isDelete":false,"isTop":false,"userImageUrl":"storage.360buyimg.com/i.imageUpload/313033363139352d383737323138373331343635383737303937393539_sma.jpg","topped":0,"replyCount":0,"score":5,"title":"","usefulVoteCount":0,"userClient":0,"anonymousFlag":1,"plusAvailable":201,"mobileVersion":"","productColor":"500ml整箱","productSize":"","textIntegral":20,"status":1,"referenceId":"1384058","referenceTime":"2020-05-16 18:53:19","nickname":"A***u","replyCount2":0,"userImage":"storage.360buyimg.com/i.imageUpload/313033363139352d383737323138373331343635383737303937393539_sma.jpg","orderId":0,"integral":20,"productSales":"[]","referenceImage":"jfs/t27634/311/1871619140/168363/bb71dc93/5bfaa3b7Nd87d2254.jpg","referenceName":"法国原装进口 依云（evian）天然矿泉水 750ml*12整箱玻璃瓶","firstCategory":1320,"secondCategory":5019,"thirdCategory":15051,"aesPin":null,"days":5,"afterDays":0}}]}}
