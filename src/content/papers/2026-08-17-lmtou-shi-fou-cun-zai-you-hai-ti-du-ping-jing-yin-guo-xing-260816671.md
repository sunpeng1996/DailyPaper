---
title: Does the LM Head Create a Harmful Gradient Bottleneck? A Causal Test
title_zh: LM头是否存在有害梯度瓶颈：因果性验证研究
authors:
- Anand Murugan
arxiv_id: '2608.16671'
url: https://arxiv.org/abs/2608.16671
pdf_url: https://arxiv.org/pdf/2608.16671
published: '2026-08-17'
collected: '2026-08-18'
category: Training
direction: 大语言模型训练 · 梯度瓶颈验证
tags:
- LM Head
- Gradient Bottleneck
- Backpropagation
- Causal Test
- Language Model Training
one_liner: 通过严格因果对照实验验证LM头梯度压缩真实但未构成有害优化瓶颈
practical_value: '- 微调LLM4Rec、电商文案生成、query改写等垂直场景模型时，无需额外设计LM头反向反馈路径，调优后的标准反传性能优于所有测试的辅助路径

  - 训练领域小模型时无需刻意压缩词表规避所谓梯度瓶颈，仅增加无目标输出类别不会显著降低训练效果

  - 设计合成评测任务（比如个性化生成、召回排序仿真任务）时，需严格控制独立采样样本量，不能将重复token计数等同于独立样本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
此前研究提出LM头将D维隐状态映射到V维词表时，反传路径最多只能传回D维梯度，95%~99%的logit梯度范数会被丢弃，属于有害优化瓶颈。但该结论混淆了客观几何现象和因果影响，缺乏严格的隔离对照验证，无法明确损失是来自反向梯度限制还是前向解码器本身的改动。
### 方法关键点
- 设计三类严格对照实验：普通全秩头+精确梯度（基准）、普通全秩头+低秩反向梯度（仅隔离反向路径秩的影响）、低秩头+精确梯度（同时改动前向后向），确保前向计算和LM头参数更新逻辑不变
- 补充多组控制实验：验证logit正交残差对LM头更新的作用、SpamLang合成任务的混淆变量、词表大小的独立影响、梯度投影指标的学习预测性、多种辅助反馈路径的优化效果
### 关键结果
实验基于WikiText-2数据集，分别在字节级4层隐宽32小模型、BPE-8192的6层隐宽96模型上跑5组配对种子：
1. 大模型半秩场景下，仅降低反向梯度秩使验证损失增加0.0586（95% CI [0.0167, 0.1005]），而降低前向头秩使损失增加0.1795（95% CI [0.1547, 0.2042]）
2. 移除LM头更新中的正交残差分量，验证损失大幅提升0.6252
3. 词表V/D扩大16倍无显著性能下降，所有测试的辅助反馈路径均未超过调优后的标准反传效果

LM头的梯度压缩是真实的几何现象，但尚未被证明会丢弃有用学习信息、成为LLM优化的有害瓶颈。
