---
title: Collaborative Personalized Preference Alignment for LLMs under Data Deficiency
title_zh: 数据不足场景下大语言模型的协同个性化偏好对齐方法
authors:
- Liyan Yang
- Yige Yuan
- Zhiqin Yang
affiliations:
- City University of Hong Kong
- University of Washington
- The Hong Kong University of Science and Technology
arxiv_id: '2610.05898'
url: https://arxiv.org/abs/2610.05898
pdf_url: https://arxiv.org/pdf/2610.05898
published: '2026-10-04'
collected: '2026-10-07'
category: LLM
direction: LLM个性化对齐 · 小样本协同训练
tags:
- Preference Alignment
- Federated Learning
- Few-shot Learning
- Pareto Optimization
- LoRA
one_liner: 提出APO协同对齐框架，解决跨/内用户梯度冲突，仅用20条样本实现LLM高效个性化偏好对齐
practical_value: '- 做C端个性化Agent、电商导购话术生成等场景的LLM对齐时，可复用瓶颈调整聚类方法，按用户多目标加权损失的排序分组，降低跨用户梯度冲突，解决单用户反馈数据不足的问题

  - 推荐/广告多目标优化场景，可借鉴梯度下降+受控上升的Pareto最优求解思路，在保证核心指标（如CTR、下单率）不下降的前提下平衡体验类指标，避免单目标优化的负向影响

  - 新用户冷启动、小众用户群体个性化等小样本场景，可复用「协同预训练公共初始化+本地Few-shot适配」的两阶段架构，大幅降低个性化训练的样本需求

  - 轻量级对齐器训练可直接复用LoRA+4位量化的配置，在3B级模型上仅需96GB以下显存即可完成多用户协同训练，降低工程落地成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM面向海量异质用户提供个性化响应时，单用户的偏好反馈数据通常极为稀缺，直接训练个性化模型效果远低于预期；现有跨用户协同学习方法存在两层梯度冲突：跨用户偏好异质导致梯度聚合时相互干扰，单用户内部多目标（有用性、无害性、真实性等）优化方向相反，无法产出适配不同用户的高质量初始化模型。
### 方法关键点
- APO（近似帕累托最优）框架分两步解决梯度冲突：第一步用瓶颈调整聚类，先按用户多目标加权损失的排序做粗分组，再用偏好调整向量做层次聚类细分组，降低跨用户梯度干扰；第二步组内结合梯度下降与受控上升训练对齐器初始化，保证瓶颈目标不退化的前提下平衡多目标，再经过适配感知元训练优化初始化，提升Few-shot适配效率。
- 理论上给出单步协同更新的次优界，以及小样本适配相对于全量数据最优模型的误差界。
### 关键实验
在Fed-ChatbotPA、UltraFeedback数据集上，以Llama-3.2-3B、Qwen2.5-3B为基座，对比Base、FedAvg、FSPO等6个基线，仅用20条本地样本适配时，平均偏好加权得分比最优基线高2~5pp，Pareto超体积最高提升12.6%，IGD最多降低50%。
### 核心结论
数据不足场景下的个性化对齐，核心是通过合理的用户分组降低梯度冲突，产出接近各用户最优域的公共初始化，再用极少量本地数据即可完成高效适配。
