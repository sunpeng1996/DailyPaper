---
title: 'FreeSolo: Linear-time Sparse Attention with Zero-Shot Length Extrapolation'
title_zh: FreeSolo：支持零样本长度外推的线性时间稀疏注意力机制
authors:
- Zekun Shi
- Alastair James Arthur Price
affiliations:
- National University of Singapore
- University of Toronto
- Sea AI Lab, Singapore
arxiv_id: '2610.17191'
url: https://arxiv.org/abs/2610.17191
pdf_url: https://arxiv.org/pdf/2610.17191
published: '2026-10-11'
collected: '2026-10-16'
category: LLM
direction: 长上下文LLM · 稀疏注意力长度外推
tags:
- Sparse Attention
- Length Extrapolation
- Long Context LLM
- KV Cache
- Linear Time Attention
one_liner: 无需长上下文微调，实现线性时间稀疏注意力及64倍训练长度的零样本外推
practical_value: '- 长会话Agent、用户长行为序列建模可复用FS-L的KV剪枝策略：按KV的L2 norm保留高重要度单元+最近单元，仅需极短续预训练（CPT）即可实现线性时间推理，无需全量重训大模型

  - 推荐系统的长短依赖建模可借鉴双分支设计：短窗口用RoPE建模近邻交互依赖，长距离检索用NoPE避免未知位置编码偏移，平衡精度和效率

  - 超长文档RAG（如百万级商品库检索）可复用FS-B的平衡树检索架构，O(Nlog²N)复杂度实现全前缀无信息丢弃的长距离检索，比全注意力大幅降低内存占用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长上下文LLM方案要么依赖固定大小循环状态导致关键信息丢失，要么混合全注意力带来二次计算开销，稀疏注意力的长序列续预训练成本高且零样本长度外推能力差，无法低成本落地业务场景的超长上下文需求。

### 方法关键点
- 双分支注意力架构：短分支用固定大小滑动窗口+RoPE建模近邻依赖，长分支用NoPE避免未知位置偏移，两路输出按头级可学习权重融合
- 两种轻量化变体：FS-L为线性时间版本，先按cell内KV最大norm剪枝前缀，再选top-K cell做token级注意力，内存占用固定；FS-B为平衡树搜索版本，构建双内容森林做分层检索，复杂度O(Nlog²N)，不丢弃任何前缀信息
- 仅需在4k训练长度下做极短CPT（约为预训练token量的5%），无需长序列训练即可适配剪枝/检索逻辑

### 关键实验结果
基于FineWeb-Edu训练的800M参数模型：4k训练长度下零样本外推到256k（64倍）时，FS-L单针检索准确率85%，FS-B达100%；16k长度下FS-B的RULER均值30.4，FS-L达22.3，远超同量级基线Raven的12.8、NAtS-L的2.8；短上下文下游任务平均准确率FS-L仅比全注意力低1.6个百分点，精度损失可控。

**最值得记住的一句话**：内存摘要仅需定位证据即可，原始证据可保留在token级KV中无需压缩，即可实现低成本长上下文外推。
