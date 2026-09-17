---
title: 'FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal
  Tokens for Retrieval and Generation'
title_zh: FLAT：图文重采样为可变长度对齐跨模态Token用于检索与生成
authors:
- Guangyu Sun
- Shlok Kumar Mishra
- Wentao Bao
- Robert Zhenheng Yang
- Xiao Wang
- Xiyuan Wang
- Yujunrong Ma
- Chen Yuan
- Max Xiangjun Fan
- Jun Xiao
affiliations:
- Meta AI
arxiv_id: '2609.16591'
url: https://arxiv.org/abs/2609.16591
pdf_url: https://arxiv.org/pdf/2609.16591
published: '2026-09-14'
collected: '2026-09-17'
category: Multimodal
direction: 多模态表征 · 跨模态检索与生成
tags:
- Multimodal Representation
- Cross-Modal Retrieval
- Text-to-Image
- Image-to-Text
- Pre-training
one_liner: 提出联合优化的跨模态预训练框架FLAT，同时支撑跨模态检索与生成两类任务
practical_value: '- 电商多模态搜广推场景可复用FLAT的联合预训练范式，统一跨模态表征同时服务商品检索、图文生成两类任务，减少多系统重复开发成本

  - 嵌套dropout对prefix-K动态长度的优化技巧可直接迁移至多模态Prompt生成、变长商品语义表征构造场景，适配不同召回/生成链路的输入长度要求

  - 线性插值、隐空间算术特性可用于电商组合检索场景，比如「A款连衣裙+蓝色」的零样本组合检索需求，无需额外微调即可实现语义组合查询'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统多模态任务拆分表征预训练、下游生成两个独立阶段，冻结的预训练嵌入成为生成性能瓶颈，无法同时适配判别式检索与生成类任务需求。
### 方法关键点
1. FLAT预训练框架联合优化共享多模态编码器与双向（T2I/I2T）生成解码器，同时引入对比对齐+跨模态生成双训练目标，让输出表征兼具判别检索能力与生成条件适配性；
2. 架构上将图文输入统一映射到1D连续序列空间，对前缀K个token施加嵌套dropout，支持动态输出长度适配不同任务需求。
### 关键结果
单阶段预训练即可实现跨模态检索与生成，T2I GenEval达71.1；微调后性能追平SOTA：T2I GenEval 83.1，MS-COCO图文captioning BLEU-4 40.5、CIDEr 138.6，MS-COCO I2T/T2I Recall@5达86.8/75.8，Flickr30K对应指标达98.3/93.6，原生支持线性插值、隐空间运算与零样本组合检索
