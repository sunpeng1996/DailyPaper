---
title: 'LESSRec: Level-Specific History Modeling for Semantic ID-Based Recommendation'
title_zh: LESSRec：面向语义ID推荐的层级专属历史建模方法
authors:
- Shangxin Yang
- Zongwei Wang
- Jing Long
- Junliang Yu
- Min Gao
affiliations:
- Chongqing University
- Griffith University
arxiv_id: '2610.37286'
url: https://arxiv.org/abs/2610.37286
pdf_url: https://arxiv.org/pdf/2610.37286
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · Semantic ID
tags:
- Generative Recommendation
- Semantic ID
- Sequence Modeling
- Attention Mechanism
- Efficient RecSys
one_liner: 针对语义ID生成式推荐的跨层级干扰问题，提出层级专属建模方案，兼顾效果与计算效率
practical_value: '- 做Semantic ID生成式推荐时，可直接复用层级隔离自注意力+层级对齐交叉注意力的设计，避免跨层级语义干扰，实测可带来6%~54%的相对效果提升，仅增加0.4%的参数

  - LESSRec+的无参数增量优化思路可直接落地：将原有共享编码器拆分为层级专属分组，总参数不变的前提下编码器计算量降低L²倍，训练收敛速度提升65%，长历史场景推理延迟最高降30%

  - 双分支交叉注意力融合思路可迁移到多粒度序列建模场景：同层级历史序列+聚合后的item级序列加权融合，权重α设为0.5左右即可兼顾细粒度模式和整体语义，无需额外调参

  - 长历史用户推荐场景优先落地LESSRec+，实测历史长度15~20的用户群体上Recall@5相对增益达53.3%，远高于短历史用户的29.8%，效果提升更显著'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于残差量化的Semantic ID生成式推荐默认混合编码所有层级的历史token，解码器无差别访问全量历史，会引入跨层级语义干扰。推理实验验证，仅允许解码器访问目标对应层级的历史时，效果反而优于全量访问，层级隔离下Recall@10相对提升可达49.46%，亟需针对层级特性优化历史建模逻辑。
### 方法关键点
- 编码器侧用Level-Isolated Self-Attention（LIS）限制每个token仅与同层级历史token交互，避免跨层级信息混淆
- 解码器侧用Level-Aligned Cross-Attention（LAC），预测某层级token时仅允许访问对应层级的历史序列
- 构造Item-Level Semantic Sequence（ILS）：将每个历史item的所有层级编码平均池化后做残差投影，补充item全局语义
- 双分支交叉注意力融合：同层级历史分支与item级分支输出按权重α加权融合，兼顾细粒度层级模式与全局语义
- LESSRec+优化：将共享编码器拆分为层级专属分组，总参数不变的前提下降低编码器计算量，支持并行运算
### 关键结果
在Games、Software、Beauty三个亚马逊公开数据集上，对比TIGER、DiscRec、SASRec等基线，覆盖RQ-VAE、RQ-Kmeans、LETTER三种tokenizer，LESSRec相对基线最高提升39.2%，LESSRec+最高提升54.3%；LESSRec+训练收敛速度提升65.2%，峰值GPU内存降低39.2%，15~20条长历史用户场景下推理延迟最高降29.5%。
### 核心结论
语义ID生成式推荐中，预测某层级token时，同层级历史的信息量远高于其他层级，针对性做层级隔离建模可同时提升效果与效率
