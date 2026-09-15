---
title: Expert-Space Exploration in MoE Reinforcement Learning
title_zh: 面向MoE大模型强化学习的专家空间探索方法
authors:
- Hongyi He
- Zhenghao Lin
- Xiao Liu
- Peng Cheng
- Yan Lu
- Yeyun Gong
affiliations:
- Tsinghua University
- Microsoft Research
arxiv_id: '2609.13058'
url: https://arxiv.org/abs/2609.13058
pdf_url: https://arxiv.org/pdf/2609.13058
published: '2026-09-10'
collected: '2026-09-15'
category: Training
direction: MoE大模型 · RL训练优化
tags:
- MoE
- Reinforcement Learning
- GRPO
- Routing Perturbation
- Expert Exploration
one_liner: 提出ESRL可控扰动MoE专家路由框架，无额外计算开销即可提升MoE大模型RL训练效果
practical_value: '- 业务中使用MoE架构LLM做生成式推荐/Agent决策的RL对齐时，可直接复用ESRL框架，无需修改奖励函数与优化目标，兼容现有GRPO训练流程，同时提升生成多样性与效果

  - 锚定高置信度专家+仅在候选池加噪声的trick，可迁移到MoE推荐模型推理阶段，在不显著损失准确率的前提下提升召回/生成结果多样性，缓解推荐同质化问题

  - 熵自适应噪声强度的设计思路，可复用在推荐多臂老虎机探索、用户兴趣探索场景，根据模型置信度动态调整探索力度，平衡探索收益与用户体验损失

  - 路由回放机制可解决MoE模型训练/推理路由不一致问题，业务中做MoE微调/RL训练时可直接接入，降低训练不稳定风险'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoE大模型RL训练仅聚焦优化稳定性与效率，将专家路由视为固定架构组件，仅靠token级采样提供探索多样性，RL训练后期策略集中后多样性显著衰减；而直接扰动路由易激活不匹配专家，导致生成质量大幅下降，亟需架构感知的可控探索机制。

### 方法关键点
- **熵自适应噪声调整**：根据路由分布的归一化熵动态调整扰动强度，路由置信度越高（熵越低）施加的噪声越强，避免对低置信路由过度干扰
- **锚定专家采样**：将激活专家拆分为K_anchored个高置信锚定专家与K_explore个探索专家，仅在Top-M候选专家池内加噪声采样探索专家，既保留可靠计算路径又控制探索范围
- **路由回放**：Rollout阶段记录实际激活的专家路径，优化阶段直接复用该路径，避免训练与Rollout阶段路由不一致导致的探索失效

### 关键实验
在Qwen3-30B、Sigma-20B、Moonlight-16B三种不同MoE架构（top-K/top-1/带共享专家）上测试，覆盖数学、科学推理、代码生成任务，对比GRPO、GSPO等基线：Qwen3-30B数学任务上相对GRPO提升Pass@1 3.2pp、Pass@8 4.5pp；科学&代码任务上相对GRPO平均提升Pass@1 2.8pp、Pass@8 12.2pp；低采样温度下增益更显著，64采样样本效果超过基线128样本效果，采样效率提升1倍。

### 核心结论
MoE的专家路由不仅是架构组件，更是可与token级采样互补的独立探索维度，可控路由扰动可在无额外计算开销的前提下大幅提升RL训练效果。
