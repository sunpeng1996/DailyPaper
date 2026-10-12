---
title: 'A Step Harder, Not a Step Too Far: The Benefits and Limits of Curriculum Difficulty
  Progression in GRPO'
title_zh: GRPO训练中课程难度递进的收益边界与优化策略
authors:
- Ronghan Li
- Fei Chen
- Mingyu Lu
affiliations:
- Dalian Maritime University
arxiv_id: '2610.13669'
url: https://arxiv.org/abs/2610.13669
pdf_url: https://arxiv.org/pdf/2610.13669
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: LLM对齐训练 · GRPO课程学习优化
tags:
- GRPO
- Curriculum Learning
- Reinforcement Learning
- LLM Alignment
- Dynamic Data Selection
one_liner: 提出随策略动态调整的分阶段难度递进课程，在GRPO训练中取得比固定中等难度更高的推理性能
practical_value: '- 做LLM对齐（Agent指令微调、生成式推荐RL训练等）时，不要长期只投喂中等难度样本，可按模型能力分阶段切换到中等偏难样本池，能拿到额外性能增益

  - 样本难度要基于当前模型状态动态重估，不要用训练前的固定难度划分，尤其适合生成式推荐、query改写这类样本难度随模型能力快速变化的场景，减少无效信号

  - 难度递进不要贪多，达到中等偏难区间即可停止，过难样本会导致性能下降；可复用论文的小诊断子集+耐心阈值的跳转规则，减少全量评估的算力消耗

  - 做GRPO训练时，可直接复用论文的5级难度划分（按样本回答成功率）和阶段跳转逻辑，快速提升训练效率和最终性能'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
GRPO依赖同prompt多回复的相对奖励计算梯度，中等难度样本（对错参半）能提供最丰富的学习信号，长期被作为优先选择，但业界尚未验证持续选择中等难度样本是否能拿到最优性能；同时样本难度随模型策略迭代动态变化，预计算的固定难度很快会和当前模型状态失配，导致训练信号浪费。
### 方法关键点
- 基于当前模型对样本的解答成功率动态估计难度，按成功率划分为B1（易）到B5（难）5个难度区间
- 对比3种训练范式：静态预计算难度课程、固定中等难度（B3）动态选样本、分阶段难度递进课程（B1→B2→B3→B4→B5）
- 阶段跳转采用固定专属诊断子集评估，当性能连续2次评估无超过噪声阈值的提升时，进入下一个难度阶段
### 关键实验
在GSM8K数学推理数据集上，基线包括标准GRPO、静态难度课程、固定中等难度课程：分阶段课程推进到B4（中等偏难）时测试准确率达0.6591±0.0077，比固定中等难度方案高1.42个百分点，比标准GRPO高1.47个百分点；进一步推进到B5（难）时准确率下降到0.6405±0.0053，收益呈非单调特征。
### 核心结论
GRPO训练中难度递进的收益是非单调的，不必执着于一直投喂梯度信号最丰富的中等难度样本，适当向中等偏难递进一步可拿到额外增益，但不要过度推进到过难样本
