---
title: 'Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation
  through Teacher-Relative Shifts'
title_zh: 基于教师相对偏移的多教师在线蒸馏 高效整合异源专家能力
authors:
- Hejian Sang
- Zhengze Zhou
- Shayan Mohajer Hamidi
- Xiaomin Li
- Rohit Jain
- Alborz Geramifard
affiliations:
- Iowa State University
- LinkedIn
- Harvard University
arxiv_id: '2610.10460'
url: https://arxiv.org/abs/2610.10460
pdf_url: https://arxiv.org/pdf/2610.10460
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: 多教师在线蒸馏 · LLM能力整合
tags:
- Knowledge Distillation
- On-Policy Distillation
- Multi-Teacher Distillation
- LLM Training
- Delta Transfer
one_liner: 提出Δ-MOPD蒸馏框架，通过教师相对基座偏移整合能力，降低训练成本同时提升效果
practical_value: '- 做垂直领域多专家蒸馏到单一小模型（如电商多场景Agent/生成式推荐底座）时，替换传统端点蒸馏为Δ-MOPD：只蒸馏教师相对自身基座的logit偏移再锚定学生初始化，可过滤异源基座的原生偏好干扰，提升多能力整合的平衡性

  - 跨tokenizer的异源模型整合可复用token字符串映射的偏移投影方法，无需统一tokenizer即可迁移能力，降低多源模型复用的门槛

  - 分阶段迭代不同领域能力时，用Δ-MOPD可降低训练顺序导致的效果波动，减少多场景模型迭代的顺序调优成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有多教师在线蒸馏（MOPD）直接迁移教师端点策略，会同步迁移教师基座原生偏好，异源教师场景下无效的基座偏好信号甚至会超过训练新增的能力信号，导致多教师信号不平衡、学生学习难度大、训练成本高。
### 方法关键点
- 提出Δ-MOPD框架，蒸馏目标改为教师端点相对自身基座的logit偏移，重新锚定到学生冻结的初始化参数，自动过滤基座原生偏好；
- 同域多教师组合场景下累加所有选中教师的偏移生成训练目标，路由场景下直接使用当前领域教师的偏移生成目标；
- 支持跨tokenizer教师适配，通过token字符串映射对齐异源词汇表的偏移信号，无需统一tokenizer即可复用外部专家能力。
### 关键结果
以DeepSeek-R1-Distill-Qwen-1.5B为学生底座，整合3-4个异源推理专家，对比标准端点蒸馏baseline：
1. 教师项范数比从5.2:1降至1.44:1，目标与学生的KL从0.152降至0.031，学习信号质量大幅提升；
2. 达到相同Math得分所需H100训练时长降低35%；
3. 3个教师组合时Math得分高4.11，5项基准平均得分高1.95；
4. 分阶段路由场景下训练顺序带来的效果gap从10.50降至6.42，训练鲁棒性显著提升。
### 核心结论
多教师蒸馏中「迁移什么」是与「选哪些教师」独立的核心设计轴，优先迁移教师训练新增的能力而非完整端点策略，可大幅提升多能力整合效率
