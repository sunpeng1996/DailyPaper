---
title: 'Abstract Priorities, Concrete Rewards: How Stated Preferences Relate to What
  People Reward in AI Responses'
title_zh: 抽象偏好与实际奖励：用户声明偏好与AI响应评分的关联研究
authors:
- Zihan Chen
- Lei Nico Zheng
- Di Zhu
affiliations:
- Stevens Institute of Technology
- University of Massachusetts Boston
arxiv_id: '2610.30763'
url: https://arxiv.org/abs/2610.30763
pdf_url: https://arxiv.org/pdf/2610.30763
published: '2026-10-22'
collected: '2026-10-23'
category: Eval
direction: LLM偏好对齐 · 人类偏好评估
tags:
- LLM Alignment
- Preference Elicitation
- Human Feedback
- Stated Preference
- Revealed Preference
one_liner: 揭示用户声明的抽象偏好与AI响应实际评分的关联依赖属性度量方式，个人偏好信息预测增益极低
practical_value: '- 做电商导购Agent、个性化文案生成时，优先优化响应长度、格式、拒答话术等具象特征，这些特征对用户满意度的影响远高于用户声明的「准确」「有创意」等抽象属性

  - 采集用户偏好时，优先抓取用户主动提出的具象反馈（比如「要更短」「要更多例子」），其对个性化的增益远高于抽象偏好问卷的结果

  - 搭建个性化推荐/Agent系统时，先投入资源优化通用基线模型，其效果增益（本研究中达1.11pp）远高于叠加少量用户个人偏好数据的增益（最高0.13pp）

  - 做RLHF标注时要校准标注结果，避免把用户对长度、格式等具象特征的偏好误判为对事实性、有用性等抽象属性的偏好'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM对齐、个性化Agent、生成式推荐系统都高度依赖用户声明的抽象偏好（如希望响应准确、简洁、安全），但这类声明偏好和用户实际为响应打分时的奖励信号是否一致尚未被系统验证，直接影响偏好采集、个性化策略的设计效率。
### 方法关键点
- 基于PRISM公开数据集：1396名参与者先完成7项AI响应属性的重要性评分，随后开展会话并为21个LLM生成的29347条回复打分，配套会话后开放反馈数据
- 设计三类属性度量方式做对照：匹配声明属性的文本proxy、拟合用户感知的复合特征、其他用户对模型的聚合感知属性
- 固定prompt做组内对比，控制模型、展示位置等干扰变量，对比不同信息源对用户holdout选择的预测增益
### 关键结果
- 未被问卷采集的具象特征（长度、格式、拒答语言）对评分的影响至少和7项声明属性的文本proxy相当，响应长度每提升1个标准差，评分升高5.56分
- 声明偏好与评分的对齐度高度依赖度量方式：与模型级聚合感知属性的相关系数为0.93，与文本proxy仅为0.08
- 个人偏好信息对holdout选择预测的最大增益仅0.13pp，而优化通用基线模型可带来1.11pp的准确率提升

最值得记住的结论：用户声明的抽象偏好仅能匹配群体层面的感知属性，完全无法预测用户实际打分时依赖的具象特征，优先优化通用模型的收益远高于堆砌少量个人偏好数据。
