---
title: 'One Graph, Multiple Gains: Single High-Quality Item-Item Graph for Multimodal
  Recommendation'
title_zh: 基于单一高质量物品-物品图的多模态推荐框架IIMRec
authors:
- Jinfeng Xu
- Zheyu Chen
- Ziyue Peng
- Shuo Yang
- Jinze Li
- Zewei Liu
- Shujie Li
- Yipeng Du
- Edith C. H. Ngai
affiliations:
- The University of Hong Kong
- The Hong Kong Polytechnic University
- The Hong Kong University of Science and Technology
arxiv_id: '2607.24607'
url: https://arxiv.org/abs/2607.24607
pdf_url: https://arxiv.org/pdf/2607.24607
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 多模态推荐 · 物品-物品图全链路复用
tags:
- Multimodal Recommendation
- Item-Item Graph
- Graph Convolution
- BPR Augmentation
- Cold Start
one_liner: 构建一次高质量物品-物品图，在推荐全链路三阶段复用，实现性能与效率双重提升
practical_value: '- 物品-物品图构建可复用NCER方法：融合多模态语义+用户行为共现信号后，用节点共享邻居占比（triadic closure原则）离线重加权边，无训练/推理开销，可有效过滤噪声边，尤其适配稀疏、冷启动场景。

  - 训练优化可直接复用INA软正样本增强：将正样本的高置信I-I邻居作为折扣软正样本扩充BPR训练集，与原生BPR优化方向完全一致无冲突，仅增加 negligible
  计算开销即可提升稀疏场景效果。

  - 表示增强可替换固定残差为RIG自适应门控：对每个item单独学习I-I传播信号的融合权重，避免噪声I-I信号污染协同过滤特征，代码改动量极小，泛化性优于固定加和方案。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有多模态推荐中的物品-物品（I-I）图普遍存在两大痛点：一是构建时仅通过cos相似度/共现计数生成，噪声多，未评估边的结构可靠性；二是仅用于I-I表示传播单一场景，价值未充分挖掘，在交互稀疏、冷启动场景下短板尤为明显。
**方法关键点**：
1. 离线构建高质量I-I图：融合多模态语义（空间+频谱特征生成的KNN图）与行为共现图，通过NCER（邻域一致性边重加权）基于triadic closure原则，用两个节点的共享邻居占比重加权边，放大可靠边、抑制噪声边，理论上可降低图的谱噪比。
2. 全链路三阶段复用：①表示增强：用RIG残差I-I门控，每个item自适应学习I-I传播信号的融合权重，避免噪声信号污染CF特征；②交互图增强：用高置信I-I邻居生成虚拟用户-物品边，扩展交互图缓解稀疏问题；③优化增强：INA软正样本增强，将正样本的Top I-I邻居作为折扣软正样本扩充BPR训练，与原生BPR优化方向一致无冲突。
**关键结果**：在Amazon Baby/Sports/Clothing、TikTok共4个数据集上，对比20个SOTA基线（含SMORE、COHESION等最新多模态推荐模型），所有指标均最优：Recall@20相对最强基线提升3.7%~5.5%，NDCG@20提升4.9%~6.7%，冷启动场景下Recall@20提升3.3%~6.7%；同时训练速度比基线快29%~53%，GPU显存占用降低37%~70%。
**核心启示**：高质量I-I图一次构建、全链路多阶段复用的范式，能同时实现效果提升与成本下降，是多模态推荐落地的高性价比优化方向。
