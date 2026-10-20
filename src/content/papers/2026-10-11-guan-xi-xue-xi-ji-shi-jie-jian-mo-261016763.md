---
title: Relational Learning as World Modeling
title_zh: 关系学习即世界建模
authors:
- Zheyu Zhang
- Gjergji Kasneci
affiliations:
- Technical University of Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.16763'
url: https://arxiv.org/abs/2610.16763
pdf_url: https://arxiv.org/pdf/2610.16763
published: '2026-10-11'
collected: '2026-10-20'
category: Agent
direction: Agent 关系型世界建模
tags:
- World Model
- Relational Learning
- In-context Learning
- Tabular Data
- Decision Making
one_liner: 构建TabWM表格世界模型与预训练生成器WorldRel，支持上下文学习预测动作引发的关系数据编辑
practical_value: '- 可借鉴TabWM上下文学习预测关系数据变更的思路，搭建电商订单/库存/物流系统的动作影响仿真工具，无需重新训练即可预判促销、改价等运营动作的连锁影响

  - 可复用WorldRel生成合成关系世界做预训练的范式，针对推荐/广告系统的用户-商品-订单关系链生成仿真数据集，预训练可预判业务动作效果的Agent世界模型

  - 递归预测关系编辑生成未来候选状态的方法，可用于电商运营Agent做多步决策搜索，比如在大促前搜索最优的优惠券发放、库存调拨策略提升整体ROI'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统关系学习仅基于现有数据库状态做预测，无法回答运营/决策场景下「动作会如何改变系统状态」的问题，而系统动态规则通常不会显式存在于数据库中。
### 方法关键点
1. 构建WorldRel可执行关系世界生成器，生成多样化的关系动态场景用于预训练；
2. 设计TabWM表格世界模型，无需参数更新，仅用少量观测到的执行记录作为上下文，就能预测新动作引发的稀疏结构化关系编辑，编辑需匹配操作类型、关系位置、值三个维度。
### 关键结果
在512个未见世界的测试集上，完全编辑预测F1从无上下文时的0.016提升到有64条观测上下文时的0.685；基于预测的未来状态做动作序列搜索，可显著提升选中动作的实际收益。
