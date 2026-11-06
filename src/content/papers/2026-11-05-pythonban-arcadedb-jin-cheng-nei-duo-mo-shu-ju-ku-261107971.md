---
title: 'ArcadeDB in Python: An In-Process Multi-Model Database'
title_zh: Python版ArcadeDB：进程内多模数据库
authors:
- Taewoon Kim
affiliations:
- HumemAI
arxiv_id: '2611.07971'
url: https://arxiv.org/abs/2611.07971
pdf_url: https://arxiv.org/pdf/2611.07971
published: '2026-11-05'
collected: '2026-11-06'
category: Other
direction: 多模数据库 · 嵌入式混合检索工具
tags:
- Multi-Model Database
- Embedded Database
- Vector Search
- Graph Database
- Python Bindings
one_liner: 推出pip一键安装的Python嵌入式ArcadeDB，同时支持文档、图、向量检索，无需额外Java环境
practical_value: '- 中小业务搭建RAG或推荐混合检索链路时，可直接用该库替代向量库+文档库+图数据库的多组件架构，消除数据同步成本

  - 原生支持返回NumPy/pandas/Arrow格式结果，可直接对接推荐特征处理、Agent推理链路，省略格式转换开发量

  - 嵌入式部署无需独立数据库服务，适合离线特征计算、本地Agent原型验证、小流量AB测试场景，降低运维成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有Python工作流若需同时支持文档事务读写、图遍历、向量相似度检索，需拆分使用多套独立系统，数据同步与一致性维护成本高，无现成单进程内支持三类能力的嵌入式存储方案。
### 方法关键点
1. 基于Java开源多模数据库ArcadeDB，通过JPype封装为Python包`arcadedb-embedded`，wheel包内置JRE，pip一键安装无需额外Java环境
2. 支持返回Python列表、NumPy数组、pandas DataFrame、Arrow表多种格式结果，可直接对接数据处理链路
3. 支持在单数据集上链式执行向量搜索、SQL过滤、图遍历的混合检索workflow
### 关键结果
完成与SQLite、DuckDB、LadybugDB、Chroma的基准测试，公开了各访问模式下的性能开销数据
