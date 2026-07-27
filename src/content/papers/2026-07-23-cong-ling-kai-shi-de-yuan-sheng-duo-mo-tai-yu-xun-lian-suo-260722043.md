---
title: Scaling Native Multimodal Pre-Training From Scratch
title_zh: 从零开始的原生多模态预训练缩放规律研究
authors:
- Haoyuan Wu
- Aoqi Wu
- Hai Wang
- Jiajia Wu
- Jinxiang Ou
- Bei Yu
affiliations:
- The Chinese University of Hong Kong
- Tencent LLM Department
arxiv_id: '2607.22043'
url: https://arxiv.org/abs/2607.22043
pdf_url: https://arxiv.org/pdf/2607.22043
published: '2026-07-23'
collected: '2026-07-27'
category: Multimodal
direction: 多模态大模型 · 预训练缩放规律
tags:
- Multimodal-LLM
- Pre-training
- Scaling-Law
- Cross-Modal-Transfer
- Vision-Language
one_liner: 揭示原生多模态预训练缩放定律，给出固定算力下模型、数据、配比的最优配置
practical_value: '- 做多模态商品理解/图文搜索的团队，可参考本文缩放定律，固定算力预算下根据图文数据配比调整模型大小、训练token数的分配：文本占比高的数据集优先堆模型容量，算效更高

  - 开发多模态电商Agent/导购助手的团队，可采用原生多模态预训练范式，无需额外对齐纯文本预训练权重，即可同时获得优质多模态感知能力与纯文本推理能力，简化架构

  - 多模态生成（商品文案/短视频脚本生成）场景可复用数据配比优化结论，调整图文训练数据比例，在控制预训练成本的前提下提升跨模态生成一致性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有纯文本预训练LLM缺乏多模态物理世界感知能力，传统晚融合多模态架构存在优化不对称问题，原生多模态预训练范式的缩放规律此前未被系统表征，固定算力下的最优训练配置不明确。
### 方法关键点
对Transformer架构视觉语言模型开展控制变量实验，建模模型参数量、训练token总数、多模态数据配比三类变量与训练损失、算力消耗的量化关系，推导缩放定律与效率边界。
### 关键结果
1. 语言任务缩放规律几乎不受多模态数据占比影响，多模态任务缩放规律对数据配比高度敏感；
2. 文本占比高的数据集仅在大模型尺度下算效更优，最优资源分配会向更大模型容量倾斜；
3. 原生多模态预训练带来正向跨模态迁移，纯文本空间推理能力提升，多模态in-context learning鲁棒性显著增强。
