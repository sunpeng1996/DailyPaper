---
title: 'TS-GEAR: Taobao Shangou GEnerative Ad Retrieval'
title_zh: TS-GEAR：面向即时配送场景的淘宝闪购生成式广告检索框架
authors:
- Guofeng Tong
- Xu Zhang
- Guangliang Yu
- Haiqiang Wang
- Guannan Cong
- Xing Guo
- Yang Zhou
- Jingjing Duan
- Shuang Li
- Feng Shi
affiliations:
- Alibaba Group
arxiv_id: '2611.12180'
url: https://arxiv.org/abs/2611.12180
pdf_url: https://arxiv.org/pdf/2611.12180
published: '2026-11-09'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · LBS场景生成式广告召回
tags:
- Generative Retrieval
- Geo-Aware Recommendation
- Semantic ID
- RL Alignment
- On-Demand Delivery
one_liner: 面向即时配送场景提出带地理感知ID、双目标注意力和GMPO对齐的工业级生成式广告检索框架，已全量上线淘宝闪购
practical_value: '- 本地生活/即时零售等LBS类生成式检索可直接复用Geo-Semantic ID设计：将分层geohash作为ID前缀，配合前缀约束解码，可省去大量后处理地理过滤的算力开销，同时实现可达性的端到端优化

  - 多场景行为聚合可借鉴Query-Geo Target Attention的双目标设计：将实时query、当前位置等强请求信号作为attention target，给历史行为关联的场景特征（如行为发生地）编码到key，能有效过滤无关历史噪声，适配用户跨场景兴趣偏移

  - 生成式检索的RL对齐阶段若遇候选集冗余、策略塌陷问题，可替换GRPO为GMPO：通过组奖励和留一法边际优势直接优化候选集整体价值，无需额外引入多样性辅助损失，同时兼顾业务优先级和候选多样性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
即时配送（外卖、闪购）场景的检索存在地理硬约束，超出配送范围的商家为完全无效候选，现有生成式检索的Semantic ID无结构化地理信息，只能靠非可微的后处理过滤，浪费beam算力且无法端到端优化；其次用户兴趣随位置、query变化显著，不加地理条件聚合历史行为会产出有偏的兴趣表示；另外自回归训练的单序列独立打分逻辑，容易生成大量近重复候选，与检索候选集整体价值的优化目标不匹配。
### 方法关键点
- 设计**Geo-Semantic ID**：将商家标识拆分为3级地理前缀（分层geohash编码，对应1250km→39km→1.2km层级）+3级语义后缀，解码时仅允许生成用户9宫格配送范围内的地理前缀，把可达性从后处理步骤变为生成目标；
- 编码器端采用**Query-Geo Target Attention**：以实时query和用户当前位置作为双目标聚合历史行为，同时将每个行为发生的位置编码到attention key，实现跨区域的用户兴趣迁移；
- RL对齐阶段提出**GMPO（Group Marginal Policy Optimization）**：在GRPO基础上用去重后的组奖励和留一法边际优势计算优势值，直接优化候选集的整体价值与多样性，无需额外引入多样性辅助损失。
### 关键实验
在淘宝闪购工业数据集（4.8M商家、0.5B交互）上对比TIGER、GNPR、OneLoc等SOTA生成式检索方案，20km生产级配送半径下HitRate@50较OneLoc提升36.3%，生成候选的地理有效率达93%以上；7天线上A/B测试采用0.1B轻量backbone，实现广告曝光+3.8%、广告收入+4.2%，目前已全量上线，日处理超1.5亿次查询。
### 核心结论
生成式检索在带强约束的场景下，将约束信息结构化编码到ID的前缀层级，配合约束解码与端到端优化，收益远高于后处理加软约束的方案。
