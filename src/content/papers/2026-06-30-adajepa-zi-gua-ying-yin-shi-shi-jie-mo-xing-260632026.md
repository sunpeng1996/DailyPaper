---
title: 'AdaJEPA: An Adaptive Latent World Model'
title_zh: AdaJEPA：自适应隐式世界模型
authors:
- Ying Wang
- Oumayma Bounou
- Yann LeCun
- Mengye Ren
affiliations:
- New York University
- AMI Labs
arxiv_id: '2606.32026'
url: https://arxiv.org/abs/2606.32026
pdf_url: https://arxiv.org/pdf/2606.32026
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent 世界模型测试时自适应优化
tags:
- World Model
- Test-time Adaptation
- MPC
- Self-supervised Learning
- JEPA
one_liner: AdaJEPA是支持测试时自监督自适应的隐式世界模型，大幅提升分布偏移下的规划成功率
practical_value: '- 电商交互导购Agent、多轮推荐场景可复用测试时自适应思路，用用户实时交互反馈做单步梯度更新，无需全量重训即可适配用户实时意图漂移，降低推荐偏差

  - 生成式推荐的多步路径规划模块（如搭配推荐、消费决策路径规划）可借鉴闭环自监督更新范式，用真实用户行为作为自适应信号，无需额外标注即可提升规划准确率

  - 线上低延迟要求的Agent决策模块可参考单步梯度更新的轻量化自适应机制，兼顾适配效果和推理时延，符合线上服务性能约束'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**
现有隐式世界模型训练后测试阶段完全冻结，遇到分布偏移时预测误差会沿规划步长累积，导致MPC规划的动作在真实环境失效，泛化能力不足，不适用于动态变化场景。

**方法关键点**
1. AdaJEPA自适应隐式世界模型支持在MPC闭环内实现测试时自监督自适应，无需额外专家标注或演示数据；
2. 执行逻辑：先规划输出动作序列并执行首个动作块，再用观测到的真实状态转移作为自监督信号做极小步梯度更新，最后用校准后的模型重新规划，实现持续动态适配。

**关键结果**
在多类目标可达任务上，仅需每次MPC重规划步骤做1次梯度更新，即可大幅提升规划成功率。
