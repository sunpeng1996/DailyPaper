---
title: 'UniTAC: Universal Task-Aware Compression via Weighted Distortion Measures'
title_zh: UniTAC：基于加权失真度量的通用任务感知压缩
authors:
- Homa Esfahanizadeh
- Matin Mortaheb
- Jinfeng Du
- Harish Viswanathan
affiliations:
- Nokia Bell Labs
arxiv_id: '2608.16696'
url: https://arxiv.org/abs/2608.16696
pdf_url: https://arxiv.org/pdf/2608.16696
published: '2026-08-17'
collected: '2026-08-21'
category: Other
direction: 任务感知通用压缩 · 语义通信
tags:
- Task-aware Compression
- Learned Image Codec
- ViT
- Rate-distortion
- Semantic Communication
one_liner: 提出无需重训即可运行时切换适配下游任务的单模型学习图像压缩框架UniTAC
practical_value: '- 多任务适配思路可迁移至多模态召回压缩场景：用下游模型梯度生成重要性向量，无需重训主干即可动态调整多模态特征压缩权重，降低端云传输带宽开销

  - 固定主干+轻量条件注入的架构可复用至LLM多场景适配：替换条件向量即可切换任务，避免多任务场景下重复部署大模型的存储成本

  - 加权重构失真的训练策略可借鉴至个性化推荐的特征压缩：根据用户/场景重要性加权压缩特征，在低带宽下保留核心业务指标'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
物理AI系统高维传感信号传输受带宽、时延、能耗严格约束，下游任务动态变化时，任务专属编码需逐任务重训，部署灵活性差，通用编码的任务相关精度损失过高。

### 方法关键点
1. 将下游任务抽象为低开销的逐分量重要性向量（可从下游模型梯度归因生成），作为编解码器的条件输入；
2. 基于随机采样的重要性向量族，针对加权重构失真一次性训练ViT架构的编码主干，运行时仅需替换注入的重要性向量即可切换适配不同任务，无需重训；
3. 理论推导了对角加权失真的任务一致性条件及权重与任务敏感度的对应关系。

### 关键结果
在0.034 bpp的局部任务上，单UniTAC模型精度达91.4%，仅比任务专属编码低1.9%，比通用编码高14.5%。
