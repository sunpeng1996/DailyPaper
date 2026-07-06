---
title: 'DataComp-VLM: Improved Open Datasets for Vision-Language Models'
title_zh: DataComp-VLM：面向视觉语言模型的改进开放数据集
authors:
- Matteo Farina
- Vishaal Udandarao
- Thao Nguyen
- Selim Kuzucu
- Maximilian Böther
- Andreas Hochlehnert
- Adhiraj Ghosh
- Marianna Nezhurina
- Karsten Roth
- Joschka Struber
arxiv_id: '2606.28551'
url: https://arxiv.org/abs/2606.28551
pdf_url: https://arxiv.org/pdf/2606.28551
published: '2026-06-25'
collected: '2026-07-06'
category: Multimodal
direction: 多模态预训练 · 数据治理基准
tags:
- VLM
- Multimodal Training
- Dataset Curation
- Benchmark
- Data-Centric AI
one_liner: 推出VLM训练数据治理基准DCVLM，配套6T多模态token数据集，验证数据混合比过滤更关键
practical_value: '- 做多模态电商推荐/搜索的VLM训练时，优先优化多源数据混合策略，而非单一数据过滤，能更快提升效果

  - 多模态训练数据配比优先倾斜指令微调数据，相比图文对为主的配比，大参数量下增益更显著

  - 可直接复用DCVLM-Baseline数据集训练电商场景多模态理解模型，节省数据治理成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前高性能VLM训练依赖大规模精细化治理的数据集，但业界缺乏系统评估数据治理策略的标准化基准，无法公平对比过滤、混合、采样等策略的实际效果。

### 方法关键点
1. 构建DCVLM基准，整合160个数据集覆盖图文对、多模态 interleaved 文档、纯文本、指令微调4类数据，总规模达6T多模态token；
2. 支持在1B-8B参数量、6.25B-200B token预算下测试各类数据治理策略，配套9个领域共52个下游评测任务。

### 关键结果
1. 验证数据混合而非过滤是高质量训练集的核心，指令占比高的混合策略比图文对占比高的策略缩放性更好，大参数量下增益进一步拉大；
2. 产出的DCVLM-Baseline数据集训练8B VLM在33个核心任务上准确率达63.6%，比SOTA开源VLM训练数据集FineVision提升5.4pp。
