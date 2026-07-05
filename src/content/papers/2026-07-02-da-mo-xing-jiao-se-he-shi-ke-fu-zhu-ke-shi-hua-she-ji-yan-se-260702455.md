---
title: When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color
  Assignment and Chart Choice
title_zh: 《大模型角色何时可辅助可视化设计？颜色分配与图表选择的跨模型研究》
authors:
- Shahreen Salim
- Klaus Mueller
affiliations:
- Stony Brook University
arxiv_id: '2607.02455'
url: https://arxiv.org/abs/2607.02455
pdf_url: https://arxiv.org/pdf/2607.02455
published: '2026-07-02'
collected: '2026-07-05'
category: LLM
direction: LLM人格模拟 可视化设计效果评估
tags:
- LLM-persona
- visualization-design
- cross-model-evaluation
- big-five
- user-simulation
one_liner: 跨3款GPT模型量化LLM人格角色在两类可视化设计任务中的适用边界
practical_value: '- 做电商UI/营销素材个性化设计时，不要过度依赖LLM persona模拟用户偏好，必须补充无persona基线和小流量真人验证

  - 抽象类营销概念（如「高端」「性价比」）的广告/商品页配色可先用LLM persona做灵感探索，具体品类（如生鲜、3C）的配色优先复用业务沉淀的成熟规则

  - 用LLM做用户偏好模拟时必须做多模型交叉验证，单模型输出的人格关联结果大概率是模型自身偏差，不可直接落地'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
早期可视化设计阶段常用LLM persona模拟不同用户的偏好，但其输出的稳定性一直不明确，无法区分结果是真实人格效应还是模型配置、任务框架带来的偏差。
### 方法关键点
基于大五人格的43种特征profile，在GPT-4o-mini、GPT-4.1-mini、GPT-5-mini三个模型上测试两类可视化相关任务：抽象/具体概念的颜色分配、不同任务上下文下的图表类型偏好。
### 关键结果数字
1. 人格-颜色关联高度依赖模型配置：GPT-4o-mini全6类概念无关联，GPT-4.1-mini全场景稳定关联，GPT-5-mini仅2/6场景存在关联；
2. 抽象概念下人格对色调方差的解释度高于模型本身，具体概念下两者效应相当且数值更小；
3. 图表选择任务中8/9的模型-上下文组合下，无persona基线和带persona输出的Top1选择一致，任务上下文对首选项的影响远高于人格特征。
