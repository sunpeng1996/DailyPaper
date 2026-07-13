---
title: 'Super-Tuning: From Activation-Aware Pruning to Sparse Fine-Tuning'
title_zh: Super-Tuning：基于激活感知剪枝的稀疏参数高效微调方法
authors:
- Ivan Ilin
- Philip Zmushko
- Peter Richtárik
affiliations:
- KAUST
- ISTA
- Yandex Research
arxiv_id: '2607.09287'
url: https://arxiv.org/abs/2607.09287
pdf_url: https://arxiv.org/pdf/2607.09287
published: '2026-07-10'
collected: '2026-07-13'
category: Training
direction: 大模型参数高效微调 · 稀疏低秩混合适配
tags:
- PEFT
- LoRA
- Sparse Fine-Tuning
- Wanda Pruning
- LLM Adaptation
one_liner: 提出基于剪枝信号的无训练稀疏PEFT方法Super与融合LoRA的混合方案Supra，同参数量下性能优于主流基线
practical_value: '- 电商垂类LLM微调（如文案生成、query理解、商品语义匹配）时，可优先尝试BottomK低权重值稀疏微调，无需梯度选参，同参数量下效果优于LoRA，且checkpoint体积更小、峰值内存更低，适合多任务部署。

  - PEFT方案选型可参考预算分配规则：小模型给LoRA分配更高预算（λ=0.8），大模型给稀疏更新分配更高预算（λ=0.3），无需增加参数量即可提升下游任务适配效果。

  - 多任务小样本微调场景下，优先选择低Wanda/低权重值的参数更新，这类参数对预训练通用能力破坏小，可快速适配电商多品类/多场景的垂类需求，降低过拟合风险。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM全参数微调成本过高，主流PEFT方法如LoRA仍有优化空间，而稀疏微调往往需要梯度计算、多轮训练才能筛选可更新参数，适配成本高；剪枝领域的参数显著性信号本身可表征参数对预训练输出的影响程度，可复用为微调的参数选择依据，在不增加参数量的前提下提升PEFT效果。
### 方法关键点
- 提出Super稀疏微调：复用Wanda剪枝的激活加权幅值打分规则（权重绝对值×输入激活L2范数），仅需一次校准前向传播即可选出固定可训练参数集，无需梯度计算，支持TopK/ BottomK两种选参模式，实验证明BottomK（选对预训练输出影响最小的参数）效果更优。
- 提出Supra混合PEFT方案：将Super稀疏更新与LoRA结合，通过λ参数控制总预算在稀疏、低秩模块的分配比例，总训练参数量与同秩LoRA完全对齐，可灵活适配不同模型规模、任务场景。
- 同步对比仅基于预训练权重幅值的PaFi式稀疏基线，验证激活加权、纯幅值两种选参规则的效果差异。
### 关键结果
在Llama-3.2-1B、Llama-3-8B上基于Math17K算术数据集微调，对比LoRA、RoSA、SIFT等同参数量基线：1B模型上Supra（BottomK，λ=0.8）平均准确率达62.23%，较LoRA高1.16pp；8B模型上纯幅值选参的Supra-Mag（λ=0.3）平均准确率达79.12%，较LoRA高5.95pp，较SIFT高1.29pp，且稀疏微调峰值内存比LoRA低15%，checkpoint体积小50%。
> 最值得记住的结论：预训练模型中对输出影响最小的低权重/低Wanda得分参数，是参数高效微调的最优更新对象，简单无训练的选参规则即可超过复杂PEFT方法的效果。
