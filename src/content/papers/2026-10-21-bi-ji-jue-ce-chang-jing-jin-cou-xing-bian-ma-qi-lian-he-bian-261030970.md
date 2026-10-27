---
title: Joint or Per-Option? Compact Encoders for Closed-Set Decisions from 17 Million
  to 1 Billion Parameters
title_zh: 闭集决策场景紧凑型编码器：联合编码vs逐选项编码（17M~1B参数）
authors:
- Tardelli Ronan Coelho Stekel
affiliations:
- Federal Institute of São Paulo (IFSP)
arxiv_id: '2610.30970'
url: https://arxiv.org/abs/2610.30970
pdf_url: https://arxiv.org/pdf/2610.30970
published: '2026-10-21'
collected: '2026-10-27'
category: LLM
direction: 闭集决策 · 紧凑型编码器优化
tags:
- Closed-set Decision
- Compact Encoder
- Joint Encoding
- Per-option Scoring
- Zero-shot Classification
one_liner: 对比闭集决策下两种选项编码方式，开源17M到1B参数的高性能紧凑型联合编码器系列
practical_value: '- 做Agent工具选择、电商用户意图分类、工单路由等闭集决策场景时，可直接复用Crivo系列联合编码器：68M/150M版本精度比435M参数DeBERTa-v3零-shot分类器高4.9~5.9个点，17M版本CPU中位数延迟仅13.5ms，比DeBERTa快50倍，可完全替代大模型prompt分类方案，大幅降本提效。

  - 若业务对选项顺序鲁棒性要求极高（如电商候选排序、工具调用对选项顺序敏感的场景），优先选择per-option逐选项编码方案，完全不受选项顺序影响；若追求吞吐量优先选联合编码，12~23%的答案波动可通过训练时随机打乱选项顺序缓解。

  - 小参数闭集决策编码器选型可参考：68M/150M是精度和延迟的最优平衡点，在未见过的零样本任务上精度与435M DeBERTa持平，训练成本仅几十美元，适合业务场景小样本微调定制。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM pipeline中闭集决策（工具选择、意图分类、零样本分类等）的主流方案存在明显缺陷：大模型prompt推理速度慢、对选项顺序高度敏感；NLI模型逐选项打分随选项数量线性增加成本；单任务微调泛化性差，无法适配动态标签集，亟需低延迟、高精度、泛化性好的紧凑型闭集决策编码器，同时明确联合编码与逐选项编码两种主流架构的优劣边界。
### 方法关键点
- 对比两种编码架构：联合编码将上下文与所有选项拼接为单序列，每个选项前加[OPT]标记，1次encoder pass即可输出所有选项分数；逐选项编码将上下文与每个选项分别拼接编码，n个选项需n次pass，后接softmax归一化分数。
- 开源Crivo系列6款联合编码器，参数覆盖17M~1B，基于Ettin reranker初始化，采用交叉熵+Brier score+知识蒸馏混合损失训练，支持最长32768 token输入，无截断处理。
- 严格做训练数据与测试集的污染审计，拆分可见/不可见任务，避免数据泄露导致结果虚高。
### 关键结果
- 32M参数控制实验：相同训练步数下，逐选项编码比联合编码在37个基准集上机会校正skill高5.8个点，相同训练计算量下高2.8个点，该优势仅在reranker初始化下存在，原始encoder初始化下两种方案无显著差异。
- Crivo-68M/150M在209个S1-Arena任务上精度比435M DeBERTa-v3零-shot分类器高4.9/5.9个点，145个未见过的任务上精度与其持平；17M版本CPU中位数延迟仅13.5ms，比DeBERTa快50倍以上。
- 联合编码方案重排选项会改变12~23%的答案，逐选项编码完全不受选项顺序影响，但逐选项编码的平均延迟是联合编码的4~27倍。
### 核心结论
闭集决策场景下，150M参数以内的紧凑型联合编码器精度已经超过400M+参数的通用零-shot分类器，延迟低1~2个数量级，是替代大模型prompt分类、NLI逐选项打分的高性价比方案。
