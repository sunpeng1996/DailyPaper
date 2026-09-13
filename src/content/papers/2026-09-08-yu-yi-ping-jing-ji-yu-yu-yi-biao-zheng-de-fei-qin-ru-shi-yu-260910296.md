---
title: 'The Semantic Bottleneck: Leveraging Semantic Representations for Non-Invasive
  Speech Decoding'
title_zh: 语义瓶颈：基于语义表征的非侵入式语音解码方法
authors:
- Gilad D. Landau
- Dulhan Jayalath
- Oiwi Parker Jones
affiliations:
- University of Oxford
- PNPL
arxiv_id: '2609.10296'
url: https://arxiv.org/abs/2609.10296
pdf_url: https://arxiv.org/pdf/2609.10296
published: '2026-09-08'
collected: '2026-09-13'
category: Other
direction: 跨模态语义解码 · 语义瓶颈架构
tags:
- Semantic Bottleneck
- Cross-Modal Mapping
- Semantic Embedding
- Speech Decoding
- Embedding Inversion
one_liner: 提出Brain2Semantics2Text架构，通过语义瓶颈实现非侵入式MEG信号到自然语言的高精度解码
practical_value: '- 低信噪比输入场景（如用户模糊搜索query、行为噪声大的推荐场景）可引入中间语义嵌入作为瓶颈层，跳过细粒度单元对齐直接提取核心意图，降低建模难度

  - 跨模态映射任务（如用户多模态行为/输入转推荐语义标签）可复用「源信号→语义流形→目标输出」两阶段架构，提升鲁棒性

  - 语义嵌入反推自然语言的思路可落地到用户意图理解、搜索query补全、个性化文案生成场景，无需细粒度标注即可还原核心语义'
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
非侵入式脑电语音解码受限于神经信号信噪比低，细粒度音素、单词级重建难度大；神经科学研究证实高层语义表征具有空间分布广、时间尺度慢、冗余度高的特性，更适合作为低信噪比信号的解码目标。
### 方法关键点
Brain2Semantics2Text采用两阶段架构：1）将句子级MEG脑电信号映射到预定义语义流形空间；2）将预测得到的语义嵌入反转为自然语言。语义瓶颈设计无需词级对齐即可还原高层语义，同时配套降噪策略提升神经信号到语义映射的可靠性。
### 关键结果
与现有非侵入式Brain2Text基准方法相比，句子级文本重建效果实现显著提升。
