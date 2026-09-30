---
title: 'ROSS: Relearning from Self-Generated Rollouts through Selective Supervision'
title_zh: ROSS：基于选择性监督复用自生成历史轨迹的训练方法
authors:
- Zhiwei Zhang
- Huayu Deng
- Fei Zhao
- Jiayan Fu
- Bin Liang
- Kam-Fai Wong
- Mu Chuan
affiliations:
- AllSpark Team
arxiv_id: '2609.35954'
url: https://arxiv.org/abs/2609.35954
pdf_url: https://arxiv.org/pdf/2609.35954
published: '2026-09-27'
collected: '2026-09-30'
category: Training
direction: LLM训练 · 历史轨迹复用
tags:
- Selective SFT
- Self-Generated Rollout
- Historical Experience Reuse
- LLM Alignment
- Agent Training
one_liner: 提出选择性监督自生成历史轨迹的训练方法ROSS，无需额外采样即可提升模型性能
practical_value: '- 训练电商导购、客服类Agent时，可保留迭代过程中所有历史版本生成的成功轨迹，无需随版本升级丢弃，降低重复采样成本

  - 做SFT优化时可复用ROSS的掩码机制：通过LLM评审过滤轨迹中的错误推理、冗余探索段，仅对有效段计算损失，既保留上下文又避免强化坏行为

  - 历史训练轨迹不仅可用于优化生成它的模型，还可迁移到同系列新初始化的模型，减少新模型的冷启动训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM后训练（RL、on-policy蒸馏等）会产生大量自生成轨迹，通常政策迭代后就被当做过期数据丢弃，但这些历史轨迹既保留了当前政策不再稳定输出的有效行为，也混杂了错误、冗余步骤，直接全轨迹回放会引入噪声，亟需细粒度的选择性监督机制来复用这些低本高效的训练数据。

### 方法关键点
- 双层选择机制：先通过结果校验筛选出成功的历史轨迹，再用LLM评审标注出轨迹中值得学习的有效片段，生成token级的监督掩码
- 全上下文保留：掩码为0的token只做上下文不算损失，不截断原始轨迹，保留有效片段生成时的完整上下文状态
- 训练目标：仅对掩码为1的有效token做teacher-forcing SFT，避免强化中间错误、冗余探索步骤

### 关键结果
在Qwen3.6-35B-A3B上验证：
- 多教师on-policy蒸馏场景下，6个基准的MOPD平均得分从58.40%提升到62.20%
- Agent RL场景下，SWE-bench Verified得分从64.20%提升到68.40%
- 效果优于继续RL/蒸馏、全正轨迹SFT等基线，同时不会损害跨域能力，甚至能提升部分非目标域性能

### 核心结论
历史自生成轨迹不是训练的临时副产品，而是可复用的行为经验库，通过选择性监督就能低成本挖掘出额外性能增益，无需额外采样新轨迹。
