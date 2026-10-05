---
title: What Should World Models Forget? Stratified Retention for Continual Adaptation
title_zh: 《世界模型该遗忘什么？面向持续适配的分层保留机制》
authors:
- Nishit Anand
- Ramani Duraiswami
- Dinesh Manocha
affiliations:
- University of Maryland, College Park
arxiv_id: '2610.03713'
url: https://arxiv.org/abs/2610.03713
pdf_url: https://arxiv.org/pdf/2610.03713
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent世界模型 · 持续学习分层保留
tags:
- Continual Learning
- World Model
- Knowledge Retention
- Evaluation Metric
- Concept Drift
one_liner: 针对世界模型知识时效性差异，提出分层保留策略及差异化评估指标，区分合理遗忘与灾难性遗忘
practical_value: '- 推荐系统特征可按不变性时长分层：长期不变属性（如物品品类）固定不随增量训练更新，短期属性（如价格、库存）实时迭代，避免旧数据干扰

  - 推荐模型评估可复用差异化保留思路：拆分不变性指标（如品类排序合理性）和时效性指标（如热点内容召回延迟），不使用单一综合指标评估持续学习效果

  - Agent 世界模型更新可采用分层逻辑：物理规则类底层知识冻结，环境实例类知识定期刷新，平衡运行稳定性与环境适配效率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有持续学习默认所有知识需永久保留，将旧数据性能下降全部判定为灾难性遗忘，完全不适用于世界模型：其预测目标是动态变化的环境，过时知识本应被主动丢弃，同时世界模型还存在物理规则等完全不可修改的不变知识，现有评估指标无法区分合理遗忘与灾难性遗忘，甚至会将完全不更新的冻结模型误判为最优。
### 方法关键点
1. 按不变性时间尺度对知识分层：分为不可修改的长期不变知识（如物理规则、物体恒存性）和随环境变化需及时更新的实例级事实两类
2. 提出差异化保留评估方法：同时上报适配流中的不变性回归测试结果和过时知识更新延迟，不做指标聚合
### 关键结果
解决了原有评估体系的误判问题，可准确衡量世界模型的持续适配能力，为动态环境下的模型更新提供了统一的评估范式
