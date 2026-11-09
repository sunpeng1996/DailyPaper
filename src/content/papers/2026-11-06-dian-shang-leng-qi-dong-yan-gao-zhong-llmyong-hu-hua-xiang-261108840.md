---
title: 'What Matters for LLM Persona Simulation: Signal Form in Cold-Start E-Commerce
  Advertising'
title_zh: 电商冷启动广告中LLM用户画像模拟的关键信号形式研究
authors:
- Jiwoo Choi
- In Ik Lee
- Woo Sung Seo
- Minho Lee
- Yun Young Choi
affiliations:
- Dosan International, South Korea
- SolverX, South Korea
arxiv_id: '2611.08840'
url: https://arxiv.org/abs/2611.08840
pdf_url: https://arxiv.org/pdf/2611.08840
published: '2026-11-06'
collected: '2026-11-09'
category: RecSys
direction: 广告冷启动 · LLM用户画像模拟
tags:
- LLM
- Persona Simulation
- Cold-start Advertising
- CTR Prediction
- Prompt Engineering
one_liner: 识别3种LLM广告用户画像模拟关键信号维度，冷启动CTR预估误差较最优非LLM基线降51.3%
practical_value: '- 冷启动广告CTR预估可直接复用LLM用户模拟方案，无需历史交互数据，适配新品、新投放计划的前置效果评估场景

  - 用户画像prompt不要添加职业、性格、时间等冗余属性，仅保留平台原生可定向的基础人口统计学属性即可，避免模型过度推断用户偏好拉高误差

  - banner blindness校准信号优先用相对定性描述，不要用定量CTR锚点（如明确告知平均CTR为0.5%），定量锚点会严重扭曲模型的点击倾向预测

  - prompt措辞是不可忽视的优化维度，相同语义不同表述会带来8%~30%的误差波动，上线前需做多版本A/B测试选定最优表述'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
电商冷启动广告场景下，新品/新投放计划无历史用户交互数据，传统CTR预估模型无法生效；LLM基于用户画像模拟点击行为是潜在解决方案，但此前业界不清楚哪些设计选择决定模拟精度，且广告点击是低概率行为，用户即使对商品感兴趣也可能因banner blindness忽略广告，直接模拟会严重高估点击率。

### 方法关键点
- 拆解影响模拟效果的三类信号维度：用户画像粒度、广告上下文信号类型、prompt措辞
- 最优prompt配置：仅用基础人口统计学画像（年龄、性别、生育状态、收入、兴趣），不添加时间、性格、职业等冗余属性；搭配通用banner blindness提醒+相对定性的广告盲差异描述，不使用任何定量CTR锚点
- 多次重复模拟单用户二元点击决策，聚合得到分人群的CTR预估结果

### 关键实验
数据集为真实Google Ads果冻品类7天投放数据，覆盖5个人口统计学人群，共97.4万次曝光、3578次点击；对比非LLM基线（固定CTR先验、基于年龄的规则CTR映射）、多种LLM变体（添加定量CTR锚点、丰富用户画像等）；最优配置MAE为24.9、MAPE为26.1%，较最优非LLM基线MAE下降51.3%，较带显式CTR锚点的LLM配置MAE下降77.3%；消融实验显示冗余用户属性会提升误差，定量锚点误差是相对定性信号的2.9倍，相同语义不同措辞的误差波动达8%~30%。

### 核心结论
给LLM注入领域知识时，信号的表达形式比注入的知识量更重要，过度丰富的属性、硬定量锚点反而会损伤模拟效果。
