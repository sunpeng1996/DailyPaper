---
title: Learning Stratified Policies for Inference-Time Objectives
title_zh: 面向推理时目标的分层策略学习方法
authors:
- Mridul Mahajan
- Xuezhou Zhang
- Aldo Pacchiano
affiliations:
- Boston University
- Broad Institute of MIT and Harvard
arxiv_id: '2611.23154'
url: https://arxiv.org/abs/2611.23154
pdf_url: https://arxiv.org/pdf/2611.23154
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: LLM训练优化 · 推理时pass@k提升
tags:
- LoRA
- pass@k
- policy_gradient
- inference_time_optimization
- GRPO
one_liner: 基于共享LLM多LoRA适配器的分层策略，替代单策略i.i.d采样提升pass@k性能
practical_value: '- 电商/广告多候选生成场景（如文案生成、query推荐的best-of-k选优），可替换单LoRA反复采样方案，训k个小LoRA各出1个候选，相同推理采样预算下提升优质候选召回率

  - 优化多候选集合目标时，可复用文中group-mean baseline替代leave-one-out构造优势函数，获得更密集的学习信号，提升训练稳定性，避免训练崩溃

  - 业务需要多策略覆盖不同用户/query场景时，无需训多个独立大模型，共享backbone加多个小LoRA联合训练即可，参数成本低且可自然涌现策略互补性，无需额外加多样性正则'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM推理时优化（如best-of-k、重排序）均依赖从单策略反复i.i.d采样，容易重复命中相同解模式，有限采样预算下覆盖度极低：例如存在5个解模式的场景下，i.i.d采样5次的全模式覆盖概率仅3.84%，采样预算浪费严重，pass@k提升遭遇瓶颈。
### 方法关键点
- 分层采样策略：给定k个采样预算，联合训练k个独立策略，每个策略恰好输出1个候选，避免重复采样的覆盖度损失
- 轻量化实现：共享冻结LLM backbone，每个策略用独立LoRA适配器实现，仅训练LoRA参数，无需存储多份完整模型
- 训练优化：针对pass@k目标，在GRPO框架下用group-mean baseline构造优势函数，比传统leave-one-out基线信号更密集，解决全对/全错样本无梯度更新的问题
### 关键实验
在算术表达式构建、逻辑推理、数独、GSM数学题4类推理任务上验证，对比相同采样预算的单LoRA基线：pass@5分别提升4.2%、2.6%、6.1%、4.9%，其中数独任务pass@5从74.2%提升到80.3%；即使将单LoRA的秩扩大5倍匹配总参数量，性能仍无明显提升，证明收益来自策略互补而非参数量增加；44%的数独问题仅被1个LoRA解决，策略互补性显著。
### 核心结论
推理时采样预算的最优分配不是从单个策略反复采样，而是分配给多个互补的小策略各出1个候选，是独立于参数量缩放的新优化轴
