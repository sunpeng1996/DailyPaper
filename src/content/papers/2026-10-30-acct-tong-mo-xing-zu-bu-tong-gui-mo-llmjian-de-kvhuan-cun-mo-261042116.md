---
title: 'ACCT: Asymmetric Cross-LLM Context Transfer'
title_zh: ACCT：同模型族不同规模LLM间的KV缓存跨模型迁移方法
authors:
- Yuzhe Liu
- Haolin Tian
- Tonghan Wang
affiliations:
- Tsinghua University
arxiv_id: '2610.42116'
url: https://arxiv.org/abs/2610.42116
pdf_url: https://arxiv.org/pdf/2610.42116
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM推理优化 · KV cache跨模型复用
tags:
- KV Cache
- Heterogeneous LLM Serving
- Context Reuse
- Inference Optimization
- Cross-Model Transfer
one_liner: 通过三层轻量模块实现同家族跨规模LLM的KV缓存迁移，大幅降低异构部署的上下文重复计算开销
practical_value: '- 电商RAG/Agent系统普遍采用异构LLM路由策略（难query调大模型、简单query调小模型），可直接复用ACCT实现历史会话、检索到的长商品详情/用户评价的KV缓存跨模型迁移，避免切换模型时重复预编码，长上下文场景下推理延迟降幅明显。

  - 三个模块的设计可迁移到现有单模型KV压缩方案优化：Cartographer的逐头逐层Query相关token排序逻辑、Allocator的全局预算下分层动态容量分配策略、Compiler的线性变换+残差校正的KV转换范式，可直接用于优化SnapKV、PyramidKV等现有压缩方案的精度与压缩比权衡。

  - 同模型族跨规模模型的映射规则（相对深度对齐、模头映射）可直接复用，无需针对每对模型定制对齐逻辑，大幅降低跨模型特征迁移的开发成本。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前异构LLM部署成为工业界主流，系统会根据任务难度、延迟要求、资源情况动态将请求路由到不同规模的模型，但同一份上下文（会话历史、检索文档、prompt前缀）在切换模型时需要重新预编码生成KV缓存，长上下文下这部分开销占比极高，现有单模型KV缓存、前缀缓存机制无法跨模型复用，造成大量冗余计算。

### 方法关键点
- 整体框架包含三个轻量模块，全程冻结源、目标基座模型：1）Cartographer：结合Query表示、上下文特征、目标层/头标识、token位置信息，为每个目标KV头的所有上下文token打分，确定保留优先级；2）Allocator：在全局KV预算约束下，为每个目标层/头动态分配保留的token数量，默认强制保留最近32个上下文token，剩余容量按打分排序分配；3）Compiler：通过线性Bridge变换+上下文相关残差校正网络，将选中的源模型KV转换为目标模型可直接读取的稀疏KV，保留原始token的位置信息。
- 训练分三阶段：先用token删除效用监督训练Cartographer的排序能力，再用答案预测损失训练Allocator的容量分配策略，最后用三层损失（表征对齐、注意力对齐、预测分布对齐）训练Compiler的KV转换能力。

### 关键结果
- 实验覆盖Qwen3、Llama、Qwen2.5三个模型族的6组双向跨规模迁移对，在5个通用能力基准、6个强上下文依赖任务上验证效果。
- 4倍KV压缩（缓存体积减少75%）下，多数任务性能持平甚至超过目标模型全量编码的效果；19K长上下文下，KV转换比目标模型上下文prefill提速6.5~21.2倍，仅占用原prefill时间的4.7%~15.3%。

最值得记住的结论：上下文计算可以作为跨模型可复用的独立资源，异构LLM部署完全可以实现上下文预编码和下游推理的解耦。
