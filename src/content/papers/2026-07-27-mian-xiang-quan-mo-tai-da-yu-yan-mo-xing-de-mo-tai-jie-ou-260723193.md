---
title: 'OmniScope: Modality-Decoupled Token Compression for Omnimodal Large Language
  Models'
title_zh: 面向全模态大语言模型的模态解耦Token压缩框架OmniScope
authors:
- Jinsen Su
- Yongdong Luo
- Yuexiao Ma
- Yibo Hu
- Meiguang Jin
- Xiaowu Zheng
affiliations:
- Xiamen University
- Alibaba Group
arxiv_id: '2607.23193'
url: https://arxiv.org/abs/2607.23193
pdf_url: https://arxiv.org/pdf/2607.23193
published: '2026-07-27'
collected: '2026-08-01'
category: Multimodal
direction: 多模态大模型推理 · Token压缩
tags:
- OmniLLM
- Token Compression
- Multimodal
- Inference Optimization
- Training Free
one_liner: 无需训练的全模态LLM Token压缩方案，跨模态显著性不匹配下仍保持高精度与推理效率
practical_value: '- 电商直播内容审核、短视频商品问答类多模态Agent可直接复用模态解耦压缩逻辑，避免跨模态指导丢弃关键信息，同时提升推理速度降低显存利用率

  - 视觉侧Anchor-Delta时序压缩策略可迁移到商品多帧图像/短视频理解场景，平衡全局语义覆盖和时序增量信息保留，高压缩比下不丢失商品核心特征

  - 音频侧按秒Token合并方案可复用到直播语音理解、口播文案识别场景，在保证时序连续性的前提下降低冗余Token占比

  - 跨模态显著性不匹配的观测可指导多模态推荐特征选择设计，避免采用单一模态特征指导其他模态特征筛选的错误方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有全模态LLM的Token压缩方法多采用单模态指导另一模态的压缩策略，统计显示78.3%的查询-音视频对的跨模态显著性峰值仅存在弱相关，高压缩比下极易丢弃另一模态的关键信息，导致精度大幅下降；同时长视频场景下音视频Token数量随时长暴涨，推理算力和内存开销急剧上升，严重限制全模态LLM的落地部署。

### 方法关键点
- 模态解耦核心设计：以查询为共享语义锚，音视频模态独立估算Token重要性，独立分配压缩预算，无需跨模态指导
- 视觉侧AD-STC策略：交替采用Anchor帧保留全局空间语义、Delta帧捕获时序增量，自适应切换压缩策略适配不同压缩比
- 音频侧每秒Token合并策略：在编码后时序嵌入上做每秒二分软匹配，合并相似Token而非直接丢弃，保留时序连续性
- 完全训练无关，无需微调即可适配不同全模态LLM

### 关键结果
在4个音视频理解基准、Qwen2.5-Omni 3B/7B两个模型尺度上测试：45% Token保留率下精度几乎无损，甚至优于全Token基准0.3个点；25% Token保留率下，7B模型精度仅下降0.35点，远超所有对比方法，同时获得最高3.53倍prefill加速，GPU内存降低15%以上。

最值得记住的设计原则：全模态LLM推理中查询可以跨模态共享，但显著性估计不需要跨模态共享。
