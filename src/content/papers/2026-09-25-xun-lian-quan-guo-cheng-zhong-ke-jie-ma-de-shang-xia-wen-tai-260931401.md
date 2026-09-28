---
title: Decodable In-Context State and Model Output Across Training
title_zh: 训练全过程中可解码的上下文状态与模型输出
authors:
- Manas Venkata Sai Ravulapalli
- Samrath Singh Chadha
affiliations:
- Efficient Computation Inc.
arxiv_id: '2609.31401'
url: https://arxiv.org/abs/2609.31401
pdf_url: https://arxiv.org/pdf/2609.31401
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM可解释性 · 探针解码与模型干预
tags:
- Probe Decoding
- In-Context Learning
- Model Steering
- LLM Interpretability
- Pretraining
one_liner: 追踪LLM全训练阶段探针解码精度与干预效果变化，澄清可解码性相关认知误区
practical_value: '- 搭建LLM驱动的推荐/Agent系统时，可在训练各阶段插入探针监控上下文绑定正确性，提前定位ICL失效问题

  - 探针引导干预收益随训练阶段提升，可在SFT/RLHF阶段引入探针引导修复推理错误，降低bad case率

  - 不要仅靠错误样本的探针可解码性判定模型是否丢失正确输出信息，需结合logits对比验证避免误判'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
过往研究证明探针可从LLM隐藏态解码正确上下文绑定、引导修复模型错误，但未明确训练全过程中探针精度、干预效果的变化规律，也未澄清可解码性与模型输出信息的关联。

### 方法关键点
1. 横跨Pythia系列模型预训练、后训练全阶段checkpoint，追踪探针精度、模型输出、引导干预响应的变化趋势
2. 对比基于最终隐藏态、候选logits训练的解码器效果差异，构造信息论反例验证可解码性的认知误区

### 关键结果数字
- 探针精度随Pythia预训练过程持续上升，探针引导干预收益从可忽略提升至两种模型尺寸下均有显著效果
- 基于最终态训练的解码器对比logits解码器，在后期checkpoint错误样本上无明显性能优势
- 错误样本的探针可解码性无法单独证明模型未丢弃正确输出信息
