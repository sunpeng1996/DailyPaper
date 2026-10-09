---
title: When KL Regularization Misfires in Group Policy Optimization
title_zh: 组策略优化中KL正则化失效问题与优化方法研究
authors:
- Fei Ding
affiliations:
- Alibaba Group
arxiv_id: '2610.12161'
url: https://arxiv.org/abs/2610.12161
pdf_url: https://arxiv.org/pdf/2610.12161
published: '2026-10-08'
collected: '2026-10-09'
category: Training
direction: 大模型策略优化训练 · KL正则化
tags:
- KL Regularization
- Group Policy Optimization
- ZCPO
- LLM Training
- RLHF
one_liner: 分析组策略优化中KL正则化7种失效模式，提出零和校准策略优化方法ZCPO
practical_value: '- 基于RLHF优化推荐排序策略、Agent决策逻辑时，可先对照本文提出的7种KL失效模式自检，避免盲目添加KL正则化引入负向效果

  - 电商多候选召回、pairwise排序等组内相对优化场景，可复用ZCPO的条件KL相对漂移校准组内奖励系数的思路，降低正则化副作用

  - 训练大模型生成电商文案、Agent多轮回复时，可参考KL随长度失衡、集中于少量token的结论，优化长序列生成的正则化策略'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
组相对策略优化（GRPO）类方法无需价值模型即可训练大模型，近年实践发现移除参考策略KL正则化反而能提升推理等任务效果，现有方案未明确KL正则化的合理引入方式。

### 方法关键点
系统性梳理KL与奖励交互的7种失效模式，覆盖奖励截断/梯度抵消后残差KL更新、同奖励组冗余正则、KL随生成长度失衡、KL集中于少量token、采样噪声等场景；提出ZCPO方法，用条件KL计算的相对漂移校准组内奖励系数，再整合到基础替代损失，避免显式KL penalty的副作用。

### 关键结果数字
公开消融实验显示，移除GRPO中的KL项后，Qwen2.5-VL-3B、7B的多模态推理平均精度（avg@8）分别从47.92%、58.78%提升至50.18%、61.30%；数学推理实验与消融实验验证ZCPO设计的有效性。
