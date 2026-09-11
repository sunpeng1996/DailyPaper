---
title: Thinking with Looped Flows
title_zh: 循环流：可扩展的稳定循环推理框架
authors:
- Ayhan Suleymanzade
- Chanhyuk Lee
- Floor Eijkelboom
- Nicholas M. Boffi
- İsmail İlkan Ceylan
- Jinwoo Kim
affiliations:
- EPFL
- KAIST
- University of Amsterdam
- Carnegie Mellon University
- TU Wien
arxiv_id: '2609.11801'
url: https://arxiv.org/abs/2609.11801
pdf_url: https://arxiv.org/pdf/2609.11801
published: '2026-09-10'
collected: '2026-09-11'
category: Reasoning
direction: 循环推理 · 流模型训练优化
tags:
- Looped Model
- Flow Model
- Denoising Objective
- Recurrent Reasoning
- Inference Scaling
one_liner: 融合流模型与循环架构，通过局部去噪目标训练循环推理模型，实现性能随推理计算量稳定提升
practical_value: '- 循环模型训练可复用局部去噪+梯度截断方案，解决长序列循环训练的梯度消失/爆炸问题，大幅降低训练成本，适配推荐系统用户长序列建模、Agent多轮推理等场景

  - 推理侧可通过调整时间网格粒度灵活权衡效果与耗时，对电商搜索推荐的不同等级请求做动态调度：低优请求增加步长提升效果，高优请求减少步长保障 latency

  - 多解场景（如电商文案生成、多候选推荐）可复用概率流+随机积分方案，无需修改训练逻辑即可生成多样化合规结果，提升推荐多样性、文案转化率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统循环推理模型依赖截断反向传播时间（BPTT）训练，梯度仅能覆盖少量循环步，无法让早期迭代为后续计算传递有效信息，易出现不稳定收敛、伪吸引子等问题，同时推理时无法通过增加计算量线性提升效果，难以适配复杂推理场景的动态算力调度需求。
### 方法关键点
- 训练阶段：给循环去噪器设计逐级降低噪声的局部去噪目标，跨步共享同一份噪声和真实标签做时序对齐，配合梯度截断避免全量BPTT的高成本与梯度不稳定问题，加入自适应计算时间（ACT）机制，准确率饱和后自动终止后续步训练，减少过拟合。
- 推理阶段：将去噪器输出的速度场结合循环状态做概率流积分，支持通过调整时间网格粒度直接增减推理步，灵活权衡效果与耗时；可选随机SDE积分方案生成多组有效解，通过ACT头做集成选优进一步提升精度。
### 关键实验
在数独、迷宫、ARC-AGI等6个推理基准上测试，对比TRM、FPRM、GRAM等SOTA循环模型：单轨迹下ARC-AGI-1准确率从44.6%提升到58.8%，ARC-AGI-2从7.8%提升到12.2%，数独准确率达97.9%，解决了90.9%的传统循环模型失效案例；仅用5个轨迹集成即可超过基线用上百个轨迹的效果，推理步从8提升到128时，数独准确率从74.5%线性提升到97.9%。
最值得记住的结论：通过流动匹配的局部去噪目标做时序对齐，可让截断梯度训练的循环模型学习到全局有效的递推状态，实现推理效果与计算量的正向可扩展。
