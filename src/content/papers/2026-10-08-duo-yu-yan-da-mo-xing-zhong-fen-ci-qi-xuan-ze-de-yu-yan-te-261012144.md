---
title: Language-Specific Effects of Tokenizer Choice in Multilingual Language Models
title_zh: 多语言大模型中分词器选择的语言特异性影响研究
authors:
- Clara Meister
- Gül Sena Altıntaş
- Antoine Bosselut
affiliations:
- EPFL
- University of Toronto
- Vector Institute
arxiv_id: '2610.12144'
url: https://arxiv.org/abs/2610.12144
pdf_url: https://arxiv.org/pdf/2610.12144
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: 多语言LLM · 分词器选型优化
tags:
- Multilingual-LLM
- Tokenizer
- Low-Resource-Language
- Model-Training
- Evaluation
one_liner: 通过123个模型+54个分词器的对照实验，量化多语言场景下分词器选择对不同语言的差异化影响
practical_value: '- 做跨境多语言电商/广告/推荐的LLM应用时，不要用全局聚合指标选分词器，必须针对目标小语种单独评测，低资源语种对分词器的敏感度是高资源语种的3倍以上

  - 不要盲目给低资源语种分配更多分词器训练权重，默认按语料占比 proportional 分配即可，强制加权反而会降低低资源语种的模型效果

  - 分词器选型阶段可先用9种语言专属的intrinsic metrics做预筛选，pairwise排序准确率达0.89，能节省90%以上的模型训练成本

  - 针对小语种的Agent/生成式推荐场景，优先保证目标语种在分词器训练语料中被覆盖，漏覆盖会直接抬升BPB，低资源语种损失更明显'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言LLM分词器优化研究多基于全局聚合指标，忽略了有限词表下不同语言的收益trade-off，低资源语种是否受分词器选择影响更大、如何高效选型等问题缺乏大规模对照实验支撑。

### 方法关键点
- 控制变量训练123个1.27B参数的decoder-only模型，仅分词器不同，覆盖54种分词器，涉及6种分词算法、多套预分词/归一化规则、4类分词训练数据分配策略
- 所有模型训练语料、token预算、优化器完全对齐，评测指标采用跨分词器可比的bits-per-byte (BPB)，覆盖31种训练语种+183种零样本语种
- 构建9种语言专属的分词器内在指标，训练pairwise排序模型实现无需预训练的分词器筛选

### 关键结果数字
- 分词器选择对低资源语种影响最大：语种BPB标准差和其在LM训练数据中的占比呈负相关（Spearman ρ=-0.52），低资源语种BPB波动是高资源的3倍以上
- 把语种排除在分词器训练外会抬升所有语种的BPB，低资源语种平均损失是高资源的2倍；但强制给低资源语种分配更高分词器训练权重反而会使其BPB上升最多达0.267
- 用语言专属内在指标预筛选分词器的held-out pairwise排序准确率达0.89，可直接替代小模型预训练筛选流程

### 核心结论
多语言场景下没有通用最优的分词器，低资源语种的分词器选型收益最大，也最容易被全局指标掩盖损失
