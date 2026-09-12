---
title: Harnessing Intrinsic Subject-Aware Attention for Controllable Multi-Subject
  Video Generation
title_zh: 基于内在主体感知注意力的可控多主体视频生成方法
authors:
- Niange Yu
- Ye Tian
- Biaolong Chen
- Miao Lu
- Aixi Zhang
- Hao Jiang
- Yunhai Tong
- Pipei Huang
affiliations:
- Alibaba Group
- Peking University
arxiv_id: '2609.11507'
url: https://arxiv.org/abs/2609.11507
pdf_url: https://arxiv.org/pdf/2609.11507
published: '2026-09-10'
collected: '2026-09-12'
category: Multimodal
direction: 多模态生成 · 可控多主体视频生成
tags:
- Diffusion Transformer
- Video Generation
- Attention Mechanism
- Reinforcement Learning
- Semantic Drift
one_liner: 挖掘DiT内在空间定位图提出DIAL框架解决多主体视频生成可控性与语义漂移问题
practical_value: '- 电商虚拟试穿、多商品展示短视频生成场景，可复用ISGM抽取逻辑提升多主体视觉一致性，无需额外训练成本

  - DiT内部注意力无监督挖掘的思路可迁移到生成式推荐的多主体内容生成场景（如直播间混排商品短视频），降低语义漂移

  - 无需额外标注自动构建RL偏好对的方法，可复用在商品文案、营销短视频等生成式内容的可控性优化，大幅降低标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
多主体视频生成面临两大核心痛点：一是保真度强度不可控，二是易出现语义漂移，无法满足虚拟试穿、个性化营销内容生成等高价值场景的细粒度可控需求。
### 方法关键点
1. 挖掘DiT内部注意力块天然生成的Intrinsic Spatial Grounding Map（ISGM），可无需额外标注精确定位参考主体
2. 提出双阶段内在注意力利用框架DIAL：低噪声阶段用ISGM引导注意力，无需重训练即可在推理时精准控制保真度强度；高噪声阶段用ISGM零成本自动构建RL偏好对，锚定模型对参考主体的注意力，缓解语义漂移
### 关键结果
在OpenS2V-Eval基准上显著优于所有基线模型，身份一致性指标稳定提升，同时实现了保真度强度的可调节控制
