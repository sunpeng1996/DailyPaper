---
title: 'History Replays Itself: Unleashing Long-Context Capability in Linear Attention'
title_zh: NoteBank：通过历史重放释放线性注意力的长上下文能力
authors:
- Li Nanbo
- Firas Laakom
- Yilan Zhang
- Piotr Piękos
- Yimeng Chen
- Liangyu Wang
- Yifan Xu
- Mateusz Ostaszewski
- Dandan Guo
- Wenyi Wang
affiliations:
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2610.15715'
url: https://arxiv.org/abs/2610.15715
pdf_url: https://arxiv.org/pdf/2610.15715
published: '2026-10-10'
collected: '2026-10-16'
category: LLM
direction: 线性注意力 · 长上下文记忆增强
tags:
- Linear-Attention
- Long-Context
- Memory-Augmentation
- Training-Free
- Plug-and-Play
one_liner: 免训练插件式记忆模块NoteBank，将线性注意力模型百万token检索精度从1.7%提升至70.3%
practical_value: '- 做Agent长会话记忆可复用NoteBank的原生特征选段+重放架构，无需额外训练嵌入/检索器，兼容Mamba、Qwen等主流线性/混合注意力模型，大幅降低外挂记忆开发成本

  - 长文档/长序列建模场景（如电商商品说明书解析、用户全生命周期行为建模）可借鉴其token区分度选关键片段策略，1M token场景下存储仅为同规格MHA KV
  cache的1/2600

  - 业务侧使用线性注意力模型做低延迟推理的场景，可直接集成训练免费版NoteBank，仅增加≤0.025% FLOPs开销即可大幅提升长上下文召回能力，无需重训模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
线性注意力具备线性时间推理、固定大小循环状态的效率优势，是长序列场景的主流技术选型，但固定状态需要同时承担实时计算和长时记忆存储功能，持续压缩历史会导致远距离信息不可逆丢失，长上下文检索精度随序列长度增长骤降，此前行业普遍认为这是线性注意力的固有性能天花板。

### 方法关键点
- 完全解耦的插件式稀疏记忆模块，无需修改backbone权重、无需额外嵌入模型/独立检索器/阅读器，完全训练免费
- 写阶段：上下文分块处理，用模型原生key的区分度筛选高价值文本片段作为note，用片段内query向量生成原生地址索引
- 寻址阶段：用query的原生特征与note地址做余弦匹配投票，召回top-R相关note，按原文顺序排序
- 读阶段：召回note直接重放给backbone做原生前向计算，可选加轻量LoRA适配读阶段提升下游任务效果

### 关键结果
在RULER 6项检索任务、LongBench v1/v2、MemoryAgentBench上验证：1M token场景下Gated DeltaNet平均检索精度从1.7%提升至70.3%，4K到1M token无明显检索衰减；新增FLOPs开销≤0.025%，持久化存储仅为同规格MHA KV cache的1/2600；在Mamba-2-8B、Qwen3.5-9B等商用级模型上也稳定取得长上下文效果提升。

### 核心结论
线性注意力的长上下文能力天花板并非来自模型本身，而是来自循环状态的记忆存储限制，通过独立的稀疏记忆归档+原生重放即可在几乎无额外开销的前提下大幅解锁其长上下文能力。
