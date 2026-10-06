---
title: 'MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution
  for Medical VQA Tasks'
title_zh: MedPrune：面向医疗VQA的拓扑高效多模态多智能体通信进化框架
authors:
- Jiuheng Wan
- Runze Li
- Chen Chen
- Tingyuan Hu
- Daiyang Yu
- Yimin Jing
- Taolin Zhang
- Richang Hong
affiliations:
- 合肥工业大学
- 南京大学
- 广东财经大学
- 华东师范大学
- 联想天禧AI技术平台
arxiv_id: '2610.06695'
url: https://arxiv.org/abs/2610.06695
pdf_url: https://arxiv.org/pdf/2610.06695
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: 多模态多智能体 · 通信拓扑剪枝
tags:
- Multi-Agent
- Communication Pruning
- Medical VQA
- Multimodal LLM
- Reinforcement Learning
one_liner: 通过动态剪枝多智能体通信拓扑的节点与边，实现医疗VQA任务性能与token效率的双重提升
practical_value: '- 多智能体系统可直接复用节点+边二阶剪枝思路：先基于RL剪去任务无关的智能体节点，再通过核范数正则化剪去低价值通信边，大幅降低token开销同时提升效果，可迁移到电商导购、用户需求理解等多智能体场景

  - 剪枝优化时采用核范数正则化代替显式剪枝约束，能自动诱导低秩稀疏拓扑结构，无需人工定义剪枝规则，降低多智能体系统的配置成本

  - 小样本场景下仅优化通信拓扑、冻结LLM参数的训练范式，可迁移到标注数据稀缺的垂直领域推荐/客服多智能体系统，避免微调导致的知识遗忘'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有医疗多智能体系统多采用静态预定义通信拓扑，存在大量冗余交互，token开销随智能体数量与交互轮次指数级增长，同时冗余连接易传播错误信息、降低推理精度，无法适配复杂多变的临床诊断需求。
### 方法关键点
- 将多科室协同诊断过程建模为异构通信图，节点对应不同专科Agent，边分为科室内部、跨科室的时空两类交互边
- 异构节点剪枝：采用Gumbel-Softmax参数化软邻接矩阵，基于策略梯度RL以任务性能为奖励优化拓扑，按节点加权度剪去任务无关Agent，从初始阶段消除无效token开销
- 异构边剪枝：节点剪枝后，以「最大化任务性能+核范数正则化约束拓扑复杂度」为复合目标，渐进式剪去低价值交互边，仅保留高诊断价值的连接
### 关键结果
在MIMIC-CXR、IU-Xray、OmniMedVQA三个权威医疗VQA基准上测试，全量训练下平均性能较最优基线提升3.65%，token效率提升37.86%；对抗攻击下性能仅下降3.1%，鲁棒性显著优于基线；10样本小样本训练下性能接近全量训练水平，无需更新LLM参数即可适配小样本场景。

多智能体系统的效率优化核心是剪掉无效的节点和交互，而非盲目增加智能体数量或交互轮次
