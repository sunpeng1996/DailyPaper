---
title: 'TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming'
title_zh: TLive-Omni：面向电商直播场景的全模态理解模型
authors:
- Yibo Hu
- Yu Qian
- Mao Gu
- Yingfan Tao
- Yuhao Chen
- Yongdong Luo
- Zhuoqun Liu
- Meiguang Jin
- Junfeng Ma
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2608.20958'
url: https://arxiv.org/abs/2608.20958
pdf_url: https://arxiv.org/pdf/2608.20958
published: '2026-08-20'
collected: '2026-08-25'
category: Multimodal
direction: 全模态大模型 · 电商直播场景理解
tags:
- Omni-modal
- E-commerce Live Streaming
- Multimodal Understanding
- Temporal Alignment
- GRPO
- MLLM
one_liner: 面向电商直播场景打造全模态理解模型，通过时序对齐、分阶段训练实现多任务效果开源领先
practical_value: '- Per-vGrid时序对齐方案可直接迁移到直播内容审核、商品自动打标等长时序多模态业务，将同时间段音视频token绑定加显式时间戳边界，降低时序匹配误差

  - 三阶段SFT训练策略适合垂直领域多模态大模型落地：先训模态对齐层，再优化单模态能力，最后联合微调全链路，减少跨模态冲突，提升训练收敛速度

  - Faithful-RFT设计适配实时性要求高的业务：放弃思考链奖励，直接用任务可验证指标打分，可同时降低生成幻觉和延迟，适配直播实时交互场景

  - 同步长度分组采样器可直接复用在多模态混合训练流程中，按模态+序列长度分组构造batch，减少padding浪费，平衡多worker算力负载'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
电商直播场景的商品信息分散在主播语音、视频帧、叠加文字、用户提问等多模态信号中，且分布在长时序的不同片段，通用全模态模型未针对直播场景的产品中心属性、长时序对齐需求、低幻觉实时响应要求优化，在直播专属任务上效果无法满足业务要求。
### 方法关键点
- 架构：基于Qwen3.5 backbone接入Qwen3-Omni预训练音频编码器，支持256K上下文；提出Per-vGrid时序token组织方法，将同时间段的视频网格、对应音频段加显式时间戳边界token绑定，实现精准音视频时序对齐
- 训练：采用三阶段SFT策略，阶段1仅训音频对齐层完成音语空间映射，阶段2训音频编码器+对齐层拓展音频理解能力，阶段3微调对齐层+大语言模型完成多模态联合适配；后接Faithful-RFT强化微调，基于GRPO用任务可验证的反馈直接打分，不奖励思考链，同时降低幻觉和生成延迟
- 工程：设计同步长度分组采样器，按模态和序列长度分组构造全局batch，减少padding和不同worker的算力不均衡；动态重采样策略对组内奖励方差接近0的样本重新生成，提升GRPO训练效率
### 关键实验
在自研电商直播基准上测试，对比Gemini、Qwen3-Omni等开源/闭源模型：ASR CER低至6.46%，商品视觉grounding AP达91.45%，视频时序定位mIoU达81.49%，视频QA准确率达93.23%，所有核心任务均达到开源SOTA水平，同时在通用多模态基准上保持竞争力，性能优于原生Qwen3.5 backbone。
> 垂直领域多模态大模型优化，需要将模型架构、数据构造、训练目标、评估协议完全对齐部署场景的核心需求，才能在保证领域效果的同时不丢失通用能力
