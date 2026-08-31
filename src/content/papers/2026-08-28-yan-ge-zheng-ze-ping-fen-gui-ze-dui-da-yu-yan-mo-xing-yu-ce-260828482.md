---
title: How Proper Scoring Rules Shape LLM Forecasting
title_zh: 严格正则评分规则对大语言模型预测能力的影响研究
authors:
- Benjamin Turtel
- Paul Wilczewski
- Kris Skotheim
- Ville A. Satopää
- Philip E. Tetlock
affiliations:
- Lightning Rod Labs
- INSEAD
- University of Pennsylvania
arxiv_id: '2608.28482'
url: https://arxiv.org/abs/2608.28482
pdf_url: https://arxiv.org/pdf/2608.28482
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: LLM训练 · 奖励函数设计
tags:
- Proper Scoring Rules
- GRPO
- LLM Forecasting
- Reward Design
- LoRA
one_liner: 对比5种严格正则评分规则作为DR GRPO训练奖励，揭示不同规则诱导的LLM预测器性能与误差结构差异
practical_value: '- 做概率输出类业务（如广告pCTR校准、Agent决策置信度输出）时可直接匹配目标选奖励：要校准度优先选Log损失，要排序能力（AUC）优先选Brier损失

  - 用GRPO类相对奖励算法训练时，可根据业务误差容忍偏好调整Beta类评分规则参数，如对低概率误报敏感可选择Beta(2,8)优化低概率区域误差

  - 构建模型集成时可组合不同奖励训练的模型，利用其偏差/信息/噪声的互补性，无需仅选择单指标最优的单模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
严格正则评分规则理论上均可诱导模型输出真实置信度，但有限训练样本、相对优化算法（如GRPO）落地场景下，不同规则的实际表现差异缺乏受控验证；对需要可靠概率输出的预测、决策、推荐校准等业务，奖励函数选择的实际影响尚不清晰。
### 方法关键点
- 基于Dr. GRPO算法用秩32 LoRA微调GPT-OSS-120B，仅调整奖励函数，模型、数据、训练步数、超参完全对齐，排除其他变量干扰
- 对比5种严格正则评分规则：Log、Brier、Spherical、Beta(2,8)、Beta(8,8)，奖励仅与最终预测概率、真实结果挂钩，不对推理过程额外加奖
- 采用时间掩码的未来标签数据集，预测输入仅包含预测时点前的公开信息，避免信息泄露
### 关键结果
数据集包含8041条2024.7-2026.1的真实世界二元预测问题（覆盖政治、经济、体育等领域），7076条训练、965条测试，基线为未微调的GPT-OSS-120B。所有奖励微调模型均优于基线：Brier训练模型Brier score最优（0.1648，较基线降11.4%）、AUC-ROC最高（0.7511，较基线升3.6%）；Log训练模型校准误差ECE最低（0.0434，较基线降60.5%）；不同规则训练的模型误差结构差异显著，Brier训练模型信息增益最高，Log训练模型噪声最低，Beta(2,8)训练模型系统偏差最小。

理论上等价的严格正则评分规则，在有限数据、相对优化的实际训练场景下会诱导出性能结构差异极大的模型，奖励选择是可主动调控的性能权衡杠杆。
