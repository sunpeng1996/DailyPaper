---
title: Retraining Seeks Stable Signals
title_zh: 模型重训练的稳定信号原理及收敛性证明
authors:
- Moritz Hardt
arxiv_id: '2607.15623'
url: https://arxiv.org/abs/2607.15623
pdf_url: https://arxiv.org/pdf/2607.15623
published: '2026-07-17'
collected: '2026-07-21'
category: Training
direction: 模型重训练 · 反馈循环收敛性分析
tags:
- retraining
- performativity
- stable_signal
- regularization
- feedback_loop
one_liner: 提出稳定信号原理，证明带正则的重训练在强模型数据影响下仍可收敛到稳定信号方向
practical_value: '- 推荐/广告系统迭代时可优先锚定商品固有质量、用户真实长期偏好这类与模型无关的稳定信号作为训练目标，降低推荐马太效应

  - 重训练流程中的正则项可新增控制模型对数据分布扰动的权重，而非仅服务于泛化性提升，可大幅降低迭代震荡

  - 用自生成数据训练LLM4Rec或决策Agent时，只要混入少量真实稳定信号样本，即可保证训练不发散，降低真实数据采样成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
大规模部署的预测模型会改变未来数据分布形成performativity效应，现有研究仅验证模型对数据影响较小时重训练可收敛到不动点，无法解释强影响场景下的收敛性与不动点存在性。
### 方法关键点
提出稳定信号原理，假设预测目标存在至少少量与模型无关的稳定分量（如商品固有质量），分析带正则的重复风险最小化流程的收敛性，理论可覆盖仿射重训练算子、模型诱导特征变化、时变异质效应、非线性响应等通用场景。
### 关键结果
1. 只要存在非零稳定信号，即使模型对目标的影响远大于稳定信号，带适当正则的重训练也会几何收敛到稳定信号方向；
2. 该理论可解释大语言模型用自生成数据训练的稳定性成因。
