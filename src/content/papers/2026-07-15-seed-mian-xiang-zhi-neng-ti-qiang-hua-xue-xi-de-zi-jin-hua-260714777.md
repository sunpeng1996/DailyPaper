---
title: 'SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning'
title_zh: SEED：面向智能体强化学习的自进化同策略蒸馏框架
authors:
- Jinyang Wu
- Shuo Yang
- Zhengxi Lu
- Fan Zhang
- Yuhao Shen
- Lang Feng
- Haoran Luo
- Zheng Lian
- Shuai Zhang
- Zhengqi Wen
affiliations:
- 清华大学
- 浙江大学
- 香港中文大学
- 南洋理工大学
- 同济大学
arxiv_id: '2607.14777'
url: https://arxiv.org/abs/2607.14777
pdf_url: https://arxiv.org/pdf/2607.14777
published: '2026-07-15'
collected: '2026-07-17'
category: Agent
direction: Agent强化学习 · 自进化同策略蒸馏
tags:
- Agentic RL
- On-Policy Distillation
- Hindsight Learning
- LLM Agent
- Reinforcement Learning
one_liner: 提出自进化同策略蒸馏框架SEED，将轨迹事后技能转化为稠密token级监督，提升长周期Agent任务性能与样本效率
practical_value: '- 电商导购Agent、搜索多轮交互Agent的RL优化可复用SEED的稠密监督构造思路：将同策略交互轨迹转化为自然语言事后技能，通过同策略蒸馏把技能内化为模型能力，无需推理时加额外prompt或RAG检索技能库，降低部署复杂度

  - 多轮推荐、长周期用户决策路径的策略优化可借鉴自进化闭环设计：用当前策略同时做行为采样和轨迹归因分析，保证监督信号和当前策略分布对齐，避免静态规则/离线技能库过时的问题，提升样本效率

  - 稀疏奖励场景（如推荐长链路转化、Agent工具调用）的credit assignment可复用skill-induced概率偏移的门控蒸馏loss：把轨迹级的成功/失败经验拆解为token级的监督信号，解决传统RL稀疏反馈指导不足的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期LLM Agent任务中，传统基于结果的RL仅提供轨迹级稀疏奖励，无法为中间决策、token级策略学习提供细粒度指导，存在episode级反馈和token级学习之间的监督鸿沟；现有事后学习方法多把经验存为静态记忆或推理时上下文，无法随策略进化自适应调整，易出现分布不匹配，指导效率低。

### 方法关键点
- 两阶段训练：第一阶段为事后技能SFT，基于离线轨迹+外部标注的技能对微调模型，让模型具备从完整轨迹提取可复用工作流、避坑规则等自然语言技能的能力
- 自进化同策略蒸馏闭环：每轮迭代用当前策略快照同时承担轨迹采样actor和轨迹分析analyzer角色，从新采集的同策略轨迹中提取事后技能，经验分布与监督信号随策略共同进化
- 稠密监督构造：固定采样的动作token，分别在原始上下文和技能增强上下文下重打分，将技能带来的概率偏移转化为门控的token级蒸馏损失，和GRPO的RL损失联合优化

### 关键实验
在ALFWorld（具身交互）、Search-based QA（搜索问答）、WebShop（电商交互）三个基准测试，对比GRPO、Skill-GRPO、SDAR等基线，以Qwen2.5-3B为骨干时，ALFWorld平均成功率比GRPO高16.8个百分点，WebShop成功率高15.6个百分点；仅用60%训练数据就能超过全量数据训练的GRPO，跨域泛化成功率比GRPO高15.3个百分点。

最值得记住的结论：将事后技能内化为模型参数比推理时额外插入技能prompt效果更优，自进化同策略监督相比静态蒸馏能更好适配策略的动态进化过程。
