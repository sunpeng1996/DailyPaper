---
title: 'Back to the Definition: Estimating Step-Level Advantages via Trajectory Graphs
  for Agentic Reinforcement Learning'
title_zh: 基于轨迹图的智能体强化学习步级优势分配框架GRAFT
authors:
- Xincheng Yao
- Haobo Fu
- Weiming Liu
- Chongyang Zhang
affiliations:
- 上海交通大学
- 腾讯AI平台部
- 教育部人工智能重点实验室
arxiv_id: '2609.28963'
url: https://arxiv.org/abs/2609.28963
pdf_url: https://arxiv.org/pdf/2609.28963
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: 智能体强化学习 · 步级信用分配
tags:
- Reinforcement Learning
- GRPO
- Credit Assignment
- Trajectory Graph
- LLM Agent
- Bellman Iteration
one_liner: 将多轮轨迹重构为统一轨迹图，通过Bellman迭代输出无PRM、符合RL定义的步级优势信号
practical_value: '- 做LLM Agent多轮任务RL训练时，可复用GRAFT的轨迹图构建逻辑，用状态精确/语义匹配合并跨轨迹相同状态，无需额外采样即可获得同状态多动作样本组，大幅降低PRM标注成本

  - 步级优势估计可直接复用Bellman迭代+Graph GAE方案，仅需终端稀疏奖励即可生成理论对齐的步级信用信号，比GRPO粗粒度分配更准确，比GiGPO单轨迹蒙特卡洛估计方差更低

  - 电商导购Agent、多轮搜索推荐Agent的RL训练可直接适配该框架，无需额外标注过程奖励，仅用最终下单/转化信号即可实现多轮决策的精准credit分配，降低训练成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前GRPO等群组RL方法是LLM Agent训练的主流范式，但仅能输出轨迹级优势，错误将整条轨迹的优势分配给所有token，无法准确衡量单步贡献，导致多轮任务训练效率低、效果差；现有步级优势方案要么需要昂贵的PRM标注，要么按步索引分组估计时引入系统性偏差，同索引不同状态的样本被错误聚合，而逐状态重采样的成本为O(N²T)完全不可接受。

### 方法关键点
- 轨迹图构建：将N条独立多轮rollout轨迹合并为统一有向图，节点为规范化状态（支持精确字符串匹配或embedding相似度阈值匹配两种模式，适配结构化环境与非结构化对话场景），边为状态间的动作转移，终端节点直接绑定稀疏成功/失败奖励
- 状态值估计：通过Gauss-Seidel迭代求解Bellman方程，从终端节点反向传播奖励值，无需额外critic网络即可得到每个节点符合RL定义的状态值估计
- 步级优势计算：单步优势定义为相邻节点的状态值差γV(s_{t+1})-V(s_t)，进一步扩展Graph GAE融合多跳后续优势做偏差-方差权衡，最终在同状态的出边组内做优势归一化
- 优化目标适配：提出GRPO-C校准优化目标，将优势分配粒度与动作粒度对齐，避免原GRPO token级分配的不匹配问题

### 关键实验
在ALFWorld、WebShop、SearchQA三类多轮Agent基准上测试，对比GRPO、GiGPO、GraphGPO等SOTA方法：1.5B参数下ALFWorld成功率比GRPO高24.6%，WebShop成功率高25.5%；7B参数下SearchQA平均成功率达48.6%，超过Search-R1、StepSearch等基线；额外时间开销仅占总训练时间的0.43%，无额外显存占用。

**最值得记住的一句话**：无需PRM、无需额外采样，仅通过跨轨迹状态聚合与Bellman迭代即可得到完全符合RL基础定义的步级优势信号，成本接近GRPO但效果提升显著。
