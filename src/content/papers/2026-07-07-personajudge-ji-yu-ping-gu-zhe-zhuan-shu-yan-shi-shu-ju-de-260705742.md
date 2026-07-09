---
title: 'PERSONAJUDGE: Simulating Individual Human Preference Judgments with Evaluator-Specific
  Demonstration Data'
title_zh: PERSONAJUDGE：基于评估者专属演示数据的个体偏好判断模拟
authors:
- Zeyu He
- Xuan Qi
- Subramanian Chidambaram
- Zhichao Xu
- Vinayak Arannil
- Lydia Chilton
- Alex C. Williams
affiliations:
- Pennsylvania State University
- AWS AI Fundamental Research
- Columbia University
arxiv_id: '2607.05742'
url: https://arxiv.org/abs/2607.05742
pdf_url: https://arxiv.org/pdf/2607.05742
published: '2026-07-07'
collected: '2026-07-09'
category: Eval
direction: 个性化评估 · LLM-as-Judge 优化
tags:
- LLM-as-Judge
- Preference Modeling
- In-Context Learning
- Personalized Evaluation
- Human-AI Alignment
one_liner: 结合评估者专属辅助数据通过上下文学习实现LLM对单个人类偏好的模拟，效果较基线最高提升9.9pp
practical_value: '- 做用户个性化偏好对齐时，优先采集用户的决策 reasoning traces 而非泛化行为埋点，前者对偏好模拟的增益更高，后者甚至可能引入噪声

  - 搭建 LLM-as-Judge 个性化评估 pipeline 时，可通过评估者的中立判断占比、与共识的偏差程度预判模拟难度，优先筛选高可模拟性样本提升评估效率

  - 跨任务用户偏好建模时，可将用户的中立使用倾向作为稳定特征引入，其跨任务相关性达 0.728，比个体可模拟性特征鲁棒性更强'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有 LLM-as-Judge 方案普遍依赖共识偏好做评估，忽略不同评估者的个体差异，无法适配个性化评估、个体偏好对齐等场景需求。
### 方法关键点
提出 PERSONAJUDGE 框架，将分类判断结果、评估者专属辅助数据（回顾式推理轨迹、界面埋点数据）组织为专属演示样例，通过 in-context learning 实现对单个评估者偏好判断的模拟；实验采用 4×4×4 因子设计，覆盖 32 名受过训练的标注员的 4200 条偏好判断数据。
### 关键结果
1. 整体性能较 Base Judge 最高提升 9.9pp；
2. 推理轨迹的性能增益最大但采集成本更高，低成本的界面埋点反而通常会损害模型性能；
3. 评估者的中立判断占比、与共识的偏差程度可预测模拟难度，其中立使用倾向是跨任务稳定属性（相关系数 r=0.728）。
