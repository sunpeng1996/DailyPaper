---
title: Can We Trust the Teacher? Decoupled Credit Direction-Magnitude for Self-Distillation
title_zh: 解耦自蒸馏中信贷方向与幅度 解决教师信号不可靠问题
authors:
- Yugu Li
- Zehong Cao
- Peizhen Li
- Yang Zhang
- Siyi Hu
- Jianglin Qiao
affiliations:
- University of Adelaide
- University of North Texas
- Curtin University
- The University of Sydney
arxiv_id: '2609.34848'
url: https://arxiv.org/abs/2609.34848
pdf_url: https://arxiv.org/pdf/2609.34848
published: '2026-09-27'
collected: '2026-09-30'
category: Training
direction: 大模型自蒸馏 · 信贷分配优化
tags:
- Self-Distillation
- Credit Assignment
- RLHF
- LLM Training
- Reasoning
one_liner: 提出解耦信贷方向与幅度的自蒸馏框架DCSD，在多类推理基准上大幅超越现有方法
practical_value: '- 做LLM驱动的Agent推理、生成式推荐内容蒸馏时，可复用DCSD的解耦思路，将更新方向与贡献幅度分开计算，避免教师信号偏差导致的错误奖励

  - 推荐系统多步决策（如搜索引导、多轮推荐）的信贷分配，可借鉴belief-margin probing判断步骤方向，用边际信息增益量化步骤贡献，减少冗余步骤的错误强化

  - 生成式推荐多步骤内容生成训练时，可复用DCSD的step-to-token分配逻辑，将步骤级信贷精准分配到token，提升生成效率，减少冗余内容输出'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RLVR仅能提供轨迹级信贷，无法区分单条推理路径内不同步骤的贡献；OPSD虽通过特权教师提供token级密集监督，但将信贷方向与幅度耦合在同一教师信号中，易受教师判断误差、偏好波动影响，要么锚定轨迹级方向丢失局部信贷灵活性，要么直接复用教师信号导致方向错误，亟需解耦两类信贷信号提升自蒸馏可靠性。

### 方法关键点
- 提出DCSD框架，将信贷方向与幅度完全解耦，分别用独立信号计算后校准教师监督
- 用belief-margin probing检测每步推理后正确答案的置信度变化，判断信贷方向，置信度不足时回退到轨迹级方向，理论上保证方向与oracle局部优势一致
- 用边际信息增益量化每步推理的非冗余信息贡献，归一化后得到信贷相对幅度
- 教师仅负责将步骤级信贷分配到步骤内的token，不能改变步骤的方向与总幅度，避免教师偏差传导

### 关键结果
在11个数学、多模态推理基准上对比GRPO、OPSD、RLSD、RLCSD等基线，数学推理整体得分较base提升8.45分，多模态推理提升7.01分；修正6% token的信贷方向，token信贷幅度降低1.5倍；平均响应长度较RLCSD缩短6.3%的同时Pass@1提升4.02%。

### 核心洞见
自蒸馏中教师信号不直接等价于可信信贷，将更新方向与贡献幅度解耦，可在保留局部信贷灵活性的同时大幅降低教师偏差的负面影响。
