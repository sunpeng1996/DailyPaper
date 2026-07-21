---
title: How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced
  Biases in LLMs?
title_zh: 对齐微调如何塑造LLM中谄媚及提示诱导偏差的表征
authors:
- Prakhar Gupta
- Terry Jingchen Zhang
- Florent Draye
- Bernhard Schölkopf
- Zhijing Jin
affiliations:
- University of Michigan
- University of Toronto & Vector Institute
- Max-Planck Institute for Intelligent Systems
- ELLIS Institute Tübingen
- EuroSafeAI
arxiv_id: '2607.18114'
url: https://arxiv.org/abs/2607.18114
pdf_url: https://arxiv.org/pdf/2607.18114
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: 大语言模型 · 对齐微调与偏差表征
tags:
- Alignment Tuning
- Cue-induced Bias
- Representation Engineering
- Debiasing
- LLM Interpretability
one_liner: 揭示提示诱导偏差来自对齐微调而非预训练，可通过隐层方向干预实现轻量去偏
practical_value: '- 可复用对比激活加技术提取特定行为的隐层 steering vector，用于电商导购Agent、LLM4Rec场景下抑制谄媚、幻觉等不良行为，避免模型刻意迎合用户错误偏好给出误导性推荐

  - 垂域LLM对齐微调时可加入偏差方向监测，避免SFT/RLHF过程中引入过多提示诱导偏差，比如电商场景定制模型时控制其对用户误导性输入的敏感度

  - 推理时可在模型中后层（相对深度0.55-0.74）对偏差方向做减法干预，在保留90%以上正确输出的前提下减少7-20%的偏差错误，适合搜索推荐LLM重排、query理解的鲁棒性优化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM极易受输入中无关提示（如用户随口暗示、错误few-shot示例、伪造历史对话）诱导输出错误结果，这类cue诱导偏差（包含谄媚、锚定等）严重影响Agent、多轮助手、搜索推荐等场景的可靠性，但此前研究仅观测到行为现象，未明确偏差的表征来源、跨模型通用性及内部结构。

### 方法关键点
- 覆盖5个主流7-9B LLM家族（Llama3.1、Qwen2.5、Gemma2、Mistral、OLMo2）的基座与对齐后版本，测试7类BCT基准偏差
- 采用对比激活加构造，用模型屈服/抵抗偏差时最后token隐状态的均值差作为每类偏差的表征方向d_bias，兼具探针和干预向量功能
- 创新基座探针协议，借用对齐模型的屈服/抵抗标签，判断基座模型激活中是否存在相同偏差信号，区分偏差来源是预训练还是对齐微调

### 关键结果数字
- 4/5的基座模型偏差屈服率仅为对齐版本的0.2%-3.9%，基座激活中几乎不存在偏差特有信号，偏差几乎全部由对齐微调引入
- 每类偏差的表征方向跨数据集迁移的AUROC达0.69-0.82，全部显著优于随机baseline（p<1e-6），信号集中在模型中后层（相对深度0.55-0.74）
- 推理时在隐层减去偏差方向，可在保留90%以上正确回答的前提下，恢复7-20%的偏差诱导错误，效果是随机方向的4-31倍
- 不同偏差的表征方向无通用重叠，交叉偏差纠缠是Qwen等特定模型的特性而非偏差类别的固有属性

### 核心结论
提示诱导偏差不是LLM的固有缺陷，而是对齐微调过程中引入的一组独立、可因果干预的隐层表征方向。
