---
title: 'When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem
  Reasoning'
title_zh: 面向困难推理任务的策略兼容联合解码RL框架PICO
authors:
- Zehao Wang
- Hanzhu Chen
- Runquan Gui
- Zhe Wang
- Lin Yang
affiliations:
- University of Science and Technology of China
- Tencent
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.36849'
url: https://arxiv.org/abs/2610.36849
pdf_url: https://arxiv.org/pdf/2610.36849
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM RL训练 · 策略兼容联合解码
tags:
- RLVR
- GRPO
- Joint Decoding
- Policy Optimization
- Reasoning
one_liner: 针对RLVR困难任务全失败采样组无有效学习信号问题，提出策略兼容联合解码框架PICO，性能显著优于现有基线
practical_value: '- 做电商导购/决策Agent的RL训练时，若频繁遇到全失败采样组无正样本的问题，可复用失败触发的联合解码机制，用专家轨迹做token级引导，避免直接SFT导致的策略漂移和表层模仿

  - 生成式推荐/搜索query生成的RL优化流程中，可直接复用动态top-k联合解码方法，在引入更高质量样本的同时保留当前模型分布，严格控制KL散度避免训练震荡

  - 基于GRPO的组相对优势RL训练中，可直接复用带重要性采样修正的混合行为优化目标，平滑引入off-policy样本，降低分布偏移对训练的影响'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR（带可验证奖励的强化学习）是提升LLM推理、Agent决策能力的主流范式，但在超过模型当前能力的困难任务上会遇到学习悬崖：如果一个批次的所有采样rollout都失败，GRPO等组相对优势估计算法会得到全0优势，没有有效学习信号；直接引入专家轨迹又会因为和当前策略分布不兼容，要么导致策略漂移变成表层模仿，要么引入特权上下文依赖，推理时脱离引导就失效。

### 方法关键点
- 仅在全失败采样组触发联合解码：用带专家信息的Teacher模型和当前Student模型的top-k token交集作为候选集，保留Student的相对概率采样，保证生成轨迹既正确又和当前策略兼容
- 动态top-k机制：自适应调整Teacher的候选集大小，保证Student在候选集上的概率质量不低于预设阈值，严格控制解码分布和原Student分布的KL散度上限
- 混合行为优化：生成的合格轨迹替换一个失败样本加入原组，用带重要性采样修正的GRPO目标优化，适配联合解码轨迹的分布偏移

### 关键实验
在DAPO-Math-17K数据集上训练，对比GRPO、LUFFY、Prefix-RFT等基线，Qwen3-4B/8B模型在数学推理基准上平均提升3.6~4.1个百分点，Agent基准ALFWorld/ScienceWorld上平均提升6.8个百分点，可挽救80%左右的全失败采样组。

### 核心结论
引入外部专家知识做RL优化时，策略兼容性和轨迹正确性同等重要，避免分布漂移的收益远高于直接用高质量离轨样本。
