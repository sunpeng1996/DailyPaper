---
title: 'Take a Step Back: A Dual-Granularity Raw Feature Empowered Intermediate Fusion
  Graph Convolutional Network for Multimodal Recommendation'
title_zh: 基于双粒度原始特征与中间融合GCN的多模态推荐框架
authors:
- Jinfeng Xu
- Zheyu Chen
- Shuo Yang
- Jinze Li
- Wenhao Yuan
- Ziyue Peng
- Puzhen Wu
- Shujie Li
- Jian Chen
- Zheng Lin
affiliations:
- The University of British Columbia
- The Hong Kong Polytechnic University
- The University of Hong Kong
- The Hong Kong University of Science and Technology
- University of Luxembourg
arxiv_id: '2611.19974'
url: https://arxiv.org/abs/2611.19974
pdf_url: https://arxiv.org/pdf/2611.19974
published: '2026-11-15'
collected: '2026-11-17'
category: RecSys
direction: 多模态推荐 · 双粒度特征与GCN融合
tags:
- Multimodal Recommendation
- GCN
- LLM
- Dual-granularity Feature
- Modality Fusion
one_liner: 用LLM预生成双粒度原始特征+中间融合GCN，多模态推荐性能较SOTA最高提8.81%
practical_value: '- 特征工程侧：可离线用MLLM生成商品粗粒度文本/视觉特征，与原始细粒度特征组成双路输入，无需在训练阶段学习多粒度表征，大幅降低稀疏场景下的训练难度，LLM调用仅需一次、特征可跨训练迭代复用，适合电商冷启动场景

  - 模态融合架构：放弃传统早/晚融合方案，采用ID锚定的GCN中间层动态权重融合，每层传播时自适应修正各模态贡献，既保留模态特有判别信息，又能捕捉跨模态信号，额外计算开销极低

  - 冷启动优化：配合预构建的冻结单张item-item语义图做一跳邻居聚合，商品冷启动场景下Recall@20相对SOTA最多提升11%，可直接复用在电商新商品推荐链路

  - 性能增强：可额外添加模态对齐、粒度对齐的InfoNCE损失，能在基础版之上再提升1%左右的Recall指标，资源充足的业务场景可作为可选优化项'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐存在两大核心痛点：一是多粒度表征训练需要充足监督信号，但推荐场景天然存在数据稀疏问题，导致表征质量低、训练难度大；二是主流依赖对比学习做模态对齐的方案会过度压缩模态特有信息，丢失关键判别特征，制约推荐性能上限。

### 方法关键点
- 双粒度原始特征构建：用MLLM离线生成商品文本/视觉的粗粒度特征，与原始细粒度特征组成双粒度输入，无需在训练阶段学习多粒度表征，大幅降低训练难度
- 中间融合GCN：以ID模态为锚点，在GCN每一层消息传播时动态计算各模态的修正权重，逐层融合跨模态信号，同时规避早融合丢失单模态特征、晚融合错过跨层跨模态信号的缺陷
- 增强策略：预构建基于原始特征相似度的冻结item-item语义图，做一跳邻居聚合增强item表征；可选择性添加模态对齐、粒度对齐的对比学习任务，进一步提升性能

### 关键实验
在4个亚马逊公开数据集（Baby、Sports、Pet、Office）上对比15个SOTA多模态推荐基线，Recall@20相对最优基线MambaRec分别提升3.54%、5.17%、8.81%、6.49%；在交互数<5的最稀疏用户组、商品冷启动场景下优势更明显，训练效率优于多数SOTA模型。

最值得记住的结论：多模态推荐无需硬扛稀疏数据训练复杂多粒度表征，退一步用LLM预生成双粒度特征+GCN中间层动态融合，性价比更高
