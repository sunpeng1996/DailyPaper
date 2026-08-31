---
title: 'Nested Byte-Level Vocabularies Are Cheap to Deploy and Expensive to Share:
  A Pre-Registered Negative Result'
title_zh: 嵌套字节级词表部署成本低但共享效果差：预注册负结果研究
authors:
- Christos Koutsiaris
affiliations:
- SAP
arxiv_id: '2608.28151'
url: https://arxiv.org/abs/2608.28151
pdf_url: https://arxiv.org/pdf/2608.28151
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: LLM tokenizer · 多粒度训练优化
tags:
- Tokenizer
- BPE
- Nested Vocabulary
- LLM Training
- Regularization
- Negative Result
one_liner: 验证嵌套字节BPE词表部署可行性，量化其多粒度共享训练的效果损失与抗噪收益
practical_value: '- 多粒度tokenizer部署场景可直接复用嵌套BPE+模型切片方案，切到2k词表能减66%权重，无精度损失、无latency上涨

  - 训练阶段不要对输出头加子词表mask约束，实测会提升0.47%~1.19%的BPB损失，反而降低模型效果

  - 需提升LLM对用户拼写错误、query噪声的鲁棒性时，可加入多粒度词表训练正则，无需额外控制token就能获得12.5~15.4%的抗噪提升，跨粒度场景效果优于BPE-dropout

  - 做多粒度共享模型训练时，每个粒度的训练数据占比要匹配业务需求，占比越低效果损失越大，不要采用统一的总token预算'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统BPE词表大小固定，粗粒度推理速度快但字符级信息损失大，细粒度语义精度高但序列更长推理成本高，不同场景通常需要独立训练多个模型。嵌套字节级BPE天然支持前缀截断得到多粒度词表，理论上可训练一个共享模型适配所有粒度，通过切片部署大幅降低工程成本，但其效果代价此前未被系统验证。
### 方法关键点
- 训练单份最大32k vocab的字节BPE词表，截断得到2k、8k、32k三个嵌套粒度，所有粒度的token id完全对齐前缀
- 设计2×2消融实验，隔离「粒度控制token」「输出头词表mask」两个变量的影响，所有模型固定种子、初始化、数据顺序保证对比公平
- 采用bits-per-byte（BPB）作为核心评价指标，避免跨词表的perplexity对比偏差
### 关键实验
基于FineWeb-Edu数据集训练30个3.1M/10.6M参数量的decoder-only模型，与固定粒度的专家模型对比：
1. 共享多粒度模型比32k专家模型BPB高3.64%，比8k专家模型高2.96%，远超预设的1%/2%可接受阈值
2. 模型切片部署完全无损，切到2k粒度可减少66%权重，latency无显著变化
3. 多粒度训练的模型在拼写噪声下的效果下降比专家模型少12.5~15.4个百分点，噪声场景下效果甚至超过对应粒度的专家模型，且该收益无需控制token即可获得
### 核心结论
嵌套词表的工程价值成立但建模价值不成立，多粒度训练的抗噪收益源于数据增强而非条件控制，模型可自行推断的控制token不会带来额外效果收益
