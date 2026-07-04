---
title: On the Role of Directionality in Structural Generalization
title_zh: 结构泛化中的方向性作用研究
authors:
- Zichao Wei
affiliations:
- Saarland University
arxiv_id: '2607.02307'
url: https://arxiv.org/abs/2607.02307
pdf_url: https://arxiv.org/pdf/2607.02307
published: '2026-07-02'
collected: '2026-07-04'
category: Reasoning
direction: 神经符号语义解析 · 结构泛化
tags:
- Structural Generalization
- Semantic Parsing
- CCG
- Neuro-Symbolic
- SLOG
one_liner: 采用带方向的CCG类型重构符号解析后端，在SLOG结构泛化基准上超越原有SOTA，验证模块增益互补性
practical_value: '- 做用户Query理解/改写时，可引入CCG方向类型编码语序特征，解决修饰词移位、论元位置变化带来的解析错误，提升Query语义匹配准确率

  - 神经符号混合架构可分场景优化：语序敏感任务优先优化符号层方向编码，递归深度敏感任务优先升级预训练编码器，二者增益互补

  - 仅30K参数的轻量符号层可作为大模型语义解析插件，无需全量微调即可快速提升特定结构场景的泛化能力'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
SLOG结构泛化基准包含5类依赖语序方向区分的测试任务，但此前SOTA AM-Parser采用的AM代数运算未编码方向信息，在位置偏移类任务上存在固有性能天花板。
### 方法关键点
基于CCG方向类型重构符号后端，采用确定性CKY算法+单线性解码器，仅30K可学习参数，搭配预训练编码器组成轻量神经符号解析系统。
### 关键结果数字
- 同BERT-base编码器下，LF精确匹配达75.9±6.4%，超AM-Parser的70.8±4.3%
- 5类位置偏移任务上领先AM-Parser 29.9pp，仅在6类递归深度任务上表现稍弱
- 更换DeBERTa-v3-large编码器后整体精度达90.7±4.9%，编码器升级可补足递归深度任务短板，与方向编码增益完全互补
