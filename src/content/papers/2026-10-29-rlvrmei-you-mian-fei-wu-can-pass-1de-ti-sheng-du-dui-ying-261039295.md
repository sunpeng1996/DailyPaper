---
title: 'There Is No Free Lunch in RLVR: Every pass@1 Gain Has a pass@k Price'
title_zh: 《RLVR没有免费午餐：pass@1的提升都对应pass@k的代价》
authors:
- Yinuo Liu
arxiv_id: '2610.39295'
url: https://arxiv.org/abs/2610.39295
pdf_url: https://arxiv.org/pdf/2610.39295
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: LLM训练 · RLVR性能权衡理论
tags:
- RLVR
- pass@k
- GRPO
- reinforcement learning
- performance tradeoff
one_liner: 从理论层面证明RLVR的pass@1提升必然伴随大k下pass@k下降，给出精确权衡边界与易用诊断工具
practical_value: '- 做基于RL的Agent/生成式推荐优化时，不能只盯着单次输出（pass@1）效果，必须评估多采样场景下的pass@k表现，避免高并发/多候选生成场景下的效果倒退

  - 可复用论文提出的诊断工具，仅需用现有评估日志里的base模型和RL优化后模型的per-prompt成功率，即可计算pass@k交叉点位置、优化代价，量化权衡收益

  - 要同时提升pass@1和pass@k，可采用论文提到的带per-prompt成功率下限的约束RL优化，通过调整γ参数在两个指标间做可控tradeoff，避免硬尾样本效果暴跌'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前工业界普遍用GRPO等RLVR方法优化LLM的推理/生成效果，观测到RLVR能显著提升pass@1，但大k采样下base模型反而会反超，业界一直争论这是训练不足的 transient 还是本质约束，没有明确的理论解释，也没有量化权衡的方法。

### 方法关键点
- 把RLVR建模为base策略在跨prompt共享的求解策略空间上的指数倾斜，证明策略概率是守恒资源，向高收益策略倾斜必然挤占其他策略的概率
- 提出两个核心假设：专属专业化（每个策略是部分prompt的唯一解）、精细覆盖（最难prompt仅由低于平均收益的策略覆盖），基于Stiemke对偶和全正核变差递减性质推导理论结论
- 给出pass@1与pass@k的最优权衡边界，以及仅需per-prompt成功率即可计算的诊断工具，可输出交叉点数量、优化代价等指标

### 关键结果数字
- 仿真实验：100%的专属/主导专业化场景下不存在免费午餐，3000个随机实例中pass@k交叉点数量边界从未被突破
- 公开曲线验证：Qwen2.5-7B经GRPO训练后，Omni-MATH数据集上pass@1提升0.149，k=256时pass@k反降0.008，完全符合理论预测；加入多样性干预的GRPO+PBA可将交叉点延后到测量范围外，契合最优边界假设

### 最值得记住的一句话
RLVR无法拓宽推理能力边界，只能沿着pass@1和pass@k的权衡边界移动，不存在无代价的性能提升
