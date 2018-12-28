# 用cytoscape.js展示neo4j网络关系图
可能因为pyneo版本不一样,导致数据结构不一样，修改了app.py中的取数逻辑

## 启动方式
1. 进入neo4j-community-3.4.1路径,导入数据后./neo4j start启动neo4j
2. python app.py启动flask

## 原作者
用可视化的方式来展示网络关系图是一件挺有趣的事情，在选定用cytoscape.js来显示neo4j图形数据库的数据后我做了一个原型，并用下面三篇博客来记录了做原型的过程。

- [用cytoscape.js展示neo4j网络关系图 - 1. Flask](http://blog.csdn.net/zhongzhu2002/article/details/45843283)
- [用cytoscape.js展示neo4j网络关系图 - 2. py2neo](http://blog.csdn.net/zhongzhu2002/article/details/46043047)
- [用cytoscape.js展示neo4j网络关系图 - 3. cytoscape.js](http://blog.csdn.net/zhongzhu2002/article/details/46049197)
