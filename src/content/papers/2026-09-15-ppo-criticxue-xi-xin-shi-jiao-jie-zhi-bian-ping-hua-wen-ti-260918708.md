---
title: 'Rethinking Critic Learning in PPO: Understanding and Mitigating Value Flattening'
title_zh: PPO Critic学习新视角：价值扁平化问题的理解与缓解
authors:
- Yizhuo Li
- Jianhao Yan
- Yun Luo
- Zhi Wang
- Futing Wang
- Rong-Xi Tan
- Kanghui Tian
- Ganqu Cui
- Ning Ding
- Peilin Zhao
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Westlake University
- Tsinghua University
- Nanyang Technological University
arxiv_id: '2609.18708'
url: https://arxiv.org/abs/2609.18708
pdf_url: https://arxiv.org/pdf/2609.18708
published: '2026-09-15'
collected: '2026-09-17'
category: Training
direction: 大模型强化训练 · PPO算法优化
tags:
- PPO
- Reinforcement Learning
- Critic Learning
- Value Flattening
- SP3O
one_liner: 提出稀疏监督SP3O算法缓解PPO Critic的价值扁平化问题，提升RLHF训练的策略性能
practical_value: '- 若业务中用PPO做LLM对齐（如推荐话术生成、Agent决策优化），可直接复用SP3O稀疏critic监督策略，仅在0.3/0.6/0.9三个相对位置计算critic损失，降低训练成本同时提升效果，无需全token监督

  - 若遇到长序列RL训练不稳定问题（如长路径用户转化建模、多轮Agent任务），可参考价值扁平化成因分析，检查critic是否对序列内状态价值变化不敏感，避免冗余更新

  - PPO训练的critic监督无需追求高密度，实验显示3个稀疏锚点效果优于16/64个锚点的密集监督，可大幅降低critic训练的计算开销，适配工业级大模型RL训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM强化学习中PPO算法的Critic常无法捕捉同一条响应内不同中间状态的真实价值变化，即价值扁平化问题，导致优势估计偏差、策略更新不稳定，尤其在长序列、大状态空间场景下问题更突出，限制RLHF的训练效果。

### 方法关键点
- 拆解价值扁平化两大成因：一是全token监督的MSE损失隐含对同响应内预测值方差的惩罚，强制critic输出平滑；二是相邻状态高度时序相关，梯度冗余会进一步拉平预测值
- 提出SP3O（SParse PPO）：不改变PPO的actor目标、采样流程，仅选择响应内少数间隔较远的状态计算critic损失，默认选取相对位置0.3/0.6/0.9三个锚点，超过6144token的长序列额外加0.95位置的锚点

### 关键实验结果
在Qwen3-4B/8B上训练，对比标准PPO、GRPO基线：数学推理任务平均准确率提升7.97个百分点，OOD通用推理任务平均提升7.33个百分点；3个锚点的稀疏监督效果优于16/64个锚点的密集配置，训练更稳定，actor更新波动更小，长响应生成的重复率从18.33%降至1.12%。

### 核心结论
PPO的critic不需要全token监督，少数间隔均匀的稀疏锚点即可同时缓解价值扁平化问题、降低训练开销、提升策略性能。
