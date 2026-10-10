---
title: Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric
  Rewards
title_zh: 组合偏好与规则奖励的前沿文生图模型后训练方法
authors:
- Yuanhao Ban
- I-Hung Hsu
- Anastasios Angelopoulos
- Wei-Lin Chiang
- Ion Stoica
- Cho-Jui Hsieh
affiliations:
- Arena Intelligence Inc
- UCLA
arxiv_id: '2610.02967'
url: https://arxiv.org/abs/2610.02967
pdf_url: https://arxiv.org/pdf/2610.02967
published: '2026-10-01'
collected: '2026-10-10'
category: Training
direction: 生成模型后训练 · 异质奖励组合优化
tags:
- Reward Modeling
- Post-Training
- Text-to-Image
- Reward Composition
- RLHF
- Human Preference
one_liner: 提出偏好+规则的异质奖励组合策略，显著提升前沿文生图模型后训练性能
practical_value: '- 电商商品图、营销素材的文生图模型优化可复用双轨奖励框架，兼顾用户审美偏好与商品属性合规性要求，避免奖励黑客

  - 推荐多目标排序、Agent多任务奖励融合场景可复用异质奖励组合策略，替代简单加权平均提升优化效果

  - 生成类任务后训练可参考小样本子集验证思路，先用1K级数据验证方案有效性再上全量，大幅降本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
前沿文生图模型后训练存在明显瓶颈，单一奖励信号无法覆盖全部人类偏好，直接加权平均融合异质奖励会导致优化效果次优，还易出现奖励黑客问题。
### 方法关键点
1. 双轨奖励体系：一是基于大规模人类偏好数据、用Bradley-Terry目标训练的偏好奖励，捕捉整体审美与感知偏好；二是规则类奖励，显式评估prompt保真度等要求，防范奖励黑客。
2. 设计适配异质信号的奖励组合策略，更有效平衡偏好优化与规则满足。
### 关键结果
在Arena文生图榜单上，RL训练的Flux2dev Elo评分比基线高69分；后训练的Ideogram-4 Elo达1223.5，超过所有开源模型。同时开源1K规模的训练子集Arena-T2I-Training支撑方案复现。
