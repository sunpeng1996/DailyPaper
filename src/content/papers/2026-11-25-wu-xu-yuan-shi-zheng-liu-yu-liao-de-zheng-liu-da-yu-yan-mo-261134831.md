---
title: Repairing the Trustworthiness of Distilled Language Models
title_zh: 无需原始蒸馏语料的蒸馏大语言模型可信度修复框架
authors:
- Kumar Shubham
- Devendra Vyas
- Vidushi Agarwal
- Jayin Khanna
- Prathosh AP
affiliations:
- Indian Institute of Science, Bengaluru
- Independent Researcher
arxiv_id: '2611.34831'
url: https://arxiv.org/abs/2611.34831
pdf_url: https://arxiv.org/pdf/2611.34831
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM蒸馏优化 · 可信度后处理
tags:
- Knowledge Distillation
- Trustworthiness
- LLM Alignment
- Preference Optimization
- Model Repair
one_liner: 提出无需原始蒸馏语料的蒸馏LLM可信度修复框架，保下游性能的同时最高提升8%可信度
practical_value: '- 业务中使用蒸馏小LLM做电商文案生成、客服应答、推荐理由生成时，可直接复用该框架修复幻觉、合规性问题，无需原始蒸馏语料，仅带来<1%的性能损失

  - 偏好损失设计（SFT损失+ORPO对数优势比损失结合）可直接复用在所有需要对齐业务规范的小模型微调场景，同时提升合规回答概率、抑制违规回答生成

  - 用通用代理数据集计算EK-FAC曲率做正则的思路，可迁移到所有需要微调时保留模型原有核心能力的场景，如给推荐场景定制LLM加合规能力无需原始训练数据'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
知识蒸馏是大模型落地低资源、端侧场景的核心方案，但蒸馏过程常导致小模型可信度（事实准确性、伦理合规性）下降，且厂商发布的蒸馏模型大多不公开原始蒸馏语料，直接做偏好优化又会破坏模型原有下游性能，现有修复方案均依赖原始训练数据，无法适配已上线蒸馏模型的后处理需求。

### 方法关键点
- 放弃对原始蒸馏语料的依赖，改用通用代理数据集估计PBRF框架所需的曲率信息，通过正则约束模型参数和输出分布的变动幅度，保证原有性能不下降
- 结合ORPO的对数优势比目标设计偏好损失，同时提升合规回答的概率、抑制违规回答的生成，适配可信度优化常用的好坏回答对标注数据
- 用EK-FAC近似逆高斯牛顿矩阵的向量乘积，把修复计算成本降到可适配1.2B级大模型的水平

### 关键实验
在GPT-2系列（120M-760M）、Qwen系列（200M-1.2B）蒸馏模型上验证，用TruthfulQA、常识伦理数据集做可信度评估，对比原始蒸馏模型：机器伦理维度最高提升8.55%，事实性维度最高提升6.1%；所有场景下perplexity下降幅度最大为1.56%，90%以上场景下降<1%，部分场景甚至略有提升；代理数据集选择对结果影响极小，通用公开语料即可满足需求。

### 核心结论
蒸馏小模型的可信度退化无需重新蒸馏，用少量偏好标注+通用代理数据做正则化微调即可在几乎不损失性能的前提下完成修复
