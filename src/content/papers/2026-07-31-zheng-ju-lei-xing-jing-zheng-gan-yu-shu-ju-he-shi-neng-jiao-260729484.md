---
title: 'Evidence-Type Competition: When Can Interventional Data Teach Language Models
  Causal Direction?'
title_zh: 证据类型竞争：干预数据何时能教会大语言模型因果方向
authors:
- Xining Xun
affiliations:
- Tsingjiao Information Science (Beijing) Co., Ltd.
arxiv_id: '2607.29484'
url: https://arxiv.org/abs/2607.29484
pdf_url: https://arxiv.org/pdf/2607.29484
published: '2026-07-31'
collected: '2026-08-03'
category: Reasoning
direction: 大语言模型 · 因果推理机制研究
tags:
- Causal Reasoning
- Interventional Data
- LLM
- Simpson's Paradox
- Activation Patching
one_liner: 发现LLM因果能力由推理上下文证据类型而非训练干预占比决定，定位了开关对应模型层
practical_value: '- 搭建营销归因、预算分配类因果决策Agent时，推理prompt需优先放置干预类证据，避免观测数据的辛普森悖论导致决策方向完全反转

  - 评估业务场景下LLM的因果能力时，可采用证据平均协议，将符号类错误从26%降至9%，提升评估准确性

  - 若需要LLM输出稳定因果结论，可在prompt预处理阶段擦除无关观测类关联数据，释放模型已学习的因果插值能力，准确率可提升0.56'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
业界普遍默认干预数据是训练LLM因果推理能力的金标准，该假设未在观测关联与因果效应符号相反的辛普森悖论场景下经过严格验证。
### 方法关键点
在全控合成环境中对照测试不同训练干预数据占比、不同推理上下文证据类型下LLM的do()响应表现，结合激活补丁、内容操纵定位因果开关的层级位置。
### 关键结果数字
训练时干预样本占比仅提升因果响应幅度，不改变响应符号，符号完全照搬推理上下文的观测关联；纯观测上下文下29/50场景出现系统性符号反转，混合上下文反转19/50，仅用干预探针时41/50正确；擦除上下文观测证据后因果准确率提升0.56，证据平均协议可将符号错误从26%降至9%；因果能力存储在模型权重中，开关位于模型中层的观测对应行，0.93B参数下该抑制效应仍稳定存在
