---
title: 'Bekko Embedding: Parameter-Efficient Multilingual Retrieval with Ultra-Compact
  Encoders'
title_zh: Bekko Embedding：参数量高效的超紧凑多语言检索编码器
authors:
- Yuichi Tateno
arxiv_id: '2607.25180'
url: https://arxiv.org/abs/2607.25180
pdf_url: https://arxiv.org/pdf/2607.25180
published: '2026-07-28'
collected: '2026-07-29'
category: RAG
direction: RAG检索 · 超紧凑多语言嵌入
tags:
- Embedding
- Multilingual Retrieval
- Model Pruning
- Parameter Efficiency
- On-device Inference
- RAG
one_liner: 仅8M/25M活跃参数的无蒸馏多语言检索嵌入模型，性能赶超数十倍参数量竞品
practical_value: '- 嵌入模型优化可参考「活跃参数（AP）」评估维度，优先压缩Transformer层而非词表矩阵，词表采用行级int8量化可将模型体积降至1/3，几乎无精度损失

  - 小模型无蒸馏训练方案可复用：剪枝时保留浅层连续层+1个深层Global注意力层，配合大规模对比数据+硬负样本微调，单GPU3天即可完成8M级检索模型训练

  - 跨境电商多语言检索、端侧Agent场景可直接测试Bekko开源模型：8M版本CPU推理比multilingual-e5-small快1.6倍，MMTEB检索nDCG@10高5.3，大幅降低无GPU环境部署成本

  - 向量检索降本可复用Matryoshka训练策略：训练时学习多粒度嵌入，输出可按需截断为384/256/128/64维，截断至256维仅损失1.3~1.8%精度，显著降低索引存储和计算开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前主流多语言检索嵌入模型参数量达数亿级，CPU、边缘设备、浏览器端推理成本极高，现有小参数模型多为无上下文的静态嵌入，检索精度差；行业过往多以总参数量为优化目标，忽略了真正决定推理速度的Transformer层活跃参数（AP）的优化空间。
### 方法关键点
- 剪枝策略：基于mmBERT-small做结构化剪枝，保留浅层连续层+1个深层Global注意力层，得到仅7.67M/24.93M AP的两个基础模型，全程无知识蒸馏
- 数据策略：使用11亿级覆盖100+语言的对比训练数据，搭配两类互补的LLM合成查询数据集（Qwen3.5-35B生成高质量复杂查询、自研轻量模型批量生成通用查询），第二阶段补充自研挖掘的多语言硬负样本微调
- 训练策略：两阶段对比学习，损失融合掩码对比损失（过滤假负样本）、Matryoshka损失（支持维度截断）、伪量化辅助损失（提升量化后精度），通过GradCache实现单GPU 8192大batch训练
### 关键结果
在MMTEB Multilingual v2检索任务nDCG@10指标上，8M AP的a8m得分56.2，超过AP为其40倍的BGE-M3、全系列multilingual-e5模型；25M AP的a25m得分57.5，与AP为其4.5倍的gte-m-base持平。a8m推理速度在x86 CPU上比multilingual-e5-small快1.6倍，词表int8量化后模型文件仅124MiB，支持树莓派、浏览器端直接运行。
> 最值得记住：嵌入模型优化的核心是压缩决定推理开销的Transformer层活跃参数，而非总参数量，仅8M活跃参数的小模型就能达到数十倍参数量大模型的多语言检索效果
