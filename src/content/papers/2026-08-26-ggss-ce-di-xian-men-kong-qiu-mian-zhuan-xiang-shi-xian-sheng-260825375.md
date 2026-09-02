---
title: 'GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative
  Vision-Language Models'
title_zh: GGSS：测地线门控球面转向实现生成式VLM推理阶段去偏
authors:
- Yiqun Sun
- Junyu Chen
- Pengfei Wei
- Lawrence B. Hsieh
affiliations:
- Magellan Technology Research Institute (MTRI)
- National University of Singapore
arxiv_id: '2608.25375'
url: https://arxiv.org/abs/2608.25375
pdf_url: https://arxiv.org/pdf/2608.25375
published: '2026-08-26'
collected: '2026-09-02'
category: Multimodal
direction: 多模态大模型 · 推理阶段去偏
tags:
- VLM
- Debiasing
- Inference-Time Optimization
- Generative Model
- Geodesic Steering
one_liner: 提出轻量测地线门控球面转向方法，保性能前提下降低生成式VLM的人口统计学偏见
practical_value: '- 推理阶段插轻量hook去偏的架构可直接复用，无需重训已上线的生成式VLM/LLM，适合电商多模态搜索、智能客服等场景快速修正偏见

  - 自适应门控仅对强偏置信号token做修正的思路，可在去偏的同时最小化对业务核心指标（如相关性、准确率）的影响

  - 单位超球面上的反事实偏置子空间挖掘+测地线保范数修正方法，可迁移到用户/物品Semantic ID、多模态embedding的刻板印象修正场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
生成式VLM已广泛应用于电商搜索、招聘推荐等人类中心场景，但存在严重的人口统计学偏见（如职业-性别刻板印象）；现有推理阶段去偏方法多适配静态embedding或CLIP类判别模型，不适用于生成式VLM，而重训去偏的GPU成本极高。
### 方法关键点
1. 在单位超球面上挖掘反事实偏置子空间；
2. 沿测地线弧转向视觉token，保留特征范数避免语义损失；
3. 新增自适应门控，仅对携带强人口统计信号的token做修正，最小化对正常推理的干扰。
### 关键结果
在4个生成式VLM上对比10种推理去偏基线+提示词去偏方案，GGSS在所有模型上取得最低平均偏见，其中3个模型的偏见下降通过配对置换检验显著性；MMStar多模态能力准确率仅比无干预基线波动±0.6p.p.，性能几乎无损。
