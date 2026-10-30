---
title: 'MASS: Multi-mask Selective Self-Distillation for Leakage-Resilient Reasoning'
title_zh: MASS：面向抗泄漏推理的多掩码选择性自蒸馏方法
authors:
- Xiuqi Liu
- Oveys Delafrooz Noroozi
- Upamanyu Madhow
affiliations:
- Chongqing Bashu Secondary School
- University of California, Santa Barbara
arxiv_id: '2610.38154'
url: https://arxiv.org/abs/2610.38154
pdf_url: https://arxiv.org/pdf/2610.38154
published: '2026-10-28'
collected: '2026-10-30'
category: Training
direction: LLM训练 · 自蒸馏推理优化
tags:
- Knowledge Distillation
- Self-Distillation
- LLM Training
- Mathematical Reasoning
- Masked Learning
one_liner: 通过多掩码参考视图聚合、选择性蒸馏和自适应掩码提升自蒸馏推理性能
practical_value: '- 生成式推荐话术、Agent决策路径蒸馏场景可复用多掩码视图构造方法，仅需单条优质样本即可生成多组互补教师信号，大幅降低多参考样本标注成本

  - 参考token级选择性加权机制，对蒸馏信号按信噪比和锚点对齐度动态加权，过滤噪声干扰，可缓解自蒸馏过程中的性能波动和过拟合问题

  - 自适应掩码策略可迁移到业务蒸馏流程，对参考样本的关键片段（如推荐理由核心卖点、推理路径关键步骤）动态调整掩码概率，提升蒸馏效率

  - 蒸馏目标优先选择正向KL而非反向KL，保留教师分布的全量合理输出，适配多候选推荐、多路径Agent决策等需要输出多样性的场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有on-policy自蒸馏依赖单条验证后的参考解决方案作为教师的特权信息，容易导致教师预测过度锚定单一推理轨迹，学生模型泛化性差、推理多样性不足，甚至出现性能崩塌、优化不稳定问题；而获取多条有效参考样本的成本极高，难以规模化落地。
### 方法关键点
- 多掩码教师构造：将单条参考方案按标点、公式边界划分为独立span，独立采样K个不同span掩码视图，取多组教师预测的算术平均作为蒸馏目标，消除单参考路径偏差
- 选择性蒸馏：基于校正信号强度、采样不确定性、与全参考锚点教师的对齐度计算每个token的蒸馏权重，过滤低信噪比噪声信号，稳定训练
- 自适应掩码：基于Shapley值估计各span对蒸馏增益的贡献，动态调整span掩码概率，优先掩码对推理路径影响大的关键片段，提升视图多样性和蒸馏效率
### 关键实验
在Qwen3-1.7B/4B/8B、OLMo-7B等多个模型上训练，使用30K数学推理样本，在AIME2024、AIME2025、HMMT2025基准上测试，相比SOTA自蒸馏基线RLSD，Qwen3-4B上Avg@12准确率提升2.41个百分点，Qwen3-8B提升2.04个百分点；OOD测试在GPQA、BBH基准上也优于所有基线，同时缓解了自蒸馏导致的推理路径过短、认知性表达被过度抑制的问题。
### 核心结论
构造互补的教师上下文而非事后修正监督信号，可以从根源上缓解自蒸馏的特权信息泄漏问题，同时保留更丰富的合理推理路径。
