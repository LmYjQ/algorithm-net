# algorithm-net
用图展示算法/数据结构/数学/物理理论之间的区别与联系
图数据库用neo4j存储和查询，web用flask和bokeh

## 定义
以下是个人的理解
模型：基于一系列假设，定义了事物特点(超参数)和行为(训练/预测)的实体
算法：求解一个抽象问题的一系列操作，过程中可能依赖一些数据结构实体，但重点在操作过程

## neo4j基本概念
1. 图由节点node和边relationship组成
2. node有label属性标识不同类别的节点，比如:人/电影。**建议格式 :VehicleOwner**
3. relationship需要两个node和一个relationship定义，比如：Tom Hanks ACTED_IN Forrest Gump。**建议格式 :OWNS_VEHICLE**
4. node和relationship都可以有属性property，比如：Tom Hanks有属性born=1956, ACTED_IN有属性roles='forrest'。 **建议格式 firstName**
# 使用方法
1. 启动neo4j: neo4j目录下 ./bin/neo4j start
2. 启动flask: python3 app.py
