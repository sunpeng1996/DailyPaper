---
title: 'RareSense: Rarity-Aware Similarity Search for Anomaly Retrieval in Transactional
  Data'
title_zh: RareSense：面向交易数据异常检索的稀有感知相似搜索方法
authors:
- Sidahmed Benabderrahmane
- Talal Rahwan
affiliations:
- New York University NYUAD, Department of Computer Science
arxiv_id: '2607.28879'
url: https://arxiv.org/abs/2607.28879
pdf_url: https://arxiv.org/pdf/2607.28879
published: '2026-07-30'
collected: '2026-08-03'
category: RecSys
direction: 稀疏数据相似搜索 · 交易异常检索
tags:
- Similarity Search
- Anomaly Detection
- Rare Itemset
- Association Rule
- Transactional Data
one_liner: 提出基于稀有项集关联规则的交易数据异常检索相似搜索框架，效果优于原子特征基线
practical_value: '- 电商反欺诈场景可直接复用框架逻辑，将交易样本映射为稀有共现规则特征，替代单特征IDF加权，提升异常交易召回准确率

  - 稀疏特征相似性计算可借鉴其多维度权重设计（融合支持度、置信度、复杂度、稳定性），缓解高频属性主导的匹配偏差

  - 推荐召回/粗排阶段的相似匹配可引入最小稀有项集作为中间结构，捕捉高阶共现信号，提升长尾物品/小众用户的匹配精度'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
传统Jaccard、余弦等稀疏集合相似性度量受高频背景属性主导，IDF加权仅能处理原子级特征，无法捕捉有效高阶共现信号，交易数据异常检索效果受限。
### 方法关键点
提出RareSense稀有感知相似框架：1）挖掘最小稀有项集作为中间结构，生成可靠稀有关联规则；2）将样本映射为稀疏稀有规则特征向量；3）融合逆支持度、置信度、提升度、结构复杂度、稳定性计算规则权重，用加权Jaccard计算相似性。证明IDF加权Jaccard是其单例特例，诱导距离为伪度量。
### 关键结果
4类跨网络安全、分类领域基准测试中，查询条件检索的宏观平均性能为所有评估度量最优；全局异常排序的宏观平均性能最优，与专业检测器效果统计相当，在异常存在可重复稀有高阶结构的场景下增益最高。
