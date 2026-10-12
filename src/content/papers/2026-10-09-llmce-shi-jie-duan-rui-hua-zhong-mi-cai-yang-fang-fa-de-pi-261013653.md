---
title: A Critical Look at Power Sampling when Test Time Sharpening LLMs
title_zh: LLM测试阶段锐化中幂采样方法的批判性分析
authors:
- Abiel Malkani Talwar
- Christopher Nemeth
- Henry Moss
affiliations:
- Lancaster University
arxiv_id: '2610.13653'
url: https://arxiv.org/abs/2610.13653
pdf_url: https://arxiv.org/pdf/2610.13653
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM推理优化 · 测试时分布锐化
tags:
- PowerSampling
- TestTimeSharpening
- LLMReasoning
- BestOfN
- LoRA
one_liner: 指出现有LLM幂采样方案未收敛到目标分布，增益源自高似然序列选择
practical_value: '- 电商/Agent场景做LLM生成优化（文案生成、推理应答）时，无需引入复杂度高的MCMC/SMC幂采样方案，直接用Best-of-N选择平均log概率最高的输出，即可获得相当的效果增益，工程落地成本极低

  - 若需通过分布锐化提升模型推理效果，优先验证底座模型与任务的对齐度：对齐度不足时锐化易出现输出过短等退化问题；对齐度足够时轻度锐化（α≈1.5）可提升pass@k，充分挖掘底座模型潜在能力

  - 做无外部奖励的模型自提升时，可直接采用模型自身输出的log似然作为奖励，通过LoRA微调拟合幂分布，无需复杂采样逻辑，即可获得稳定的效果提升'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
RLVR被证实可大幅提升LLM推理能力，但近期研究发现其本质是分布锐化，仅放大底座模型已有能力。现有方案尝试通过MCMC/SMC采样幂分布π^α复现RLVR增益且无需奖励信号，但这类方案的收敛性、增益来源及目标分布的实际价值从未被系统性验证，存在大量工程资源浪费的可能。
### 方法关键点
- 验证现有MCMC、SMC幂采样方案的收敛性：发现实际算力下均出现粒子退化，输出似然对α不敏感，本质是高似然序列搜索而非拟合π^α
- 提出Power-RLOO微调方案：基于KL正则化RL目标，以模型自身输出的log似然为奖励，通过LoRA微调直接拟合幂分布π^α，完全规避采样收敛问题
- 设计轻量化基线：带重采样的Best-of-N，每生成R个token保留k个最高似然前缀，可复现复杂采样方案的大部分增益
### 关键实验结果
在MATH500数学推理、GPQA多学科问答两个基准上测试，核心结论：
1. Best-of-N（选择平均log概率最高的序列）在所有模型上均匹配或超过Power-SMC效果，如Qwen2.5-7B-Instruct上MATH500准确率77.0% vs Power-SMC的76.9%
2. 仅当底座模型与任务对齐度足够时，拟合幂分布才有增益：Qwen2.5-7B-Instruct上Power-RLOO达到78.4% MATH500准确率、41.0% GPQA准确率，较低温采样提升约3pct
3. 对齐度差的模型拟合幂分布会出现长度退化，输出过短无实用价值；轻度锐化（α=1.5）反而提升pass@k，可挖掘底座模型未被激活的潜在能力

**最值得记住的结论**：幂采样的增益本质是选择底座模型本身已有的高似然优质序列，而非拟合目标分布带来的提升，简单的Best-of-N即可实现大部分收益
