---
title: 'Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution
  and Trajectory Mass Normalization'
title_zh: 面向LLM Agent的双轴策略优化：贝叶斯反馈归因与轨迹质量归一化
authors:
- Yingxuan Zhuang
- Binhe Yu
- Jingxiao Yang
- Ruopei Sun
- Ziting Li
- Cheng Tan
- Xuhong Zhang
- Jianwei Yin
- Jintao Chen
affiliations:
- Zhejiang University
- University of Science and Technology of China
- University of New South Wales
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.19830'
url: https://arxiv.org/abs/2609.19830
pdf_url: https://arxiv.org/pdf/2609.19830
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 强化学习策略优化
tags:
- LLM Agent
- Policy Optimization
- Reinforcement Learning
- GRPO
- Trajectory Optimization
one_liner: 提出双轴策略优化框架BATON，从轨迹内外两个维度提升LLM Agent强化学习性能
practical_value: '- 训练多轮交互Agent（如电商导购Agent、搜索多轮query引导Agent）时，可直接复用TMN轨迹质量归一化模块，解决长失败轨迹占优化权重过高的问题，仅改聚合规则几乎无额外开销

  - 贝叶斯反馈归因（BFA）可直接嵌入现有GRPO/GiGPO训练流程，无需改动原有奖励、优势估计逻辑，仅通过对比执行动作和反事实动作的反馈兼容性重加权，就能稳定提升3-5%的任务成功率

  - 做搜索推荐Agent的RL训练时，可参考双轴拆分思路，把单步决策权重分配和全轨迹聚合权重拆分优化，避免长轨迹干扰训练收敛，同时降低推理时的交互步数，节省推理成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有LLM Agent强化学习存在两个核心问题：一是轨迹内反馈利用不充分，无效重复动作多；二是轨迹间聚合存在长度偏差，长失败轨迹最多可占60%的优化权重，主导训练方向导致效果不佳，需同时解决轨迹内归因和轨迹间聚合的双重问题。

### 方法关键点
- 提出双轴优化框架BATON，两个模块独立可插拔，不改动原有RL训练的奖励、优势估计、剪枝、rollout逻辑：
  1. 贝叶斯反馈归因（BFA）：对每步决策采样反事实动作，对比执行动作和反事实动作与环境反馈的兼容性，计算贝叶斯证据比生成归一化归因权重，重分配轨迹内各步的优化权重
  2. 轨迹质量归一化（TMN）：将原有按token数加权的轨迹聚合规则改为每条完整轨迹权重均等，消除长轨迹的权重优势
- 统一目标函数先对单条轨迹内加权损失求平均，再对batch内所有轨迹求平均，保证两个模块独立生效。

### 关键实验
在ALFWorld、WebShop、搜索增强QA三个场景测试，兼容GRPO、GiGPO两种主流无critic RL算法，覆盖1.5B/3B/7B模型尺度：
- 1.5B Qwen2.5+GRPO组合下，ALFWorld成功率从72.9%提升至85.6%，WebShop成功率从57.1%提升至68.2%
- 7B Qwen2.5+GiGPO组合下，搜索增强QA平均精确匹配从47.1%提升至48.7%，ALFWorld成功率从90.9%提升至94.9%
- 两个模块独立增益可叠加，TMN仅增加2%训练耗时，全框架额外耗时不超过17%，同时推理时轨迹长度缩短20%以上，降低交互成本。

### 核心结论
LLM Agent强化学习优化可拆分为轨迹内权重分配和轨迹间聚合两个独立维度，仅优化聚合规则就能获得明显增益，无需大幅改动原有训练流程。
