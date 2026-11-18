---
title: What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution
title_zh: '"偏见头"实际度量什么？注意力头层面偏见归因的不可识别性'
authors:
- S. M Seefat Alam
affiliations:
- Bangladesh University of Engineering and Technology, Dhaka
arxiv_id: '2611.23218'
url: https://arxiv.org/abs/2611.23218
pdf_url: https://arxiv.org/pdf/2611.23218
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 大语言模型 · 注意力头归因与公平性
tags:
- LLM Fairness
- Attention Head
- Bias Attribution
- Model Interpretability
- Ablation Study
one_liner: 验证LLM注意力头偏见定位方法的归因混淆问题，证明消融选定偏见头无法降低模型不公平率
practical_value: '- 做LLM偏见消融优化时，不要盲信注意力头层面的归因结果，需先验证归因变量的独立性，避免无效操作

  - 对LLM输出的公平性评估，要拆分prompt、输出长度、保护组特征等混淆变量的影响，避免评估偏差

  - 业务侧实现Agent/LLM推荐的公平性调控，优先采用prompt工程、推理对齐方案，不要优先选用头消融这类低效方案'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有定位LLM社会偏见到单个注意力头、通过消融去偏的方法，仅用公平性指标验证效果，从未证明选头统计量确实在度量偏见，存在归因混淆风险。
### 方法关键点
在Qwen-2.5-7B-Instruct、Llama-3.1-8B-Instruct上审计主流偏见头定位方案，通过干预实验拆分响应长度、prompt身份、公平标签、保护组token等变量的关联，统计各变量对选头统计量的方差贡献。
### 关键结果数字
1. 初始观测到偏见头map与无标签响应长度map相关系数达ρ=-0.950（Qwen）、-0.768（Llama），但固定prompt后响应长度仅解释1%的统计量方差，prompt身份解释64%的方差
2. 固定prompt下公平标签、响应长度、保护组token共线性φ=0.95，观测分析无法区分三者的影响
3. 所有测试的偏见头集合消融后均未降低不公平率，其互补集合消融会稳定破坏模型拒绝行为（p=2.7×10^-5）
