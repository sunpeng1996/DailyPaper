---
title: 'PoEM: Predicting RL Outcomes from Existing Policies'
title_zh: PoEM：无需额外RL训练即可预测新奖励下的策略优化结果
authors:
- Kimia Hamidieh
- Giannis Daras
- Antonio Torralba
affiliations:
- MIT CSAIL
arxiv_id: '2609.30226'
url: https://arxiv.org/abs/2609.30226
pdf_url: https://arxiv.org/pdf/2609.30226
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: 大模型RL对齐 · 策略组合
tags:
- RLHF
- LoRA
- Policy Composition
- Alignment
- Reinforcement Learning
one_liner: 通过线性组合已有单奖励RL适配器的log策略，无额外训练拟合新奖励下的RL最优策略
practical_value: '- 多目标对齐场景可复用该思路：电商推荐/营销文案生成常需要平衡点击率、转化率、合规性、用户好感度等多目标，无需重新做全量RLHF训练，直接组合已有的单目标LoRA适配器，大幅节省训练成本

  - 可用于新业务目标的预验证：上线新的业务考核指标（如话术友好度、商品合规性、退费率关联指标）前，先用PoEM快速预览策略效果，再决定是否投入资源做全量RL训练，降低试错成本

  - 低资源奖励适配：对于标注/评估成本高的奖励（如人工打分的用户满意度、客服对话解决率），仅需数百条校准样本即可拟合组合权重，近似全量RL训练的效果，降低奖励工程成本

  - 推理端动态调优：流量分组实验时，可在推理端动态调整不同业务目标的权重，无需重新部署模型，快速验证不同目标组合的业务效果，提升迭代效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型后训练阶段的RL对齐（如RLHF、DPO、GRPO）计算成本高、训练不稳定，且每次调整奖励函数或组合多目标都需要重新跑全量RL流程；现有权重平均、best-of-N等方法要么效果随组合模型数量增加明显下降，要么适用范围窄、推理成本高，亟需无需额外RL训练即可快速获得新奖励下最优策略的方法。
### 方法关键点
- 理论推导：若新奖励是已有奖励的线性组合，新最优策略的log空间等于基础模型与各单奖励策略log比值的加权线性组合，无需重新训练
- 权重拟合：仅需少量（数百条）校准样本，通过岭回归用现有奖励得分或策略log比值拟合新奖励对应的组合权重，全程不更新模型参数
- 覆盖度预判：提出Coverage Score指标，预先判断新奖励对应的最优策略是否落在现有策略的log空间子空间内，提前筛选可近似的目标，避免无效组合
- 跨模态适配：分别给出自回归LLM的token级解码组合公式、扩散模型的去噪器组合公式，适配文本、图像多模态场景
### 关键结果
- 文本场景：在Qwen3-0.6B的20个单奖励LoRA适配器、10个公开RM的PPO适配器上测试，组合奖励场景下PoEM的奖励恢复率达0.83~1.00，误差接近两次不同种子RL训练的固有差异；9/10的held-out奖励下效果优于最优单专家
- 图像场景：在Stable Diffusion v1.4的13个DDPO训练的LoRA适配器上测试，可近似复现held-out奖励微调的生成效果
### 核心结论
不同单奖励微调的适配器参数空间接近正交，但log策略空间的有效秩远低于参数空间，大部分新奖励的最优策略都落在现有策略的低秩子空间内，无需重新训练即可组合得到
