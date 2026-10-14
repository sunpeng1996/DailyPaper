---
title: 'Beyond Prompt Count: How Data Shapes Transfer in On-Policy Distillation'
title_zh: On-Policy蒸馏中数据特征对知识迁移效果的影响研究
authors:
- Jiaxuan Wang
- Jiafei Lyu
- Yuchen Cai
- Siye Wu
- Pengyuan Wang
- Jiashun Liu
- Xiang Cheng
- Kai Yang
- Yangkun Chen
- Saiyong Yang
affiliations:
- 南京大学
- 腾讯
- 中国人民大学
arxiv_id: '2609.37377'
url: https://arxiv.org/abs/2609.37377
pdf_url: https://arxiv.org/pdf/2609.37377
published: '2026-09-28'
collected: '2026-10-14'
category: Training
direction: LLM On-Policy蒸馏 训练数据优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Prompt Engineering
- Transfer Learning
one_liner: 系统揭示On-Policy蒸馏的Prompt效率与来源偏好，验证随机采样为高性价比训练基线
practical_value: '- 做LLM领域微调/蒸馏时，优先选择均匀随机采样作为prompt基线，无需投入高成本做复杂的prompt筛选、来源过滤，多数场景下可达到最优性价比

  - 小参数量模型蒸馏可复用极小prompt策略：仅需数条到数十条prompt即可接近大prompt池的效果，可大幅降低训练数据准备与计算成本

  - 遇到蒸馏负迁移时无需全流程重训，切换到验证有效的prompt源继续训练即可快速恢复性能，大幅降低排障与重训成本

  - 无需迷信特定来源prompt的通用效果：prompt的有效性与师生模型对、目标任务强相关，需结合自身场景小范围验证后再确定最优prompt源'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）已广泛用于LLM小模型轻量化、领域专项能力整合、训练阶段能力恢复，但prompt选择对迁移效果的影响机制长期不明，工业界缺乏可落地的prompt选择指导，不清楚是否需要投入成本做prompt筛选、多少prompt可满足训练需求。

### 方法关键点
- 覆盖3类典型师生对：RL续训对、SFT续训对、跨模型蒸馏对，涉及数学推理、代码生成、多领域指令遵循等下游任务
- 从prompt数量、来源、选择策略三个维度开展对照实验，结合参数对齐、功能对齐、隐藏态干预等方法诊断迁移机制
- 对比8种定向prompt选择策略（语义多样性、难度筛选、梯度优化等）与均匀随机采样的效果与成本

### 关键结果
1. OPD prompt效率极高：4个DAPO prompt即可达到3840个DeepMath prompt的数学得分，prompt数量效率差达960倍；单prompt最多可实现大prompt池95%以上的性能
2. prompt效果无通用属性：更换同参数教师模型可完全反转数学、代码prompt的相对效果，同一prompt在不同师生对的效果差异可达20pct以上
3. 所有测试的定向选择、来源过滤策略均无法稳定优于均匀随机采样，反而额外增加数倍到数十倍的GPU筛选成本
4. 负迁移易恢复：出现负迁移后切换到有效prompt源继续蒸馏，代码任务得分可从50.03提升至63.16，超过原生训练的61.79

### 核心结论
Prompt效率不等于可互换性，均匀随机采样是OPD数据选择的高性价比基线，无明确增益证据时无需额外开展复杂prompt筛选
