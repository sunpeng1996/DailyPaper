---
title: Cross-Question Reliable Reinforcement Learning
title_zh: 跨问题可靠强化学习CARE：提升LLM置信度预测的低风险覆盖率
authors:
- Hector G. Rodriguez
- Marcus Rohrbach
affiliations:
- TU Darmstadt
- hessian.AI
arxiv_id: '2611.25292'
url: https://arxiv.org/abs/2611.25292
pdf_url: https://arxiv.org/pdf/2611.25292
published: '2026-11-18'
collected: '2026-11-20'
category: Training
direction: LLM训练 · 置信度预测 选择性预测
tags:
- Reinforcement Learning
- Confidence Estimation
- Selective Prediction
- RLVR
- Large Language Models
one_liner: 提出跨问题置信度奖励框架CARE，无需额外模块大幅提升LLM低风险下的任务覆盖率
practical_value: '- 电商/广告Agent的答案置信度校准可复用CARE的跨batch相对奖励设计，无需额外置信度分类器，直接在RL训练阶段加入奖励项，降低推理成本，适合高客单价商品导购、广告文案自动筛选等低风险场景

  - 推荐系统排序场景可借鉴置信度多样性奖励设计，避免模型打分集中在少数区间，提升排序区分度，尤其适用于低容错的召回/精排阶段阈值筛选

  - 多Agent协作中worker Agent的结果过滤可复用C@r优化逻辑，针对不同业务风险容忍度（如内容审核容错1%、商品推荐容错5%）定制训练目标，提升自动处理覆盖率同时控制错误率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM置信度训练采用逐点奖励，将置信度往0/1两端推，丢失不同答案的相对置信度信息，导致低风险容忍度下的任务覆盖率极低，无法满足高 stakes 场景选择性预测需求，额外引入置信度分类器还会提升推理成本。

### 方法关键点
- 提出跨问题奖励框架CARE，基于同batch所有问答对的置信度、正确性标签，计算不同风险容忍度下的最优弃权阈值：正确答案高于阈值、错误答案低于阈值获正向奖励，反之惩罚，奖励幅度与到阈值的距离正相关
- 新增两类置信度多样性奖励：熵奖励鼓励置信度均匀分布在[0,1]区间的不同分箱，唯一性奖励鼓励同batch内置信度值不重复，避免置信度坍缩到少数粗粒度数值，提升低风险下的区分度
- 所有奖励可直接加入现有RLVR训练流程，无需额外模块、无单独训练阶段，推理时模型直接输出答案和置信度，无额外成本

### 关键实验结果
- 数学领域训练（Big-Math-Digits），对比SOTA逐点方法RLCR，C@5（5%风险容忍度下的覆盖率）从0.8%提升至42.4%，AURC降低35%
- 多跳QA领域训练（HotpotQA），OOD迁移到通用知识、推理、数学基准时，C@5从12.3%提升至23.6%，同时保持甚至提升答案准确率，无精度损失
- 效果在Qwen2.5-7B、Gemma 4 E2B-it等不同模型规模和家族上均稳定生效

**最值得记住的一句话**：置信度训练的核心是相对排序而非逐点匹配二元标签，跨样本的相对奖励能在不损失精度的前提下大幅提升低风险场景的自动处理覆盖率。
