---
title: 'MInTRL: Off-policy Intervention can boost On-policy RL'
title_zh: MInTRL：稀疏离策略干预增强在策略强化学习框架
authors:
- Mingyu Chen
- Yefan Tao
- Gerald Friedland
- Xuezhou Zhang
- Chris Kong
affiliations:
- Amazon Web Services
- Boston University
arxiv_id: '2609.12419'
url: https://arxiv.org/abs/2609.12419
pdf_url: https://arxiv.org/pdf/2609.12419
published: '2026-09-10'
collected: '2026-09-15'
category: Training
direction: 大语言模型强化学习训练优化
tags:
- RL
- On-policy RL
- Off-policy Intervention
- LLM Training
- Advantage Regression
one_liner: 通过稀疏局部离策略干预扩展在策略RL探索边界，兼顾覆盖率与可学习性，效果显著优于各类基线
practical_value: '- 做生成式推荐/RL排序的训练时，可复用稀疏干预思路：不用全量蒸馏大模型的推荐结果，仅在匹配逻辑出错的节点做局部修正，既引入优质外部先验，又避免全量离策略数据导致的分布偏移，降低训练不稳定风险

  - 训练混合来源轨迹的RL模型时，可直接采用基于纯在策略rollout的优势回归损失，无需复杂的重要性采样修正，适配业务中多数据源混合训练的场景，训练稳定性更高

  - 干预强度控制经验可直接复用：离策略干预token占比控制在2%~4%时收益最高，过度干预反而会导致模型漂移，尤其适合电商导购Agent的多轮决策、工具调用类RL训练场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有在策略RL（如GRPO）训练大模型时，探索范围受限于当前策略的采样能力，很难发现超出原有能力边界的优质推理/决策路径；而直接引入全量离策略数据（如蒸馏教师模型完整轨迹）又会产生严重分布偏移，导致训练不稳定、效果上限低，如何在不牺牲可学习性的前提下扩展探索边界是核心痛点。
### 方法关键点
- 半在策略rollout采样：当前策略按块生成内容，由裁判-干预模型（可采用更强教师模型或带特权信息的同模型）审核，发现错误后仅生成短修正片段，立刻交回控制权给当前策略，保证轨迹大部分为在策略生成，仅少量干预token为离策略
- 回归式RL训练目标：采用序列级优势回归损失，无需重要性采样即可直接用混合来源的轨迹训练，避免重要性权重累积导致的梯度爆炸/消失问题
- 工程优化：干预部分的token用常数锚定替代当前策略的log概率，降低弱策略对优质干预信息的约束；训练后期关闭干预，切换为纯在策略训练，避免错误干预的负面影响
### 关键实验
基于Qwen3-1.7B/4B基座，在数学推理（AIME2025/2026、HMMT2025）和代码生成（LiveCodeBench、HumanEval+、MBPP+）数据集测试，对比GRPO、OPD、MENTOR、SFT+GRPO等基线，MInTRL-Const在1.7B规模上数学平均得分35.45、代码平均61.95，较最强基线分别高13.61、14.12个百分点；4B规模上数学平均55.73、代码72.63，较最强基线分别高3.02、6.80个百分点；干预token占比在2%~4%时效果最优，过高反而会出现性能下降。
### 核心结论
适度的稀疏离策略干预可以大幅提升在策略RL的性能，超过阈值后反而会因为分布偏移损害效果，平衡探索覆盖率与模型可学习性是RL训练优化的核心
