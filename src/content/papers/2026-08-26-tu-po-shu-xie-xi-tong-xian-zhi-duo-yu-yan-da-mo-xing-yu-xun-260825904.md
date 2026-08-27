---
title: 'One Form to Transfer Them All: Pretraining Multilingual Language Models Beyond
  Native Orthography'
title_zh: 突破书写系统限制：多语言大模型预训练的输入表示对比研究
authors:
- Muge Zhang
- Aaron Jencks
- Krishna Badikela
- Yulia Tsvetkov
- Sachin Kumar
affiliations:
- Ohio State University
- Paul G. Allen School of Computer Science & Engineering, University of Washington
arxiv_id: '2608.25904'
url: https://arxiv.org/abs/2608.25904
pdf_url: https://arxiv.org/pdf/2608.25904
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 多语言LLM预训练 · 跨书写系统迁移
tags:
- Multilingual-LLM
- Cross-lingual-Transfer
- Romanization
- IPA
- Autoregressive-Pretraining
one_liner: 系统对比三类输入表示在多语言自回归预训练的效果，证实预训练阶段引入罗马化跨语言迁移最优
practical_value: '- 跨境电商多语言搜索/意图识别场景：针对覆盖多书写系统的小语种，可在预训练阶段直接用Uroman做罗马化处理，比下游微调效果更好，还能降低非拉丁语言的token长度，减少推理成本

  - 语音+多模态跨境推荐场景：对印地语-乌尔都语这类语音高度接近、书写完全不同的语言，可引入IPA表示作为补充特征，提升跨语言迁移效果

  - 基于现有多语言LLM的业务迭代：不要随意对原生文字预训练的多语言基座做罗马化微调，仅当基座完全未覆盖目标书写系统时，该操作才会带来小幅收益

  - 多语言客服Agent选型：优先选择预训练阶段已做罗马化处理的多语言基座，跨小语种迁移的落地成本更低、效果更稳定'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言大模型的跨语言迁移高度依赖词汇重叠，使用不同书写系统的近缘语言（如印地语与乌尔都语）几乎无词汇重叠，迁移效果极差；此前的脚本均衡方案多针对编码器模型，或仅在下游微调阶段引入，缺乏对主流自回归模型的系统对比验证。

### 方法关键点
- 对比4种输入方案：原生文字、IPA（去除重音、长度标记等提升跨语言重叠）、Uroman罗马化，以及原生文字预训练后罗马化微调的对照组
- 训练3个规模的自回归模型：467M、709M、1.03B参数，全程控制架构、数据、词表大小、训练流程完全一致，消除无关变量干扰
- 训练数据覆盖4组典型语言对：英-西（同拉丁脚本）、俄-波（不同脚本同语系）、印地-乌尔都（不同脚本语音几乎一致）、泰米尔-马拉雅拉姆（不同脚本同语系），总词量217亿

### 关键实验结果
- 下游任务覆盖XNLI推理、MASSIVE意图分类、XL-Sum摘要，同时测试见过和未见过的语言，罗马化预训练在所有任务、所有模型规模下效果最优
- 大模型规模下，罗马化预训练在未见过的语言上MASSIVE任务Macro F1达70.42%，比原生文字预训练高9个百分点
- IPA仅在印地-乌尔都语对上和罗马化效果相当，其余场景均落后于罗马化
- 原生预训练后罗马化微调会使已覆盖语言的F1最高下降24.5个百分点，仅对基座完全未覆盖的书写系统有小幅提升

### 核心结论
对于需要优先保障跨未知书写系统迁移能力的多语言模型，罗马化应作为预训练阶段的核心设计选择，而非下游临时修复方案
