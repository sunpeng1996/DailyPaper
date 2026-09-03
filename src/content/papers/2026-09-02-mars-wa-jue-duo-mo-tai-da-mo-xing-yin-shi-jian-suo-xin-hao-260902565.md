---
title: 'MARS: What Retrieval Signals Are Hidden in Multimodal Large Language Models
  for Text-Video Retrieval?'
title_zh: MARS：挖掘多模态大模型隐式检索信号的文本-视频检索框架
authors:
- Uicheol Jung
- Juyoung Hong
- Geuntaek Lim
- Yukyung Choi
affiliations:
- Sejong University
arxiv_id: '2609.02565'
url: https://arxiv.org/abs/2609.02565
pdf_url: https://arxiv.org/pdf/2609.02565
published: '2026-09-02'
collected: '2026-09-03'
category: Multimodal
direction: 多模态检索 · 跨模态表征对齐
tags:
- Multimodal Retrieval
- Text-Video Retrieval
- MLLM
- Embedding
- Hard Negative
- LoRA
one_liner: 融合多模态大模型多层隐状态与多槽位对齐，结合硬负样本优化实现SOTA文本-视频检索
practical_value: '- 跨模态检索场景（电商文本搜商品/短视频、内容平台检索）可直接复用多层隐状态加权融合策略，放弃仅用MLLM最后层单token
  embedding的常规做法，细粒度检索效果提升明显

  - 多槽位嵌入设计可迁移到相似内容区分场景：新增可学习表征token搭配多样性损失、硬负样本槽位特化损失，无需改动MLLM主结构即可强化对相似负样本的区分能力

  - 工程落地成本低：仅训练LoRA参数、层融合权重、槽位token三类参数，视频/商品侧embedding可预计算，在线查询仅需计算query embedding与相似度，延迟符合线上要求

  - 框架通用度高，无需核心改动即可迁移到文本-图片检索、图文商品检索等其他跨模态检索场景'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前基于MLLM的跨模态检索普遍仅抽取最后一层单个token的表征，会将多粒度、多维度的跨模态匹配信号压缩为单一向量，导致细粒度区分能力不足，无法有效区分语义/视觉高度相似的负样本，这也是电商、短视频等场景下相似内容检索的核心痛点。
### 方法关键点
- 多层槽位表征：在prompt回复位插入M个可学习的自适应表征token，每个对应一个独立槽位，为每个槽位学习专属的解码器层权重，融合所有层的隐状态生成槽位嵌入
- 槽位对齐匹配：文本与视频的对应槽位单独计算余弦相似度，均匀聚合所有槽位得分得到最终检索分，避免单向量的信息压缩损失
- 多目标优化：同时优化三类损失：对称InfoNCE损失做跨模态对齐，槽位多样性损失避免同输入槽位冗余，硬负样本感知的槽位特化损失引导不同槽位专注区分不同的困难负样本
### 关键结果
在4个标准文本-视频检索基准上，MARS直接检索模式下T2V平均R@1达67.0、V2T达64.5，较SOTA的InternVideo2-6B分别高2.6/2.6个百分点；搭配DSL后处理后T2V/V2T平均R@1达71.6/72.0，搭配重排后T2V平均R@1达73.2，均为SOTA；在线计算成本较InternVideo2低65%以上，适配线上低延迟需求；在Qwen2-VL、VideoLLaMA3等不同MLLM骨干上可稳定提升2-3个点R@1，通用性强。
**最值得记住的一句话**：MLLM各层都隐含有价值的检索信号，多层融合+多槽位分治是低代价提升跨模态检索效果的有效路径
