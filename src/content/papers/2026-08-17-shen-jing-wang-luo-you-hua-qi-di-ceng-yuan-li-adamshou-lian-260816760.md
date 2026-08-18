---
title: On the Principles Behind Neural Network Optimizers
title_zh: 神经网络优化器底层原理：Adam收敛性、结构洞察与Adam-mini设计
authors:
- Yushun Zhang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2608.16760'
url: https://arxiv.org/abs/2608.16760
pdf_url: https://arxiv.org/pdf/2608.16760
published: '2026-08-17'
collected: '2026-08-18'
category: Training
direction: 大模型训练 · 优化器理论与设计
tags:
- Adam
- Optimizer
- LLM Training
- Hessian
- Memory Efficiency
one_liner: 从理论层面解释Adam收敛性与Transformer适配性，提出显存减半的Adam-mini优化器
practical_value: '- 训练垂类小LLM/推荐场景Transformer模型时，小batch场景可将β2从0.95提升至0.999，避免Adam发散、稳定训练

  - 训练大参数量推荐/多模态模型时，可直接复用Adam-mini，显存占用降50%且不损失效果，降低训练成本

  - 尝试Muon优化器训练大模型时，采用Head-wise Muon设计适配Attention的Hessian块结构，提升训练效率

  - 调参时β2无需盲目调大，超过batch size对应阈值后，进一步提升β2可能反而降低训练效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Adam是LLM与Transformer类模型的默认优化器，但长期存在收敛性理论争议，且其在Transformer上效果远优于SGD的底层原因不清晰；大模型训练成本极高，优化器的稳定性、效率优化空间大，亟需理论指导与低成本落地方案。

### 方法关键点
- 论证Adam存在依赖batch size的收敛-发散相变：固定任务下β2大于batch size对应阈值即可保证收敛，无需修改更新规则
- 从Hessian结构层面解释Adam适配Transformer的原因：Transformer训练过程中Hessian会演化为准块对角结构，且块间异质性强，Adam的对角预条件正好适配该结构
- 基于结构洞察提出Adam-mini：无需维护每个参数的二阶动量，仅按参数块（对应Hessian块）维护学习率，大幅降低显存占用

### 关键结果数字
- Adam-mini在Transformer、CV等任务上效果与原版Adam完全对齐，显存占用降低50%
- Head-wise Muon设计已被DeepSeek、Kimi K3等大模型训练采用，验证了结构洞察的有效性
- 小batch训练LLM时，将β2从0.95提升到0.999可显著提升训练稳定性，该结论已被多项工业界训练实践验证

最值得记住的一句话：优化器的表现高度绑定神经网络的内在结构特征，而非通用理论推导的普适结论，针对特定模型结构做优化器适配可获得效率与效果的双重收益。
