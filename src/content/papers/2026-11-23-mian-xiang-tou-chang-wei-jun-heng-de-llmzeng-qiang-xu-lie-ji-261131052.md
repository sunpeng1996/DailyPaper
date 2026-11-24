---
title: 'From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization'
title_zh: 面向头长尾均衡的LLM增强序列推荐及权衡优化
authors:
- Adeep Hande
- Shaghayegh Agah
- Neeraj Sharma
- Karina Halevy
- Sardar Hamidian
affiliations:
- Comcast Applied AI Research
- Carnegie Mellon University Department of Computer Science
arxiv_id: '2611.31052'
url: https://arxiv.org/abs/2611.31052
pdf_url: https://arxiv.org/pdf/2611.31052
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 序列推荐 · LLM数据增强 长尾优化
tags:
- LLM
- Sequential Recommendation
- Data Augmentation
- Long Tail
- Popularity Bias
one_liner: 按交互频次分组做LLM合成交互增强，在控制整体精度损失前提下大幅提升长尾推荐效果
practical_value: '- 长尾优化可按物品交互频次的对数百分位做动态分组，无需人工设定阈值，适配不同业务的流行度分布，针对每组单独制定增强策略

  - 做LLM交互增强时，优先用轻量Embedding召回匹配的长尾候选池再给LLM选择，合成交互插在用户序列倒数第3位效果最优，单用户仅加1条合成交互即可平衡效果和分布偏移

  - 多组同时增强时不要直接叠加单组最优比例，要作为多目标优化问题校准总增强比例≤15%，可将整体NDCG损失≤5%作为业务可接受的约束边界'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐存在严重流行度偏差，头部15%物品占据95%以上交互，长尾/冷启物品因交互稀疏NDCG相比头部下降92%-95%；传统增强方法未引入新曝光信号，现有LLM增强方案未区分长尾层级，也未量化整体精度与长尾收益的权衡边界，难以直接落地。
### 方法关键点
- 按物品交互频次的对数百分位动态分成4组：G0冷启（0交互）、G1极长尾（0-75分位）、G2普通长尾（75-95分位）、G3头部（95分位以上），适配不同数据集的流行度分布
- 增强流程：先用轻量Embedding召回与用户偏好匹配的目标组top10候选，再用LLM从候选中选1个最匹配的，插入用户交互序列倒数第3位，重训基础模型SASRec
- 采用坐标下降法依次优化候选选择、增强比例、跨组分配、LLM配置四个维度，约束整体NDCG@20下降≤5%，最大化各组NDCG@20和覆盖率
### 关键实验
在公开数据集MovieLens-32M和Comcast工业视频数据集上测试，基线为原生SASRec：工业数据集上G1（极长尾）NDCG@20提升超100%，G2（普通长尾）提升60%；MovieLens上G1提升40%，G2提升25%，整体NDCG损失控制在2%以内，冷启物品NDCG最高提升6.6倍。
### 核心结论
单组最优的增强策略无法直接叠加，跨组LLM增强本质是多目标约束优化问题，需根据业务优先级动态分配不同长尾组的增强预算
