---
title: '\k{appa}-LoRA: Condition Numbers Reveal Which LoRA Matrices Worth Updating'
title_zh: κ-LoRA：基于条件数筛选高价值LoRA矩阵的高效微调方法
authors:
- Jianghui Wang
- Silong Yong
- Francesco Orabona
- Marco Canini
- Katia P. Sycara
- Yaqi Xie
affiliations:
- King Abdullah University of Science and Technology
- Carnegie Mellon University
arxiv_id: '2607.22489'
url: https://arxiv.org/abs/2607.22489
pdf_url: https://arxiv.org/pdf/2607.22489
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: 参数高效微调 · LoRA优化
tags:
- LoRA
- PEFT
- Fine-Tuning
- Condition Number
- Efficient Training
one_liner: 通过预训练权重条件数筛选需更新的LoRA矩阵，降本提效同时持平全量LoRA性能
practical_value: '- 电商/推荐场景的垂域LLM微调、LLM4Rec生成式推荐适配时，可直接复用κ-LoRA的条件数筛选逻辑，默认选top 50%高条件数矩阵加LoRA，平均减少16%微调耗时、4.5%显存占用，业务效果基本无损失

  - 筛选逻辑仅需在训练前对预训练权重做一次截断SVD计算，无梯度/验证集依赖，可无缝嵌入现有PEFT流水线，额外计算开销可忽略，适配所有主流Transformer基座

  - 算力紧张时可根据业务对效果的容忍度调整筛选比例α，α=50%是帕累托最优拐点，α最低可降到30%仍能保留90%以上的全LoRA性能，适合端侧模型微调、快速实验等场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LoRA是当前应用最广的参数高效微调方法，但默认对Transformer所有投影矩阵均匀添加适配器，存在大量冗余计算；在大模型微调、端侧部署等资源受限场景下成本过高，且不同矩阵对微调的贡献差异极大，均匀分配算力的策略天生低效。
### 方法关键点
- 首次验证预训练Transformer权重的条件数（最大奇异值/最小奇异值比值）与LoRA微调增益高度正相关：高条件数矩阵存在未充分利用的特征方向，低秩更新能带来更大性能增益；低条件数矩阵各方向变换均衡，更新收益极低
- 提出κ-LoRA：训练前对每个候选投影矩阵做截断SVD计算条件数，按架构组（注意力投影、MLP投影）内排名，仅对top α比例的高条件数矩阵添加LoRA适配器，其余权重完全冻结
- 筛选逻辑完全无数据、无训练依赖，仅需离线计算一次，结果可跨下游任务复用
### 关键实验结果
覆盖LLaMA2-7B、Mistral-7B、Gemma-7B、DeBERTa-v3等主流基座，测试数学推理、代码生成、对话、NLU等10+任务，与标准全量LoRA对比：α=50%时训练参数减半，平均微调时间降低16.2%，显存占用降低4.5%，11/15个任务效果持平或超过全量LoRA；GLUE任务训练时间最高降低22.2%，整体效果仅差0.53个点（排除高方差RTE任务后仅差0.04点）。
### 最值得记住的结论
LoRA的微调增益高度集中在少部分高条件数矩阵，仅更新前50%就能以一半的训练成本达到几乎相同的下游效果
