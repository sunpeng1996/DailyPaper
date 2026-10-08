---
title: 'EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory'
title_zh: EngramEdit：基于条件内存的大语言模型解耦知识更新方法
authors:
- Hongru Cai
- Ran Wei
- Wenjie Wang
- Chengfa Wu
- Ning Song
- Yongqi Li
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- Hangzhou Diagens Biotechnology Co., Ltd
- University of Science and Technology of China
arxiv_id: '2610.10533'
url: https://arxiv.org/abs/2610.10533
pdf_url: https://arxiv.org/pdf/2610.10533
published: '2026-10-06'
collected: '2026-10-08'
category: LLM
direction: LLM知识编辑 · 条件内存架构优化
tags:
- Knowledge Editing
- Conditional Memory
- n-gram Embedding
- LLM
- Model Updating
one_liner: 固定Transformer主干，通过带正则的n-gram嵌入联合更新实现低侵入高泛化的LLM知识编辑
practical_value: '- 电商/广告场景实时更新商品、活动、规则类知识时，可复用该框架仅编辑n-gram嵌入，无需微调Transformer主干，大幅降低更新成本并保留模型通用能力

  - 生成式推荐/Agent业务中，可借鉴「多语义表述生成+联合更新」设计，确保不同用户query的口语化/多样化表述都能命中更新后的正确知识，提升编辑泛化性

  - 知识注入时可复用其复用正则策略：对短、高频n-gram施加更强更新惩罚，避免修改通用语义表达，大幅降低知识编辑的副作用'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
基于n-gram条件内存的LLM（如DeepSeek Engram、Qwen3.8-Flash）已验证可在低计算开销下扩容模型容量，且事实知识主要存储在n-gram嵌入中，具备知识与计算解耦的潜力，但此前没有成熟的编辑方案：常规知识编辑要么修改Transformer主干导致通用能力退化，要么直接更新n-gram嵌入会遇到多表述激活不同n-gram、共享n-gram更新冲突等问题，导致编辑成功率低、泛化差、无关知识被篡改。
### 方法关键点
- 针对每个待编辑事实，生成K个语义等价的不同表述，覆盖更多可能被激活的n-gram
- 固定Transformer主干参数，仅优化临时共享扰动，得到每个表述对应的目标内存表征
- 构建表述到激活n-gram的映射矩阵，联合求解所有n-gram嵌入的更新量，对长度更短、语料中出现频率更高的n-gram施加更强的正则惩罚，避免影响无关知识
### 关键实验
在CounterFact、ZsRE、MQuAKE数据集上对比FT、AdaLoRA、MoEEdit等基线，编辑成功率接近100%，泛化到未见过的表述的准确率达97%，CoT多跳推理准确率是最强基线的3倍，连续完成5000次编辑后仍保留96%以上的通用能力，无关知识几乎不受影响。

**最值得记住的一句话**：条件内存不仅可用于扩容LLM容量，还能作为独立的可编辑知识接口，实现完全解耦的事实更新与通用能力保留。
