---
title: 'LQ-Rec: Late Quantization for Sequential Recommendation'
title_zh: LQ-Rec：面向序列推荐的后量化生成式推荐方法
authors:
- Satoshi Koide
- Yueqi Wang
- Julian McAuley
affiliations:
- Toyota Motor North America
- UC San Diego
arxiv_id: '2611.25256'
url: https://arxiv.org/abs/2611.25256
pdf_url: https://arxiv.org/pdf/2611.25256
published: '2026-11-18'
collected: '2026-11-20'
category: GenRec
direction: 生成式推荐 · Semantic ID后量化优化
tags:
- Sequential Recommendation
- Semantic ID
- Residual Quantization
- Generative Retrieval
- Anytime Inference
one_liner: 后量化序列推荐范式解耦模型与量化误差，实现语义ID可扩展、单模型任意压缩
practical_value: '- 语义ID生成范式可直接迁移：将量化操作移至候选物品侧，避免序列编码器处理离散token带来的内存和精度损失，适配大SKU规模的电商序列推荐场景

  - 两阶段训练流程可复用：先做连续空间排序预训练，再做前缀感知的量化微调，无需为不同精度要求训练多套模型，大幅降低多场景部署的迭代维护成本

  - 任意压缩特性可直接落地业务：仅截断Semantic ID前缀即可动态权衡推荐精度和推理延迟，适配首页推荐、猜你喜欢等不同latency要求的业务场景

  - 量化损失评估逻辑可复用：量化导致的排序损失可通过控制单物品量化误差和得分margin进行约束，可用于业务上线前评估语义ID压缩的精度损失上限'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式序列推荐普遍将量化操作置于序列编码器之前，耦合模型与量化误差，导致Semantic ID长度增加时排序精度不升反降、内存开销呈平方级增长，无法兼顾存储效率、推理速度和排序效果。

### 方法关键点
- 后量化（LQ）范式仅在候选物品侧做离散化，序列编码器和打分逻辑全程运行在连续空间，实现模型误差与量化误差的加性分解，从理论上保证量化带来的排序损失可被有效约束
- 两阶段训练策略：第一阶段S2H-QA通过退火策略从连续排序损失过渡到量化感知排序损失，端到端联合训练序列编码器和残差量化器；第二阶段Prefix-MQA固定编码器，针对所有Semantic ID前缀长度优化交叉熵损失，实现单模型支持任意前缀截断
- 推理仅需1次序列编码器前向计算，通过Semantic ID前缀树beam search检索物品，无额外Transformer前向开销

### 关键实验结果
在Toys、Beauty、Sports、Yelp四个公开数据集上对比10个主流基线，Semantic ID长度M=16时Recall@10较最优同配置语义ID基线RPG分别提升19%、23%、31%、57%；单模型无需重训，仅截断Semantic ID前缀即可实现精度-推理成本的动态权衡；在MemGen泛化测试集上NDCG@10较所有基线最高提升45%。

### 核心结论
量化操作的放置位置比量化器本身的设计对Semantic ID推荐系统的效果影响更大，将量化后置到候选侧可同时解锁精度、扩展性、泛化性三重收益
