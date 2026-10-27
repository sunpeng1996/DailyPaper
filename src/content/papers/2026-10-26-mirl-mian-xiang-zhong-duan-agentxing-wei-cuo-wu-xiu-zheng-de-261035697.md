---
title: 'MiRL: Error-Targeted Reinforcement Learning for Correcting Terminal Agent
  Misbehaviors'
title_zh: MiRL：面向终端Agent行为错误修正的定向强化学习方法
authors:
- Runchu Tian
- Zaid Khan
- Zun Wang
- Justin Chih-Yao Chen
- Mohit Bansal
affiliations:
- University of North Carolina at Chapel Hill
arxiv_id: '2610.35697'
url: https://arxiv.org/abs/2610.35697
pdf_url: https://arxiv.org/pdf/2610.35697
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: Agent训练优化 · 错误定向强化学习
tags:
- Reinforcement Learning
- LLM Agent
- Terminal Agent
- Data Efficiency
- Error-Targeted Learning
one_liner: 通过定位Agent泛化错误模式，从错误步骤启动RL训练，大幅提升终端Agent训练效率与性能
practical_value: '- 可复用错误定向优化框架：先聚类业务中占比最高的通用错误（如电商导购Agent答非所问、推荐系统重复召回），替代零散修复单case，优化ROI更高

  - RL训练算力优化技巧：无需全链路rollout，从错误发生的前缀步骤启动训练，可大幅减少无效计算，适合算力有限的业务场景

  - 奖励函数设计思路：在最终任务reward之外增加行为约束reward，避免出现「结果正确但路径违规」的伪正例（如客服答对但漏了合规话术）'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有终端Agent训练依赖大规模环境采样，单轮训练动辄需要数天8卡H100算力，成本极高；而此前的错误定向学习仅适配单轮任务，无法直接迁移至多步长的终端Agent场景，同时现有Agent错误分析仅用于调试，未用于驱动训练，大量算力浪费在模型已经能正确执行的步骤上。
### 方法关键点
- 错误画像：先跑通现有策略的全量轨迹，定位每一步错误，聚类出跨环境重复出现的通用错误模式，实验中8类高频错误覆盖了52.1%的总错误步
- 前缀启动RL：训练时从错误发生的前缀步骤直接启动rollout，无需从任务初始状态跑起，大幅减少无效步骤的算力消耗
- 双维度奖励设计：仅当rollout同时满足「最终任务通过」和「未触发目标错误」两个条件时才给正反馈，避免「结果正确但行为错误」的伪正例强化
### 关键结果
基于Qwen3.5-4B训练，在Terminal-Bench Lite上准确率达51.8%，优于SOTA TMax-4B的47.4%；在Terminal-Bench 2.1上准确率21.3%与TMax-4B持平，仅用后者35%的rollout量，总训练成本降低44%；训练后目标错误的发生频率平均降低43%~57%。
> 最值得记住的一句话：少部分可泛化的高频错误贡献了大部分的任务失败，定向优化这些错误的效率远高于盲目扩大训练数据集
