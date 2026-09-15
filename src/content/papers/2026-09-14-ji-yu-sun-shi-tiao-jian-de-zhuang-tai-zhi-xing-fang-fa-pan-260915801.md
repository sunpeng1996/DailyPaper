---
title: When Should a World Model Move? Loss-Conditioned State Execution
title_zh: 基于损失条件的状态执行方法：判断何时触发世界模型更新
authors:
- Jintao Xu
- Zhengyu Chen
- Ben Zhang
- Yongzhi Qi
- Jianshen Zhang
affiliations:
- JD.com Supply Chain Tech Team Y
arxiv_id: '2609.15801'
url: https://arxiv.org/abs/2609.15801
pdf_url: https://arxiv.org/pdf/2609.15801
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: Agent 世界模型执行决策优化
tags:
- World_Model
- Decision_Making
- Calibration
- Inventory_Forecasting
- Loss_Optimization
one_liner: 提出模型无关的损失条件状态执行机制，判断执行世界模型提案或保留当前状态
practical_value: '- 电商库存预测场景可复用该框架，无需全量执行世界模型预测，仅对损失增益置信度为正的分组更新，降低计算成本同时提升预测精度

  - Agent 世界模块设计时，可替代传统仅靠预测置信度的调用逻辑，基于下游业务损失校准触发条件，避免预测准确但业务损失升高的问题

  - 推荐系统的策略更新/召回结果刷新决策可复用该分组校准逻辑，对不同用户/物品组单独判断是否执行新策略，降低全量上线风险'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
世界模型传统仅依靠预测置信度判断是否更新状态，常出现预测排序精度高但下游业务损失反而上升的问题，无法保证更新的实际收益。
### 方法关键点
1. 形式化定义状态可迁移性为存在可降低损失的可行修正，与单一提案的收益解耦；
2. 从预测分布生成损失相关的可行提案，在独立校准单元上分组评估提案相对保留当前状态的有界损失增益，仅对增益置信下界为正的组执行更新；
3. 理论证明校准单元独立同分布时，被接受的分组高概率比保留原状态的期望损失更低。
### 关键结果
- M4月度预测数据集上，仅对14.0%的序列执行提案，bounded loss达0.588，优于保留原状态的0.599和全量执行的0.621；
- 京东6类不健康库存约束预测场景验证，即使预测排序信号很强，仍存在大量保留原状态损失更低的情况，证明事件可预测性与状态执行需分开评估。
