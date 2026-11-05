---
title: 'EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation
  RL'
title_zh: EmoReward：面向情感视频生成强化学习的自进化奖励校准机制
authors:
- Mingzhe Zheng
- Yue Wu
- Jing Tan
- Chang Zou
- Dengyang Jiang
- Zeyue Tian
- Xuanhua He
- Ryan Xu
- Yunyang Ge
- Sihui Ji
affiliations:
- The Hong Kong University of Science and Technology
- Tencent Hunyuan
- Fudan University
- University of Waterloo
arxiv_id: '2611.06518'
url: https://arxiv.org/abs/2611.06518
pdf_url: https://arxiv.org/pdf/2611.06518
published: '2026-11-03'
collected: '2026-11-05'
category: Training
direction: 生成式模型训练 · RL奖励校准
tags:
- RLHF
- Reward Calibration
- GRPO
- Video Generation
- Self-Evolution
one_liner: 提出无需更新奖励模型的跨轮次自进化奖励校准框架EmoReward，提升情感视频生成效果
practical_value: '- 多奖励融合场景可复用 Reflective Reward Gating 思路，为每个奖励信号新增场景适配门控（如人脸置信度、语义冲突度），避免无效信号干扰优化，可直接迁移到电商短视频/商品图文生成的RL对齐流程

  - 跨训练轮次的 RewardMemory 机制可复用到推荐系统多目标排序场景，无需更新排序模型，仅根据历史业务效果动态调整多目标权重，大幅降低迭代成本

  - 自进化奖励校准范式可用于Agent的反馈优化流程，从历史交互轨迹中蒸馏不同评测信号的可信度，动态分配权重，减少对大规模人工标注的依赖'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
GRPO等RL算法在代码、数学等可验证领域效果优异，但在情感视频生成这类无明确标准答案的主观场景中，固定权重的多奖励融合难以适配不同场景下的信号可靠性，容易出现奖励黑客；而RLHF的人工标注成本高、难以规模化，且审美差异导致跨场景的情感线索校准困难，亟需自适应的奖励校准机制。

### 方法关键点
- 分Plan-Act-Reflect-Evolve四阶段流程：Plan阶段将情感prompt转化为包含效价、唤醒度、面部动作单元、肢体线索的EmoScript作为评估依据
- Act阶段用7类异构奖励原语（VLM裁判、面部AU、肢体线索、时序证据等）分别打分并输出有效性标识
- Reflect阶段的Reflective Reward Gating根据训练阶段、人脸置信度、语义冲突、情感微妙度四个维度做实例级门控，动态过滤无效信号，归一化有效奖励权重后融合得到情感奖励
- Evolve阶段的RewardMemory从已完成的训练轮次轨迹中，按情感场景分组计算每个奖励原语和最终效果的相关性，生成固定的权重乘数用于下一轮训练，全程不更新奖励模型参数

### 关键实验
在HunyuanVideo 1.5上基于302个未见过的情感prompt测试，对接DanceGRPO、FlowGRPO、SAGE-GRPO三种RL算法，VideoAlign Overall分分别提升0.3218、0.2343、0.5645；用户评测中情感保真度的Good占比达60%，比纯SAGE-GRPO高7个百分点，Bad占比从31.5%降至15.4%，同时时序一致性、视觉质量的各项指标均为最优。

### 核心结论
**无需更新生成模型或奖励模型参数，仅通过动态调整多奖励的权重分配，即可实现跨训练轮次的自进化优化，大幅降低主观生成任务的对齐成本**
