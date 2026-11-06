---
title: '$D^2$-OPD: Separating Direction and Distance in Extrapolative On-Policy Distillation'
title_zh: 《D²-OPD：解耦外推式 on-policy 蒸馏的方向与距离》
authors:
- Bowen Fang
- Dingmin Wang
- Hengzhi Pei
affiliations:
- Columbia University
- AWS AI Lab
- Amazon AGI
arxiv_id: '2611.07241'
url: https://arxiv.org/abs/2611.07241
pdf_url: https://arxiv.org/pdf/2611.07241
published: '2026-11-04'
collected: '2026-11-06'
category: Training
direction: LLM 知识蒸馏 · on-policy 训练优化
tags:
- Knowledge-Distillation
- On-Policy-Training
- LLM-Optimization
- Extrapolative-Distillation
- Mathematical-Reasoning
one_liner: 解耦外推式 on-policy 蒸馏的方向与距离，在数学推理任务上大幅超越现有蒸馏SOTA
practical_value: '- 电商/推荐场景下做域内大模型→小模型蒸馏时，可复用D²-OPD的硬KL约束设计，限定蒸馏目标和教师模型的分布距离，避免外推过度引入无关token，减少生成式推荐的输出乱码/无关内容问题

  - 蒸馏方向无需人工固定参考，可自适应结合教师后训练偏移、初始师生差距两个信号加权，适配不同蒸馏阶段的分布对齐需求，降低超参数调优成本

  - 冷启动蒸馏场景（比如小模型base版直接蒸馏大模型SFT版）可替换reverse KL为forward KL损失，给学生低概率token保留非零梯度，解决师生初始分布重叠低导致的蒸馏失效问题，无需额外SFT预训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有外推式On-Policy Distillation（OPD）方法耦合外推方向与距离，固定系数下不同prefix的外推距离波动极大，容易给教师低概率token分配过高权重，导致蒸馏不稳定、效果退化，甚至出现响应长度异常膨胀的问题；同时师生初始分布重叠度低的冷启动场景下，传统reverse KL损失梯度消失，蒸馏基本失效。
### 方法关键点
- 解耦外推方向与距离：每个prefix设置硬KL约束，限定蒸馏目标和归一化教师top-K分布的距离上限，从机制上避免外推过度引入噪声
- 自适应方向构造：结合教师后训练偏移量、初始师生差距两个信号，按信号方差自适应加权，给更近的参考信号分配更高权重，无需人工固定单一参考
- 采用forward KL作为蒸馏损失，针对学生低生成概率的token保留非零梯度，同时增加概率质量转移项，引导学生分布向教师top-K token集对齐
### 关键实验结果
基于Qwen3系列3组师生蒸馏场景测试，评估集为AIME24、AIME25、AMC23数学推理benchmark，对比OPD、ExOPD、Direct-OPD等6个SOTA基线：8B→4B-Base蒸馏场景下平均得分47.19，比标准OPD高19.62点，比最强基线TOP-D高9.45点；冷启动蒸馏场景（4B→1.7B-Base）下无需SFT预训练，得分比SFT+OPD方案高1.51点；单步训练耗时仅比标准OPD高15%，工程 overhead 极低。
### 核心结论
外推式蒸馏的核心是在可信范围内沿最优方向移动，而非无限制偏离教师模型，才能兼顾训练稳定性和效果收益。
