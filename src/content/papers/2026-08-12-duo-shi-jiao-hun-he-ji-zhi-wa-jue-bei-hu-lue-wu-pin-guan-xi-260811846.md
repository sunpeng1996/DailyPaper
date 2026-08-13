---
title: 'From Overlooked to Explored: Recovering Item Relations via Mixture of Perspectives
  for Sequential Recommendation'
title_zh: 多视角混合机制挖掘被忽略物品关系的序列推荐方法
authors:
- Junyoung Kim
- Wonbin Kweon
- Woojoo Kim
- Jaehyung Lim
- Dongha Kim
- Hwanjo Yu
affiliations:
- Pohang University of Science and Technology
- University of Illinois Urbana-Champaign
arxiv_id: '2608.11846'
url: https://arxiv.org/abs/2608.11846
pdf_url: https://arxiv.org/pdf/2608.11846
published: '2026-08-12'
collected: '2026-08-13'
category: RecSys
direction: 序列推荐 · 注意力校准
tags:
- Sequential Recommendation
- Self-Attention
- Similarity Bias
- Attention Calibration
- Mixture of Perspectives
one_liner: 提出PRISM多视角校准模块，缓解自注意力相似性偏差，大幅提升序列推荐全场景性能
practical_value: '- 可直接把PRISM作为即插即用模块嵌入现有Transformer序列推荐架构（如SASRec、BERT4Rec）的层间，无需大幅重构模型，即可缓解相似性偏差，提升跨品类、搭售推荐的效果，落地成本极低

  - 双视角设计可直接复用：Affinity View优化同语义组物品关联、Contrast View挖掘跨语义组潜在关联的思路，适配电商跨品类推荐、搭配推荐场景，解决用户隐藏需求挖掘的痛点

  - Semantic Anchor Router的噪声门控设计可解决冷启动场景下物品语义分组不平衡的问题，尤其适合新用户、新物品少交互的推荐场景

  - PRISM全透镜参数共享的设计额外参数量极低（K=4仅比SASRec多4万左右参数），推理延迟接近原生Transformer，适合高并发线上推荐场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Transformer-based序列推荐的点积自注意力存在固有相似性偏差，过分关注与查询物品相似的同质物品，系统忽略携带有效偏好信号的异质跨组物品关系（如买跑鞋后的运动水壶需求），导致用户复杂偏好捕捉不全，现有注意力校准、意图建模、MoE等方案均未从根源解决该偏差，限制推荐效果提升。

### 方法关键点
- 轻量PRISM模块插在Transformer层之间，通过K个参数共享的Perspective Lenses校准注意力：
  1. Semantic Anchor Router：带噪声门控的语义分组模块，为每个物品生成语义组成占比和主语义锚点，保证分组均衡
  2. 双视角校准：查询物品与透镜语义组匹配时启用Affinity View，优化同组同质关联；不匹配时启用Contrast View，挖掘被抑制的跨组异质关联
  3. 辅助训练损失：LSPCL序列级对比损失对齐同目标用户的序列表示，LCCL协同一致性损失保证多透镜输出语义空间一致

### 关键结果
在7个公开基准数据集（Amazon 5个子品类、ML-1M、Yelp）上对比13个SOTA基线，PRISM所有指标全面领先：HR@5最高提升9.44%，NDCG@5最高提升11.15%；冷启动场景（序列长度<5）较基线最高提升12.44%，低相似度跨品类目标推荐场景较基线最高提升39.4%，同时参数量、推理延迟接近原生Transformer。

> 最值得记住的结论：自注意力的相似性偏差是序列推荐跨品类隐藏需求挖掘的核心瓶颈，相比盲目增加模型容量，显式校准同质/异质关系的性价比更高。
