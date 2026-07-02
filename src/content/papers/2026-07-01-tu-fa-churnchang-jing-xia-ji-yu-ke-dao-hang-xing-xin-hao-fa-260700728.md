---
title: 'When to Repair a Graph ANN Index: Navigability-Signal-Triggered Local Repair
  Protects Tail Recall Under Bursty Churn'
title_zh: 突发churn场景下基于可导航性信号触发的Graph ANN索引修复优化
authors:
- Madhulatha Mandarapu
- Sandeep Kunkunuru
affiliations:
- VaidhyaMegha Private Limited, India
arxiv_id: '2607.00728'
url: https://arxiv.org/abs/2607.00728
pdf_url: https://arxiv.org/pdf/2607.00728
published: '2026-07-01'
collected: '2026-07-02'
category: RecSys
direction: 向量召回 · Graph ANN索引动态维护
tags:
- Graph ANN
- Vector Search
- Recall Optimization
- Index Maintenance
- Bursty Churn
one_liner: 同等修复预算下，可导航性信号触发的Graph ANN局部修复显著提升突发churn下的长尾召回
practical_value: '- 电商/推荐向量召回层（HNSW、DiskANN等）可替换原有固定周期修复策略，用小流量probe召回作为触发信号，同等算力预算下提升长尾商品召回率，尤其适配大促等商品上下架突发波动场景

  - 修复预算有限的中小业务，优先在稀疏、高维向量索引（如多模态商品embedding、用户行为embedding）上部署该策略，收益更显著；鲁棒性强的稠密低维索引收益有限可暂不改造

  - 评估索引修复策略时可复用论文的同预算对比协议，固定consolidation次数做公平对比，避免多堆资源带来的虚假收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Graph ANN索引（HNSW、DiskANN等）是当前电商搜索推荐向量召回的核心组件，在商品/内容上下架的突发churn场景下，删除节点会导致搜索路径断裂、召回率下降，现有固定周期修复策略要么修复不及时导致召回暴跌，要么过度修复浪费算力，亟需更智能的修复触发机制。

### 方法关键点
- 设计三类修复策略做同预算对比：无修复（基线）、固定周期修复（现有工业界方案）、可导航性信号触发修复（新方案）
- 可导航性信号采用独立于评估集的小体量probe查询集的recall@10，计算成本极低，无需引擎内部埋点，与真实召回的斯皮尔曼相关系数达0.95，是有效领先指标
- 采用同预算评估协议，固定consolidation次数对比效果，排除修复投入差异带来的干扰

### 关键实验
在SIFT-128、Fashion-MNIST-784两个公开数据集，模拟突发churn流测试：
- 同等1次修复预算下，信号触发策略比固定周期策略，SIFT数据集最低recall@10提升0.014，Fashion-MNIST提升0.050，平均召回提升<0.005
- 收益集中在长尾/最差召回，索引越稀疏脆弱（图度数越小）收益越高，预算充足或索引鲁棒性强时收益趋近于0
- 100k向量规模下收益依然稳定，最低recall@10提升0.009

**最值得记住的一句话**：在修复预算有限、churn波动大的场景下，Graph ANN索引的修复时机选择比修复投入多少更影响长尾召回表现。
