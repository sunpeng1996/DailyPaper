---
title: 'Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research'
title_zh: Épi：支持跨会话持续迭代进化的自主科研智能体
authors:
- Yue Huang
- Zhangchen Xu
- Xiaonan Luo
- Zheyuan Liu
- Lichi Li
- Yiping Wang
- Peiyang Song
- Eric Gabriel Ramos
- Enze Xie
- Olexandr Isayev
affiliations:
- Bake AI
- MIT
- Stanford University
- Microsoft
- NVIDIA
arxiv_id: '2610.24944'
url: https://arxiv.org/abs/2610.24944
pdf_url: https://arxiv.org/pdf/2610.24944
published: '2026-10-17'
collected: '2026-10-21'
category: Agent
direction: 长周期智能体 · 持续迭代架构设计
tags:
- Autonomous Agent
- Hierarchical Memory
- Branching Search
- Self-Improving
- Cost Control
one_liner: 通过层级记忆、版本分支与独立评审实现跨会话自主探索的科研Agent架构
practical_value: '- 层级记忆冷热分离设计可直接迁移到生成式推荐/广告的长会话用户意图理解场景：将用户短期行为、长期兴趣、历史反馈分层存储，查询时仅召回相关片段填充上下文，既降低token消耗又避免信息遗漏

  - 版本分支+自动回溯机制可复用在推荐策略/广告素材A/B测试 pipeline：每个候选策略独立存储完整代码、效果数据、上线原因，效果不达标时一键回滚到历史最优版本，同时保留失败案例避免重复踩坑

  - 固定验证规则(ruler)+独立评审的双校验机制可解决Agent生成方案的自评估偏差问题：在电商文案生成、商品选品场景，先确定统一的转化、合规评估规则，用独立校验模块统一打分，避免Agent生成无效自嗨内容

  - Épi-turbo的预占预算+按需调用机制可将LLM驱动的推荐/广告优化场景的大模型调用成本降低30%以上：提前为每个任务分配调用额度，仅在实验结果能改变后续决策时才调用大模型，避免无效请求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自主Agent仅支持单会话运行，面对跨天/多轮的长周期优化任务时，存在历史状态丢失、经验无法复用、探索方向单一难以回溯的痛点，无法支撑需要持续迭代的复杂科研、工程优化类需求。

### 方法关键点
- 层级记忆架构：拆分短/长时记忆，短存存储当前任务上下文、运行状态，长存存储可复用经验、失败案例及原因，跨会话时仅拉取相关记忆填充上下文，避免历史信息过载
- 版本化分支机制：每个探索方向独立成分支，保留完整代码、实验数据、决策原因，可随时回溯到历史版本重启探索，放弃分支时记录原因留档
- 独立评审+固定验证规则：每个任务启动前先确定统一的评估规则(ruler)与收益阈值，用独立模型评审实验结果合理性，避免自评估偏差与奖励黑客问题
- Épi-turbo轻量化配置：针对算法开发场景裁剪非必要组件，加入预算管控机制，提前预留模型调用额度，成本超支前自动终止无效探索

### 关键实验结果
数学发现任务上产出120项破纪录结果，包括n皇后常数区间收窄84倍、四次费根鲍姆吸引子维度区间收窄超360万倍，还给出了Tuza猜想在分裂图场景的计算机辅助证明；算法开发任务上，在30个FrontierOR运筹优化基准（含路径规划、调度、生产规划等）上，Épi-turbo比Codex总分高5.4%，模型成本仅为后者的64%，生成程序的中位数运行时间从9.3s降到2.9s。

### 核心结论
对于长周期落地的Agent系统，跨会话状态留存、经验复用与成本管控能力的优先级远高于单次推理的效果上限。
