---
title: 'BLANC: Discovering Patent White Space via Changes in Normalized Pointwise
  Mutual Information Between Multi-View Clusters'
title_zh: BLANC：基于多视图聚类间NPMI变化的专利空白挖掘方法
authors:
- Shuichi Miyazawa
- Kensuke Fujii
affiliations:
- AGC Inc., Tokyo, Japan
arxiv_id: '2608.26685'
url: https://arxiv.org/abs/2608.26685
pdf_url: https://arxiv.org/pdf/2608.26685
published: '2026-08-27'
collected: '2026-08-29'
category: Other
direction: 多视图语义建模 · 空白机会挖掘
tags:
- Multi-view Clustering
- NPMI
- Topic Modeling
- Patent Analysis
- White Space Detection
one_liner: 提出融合多视图语义建模、NPMI关联量化、ΔNPMI度量的三阶段专利空白挖掘管线
practical_value: '- 多视图语义拆分思路可迁移到电商商品/用户兴趣多维度聚类，例如拆分用途、特性、性价比三个维度做交叉关联分析，挖掘蓝海品类

  - ΔNPMI（全局-局部共现差值）度量可直接复用在推荐系统蓝海item挖掘、搜索query新关联推荐场景，规避纯共现方法泛化性差问题

  - 无ground truth场景下的人工构造样本depletion测试方法可借鉴到新推荐策略的离线有效性校验，无需真实AB测即可快速验证方案潜力'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
专利空白（未探索但高价值的技术领域）挖掘对研发战略规划至关重要，现有方法依赖人工标注或单视图聚类，缺乏可量化的空白检测能力，且无统一真值难以验证。
### 方法关键点
三阶段BLANC管线：1）沿应用场景、创新性、创造性三个语义维度做多视图神经主题建模；2）用NPMI量化跨维度聚类关联度；3）提出ΔNPMI度量，筛选用户指定关键词过滤语料后NPMI大幅下降的组合，识别「全局成熟、局部未探索」的空白机会。
### 关键结果
在USPTO的ML/AI（5417件）和玻璃成分（1982件）数据集上，移除目标组合75%文档时，BLANC召回率分别达34.1%、27.3%，191组诱饵试验零误召回；单视图建模无召回，传统共现方法无特异性；私有数据集上挖掘出的氟表面处理×翘曲抑制组合获专家验证，ΔNPMI最高达0.48。
