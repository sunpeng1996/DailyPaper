---
title: Claim-Level Reliability Assessment for Efficient Test-Time Reasoning
title_zh: 面向高效测试时推理的声明级可靠性评估框架
authors:
- Sen Xu
- Wei Wang
- Shixi Liu
- Jixin Min
- Yingwei Dai
- Zhibin Yin
- Yirong Chen
- Junlin Zhang
affiliations:
- Sina Weibo Inc.
arxiv_id: '2608.11994'
url: https://arxiv.org/abs/2608.11994
pdf_url: https://arxiv.org/pdf/2608.11994
published: '2026-08-12'
collected: '2026-08-13'
category: Reasoning
direction: LLM测试时推理优化 · 轻量自验证
tags:
- Test-Time Scaling
- Reasoning
- Self-Verification
- Consensus Aggregation
- LLM Inference
one_liner: 无需训练的声明级可靠性评估框架，同等推理预算下优于自洽性等基线方法
practical_value: '- 电商Agent导购/复杂Query理解场景可直接复用CLR逻辑：先抽取回答的核心决策声明，再针对性证伪，无需全链路重跑即可降低错误回答率，最高可省37%推理token

  - 生成式推荐候选排序环节可借鉴非线性加权机制：对每个召回候选的关键决策特征（如用户偏好匹配度、库存约束、合规要求）做验证，按验证通过率的M次方加权聚合，突破多数投票的错误共识

  - 大模型推理成本优化场景可参考预算分配策略：将一半推理调用量从生成更多候选转向已有候选的关键声明验证，在多数场景下可实现精度不降甚至提升，同时降低token消耗'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有测试时推理优化方法存在两大瓶颈：一是基于token概率、全链路评分的方法信噪比低，易掩盖局部致命逻辑错误；二是多采样自洽性方法随采样量增长成本线性提升，且容易被错误的多数共识误导，无法充分利用已有计算预算挖掘正确候选。
### 方法关键点
- 无训练两阶段框架：第一阶段采样K条推理轨迹，每条抽取M条决策关键声明（直接影响结果正确性的中间结论、约束、逻辑节点），过滤无意义常规token
- 证伪式轻量验证：第二阶段复用同一模型，仅基于原问题和抽取的声明针对性搜索反例/逻辑漏洞，利用「构造完整解难、证伪单条声明易」的不对称性降低验证成本
- 非线性加权聚合：每条轨迹的可靠性得分为未被证伪声明占比的M次方，对错误声明施加重罚，可靠少数派可推翻错误多数共识
### 关键结果
在4款LLM、4个推理基准上匹配模型调用预算对比自洽性基线：GPT-OSS-20B在CMIMC25数据集上精度较Cons@64提升4.69pp，token消耗降低37%，较pass@1提升27.15pp；Gemma-4-12B-it在HMMT25上精度提升12.08pp；平均可纠正37%的可恢复错误共识（正确候选已存在但多数投票错误的场景）。
### 核心洞见
测试时推理预算无需全部投入生成更多候选，将一半算力转向关键决策点的针对性证伪，可获得更优的精度-成本权衡。
