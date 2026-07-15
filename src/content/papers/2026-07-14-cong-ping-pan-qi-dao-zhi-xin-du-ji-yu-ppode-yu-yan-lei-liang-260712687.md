---
title: 'From Critic to Confidence: PPO for Language-Based Quantitative Prediction
  with Confidence Estimation'
title_zh: 《从评判器到置信度：基于PPO的语言类量化预测与置信度估计》
authors:
- Mehak Dhaliwal
- Rasta Tadayon
- Andong Hua
- Haewon Jeong
- Yao Qin
arxiv_id: '2607.12687'
url: https://arxiv.org/abs/2607.12687
pdf_url: https://arxiv.org/pdf/2607.12687
published: '2026-07-14'
collected: '2026-07-15'
category: Training
direction: LLM微调 · PPO与置信度校准
tags:
- PPO
- Confidence Estimation
- LLM Fine-tuning
- Reinforcement Learning
- Quantitative Prediction
one_liner: 提出CARE-PPO强化学习框架，联合学习准确数值预测与可靠置信度信号，置信度对齐效果显著优于基线
practical_value: '- 可复用CARE-PPO的置信度对齐奖励设计，应用在LLM4Rec的打分、预估类任务（如转化率预测、商品价格预估），同时输出预测值与可靠置信度，降低高置信错误对业务的损伤

  - 推理时直接复用PPO的critic作为置信度estimator，无需额外新增模型分支或后处理逻辑，工程实现成本低，适合业务侧快速落地

  - 该框架的OOD鲁棒性优势可迁移到跨域推荐、冷启动预测场景，解决分布偏移下传统监督微调预测置信度不可靠的问题'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM做基于自然语言的量化预测时易出现幻觉、过度自信错误，现有方法无法同时保障预测准确率与置信度信号的可靠性，限制了LLM在高风险量化决策场景的落地。

### 方法关键点
提出CARE-PPO强化学习框架，将不确定性估计的损失预测与actor-critic结构的PPO微调打通，设计了和预测误差绑定的置信度对齐奖励，给actor提供dense误差感知反馈的同时，引导critic学习和预测质量对齐的价值函数，推理阶段直接复用critic作为置信度估计器，无需额外模块。

### 关键结果
在医疗、金融两个真实任务，Qwen-3的4B、8B两个参数规模上验证，CARE-PPO的量化预测效果优异，置信度对齐效果显著优于基于logit、口头输出的基线方法，在跨域OOD场景下增益依然保持，同时相比监督微调降低了任务特定过拟合，通用指令遵循能力下降更少。
