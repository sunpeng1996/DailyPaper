---
title: 'GPDPO: Learning from Reward Conflicts via Group Pareto-Dominance Policy Optimization'
title_zh: GPDPO：基于组Pareto优势策略优化的多奖励冲突学习
authors:
- Zixuan Xu
- Haoxuan Chen
- Jiangxin Sun
- Jian-Fang Hu
affiliations:
- ISEE Lab, Sun Yat-sen University
- Computer Science and Technology, University of Trento
arxiv_id: '2610.35480'
url: https://arxiv.org/abs/2610.35480
pdf_url: https://arxiv.org/pdf/2610.35480
published: '2026-10-26'
collected: '2026-10-27'
category: Training
direction: 多目标LLM对齐 · 多奖励策略优化
tags:
- Multi-Reward RL
- Pareto Dominance
- Policy Optimization
- LLM Alignment
- GRPO
one_liner: 从多奖励冲突过滤丢弃的响应中挖掘Pareto主导的成对偏好信号，提升多目标LLM对齐效果
practical_value: '- 多目标对齐场景（如兼顾CTR、CVR、客单价、负反馈的生成式推荐、Agent工具调用）可复用GPDPO思路：冲突过滤后不要直接丢弃样本，先挖掘样本间Pareto主导的成对偏好作为辅助训练信号，不增加额外采样/标注成本

  - 现有GRPO/GD2PO多奖励训练流程不需要做大改，仅新增轻量Pareto配对+交叉熵偏好损失即可迁移，λ取0.05~0.1区间鲁棒性好，无需精细调参

  - 多目标排序/召回的样本筛选阶段，可参考Pareto主导判断逻辑，从被过滤的冲突样本中挖掘可靠的pairwise监督信号，提升样本利用率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多奖励RL是LLM多目标对齐的核心方案，但不同奖励维度的信号冲突会导致更新方向模糊，现有GD2PO等方法直接过滤冲突响应，会丢弃大量隐含的有效监督信息，同时冲突过滤决策对参考组敏感，稳定性不足。
### 方法关键点
- 保留GD2PO的冲突过滤机制，对组内所有响应对做Pareto dominance判断：一个响应在所有奖励维度不劣于另一个、且至少一个维度更优，即构成可靠偏好对
- 筛选至少包含一个被过滤响应的Pareto偏好对，构造成对偏好损失，仅对被过滤响应回传梯度，未过滤响应作为固定锚点
- 总损失为原有多奖励策略梯度损失加λ加权的偏好损失，不需要额外采样或奖励评估，可无缝嵌入现有GRPO类训练流程
### 关键结果
在API-Bank工具调用任务上测试Qwen3-1.7B/4B两个模型，对比GRPO、GDPO、GD2PO基线：2奖励设置下，GPDPO比GD2PO的Correct Acc提升1.34~2.51个百分点；3奖励设置下提升0.84~2.01个百分点，在难度最高的Level3子集最多提升6.1个百分点，同时训练阶段冲突率下降更快、政策熵保持更高，缓解过拟合。
最值得记住的结论：多奖励冲突场景下，被组级过滤判定为无效的样本，依然可能和其他样本形成可靠的成对偏好关系，是成本极低的增量监督信号来源。
