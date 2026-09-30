---
title: Do We Really Need KL Divergence for On-Policy Distillation of Large Language
  Models?
title_zh: 大模型同策略蒸馏是否真的需要KL散度？
authors:
- Wenze Lin
- Jiyuan Long
- Jiale Zhao
- Shenzhi Wang
- Xitai Jiang
- Ce Luo
- Rui Lan
- Qianli Ma
- Fukang Wen
- Hui Wu
affiliations:
- Tsinghua University
- Beihang University
- National University of Singapore
- The Chinese University of Hong Kong
- E Fund Management Co., Ltd.
arxiv_id: '2609.33791'
url: https://arxiv.org/abs/2609.33791
pdf_url: https://arxiv.org/pdf/2609.33791
published: '2026-09-26'
collected: '2026-09-30'
category: Training
direction: 大模型蒸馏 · 训练优化
tags:
- Knowledge Distillation
- On-Policy Distillation
- KL Divergence
- Multi-Teacher Distillation
- LLM Training
one_liner: 证明LLM同策略蒸馏仅需高分歧token方向指导无需KL散度，提出更优的多教师蒸馏方案
practical_value: '- 做LLM4Rec/Agent小模型蒸馏时，可直接用BinaryOPD替换KL散度损失，仅需判断师生对token的概率高低分配±1奖励，计算复杂度大幅降低，效果不下降甚至更优，适合业务端侧模型快速迭代

  - 多场景（搜索/推荐/广告）小模型能力合并时，可复用C-MOPD架构，所有领域教师同时指导每个样本，仅在教师无强冲突时更新，避免传统单路路由导致的旧领域能力遗忘，降低多能力整合的成本

  - 蒸馏训练时可提前过滤掉90%以上的低分歧token，仅保留<2%的高分歧token做梯度更新，训练速度提升明显，效果几乎无损，适合大流量业务下的小模型快速上线场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
KL散度是知识蒸馏领域长期沿用的默认损失，近年兴起的大模型同策略蒸馏（OPD）也默认采用反向KL作为优化目标，但KL散度计算复杂度高，其在反复迭代的同策略训练场景下的必要性从未被验证，亟需探索更轻量、高效的蒸馏方案。
### 方法关键点
- 提出BinaryOPD：无需计算KL散度，仅对教师模型概率高于学生的token给予+1奖励，反之给予-1奖励，仅保证更新方向指向教师即可完成蒸馏。
- 发现核心规律：仅占比<2%的师生高分歧token对蒸馏效果起决定性作用，占比90%以上的低分歧token即使更新方向偏离教师也不会显著影响最终效果。
- 提出C-MOPD多教师蒸馏方案：每个样本同时接收所有领域教师的指导，教师无分歧时统一更新，有分歧时仅在冲突小于阈值ϵ时按领域教师方向更新，避免跨域能力冲突与遗忘。
### 关键实验
在数学（DAPO-Math-17k、DeepMath）、代码（Eurus）数据集上，覆盖1.5B~30B不同尺度模型测试：BinaryOPD效果与标准OPD持平甚至略优，数学任务平均高0.5~1.0个百分点，代码任务效果几乎一致；仅保留<2%的高分歧token训练，效果与全量token训练完全对齐；C-MOPD相比传统单样本路由的MOPD，数学任务平均高1.2个百分点，代码任务平均高1.6个百分点。
### 核心结论
同策略蒸馏的核心是少量高分歧token的方向对齐，而非全token的分布匹配，KL散度携带的幅度信息在同策略反复迭代的场景下完全冗余。
