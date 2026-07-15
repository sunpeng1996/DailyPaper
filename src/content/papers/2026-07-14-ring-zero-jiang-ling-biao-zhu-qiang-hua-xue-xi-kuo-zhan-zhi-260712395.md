---
title: 'Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning'
title_zh: Ring-Zero：将零标注强化学习扩展至万亿参数实现推理涌现
authors:
- Xinyu Tang
- Gangqiang Cao
- Yurou Liu
- Yuliang Zhan
- Xiaochong Lan
- Yifan Li
- Yuchen Yan
- Han Peng
- Zican Dong
- Zhenduo Zhang
arxiv_id: '2607.12395'
url: https://arxiv.org/abs/2607.12395
pdf_url: https://arxiv.org/pdf/2607.12395
published: '2026-07-14'
collected: '2026-07-15'
category: Training
direction: 大模型训练 · 零标注RL规模扩展
tags:
- Zero RL
- Scaling Law
- Chain-of-Thought
- Emergent Ability
- Large Language Model
one_liner: 推出万亿参数Zero RL稳定训练管线，验证规模扩展带来的推理能力涌现与训练阶段特性
practical_value: '- 做Agent推理优化时可参考其提出的CoT三维评估框架（可理解性、可复现性、效率），替代仅看最终答案准确率的评估逻辑，提升规划路径的实用性

  - 大模型微调/RLHF环节可复用裁剪重要性采样、训推比例校正、混合精度控制的优化trick，提升大参数模型训练稳定性

  - 验证了规模扩展对推理能力的提升规律，业务侧做大模型驱动的推荐/搜索Agent时，可优先通过参数规模扩容而非人工规则优化突破性能天花板'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有Zero RL（无需人工标注、仅用可验证奖励的强化学习）研究受算力限制仅适配小模型，万亿参数规模下的训练动态与涌现能力尚未被探索，直接扩规模存在可读性差、token冗余、推理深度无法自适应的问题。
### 方法关键点
推出稳定高效的Zero RL训练管线，融合裁剪重要性采样、训推比例校正、混合精度控制等算法与系统级优化，同时配套覆盖可理解性、可复现性、效率三维的CoT质量评估框架，避免仅用最终答案准确率的评估偏差。
### 关键结果数字
1. 1T参数模型大幅提升样本效率与性能上限，在7个数学推理基准上达到极具竞争力的性能；
2. 训练过程天然分为「探索期→打磨期」两个连续阶段；
3. 模型自发生成拟人化表达、结构化输出、自我验证、并行推理等5种高级认知行为，人工启发式规则不再必要。
