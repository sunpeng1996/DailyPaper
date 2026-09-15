---
title: 'Unlocking the Unsolvable: Teacher-Guided Curriculum for Data-Efficient RLVR'
title_zh: 教师引导课程学习解锁RLVR不可解问题，实现高效推理提升
authors:
- Yukang Zhu
- Zhen Han
affiliations:
- Independent Researcher
- Amazon
arxiv_id: '2609.13997'
url: https://arxiv.org/abs/2609.13997
pdf_url: https://arxiv.org/pdf/2609.13997
published: '2026-09-12'
collected: '2026-09-15'
category: Training
direction: 大模型推理 · RLVR高效训练
tags:
- RLVR
- Curriculum Learning
- Data Efficiency
- Mathematical Reasoning
- GRPO
one_liner: MFC课程仅用128道不可解问题实现RLVR 16倍数据效率，拓展推理边界
practical_value: '- 业务RL训练中遇到的全失败无梯度难例（如复杂query理解、冷启动推荐难case）无需丢弃，可引入强模型的分步推理结果作为hint构造梯度信号，盘活难例价值

  - MFC单调调度逻辑可直接复用：仅当模型在更低hint占比下成功完成任务时才降低hint量，避免训练测试分布偏移，比双向调整的AdaBack更适配难例调优场景

  - 训练数据成本高的场景可参考16倍数据效率结论：优先筛选当前模型的不可解难例做课程训练，无需全量数据即可达到甚至超过全量训练效果，大幅降低标注与计算成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RLVR训练中，超出当前模型能力的不可解问题（所有rollout全失败，无梯度信号）会被完全浪费，但这类难例恰恰是拓展模型能力边界的最高价值样本；同时标准GRPO训练易出现推理边界收缩，大k的pass@k甚至低于base模型。
### 方法关键点
- 用更强教师模型为每个不可解问题生成结构化推理trace，通过控制trace暴露比例ρ构造不同难度梯度的训练样本，将单个无梯度难例转化为可产生有效梯度的训练集
- Monotone Frontier Curriculum（MFC）为每个样本维护当前最大允许hint步数gcurr，仅当模型在更低hint步数下成功时才下调gcurr，失败不调整，全程单调向无hint（ρ=0）推进，最小化训练测试分布偏移
- 对比现有反向链课程（多ρ混合采样的Mixture、双向调整可行区间的AdaBack），MFC可持续提升无hint训练占比，避免分布偏移损耗
### 关键实验
- 数据集：从OpenR1-Math-220k筛选2000道混合难度题，取Qwen3-1.7B pass@64=0的128道不可解题作为训练集
- 对比基线：全量2000题训练的GRPO、Mixture课程、AdaBack课程
- 核心结果：仅用128道题训练的MFC在9个基准平均pass@1达47.3%，超过全量GRPO的44.3%，数据效率提升16倍；AIME数据集pass@256比GRPO高10pp，显著拓展推理边界；MFC最终无hint训练占比达60%，比AdaBack高20pp
### 核心结论
模型完全做不对的难例不是负担，通过梯度可控的课程设计，极少量难例就能带来远超全量混合数据的能力提升
