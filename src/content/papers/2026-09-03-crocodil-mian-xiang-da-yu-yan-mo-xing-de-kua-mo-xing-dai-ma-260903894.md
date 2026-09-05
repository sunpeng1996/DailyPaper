---
title: 'CROCODIL: Cross-Model Code Editing with LLMs'
title_zh: CROCODIL：面向大语言模型的跨模型代码编辑框架
authors:
- Linghan Zhong
- Aditya Thimmaiah
- Jayanth Srinivasa
- Milos Gligoric
- Junyi Jessy Li
affiliations:
- The University of Texas at Austin
- Cisco Research
arxiv_id: '2609.03894'
url: https://arxiv.org/abs/2609.03894
pdf_url: https://arxiv.org/pdf/2609.03894
published: '2026-09-03'
collected: '2026-09-05'
category: LLM
direction: LLM代码编辑 · 后训练对齐优化
tags:
- LLM
- Code Editing
- Post-training
- Reward Engineering
- Alignment
one_liner: 提出双奖励驱动的后训练框架，解决多LLM混用场景下代码跨模型编辑的过度修改问题
practical_value: '- 多LLM/多Agent协作场景（如多Agent生成商品文案、推荐话术）可复用「相似度奖励+任务正确性奖励」的双奖励组合，解决不同模型输出风格不统一导致的过度修改问题

  - 对齐阶段采用奖励乘积而非加权和优化，可同时兼顾多目标约束避免单目标倾斜，可复用到生成式推荐场景，同时保障生成内容相关性和合规性

  - 跨模型输出风格适配无需重新预训练，仅通过后训练对齐即可优化，可降低多LLM混合部署的迭代成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
开发团队多LLM助手混用已成常态，不同LLM训练数据差异导致编码风格偏好不同，编辑其他LLM生成的「异源代码」时普遍存在过度修改问题，既降低开发效率，也可能引入非必要功能风险。

### 方法关键点
1. 提出后训练框架CROCODIL，无需改动LLM预训练权重，仅通过后训练对齐优化跨模型编辑效果
2. 设计双奖励机制：相似度奖励惩罚过大修改，抑制无意义风格调整；执行奖励基于构建、测试通过率打分，保障功能正确性
3. 采用两个奖励的乘积作为优化目标，驱动策略在不降低编辑任务成功率的前提下最小化编辑量

### 关键结果
可大幅降低跨模型代码编辑的过度修改比例，同时完全保留原有功能正确性，相关代码已开源。
