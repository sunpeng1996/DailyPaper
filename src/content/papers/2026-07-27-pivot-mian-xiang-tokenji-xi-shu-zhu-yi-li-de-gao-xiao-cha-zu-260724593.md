---
title: 'PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention'
title_zh: PIVOT：面向Token级稀疏注意力的高效查询组索引方法
authors:
- Hong Liu
- Yuan Cheng
- Lin Niu
- Yi Su
- Yufei Xue
- Anmin Liu
- Guanghua Yu
- Jianchen Zhu
affiliations:
- Tencent
arxiv_id: '2607.24593'
url: https://arxiv.org/abs/2607.24593
pdf_url: https://arxiv.org/pdf/2607.24593
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: 长上下文LLM推理 · 稀疏注意力加速
tags:
- Sparse Attention
- Long Context Inference
- DSA
- Index Optimization
- LLM Serving
one_liner: 训练免改的DSA索引器替代方案，靠查询组共享扫描实现长上下文4倍索引加速无精度损失
practical_value: '- 业务中若使用支持DSA的大模型（DeepSeek/GLM-5等）做长上下文用户行为分析、商品匹配，可直接替换PIVOT索引器，长上下文下最多降低40%端到端延迟，完全无精度损失

  - 序列推荐、搜索的稀疏召回/topk选择模块可复用PIVOT思路：对相邻/相似查询分组，聚合生成代理query做粗筛，再单query精排小候选集，大幅降低全量扫描开销

  - 电商客服Agent、多轮对话Agent的长上下文推理可配合MTP+PIVOT使用，两份加速收益叠加，无需修改现有模型架构，训练零成本

  - 可根据业务请求的上下文长度动态切换变体：短上下文用PIVOT-Reuse降开销，长上下文切PIVOT-Refine保精度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM推理中，DeepSeek Sparse Attention（DSA）虽将主Attention复杂度从O(L²)降至O(Lk)，但索引器需为每个query全前缀扫描token，仍保留O(L²)开销，200K上下文下索引占prefill延迟81%、decode延迟41%，成为新瓶颈。现有优化均沿token/head/layer轴展开，未利用相邻query top-k选择高度重叠的冗余特性，存在优化空间。
### 方法关键点
- 完全兼容原有DSA接口，训练零成本，下游Sparse MLA、KV cache无需修改即可替换
- 分组策略：prefill阶段将连续query按固定大小g（默认4）分组；decode阶段直接复用MTP（多token预测）单步生成的d+1个query作为分组，无额外开销
- 代理查询生成：对组内query的索引头做均值 pooling 得到单个代理query，仅执行1次全前缀扫描得到共享候选集
- 双变体适配不同场景：PIVOT-Reuse直接共享代理query的top-k结果，速度最快；PIVOT-Refine保留代理top-c（默认c=2k）候选集，每个query在小候选集内重打分选top-k，精度和原生DSA完全对齐
### 关键结果
- 测试模型为DeepSeek-V3.2、GLM-5.1，覆盖LongBench、RULER两大长上下文基准
- PIVOT-Refine精度完全对齐原生DSA，索引器最高提速4×，256K上下文下端到端延迟最高降低1.6×
- 与现有DSA优化方案（如IndexCache）完全正交，可叠加使用获得额外收益
### 核心洞见
相邻query的注意力选择存在天然冗余，跨query共享计算是长上下文稀疏注意力优化的第四类核心轴，与token/head/layer轴完全正交。
