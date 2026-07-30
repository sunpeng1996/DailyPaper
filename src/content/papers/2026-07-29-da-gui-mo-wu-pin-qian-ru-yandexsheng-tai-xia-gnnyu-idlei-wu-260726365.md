---
title: 'Embedding Items at Scale: Comparing GNN-Based and ID-Based Item Embeddings
  in the Yandex Ecosystem'
title_zh: 大规模物品嵌入：Yandex生态下GNN与ID类物品嵌入效果对比
authors:
- Sergei Makeev
- Artem Matveev
- Vladimir Baikalov
- Kirill Khrylchenko
affiliations:
- Yandex
arxiv_id: '2607.26365'
url: https://arxiv.org/abs/2607.26365
pdf_url: https://arxiv.org/pdf/2607.26365
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 推荐系统 · 物品嵌入方案选型
tags:
- Item Embedding
- GNN
- Sequential Recommendation
- Two-Tower
- Industrial Case Study
one_liner: 工业级场景下横向对比GNN预训练与端到端ID物品嵌入的效果成本，给出选型参考
practical_value: '- 大规模场景（千万级物品、亿级交互）下直接选择端到端多hash ID嵌入即可，预训练GNN嵌入的收益不足以覆盖额外训练与运维成本

  - 低资源场景（不足百万级交互、物品量级小）可优先用TwHIN等轻量GNN预训练嵌入补全信息，再搭配微调进一步提升效果

  - 工业级排序链路可直接将Transformer双塔的相似度分作为特征输入CatBoost等重排模型，能稳定提升nDCG等核心指标

  - 多hash ID embedding设置6次查找、64维的配置即可在效果和性能间取得较好平衡，适配电商/内容推荐场景落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Transformer序列推荐模型高度依赖物品嵌入方案，现有方案分为GNN预训练嵌入、端到端ID嵌入两类，但此前无工业级大规模场景下同时覆盖效果、成本的横向对比研究，无法为业务选型提供可落地的参考标准。

### 方法关键点
- 采用统一双塔架构：用户塔用双向Transformer编码用户交互序列，物品塔融合文本特征与物品嵌入（GNN/ID）后经残差网络输出表征，以余弦相似度作为匹配分
- 训练分为两阶段：预训练采用下一个物品预测任务+批次负采样softmax损失，微调采用点击预测pointwise损失+交互/非交互对pairwise损失的加权和
- 对比方案覆盖：GNN类含Transductive的TwHIN、Inductive的MultiBiSage，ID类采用多hash嵌入，同时测试两类嵌入融合、GNN嵌入微调等变体

### 关键实验
实验覆盖3个Yandex业务场景：大规模电商Yandex Market（亿级物品、年交互日志）、大规模音乐Yandex Music（百万级曲目、千亿级交互）、低资源生鲜电商Yandex Lavka（2.5万物品、1500万交互，公开数据集）。核心结果：大规模场景下ID嵌入比GNN嵌入在Market场景nDCG最高高0.448%，Music场景加权pair准确率高0.155%；两类嵌入融合仅额外提升0.036%nDCG，收益可忽略；低资源场景下TwHIN预训练嵌入比ID嵌入nDCG@5高0.9%。

**最值得记住的结论**：低资源场景预训练GNN嵌入收益显著，大规模场景下端到端ID嵌入的性价比远高于预训练GNN嵌入。
