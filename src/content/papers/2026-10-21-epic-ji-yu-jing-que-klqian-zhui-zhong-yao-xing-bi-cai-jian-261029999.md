---
title: 'EPIC: Rethinking Trust Regions for Autoregressive LLM Policies via Exact-KL
  Prefix Importance-Ratio Clipping'
title_zh: EPIC：基于精确KL前缀重要性比裁剪的自回归LLM策略信任域重构
authors:
- Chengxi Li
- Hanlin Wu
- Zhicheng Cai
- Huan-ang Gao
- Wei-Ying Ma
- Jingjing Liu
- Hao Zhou
affiliations:
- 清华大学AIR
- SIA-Lab（清华AIR与字节跳动Seed联合实验室）
- 清华大学计算机科学与技术系
arxiv_id: '2610.29999'
url: https://arxiv.org/abs/2610.29999
pdf_url: https://arxiv.org/pdf/2610.29999
published: '2026-10-21'
collected: '2026-10-22'
category: Training
direction: LLM强化学习 · PPO裁剪优化
tags:
- PPO
- Reinforcement Learning
- MoE
- Off-policy Training
- Trust Region
one_liner: 提出前缀级裁剪的PPO变体EPIC，显著提升离线MoE LLM强化学习的稳定性与性能
practical_value: '- 生成式推荐/Agent LLM的RL对齐场景，可替换原有GRPO/GSPO裁剪逻辑为EPIC前缀级裁剪，无需额外存储路由信息即可降低长序列生成（如商品长文案、多轮Agent交互规划）的训练不稳定风险

  - MoE大模型RL训练可复用EPIC的内存优化设计，相比R2/R3路由回放方案最高降低93%的驱动进程内存开销，显著降低大模型对齐的集群资源成本

  - 序列决策类推荐任务（如会话推荐、多步导购路径规划）的RL优化可借鉴前缀重要性权重校正思路，解决累计决策偏移被传统单步裁剪忽略的问题，提升长序列决策稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM强化学习训练广泛采用PPO类裁剪方案，传统GRPO的token级裁剪仅考量当前token的条件概率，忽略前缀上下文本身由策略生成的特性，无法感知累计策略偏移；GSPO的序列级裁剪则会抑制早期前缀的有效更新信号，在离线训练、长序列生成、MoE模型场景下训练不稳定问题尤为突出。现有R2/R3等路由回放方案虽能缓解MoE训练偏移，但会引入额外内存开销，限制训练吞吐。

### 方法关键点
- 将自回归生成建模为有限 horizon MDP，推导得出前缀累计似然比是每步策略提升项的精确重要性权重
- 基于精确reverse-KL坐标`r_pre - 1 - log(r_pre)`构建前缀级信任域，其在行为策略下的期望等于前缀分布的KL散度，无需依赖局部二次近似或专家路由回放
- 工程实现高效兼容现有RL pipeline：通过累计和计算前缀对数似然比，经几何平均归一化后使用直通梯度保留当前token的梯度路径，仅修改裁剪逻辑即可嵌入现有训练框架

### 关键实验结果
基于Qwen3-30B-A3B稀疏MoE模型在数学推理数据集训练，对比GRPO、GSPO、DAPO等基线，四套推理基准平均准确率达39.34%，较GRPO高出10.69个百分点，较GSPO高出6.50个百分点；对比R2、R3路由回放方案性能相当，驱动进程内存开销分别降低77.5%、93.0%。

最值得记住的结论：自回归序列RL优化的信任域约束必须考虑前缀累计策略偏移，而非仅约束单token或全序列的单一粒度概率比。
