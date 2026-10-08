---
title: 'A Good Self-Teacher Meets the Student Where They Are: Joint On-Policy Learning
  and Teaching'
title_zh: 联合同策略学习与教学（JOLT）：适配学生能力的自蒸馏训练框架
authors:
- Randy Ardywibowo
- Arnav Dalal
- Jiantao Jiao
affiliations:
- Perplexity
- NVIDIA
arxiv_id: '2610.10447'
url: https://arxiv.org/abs/2610.10447
pdf_url: https://arxiv.org/pdf/2610.10447
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM训练 · 同策略自蒸馏优化
tags:
- On-Policy Distillation
- Self-Distillation
- Reinforcement Learning
- Knowledge Distillation
- LLM Training
one_liner: 联合训练同一模型的特权教师与无特权学生角色，提升RL训练效率与多类任务性能
practical_value: '- 训练电商导购/客服Agent、生成式推荐文案模型时，可复用双角色设计：用带特权信息（历史正确工单、商品知识库）的教师角色生成稠密监督信号，降低对稀疏最终奖励的依赖，减少训练标注成本

  - 做模型蒸馏时可引入教师-学生token级KL正则约束，避免特权信息导致的教师生成内容脱离学生当前能力，解决蒸馏监督信号不匹配导致的性能下降问题

  - 计算资源有限的中小模型迭代场景可优先复用JOLT范式：在推理类任务上可比GRPO少用13× completion tokens、6.5×训练token达到相同精度，大幅缩短训练周期'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于结果奖励的RL存在监督稀疏问题，在长周期Agent、复杂推理任务上成功轨迹少、生成成本高；同策略自蒸馏（OPSD）虽可通过特权信息生成稠密监督，但教师常利用学生没有的信息走捷径，生成的监督信号与学生当前能力不匹配，反而会降低学生性能，亟需适配学生能力的蒸馏训练框架。

### 方法关键点
- 推导得到奖励一致性教师的充要条件：教师的局部蒸馏更新需与学生的奖励梯度正相关，要求教师在性能优异的同时与学生当前策略保持接近
- 设计JOLT框架：同一套参数共享教师和学生双角色，教师接收特权信息，训练目标结合结果奖励与向学生对齐的token级KL正则；学生无特权信息，接收教师的稠密同策略蒸馏信号
- JOLT+扩展：在学生侧额外加入结果奖励监督，同时兼顾稠密蒸馏信号与稀疏结果反馈

### 关键结果
在数学推理、代码生成、工具使用、终端Agent四类任务上对比GRPO、OPSD、π-Distill基线，JOLT+较GRPO在MATH上绝对提升4.2%、LCBv6提升3.0%、AppWorld提升9.9%、Terminal-Bench pass@32提升4.5%；无学生直接奖励时，JOLT在MATH上用13×更少的生成token、6.5×更少的训练token即可达到与GRPO相同精度。

最值得记住的一句话：好的自教师要适配学生的当前能力，而非单纯追求自身性能最优。
