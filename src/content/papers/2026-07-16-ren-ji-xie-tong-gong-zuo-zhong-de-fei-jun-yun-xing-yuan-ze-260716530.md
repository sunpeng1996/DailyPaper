---
title: Nonuniformity Principle in Human-AI Coworking
title_zh: 人机协同工作中的非均匀性原则
authors:
- An Luo
- Jie Ding
affiliations:
- University of Minnesota
arxiv_id: '2607.16530'
url: https://arxiv.org/abs/2607.16530
pdf_url: https://arxiv.org/pdf/2607.16530
published: '2026-07-16'
collected: '2026-07-22'
category: Agent
direction: Agent 人机协同监督调度优化
tags:
- Human-AI-Collaboration
- Agent-Oversight
- Long-Horizon-Agent
- Workflow-Optimization
- Scalable-Oversight
one_liner: 提出人机协同非均匀性原则，最优人类监督间隔沿工作流非递减，平衡对齐质量与人力成本
practical_value: '- 长链路Agent任务（如电商文案全流程生成、广告素材审核链）可直接采用前密后疏的非递减间隔监督策略，减少后期返工和token消耗

  - 人力成本高的业务场景（如高客单价商品推荐策略审核、合规内容审核）可复用论文给出的贪心调度算法，输入业务自定义的任务阶段数、监督次数、审核效果系数、成本-误差比即可快速计算最优监督点

  - 落地时可先小流量跑数，用实际业务的审核成本、对齐误差数据校准κ和η参数，快速适配自身业务流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长 horizon Agent 任务（文本生成、代码生成、科学发现等）已大规模落地，人类监督是保障输出对齐人类意图、控制风险的核心手段，但人力时间成本有限，现有研究缺乏最优监督节点调度的可落地指导，不合理的监督安排要么导致输出质量不达标，要么造成人力成本浪费。
### 方法关键点
- 形式化人机协同调度问题：T个任务阶段内分配K次人类监督，目标是最小化「最终输出与人类隐式意图的对齐损失+人类监督总成本」
- 提出非均匀性原则：最优监督点的间隔沿工作流非递减，前期监督更密集——早期干预能快速缩小Agent的搜索空间，对齐人类隐式意图，后期监督成本随已完成内容增加而升高，可降低监督频率
- 给出可直接落地的贪心调度算法：仅需输入任务阶段数T、监督次数K、监督后误差残留系数κ、成本-误差比η，即可快速计算最优监督点序列
### 关键实验
在两个长链路任务上验证：①40篇ICLR 2026论文的相关工作生成任务；②10个HTML页面构建任务，均设置T=10、K=3，对比5种监督策略+无监督基线。符合非均匀性原则的策略均位于Pareto前沿：相关工作生成任务中Spread策略（间隔1/3/5）质量达5.06（满分10），比均匀间隔策略高0.05、成本低58tokens；HTML构建任务中Tilt-Early策略（间隔1/2/3）质量达7.74，比均匀间隔策略高0.18、成本低33%。
### 核心结论
长链路人机协同的最优监督策略一定是前密后疏的非递减间隔安排，而非均匀或前疏后密。
