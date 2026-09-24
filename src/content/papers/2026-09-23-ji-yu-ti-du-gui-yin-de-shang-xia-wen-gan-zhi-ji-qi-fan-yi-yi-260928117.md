---
title: Scaling Attention Head Analysis via Gradient-Based Attribution in Context-Aware
  Machine Translation
title_zh: 基于梯度归因的上下文感知机器翻译注意力头规模化分析
authors:
- Paweł Mąka
- Yusuf Can Semerci
- Jan Scholtes
- Gerasimos Spanakis
affiliations:
- Maastricht University
- Department of Advanced Computing Sciences
arxiv_id: '2609.28117'
url: https://arxiv.org/abs/2609.28117
pdf_url: https://arxiv.org/pdf/2609.28117
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM可解释性 · 注意力头功能分析
tags:
- Attention Head
- Interpretability
- Gradient Attribution
- LLM
- Machine Translation
one_liner: 提出梯度驱动的注意力头归因框架，可规模化分析LLM注意力头，验证通用头存在与功能冗余性
practical_value: '- 做LLM4Rec/Agent推理加速时，可复用该归因方法识别冗余注意力头做剪枝，降低推理延迟

  - 微调电商/广告垂直领域LLM时，可通过该方法定位通用功能头，固定通用头仅微调专用头降低训练成本

  - 分析RAG/生成式推荐的LLM注意力分布时，可用该梯度归因方法验证注意力是否落在关键语义片段上，提升结果可解释性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
大模型参数规模激增，注意力头内部功能可解释性分析难度高，现有方法无法支持大规模LLM的注意力头因果分析，难以高效定位头的功能价值与冗余性。
### 方法关键点
提出基于梯度的注意力头归因策略，将Token-level Max-Margin损失反向传播到注意力图，构建可规模化的注意力头因果分析框架，适配大模型场景。
### 关键结果
1. 在上下文感知机器翻译消歧任务上，跨4个模型、4个语言方向分析50种语言现象，在3模型2语言方向上验证了方法鲁棒性
2. 发现存在"通用型"注意力头，关注不同关系时均能提升模型性能
3. 注意力头对特定关系的平均注意力权重与模型性能无强关联，证明训练过程会产生头功能冗余
