# 2020本科生毕业设计：《疫情区块链微博系统设计与实现》

## 本项目遵顼开源精神，在该仓库中对系统实现过程中涉及到的部分代码做出展示

项目介绍地址：http://ec2-54-172-127-195.compute-1.amazonaws.com:8090

-----------------------

# 内容说明

* [news.py](http://github.com/Edward-21/Blockchain_Microblog/blob/master/host_blog/news.py)

  一个Python爬虫，用于从链一新闻网上指定或按照搜索结果爬取新闻的内容并打印。

* [pg2my.py](https://github.com/Edward-21/Blockchain_Microblog/blob/master/host_blog/pg2my.py)

  一个Python脚本，用于从Mastodon开源社交软件的后台数据库（PostgreSQL数据库）中提取系统所需的数据并写入MySQL数据库。

* [md5mail.py](https://github.com/Edward-21/Blockchain_Microblog/blob/master/host_blog/md5mail.py)

  一个Python脚本，用于对MySQL数据库中的数据进行初步加密并将相关信息整合后上传到NEM区块链的Symbol测试网，最终保存所得的重要结果。

* [upip.py](https://github.com/Edward-21/Blockchain_Microblog/blob/master/host_show/upip.py)

  一个Python脚本，用于从另一台服务器上的MySQL数据库中查询数据，经过简单处理后上传IPFS服务器，然后将关键结果保存到本地。

* [myview](https://github.com/Edward-21/Blockchain_Microblog/tree/master/host_show/myview)

  一个Spring Boot项目，用于将系统已保存的数据以精美且友好的方式展示给有需要的用户，同时提供丰富的外部链接，帮助浏览者验证项目结果的正确性和有效性。

--------------------------------------------------------------------------------------------

# 项目简述

## 项目目标

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;利用Mastodon开源工程搭建微博社区，通过数据库技术将用户发布的内容上传至NEM区块链，赋予用户数据各种区块链才具有的特性。此后，根据区块链的种种数据存储优势，系统可以为相关公共安全事业，尤其是疫情防控工作提供创新型的技术保障。  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本项目的实现本质上是区块链技术在当下互联网产业中的一种应用模式的落地，希望能够为未来相关技术的普及性应用在某些范围内开拓原始思路，也希望能够对相关探究提供一定程度上的参考意义。

## 技术支持

* [Mastodon](https://github.com/tootsuite)

  Mastodon开源社交软件，具有分布式和去中心化的特点，可跨服务器开展社交活动，是本项目的基础数据来源。

* [NEM](https://github.com/nemtech)

  NEM区块链，作为一条类似于以太坊的双层区块链，其性能极高，可高度模块化和定制化，对开发者非常友好，是承载本项目上传数据的区块链。

* [IPFS](https://github.com/ipfs)

  IPF即为星际文件系统，是该项目的补充模块，系统将把上传区块链完成后的结果写入文本文档并最终上传到IPFS服务器上。

* [Spring Boot](https://github.com/spring-projects)

  Spring Boot开源应用框架，提供具有控制反转特性的容器，帮助开发者简化构建Java应用，尤其是各种Web应用的工作，本项目的展示页面即在该框架下完成，用户可以在相关网址浏览存储在数据库中的需要向用户展示的数据处理结果。

----------------------------------------------------------------------------------------------------------------------

# 联系作者

欢迎所有对本项目感兴趣的开发者访问系统所持有的Mastodon开源微博社区：https://mastodon-test233.xyz<span></span>，联系站点管理员账号（@admin@<span></span>mastodon-test233.xzy）即可向作者了解更多细节。

-----------------------------------------------------------------------------------------------------------
