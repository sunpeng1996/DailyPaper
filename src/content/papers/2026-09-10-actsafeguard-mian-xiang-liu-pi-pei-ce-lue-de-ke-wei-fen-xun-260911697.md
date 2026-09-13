---
title: 'ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for
  Flow-Matching Policies'
title_zh: ActSafeGuard：面向流匹配策略的可微分训练对齐约束执行框架
authors:
- Jianming Ma
- Rongjun Jin
- Xiaxi Si
- Yang Zhang
- Yiheng Li
- Yue Gao
affiliations:
- Shanghai Jiao Tong University
- Shanghai Institute of Innovation
arxiv_id: '2609.11697'
url: https://arxiv.org/abs/2609.11697
pdf_url: https://arxiv.org/pdf/2609.11697
published: '2026-09-10'
collected: '2026-09-13'
category: Training
direction: 生成式策略约束 · 训练对齐防护
tags:
- Flow Matching
- Constraint Enforcement
- Differentiable Layer
- Safe Deployment
- Embodied AI
one_liner: 提出可微分训练对齐的防护层，实现流匹配策略输出100%符合硬约束且不降低任务性能
practical_value: '- 生成式输出带硬约束的场景（如合规文案生成、广告出价生成、权益发放额度控制），不要仅做推理侧后处理修正，可将约束规则封装为可微分层嵌入训练流程，从根源解决训推不一致导致的违规问题

  - 边界感知梯度的射线缩放算子设计思路可复用，避免传统截断后处理导致的梯度消失/偏差，让模型主动学习合法输出区间，不需要额外调整损失函数

  - 低侵入式safeguard层架构可直接对接现有主干模型，不需要改写原有训练pipeline，适合业务侧快速验证新增约束规则，迭代成本低'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
VLA、WAM等具身生成式策略生成的输出常违反物理硬约束，现有安全方案要么仅优化统计安全目标无逐步确定性保证，要么仅在推理侧做后置修正，存在严重训推不一致，部署时易出现不可行风险。
### 方法关键点
1. 设计可微分、训练对齐的ActSafeGuard防护层，将硬约束直接融入策略学习流程，而非仅作为推理侧外挂组件
2. 实现解析射线缩放算子，支持边界感知梯度回传，引导模型自然学习合法输出流形，对原有主干模型完全无侵入
### 关键结果数字
在π₀.₅、Fast-WAM等多个标准主干、多任务场景下验证，可实现100%逐步输出安全率，同时完整保留甚至提升原有任务的成功率，可扩展性强
