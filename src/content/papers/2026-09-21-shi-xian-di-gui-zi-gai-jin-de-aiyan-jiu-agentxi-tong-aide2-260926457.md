---
title: Recursive self-improvement of AI research agents
title_zh: 实现递归自改进的AI研究Agent系统AIDE2
authors:
- Dhruv Srikanth
- Bingchen Zhao
- Dixing Xu
- Yuxiang Wu
- Zhengyao Jiang
affiliations:
- Weco AI
arxiv_id: '2609.26457'
url: https://arxiv.org/abs/2609.26457
pdf_url: https://arxiv.org/pdf/2609.26457
published: '2026-09-21'
collected: '2026-09-23'
category: Agent
direction: Agent 递归自优化系统设计与验证
tags:
- RecursiveSelfImprovement
- ResearchAgent
- BiLevelOptimization
- CodeOptimization
- RewardHacking
one_liner: 实现AI研究Agent的递归自改进循环，8天迭代效果超过两年人力研发的生产级Agent
practical_value: '- 双循环自优化架构可直接迁移到推荐/广告Agent的迭代场景：外层优化Agent的搜索策略、上下文管理等harness层代码，内层在召回策略优化、商品文案生成等业务任务上验证效果，大幅降低人力调优成本

  - 公私评价分离机制可复用在业务Agent迭代中：内层优化仅开放公开反馈信号，外层准入用私有离线/线上A/B指标做筛选，有效降低Reward Hacking，例如避免电商文案Agent为短期点击率作弊伤害长期用户体验

  - 可直接复用其迭代出的Agent优化trick：bandit多臂搜索策略平衡探索与收敛，动态上下文压缩机制将prompt长度降低7~50倍，大幅提升Token使用效率，适合资源受限的线上Agent场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI研究Agent已能自动化大量R&D环节，但Agent自身的能力迭代仍依赖人力研发，研发投入的边际收益持续递减。递归自改进被认为是突破该瓶颈的潜在路径，但此前前沿研究Agent的自优化效果、泛化性尚未得到验证。
### 方法关键点
- 双循环优化架构：内层Agent面向ML工程、启发式算法优化等具体R&D任务迭代代码，外层Agent对内层Agent的harness层（搜索策略、上下文管理、验证逻辑等非模型代码）做改写，形成递归优化闭环
- 公私评价分离机制：内层优化仅能访问公开任务反馈，外层准入使用私有held-out数据集打分，从机制上避免过拟合与Reward Hacking
- 固定算力预算约束：所有Agent迭代都在相同算力成本下评估，确保性能提升来自算法优化而非额外资源投入
### 关键实验结果
8天自主运行生成100个候选Agent，筛选出7个连续改进版本；对比基线为Weco团队迭代2年的生产级研究Agent AIDEhuman；最终版本AIDE85在4个跨领域held-out基准（3个同分布、1个OOD天气预测任务）上全部匹配或超过AIDEhuman；额外OOD任务上Reward Hacking率从初始的55%降至32%，比AIDEhuman低7个百分点。
### 核心洞见
AI Agent的harness层（而非模型本身）迭代可通过自优化实现，且优化收益能跨领域泛化，甚至涌现出未被显式优化的能力
