---
title: What Should We Ask Next? Retrieval-Aware Question Learning under Partial Evidence
title_zh: 部分证据场景下检索感知的交互式问题学习框架RAVEL
authors:
- Lyucheng Qian
- John Yuehan Zhang
- Pingyu Wang
affiliations:
- Sichuan University
- University of California, Berkeley
arxiv_id: '2609.21924'
url: https://arxiv.org/abs/2609.21924
pdf_url: https://arxiv.org/pdf/2609.21924
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 交互式检索决策优化
tags:
- Interactive Retrieval
- Reinforcement Learning
- Question Generation
- Multimodal LLM
- QLoRA
one_liner: 基于在线RL的检索感知交互式问题生成框架，直接用检索排名反馈优化问题策略
practical_value: '- 电商会话搜索/导购Agent场景可直接复用结论：离线标注的「高区分度/用户感知有用」问题和实际检索增益相关性<0.1，不要迷信人工标注的问题优先级，优先用端到端检索反馈做优化

  - 两阶段低成本训练方案可直接落地：先做SFT冷启动问题生成模型，再用GRPO做在线RL微调，全程固定检索器/回答器，仅更新QLoRA adapter，训练成本仅需26.5
  GPU小时

  - 奖励设计可直接迁移：以Reciprocal Rank提升为基础奖励，加Top1命中额外奖励，叠加无效/重复问题惩罚，配合有效性gate过滤违规输出，避免模型钻奖励漏洞

  - 多轮交互提问策略可参考：优先询问本地化开放属性问题（如鞋款、下装、配饰等），比封闭式yes/no问题能带来3倍以上的检索增益，对初始难query提升尤其明显'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有交互式检索系统依赖离线标注的QA对优先级训练问题生成策略，但问题的实际价值由其触发的回答、后续检索排名变化共同决定，静态标注的区分度、人工感知有用性与最终检索增益的Spearman相关性仅为0.05左右，几乎无指导意义，亟需对接完整检索链路反馈的在线学习方案。

### 方法关键点
- 两阶段训练：先基于LLaVA-OneVision做1 epoch QLoRA SFT冷启动问题生成器，再用Group Relative Policy Optimization做在线RL微调，全程固定检索器、回答器，仅更新问题生成器的QLoRA adapter
- 状态输入：直接向问题生成器输入当前Top-4检索候选、对话历史、累计检索文本、轮次信息，无额外候选选择模块
- 奖励设计：以Reciprocal Rank提升为基础奖励，加命中Rank1的0.35额外奖励，重复问题罚0.02，无效问题罚0.2，配合有效性gate过滤不符合交互协议的问题
- 训练逻辑：每个状态采样G个候选问题，分别走完提问-回答-重检索全链路，用组归一化的排名反馈更新策略

### 关键结果
在Interactive-PEDES数据集5轮交互实验中，RAVEL的Rank-1达到73.73%，比SOTA基线LLaVA-ReID高5.79个点，BRI降低0.061；迁移到CUHK-PEDES等3个通用文本ReID数据集，Rank-1平均提升8个点以上。

### 最值得记住的一句话
交互式检索中，静态标注的「好问题」毫无价值，只有能实际带来检索排名提升的问题才是好问题。
