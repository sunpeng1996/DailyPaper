---
title: Towards Zero-Shot Task Transfer with Neurosymbolic World Models
title_zh: 基于神经符号世界模型的零样本任务迁移方法
authors:
- Isidoro Tamassia
- Lennert De Smet
- Giuseppe Marra
affiliations:
- KU Leuven, Department of Computer Science, Belgium
arxiv_id: '2608.17959'
url: https://arxiv.org/abs/2608.17959
pdf_url: https://arxiv.org/pdf/2608.17959
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 零样本任务迁移 · 神经符号世界模型
tags:
- Neurosymbolic AI
- World Model
- Zero-Shot Transfer
- Reinforcement Learning
- Task Generalization
one_liner: 解耦观测重构与奖励预测，基于神经符号世界模型实现同状态空间下新任务零样本迁移
practical_value: '- 电商多场景Agent（智能导购、库存调度等）落地可参考「环境建模+目标预测」解耦思路，同环境预训练模型可快速适配GMV/转化率/客单价等不同业务目标，无需重训环境模型，大幅降低成本

  - 推荐系统多目标迁移场景可复用符号化隐层分量设计，将与业务目标强相关的特征显式抽取为符号化组件，切换目标时仅调整目标预测头即可实现快速冷启动

  - 多任务强化学习落地时，可优先将奖励预测依赖的特征做结构化符号化，降低跨任务迁移的样本需求，适合新业务线快速上线'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于模型的强化学习的神经世界模型隐表示与训练任务强绑定、不可解释，在环境动态不变仅奖励函数调整的场景下泛化性差，无法实现零样本任务迁移。
### 方法关键点
1. 设计神经符号世界模型架构，将全隐态拆分为结构化符号分量 + 通用隐层分量两部分
2. 奖励预测仅依赖结构化符号分量，完全解耦观测重构与奖励预测两个任务
3. 新任务仅需定义基于同符号状态空间的奖励函数，无需额外环境交互即可完成适配
### 关键结果
相比纯神经世界模型，在同环境多奖励函数的迁移任务上泛化性能显著提升，可实现完全零样本任务迁移，不需要额外交互数据支撑。
