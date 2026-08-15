---
title: 'Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage
  in Document MLLMs'
title_zh: 超越视觉证据：文档多模态大模型关系隐私泄露的揭示与缓解
authors:
- Beining Xu
- Hairui Wang
- Jiaxin Wang
- Changsheng Chen
- Anirban Chakraborty
affiliations:
- Shenzhen MSU-BIT University
- Indian Institute of Science
arxiv_id: '2608.12911'
url: https://arxiv.org/abs/2608.12911
pdf_url: https://arxiv.org/pdf/2608.12911
published: '2026-08-13'
collected: '2026-08-15'
category: LLM
direction: 多模态大模型 · 隐私保护与去学习
tags:
- MLLM
- Privacy Leakage
- Unlearning
- Document Understanding
- KIE
one_liner: 揭示文档MLLM弱视觉证据下的关系隐私泄露问题，提出动态关系去学习框架及专用评测基准
practical_value: '- 电商/支付场景下的文档KIE MLLM可直接复用DRUF框架，在保留提取准确率的前提下降低敏感字段关联泄露风险

  - 涉及用户敏感信息的多模态模型上线前，可参考DocPrivacyBench的构造思路，补充弱视觉证据下的隐私泄露评测环节

  - 关系解耦去学习RDU模块的设计思路可迁移到推荐系统用户敏感属性关联记忆的擦除场景，避免多维度隐私泄露'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有MLLM隐私研究多聚焦通用场景，面向身份证等文档处理的领域MLLM的关系隐私泄露风险未被充分挖掘，输入视觉证据不足时，模型会依赖训练中记忆的字段关联推断缺失内容，导致多维度敏感信息共同泄露。

### 方法关键点
1. 动态关系去学习框架DRUF，包含关系解耦去学习RDU模块和动态集合更新机制，抑制高风险字段对泄露的同时保留KIE性能
2. 构建DocPrivacyBench基准，可系统评测模型在视觉证据缺失/极少场景下的隐私泄露风险
3. 基于该基准完成3种MLLM、6种去学习方法的泄露抑制效果与性能保留水平测评

### 关键结果数字
现有MLLM在视觉证据不足时普遍存在隐私泄露，数据集噪声越高泄露越严重；DRUF相比最强基线的泄露抑制效果提升4.8个百分点，同时保持稳定的文档信息提取性能
