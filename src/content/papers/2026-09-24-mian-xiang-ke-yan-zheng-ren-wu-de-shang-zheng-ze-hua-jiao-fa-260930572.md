---
title: 'Entropy Regularization: A Free Correction to Cross-Entropy for Verified Demonstrations'
title_zh: 面向可验证任务的熵正则化交叉熵训练优化方法
authors:
- Mihir Dhanakshirur
- Adam Ousherovitch
- Ambuj Tewari
affiliations:
- Department of Statistics, University of Michigan
arxiv_id: '2609.30572'
url: https://arxiv.org/abs/2609.30572
pdf_url: https://arxiv.org/pdf/2609.30572
published: '2026-09-24'
collected: '2026-09-28'
category: Training
direction: LLM微调 · 损失函数优化
tags:
- Cross-Entropy
- Entropy Regularization
- Supervised Fine-Tuning
- LoRA
- Verifiable Task
one_liner: 提出熵正则化交叉熵损失，无额外成本提升多正确解可验证任务的SFT效果
practical_value: '- SFT阶段可直接复用ER-CE损失，在多正确解业务场景（如Agent工具调用、商品合规文案生成、SQL生成）中增加token-level熵正则，几乎无额外训练成本即可提升输出通过率

  - 熵正则强度λ可根据任务调优：逻辑类任务（代码、推理、规则生成）最优λ在1-4区间，创意类生成任务可从0.3起步测试，避免正则过强导致输出多样性不足

  - 大模型微调（LoRA/全参数）时，熵正则计算可采用分块梯度检查点优化显存，适配大词表场景，训练速度与原生CE基本持平

  - 针对有明确可验证规则的业务场景优先替换CE为ER-CE，实测可稳定带来4%-9%的绝对通过率提升'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有LLM SFT普遍采用交叉熵（CE）损失，但在数学推理、代码生成等存在多正确解的可验证任务中，训练目标是生成任意可通过验证的输出，而非完全复现单条专家演示。CE损失会强迫模型学习专家演示的个性化细节，导致概率质量扩散到错误输出，与最终验证通过率目标存在系统性错配，此前无可落地的低成本优化方案。
### 方法关键点
- 提出熵正则化交叉熵（ER-CE）损失，在原生CE基础上新增token-level Shannon熵惩罚项，用可微的熵作为输出支持集大小的代理，约束模型概率质量不向未观测的错误输出扩散
- 理论证明在诱导支持集有限、非零输出概率存在下界的假设下，ER-CE可PAC学习最优策略，解决原生CE无法对齐验证风险的缺陷
- 工程上采用分块梯度检查点优化熵计算的显存占用，适配大词表场景，训练速度、显存开销与原生CE几乎一致
### 关键结果
在三类可验证任务上对比原生CE SFT基线：1) GSM8K数学推理，1.5B模型最优λ=8时Pass@1提升9%；2) MBPP代码生成，1.5B模型最优λ=1时Pass@1提升4.4%；3) MATH竞赛数学题，7B模型最优λ=4时Pass@1提升5.17%；温度采样下的增益是贪心解码的2倍左右。
> 最值得记住的结论：对于输出有明确验证规则、存在多正确解的SFT任务，ER-CE是几乎无额外成本的CE替代方案，可稳定提升验证通过率
