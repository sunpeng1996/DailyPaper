---
title: Steering Neural Network Training through Interpretable Constraints Based on
  Partial Dependence
title_zh: 基于偏依赖可解释约束的神经网络训练引导方法
authors:
- Yann Claes
- Pierre Geurts
- Vân Anh Huynh-Thu
affiliations:
- Montefiore Institute, University of Liège
arxiv_id: '2607.08641'
url: https://arxiv.org/abs/2607.08641
pdf_url: https://arxiv.org/pdf/2607.08641
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 可解释AI · 模型训练约束优化
tags:
- Interpretable AI
- Partial Dependence
- Training Constraint
- Explanation-Guided Learning
- Regression
one_liner: 提出基于Partial Dependence的可解释训练约束，使模型行为对齐领域先验，提升效果与数据效率
practical_value: '- 推荐/广告模型训练时，可将确定性业务先验（例如价格对点击率的负向影响、活动力度对转化率的正向曲线）转化为Partial Dependence约束加入损失，避免模型学到违背业务常识的特征关联，降低bad
  case概率

  - 冷启动等小样本场景（例如新品推荐、新行业广告投放），可引入该约束对齐已知领域知识，大幅降低对标注数据的依赖，提升模型数据效率

  - 对可解释性合规要求高的场景（例如金融借贷推荐、医疗相关内容推送），可通过该方法确保模型解释与业务共识一致，满足监管要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有XAI研究多聚焦事后解释方法，极少探索如何引导模型生成符合领域先验的解释，且现有解释引导训练方法多针对分类任务，默认已知高贡献特征，无法适配需对齐函数级先验的回归场景。
### 方法关键点
在常规训练损失之外加入基于Partial Dependence的约束损失，引导模型对指定特征的平均响应严格对齐用户提供的领域函数知识，无需预先假设特征重要性。
### 关键结果
在多类回归任务（含动态系统预测）上验证：相比无约束基准模型，该方法训练的模型效果更优，数据效率显著提升，且模型输出解释100%对齐输入的先验知识，无约束模型无对齐能力
