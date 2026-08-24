---
title: 'One Hierarchy, Two Systems: Semantic Product IDs for Discovery-Surface Ranking
  and Search-Page Query Reformulation'
title_zh: 基于统一语义产品ID层级的推荐排序与搜索查询改写方案
authors:
- Steven Xu
- Sanjyot Thete
- Saathvik Dirisala
- Raghav Saboo
- Nimesh Sinha
- Leo Shao
- Elyse Winer
- Sudeep Das
- Martin Wang
- Kyle MacDonald
affiliations:
- DoorDash Inc.
arxiv_id: '2608.20640'
url: https://arxiv.org/abs/2608.20640
pdf_url: https://arxiv.org/pdf/2608.20640
published: '2026-08-21'
collected: '2026-08-24'
category: GenRec
direction: 生成式推荐 · Semantic ID跨场景复用
tags:
- Semantic ID
- Query Reformulation
- Ranking
- Hierarchical Clustering
- E-commerce
one_liner: 基于统一层级Semantic ID同时优化电商推荐排序与搜索Query改写效果，无需共享模型参数
practical_value: '- Semantic ID层级可作为跨搜索/推荐的统一语义底座，无需跨场景共享模型参数，仅复用语义聚合逻辑即可实现信号迁移，大幅降低多场景对齐成本

  - 推荐排序侧可直接复用SID前缀构建两类特征：基于前缀的多粒度行为统计稠密特征，以及基于SID BPE子词的用户历史序列特征，可快速提升跨商家偏好泛化效果

  - Query改写侧可将查询先映射到SID概念再挖掘 transitions，能天然合并同义词、拼写变体的行为信号，同时结合层级下探实现粗细粒度的查询建议，再叠加商家在售商品过滤即可大幅降低无效推荐

  - 生产落地可直接采用3阶段残差量化构建SID，每个阶段512个centroid即可兼顾语义区分度和计算效率，无需复杂调参'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多商家电商平台中，同款/相似商品在不同商家下有独立ID，用户行为信号分散无法跨商家复用；而人工定义的商品类目粒度过粗，无法支撑细粒度个性化。同时搜索侧Query改写依赖字符串级session transitions，存在拼写变体、同义词、跨品类歧义等问题，两类场景长期缺乏可复用的统一语义商品表示。

### 方法关键点
- 用Gemini embedding编码商品文本属性（名称、品牌、规格），采用3阶段残差K-means量化生成3级Semantic ID（L1/L2/L3，每级512个centroid），前缀越长语义粒度越细
- 推荐排序侧：基于SID前缀构建多粒度稠密统计特征（用户偏好、区域商品表现），同时对SID做BPE子词切分构建用户历史序列与候选商品匹配特征，输入多任务排序模型
- Query改写侧：将Query按关联加购行为映射到对应粒度SID概念，挖掘SID级的session transitions做横向跳转建议，同时支持从L2下探到L3做细粒度意图细化，最终经LLM渲染为用户可见Query，叠加商家在售商品过滤

### 关键实验
- 排序侧离线Ablation：仅SID特征就带来MRR@5相对提升4.88%；在线实验首坑加购率提升8%，次坑提升16%，头部商品曝光占比下降2.1pct，客单价提升0.31%
- Query改写侧离线：相比人工类目，SID减少7.9%的意图跳转损失；相比字符串transitions，LLM打分的建议质量从0.522提升到0.734；在线实验加购位置下降1.57%，搜索滚动深度下降1.87%，购买MRR提升0.56%

### 核心结论
SID是跨场景可复用的语义先验，而非完整的任务意图表示，各场景可在SID基础上叠加自身任务信号与上下文，无需共享模型或训练逻辑即可获得增益
