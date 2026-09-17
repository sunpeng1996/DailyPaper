---
title: Modality-Autoregressive World-Action Models
title_zh: 模态自回归世界动作模型ModAR
authors:
- Adam Hung
- Bardienus P. Duisterhof
- Deva Ramanan
- Jeffrey Ichnowski
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.17524'
url: https://arxiv.org/abs/2609.17524
pdf_url: https://arxiv.org/pdf/2609.17524
published: '2026-09-14'
collected: '2026-09-17'
category: Agent
direction: Agent世界模型 · 多模态序列生成
tags:
- Multimodal
- World Model
- Autoregressive
- Denoising
- Agent
one_liner: 提出首个动作预测前自回归去噪多模态的世界动作模型ModAR，训练成本更低性能更优
practical_value: '- 多模态融合可采用逐模态自回归生成范式，让后序模态依赖前置模态特征，效果优于并行融合，可迁移至多模态商品内容生成、多模态召回场景

  - 特征选择优先保留高信息量模态（如语义特征、结构特征、行为轨迹），砍掉冗余原始模态（如低价值原始图文），可同时降本提效，适用于推荐特征工程、Agent感知模块优化

  - 无预训练的自回归去噪建模可大幅降低训练算力消耗，可借鉴到垂类小样本多模态模型训练，减少通用预训练依赖'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有世界动作模型（WAMs）多仅通过预测RGB建模未来，未高效融合深度、预训练视觉特征、点轨迹等可捕捉几何、语义、运动信息的模态，多模态融合范式缺乏统一最优方案。
### 方法关键点
提出ModAR，是首个在动作预测前先对多种未来模态进行自回归去噪的WAM，每步模态预测可基于已生成的前置模态结果，无需依赖预训练模型，支持从零训练。
### 关键结果
1. 预测点轨迹、DINO特征、深度图可稳定提升WAMs性能，新增RGB预测无一致收益；
2. 序列生成范式优于现有WAM结构，所有数据规模下成功率均为最高；
3. 对比微调后的预训练基线Flex-π，ModAR平均成功率达75%（基线72%），训练FLOPs降低20倍且无需预训练；
4. 在3个真实世界双手操作任务上优于所有基线，加入人类视频数据可进一步提升效果。
