# algorithm-net
用图展示算法模型/（求解模型的）数学方法之间的区别与联系

# 图模型定义
## 节点node
### 模型：经典机器学习模型/深度学习模型等
模型名称
### 算法：求解模型使用的算法
### 应用：模型在某个领域的应用

## 边relationship
### 模型的发展：模型A改进成为模型B
### 模型的求解：算法G可以求解某个模型M
### 模型应用于：一个模型通常可以应用到多个领域


## neo4j基本概念
1. 图由节点node和边relationship组成
2. node有label属性标识不同类别的节点，比如:人/电影。**建议格式 :VehicleOwner**
3. relationship需要两个node和一个relationship定义，比如：Tom Hanks ACTED_IN Forrest Gump。**建议格式 :OWNS_VEHICLE**
4. node和relationship都可以有属性property，比如：Tom Hanks有属性born=1956, ACTED_IN有属性roles='forrest'。 **建议格式 firstName**
# 使用方法
1. 启动neo4j: neo4j目录下 ./bin/neo4j start
2. 启动flask: python3 app.py
