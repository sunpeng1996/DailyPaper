---
title: End-to-End Fairness Optimization with Fair Decision-Focused Learning
title_zh: 基于公平决策聚焦学习的端到端公平性优化框架
authors:
- Yu Wang
- Violet
- Chen
affiliations:
- Stevens Institute of Technology
arxiv_id: '2607.29441'
url: https://arxiv.org/abs/2607.29441
pdf_url: https://arxiv.org/pdf/2607.29441
published: '2026-07-31'
collected: '2026-08-04'
category: Other
direction: 公平决策优化 · 端到端学习
tags:
- Fairness Optimization
- Decision-Focused Learning
- End-to-End Learning
- Resource Allocation
- Multi-Task Learning
one_liner: 提出端到端公平优化框架与公平决策聚焦学习范式，联合优化预测决策全流程公平性
practical_value: '- 电商资源分配场景（广告预算、流量倾斜、权益发放等）可复用该框架，同时优化预测侧（如转化率预测）的群体准确率差异和决策侧的分配公平性，避免单阶段优化的公平漏判

  - 多目标训练可借鉴FDFL的梯度融合方案，将决策公平损失作为预测模型训练的额外约束，端到端降低预测误差带来的决策公平退化

  - 涉及约束型决策的Agent系统可复用可微优化层+闭式解的实现思路，解决决策层对预测层参数求导的落地问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有预测-决策两阶段系统的公平性通常在预测、决策侧分开优化，预测阶段的跨群体准确率偏差会直接传导到决策侧，导致最终资源分配的公平性损失，单阶段优化无法覆盖全流程公平风险。
### 方法关键点
1. 提出E2EFO端到端公平优化统一框架，面向群体公平的资源分配场景，同时约束预测阶段跨群体准确率差异、决策阶段alpha公平性指标；
2. 提出FDFL公平决策聚焦学习范式，通过多任务梯度融合，联合优化预测精度、预测公平性、预测误差导致的决策公平损失三项目标；
3. 推导易处理公平分配场景下决策雅可比闭式解，通用场景引入可微优化层解决求导问题，同时给出FDFL目标的有限样本泛化界。
### 关键结果
医疗单资源分配、合成多资源分配实验验证，相比分阶段优化公平性的基线方案，联合优化方案的决策公平损失显著降低，同时预测精度无明显衰减。
