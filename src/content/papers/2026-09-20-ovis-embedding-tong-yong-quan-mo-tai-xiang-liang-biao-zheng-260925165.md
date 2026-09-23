---
title: 'Ovis-Embedding: Pushing the Frontiers of Universal Omni-Modal Embeddings'
title_zh: Ovis-Embedding：通用全模态向量表征的前沿突破
authors:
- Embedding Team
affiliations:
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2609.25165'
url: https://arxiv.org/abs/2609.25165
pdf_url: https://arxiv.org/pdf/2609.25165
published: '2026-09-20'
collected: '2026-09-23'
category: Multimodal
direction: 全模态Embedding · 跨模态统一检索
tags:
- Omni-Modal Embedding
- Cross-Modal Retrieval
- Contrastive Learning
- Knowledge Distillation
- LLM Adaptation
one_liner: 基于原生多模态大模型训练的全模态Embedding，覆盖图文音视频，实现跨模态检索SOTA
practical_value: '- 电商跨模态搜索/商品召回场景可直接复用同质源采样trick：每个微批次样本来自同一任务，构造同任务hard negatives，避免模型学习模态等捷径特征，提升细粒度语义匹配精度

  - 工程部署可复用低秩特征分解方案：同一编码器可输出128/256/512/1024/2048多维度向量，适配不同存储、延迟预算，仅带来极小的性能损失

  - Agent多模态记忆/工具检索场景可复用原生多模态初始化方案：直接基于预训练全模态大模型改造，移除生成头即可得到统一Embedding，无需新增模态专属投影层，降低开发成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Embedding大多在图文底座上额外拼接音频分支，未原生实现全模态统一对齐，无法支撑图文音视频任意模态到任意模态的检索需求；而电商内容检索、Agent多模态记忆、RAG等场景对跨模态统一表征的需求日益迫切，需要能兼容单模态、 interleaved多模态输入的通用Embedding方案。

### 方法关键点
- 原生全模态底座改造：直接基于预训练Qwen-Omni（全模态）、Qwen3.5（图文）底座，移除语言模型生成头，取最后一个非padding token的隐藏态作为检索Embedding，无额外模态专属投影层，保留原生跨模态对齐能力
- 数据构造与采样：构建覆盖图文音视频、 interleaved多模态、Agent任务的50M高质量query-positive-negative训练对，采用同质源采样策略，每个微批次样本来自同一数据集，去重后构造同任务hard negatives，减少模态捷径
- 四阶段训练优化：1）LoRA对比预训练，用focal loss加权难例，结合Embedding蒸馏迁移模态专家的细粒度相似度结构；2）全参数微调，用同质源采样提升细粒度语义区分度；3）退火蒸馏，上采样学生错例，动态调整蒸馏权重，补全短板能力；4）低秩特征分解，支持多维度弹性Embedding输出

### 关键结果
- MMEB-v3全模态检索基准：Ovis-Embedding-Omni-3B得分78.3，领先第二名e5-omni-7B 3.3个百分点，包揽全部6个模态组第一
- MMEB-v2图文检索基准：Ovis-Embedding-VL-9B得分84.5，领先第二名2.1个百分点，包揽5个任务组中的4个第一
- 同时在MVEB视频检索、MAEB音频检索、RTEB文本检索基准上均取得SOTA性能

### 核心结论
原生全模态大模型作为Embedding底座的效果显著优于拼接独立模态塔的方案，全模态统一训练可有效解决模态碎片化问题，为任意模态到任意模态的检索提供可行路径
