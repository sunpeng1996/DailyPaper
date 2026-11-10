---
title: 'LEGIT: Live Eligibility Gating over Identifier Tries for Constrained Decoding
  of Heterogeneous Pages'
title_zh: LEGIT：生成式推荐整页解码的标识符前缀树动态准入门控
authors:
- Felix Fang
- Zheng Liu
- Robert Saliba
affiliations:
- Uber Technologies, Inc.
arxiv_id: '2611.10357'
url: https://arxiv.org/abs/2611.10357
pdf_url: https://arxiv.org/pdf/2611.10357
published: '2026-11-07'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · Semantic ID约束解码
tags:
- GenRec
- Semantic ID
- Constrained Decoding
- Trie
- LLM Serving
one_liner: 提出适配生成式推荐整页解码的动态约束校验方案，开销仅为无约束解码的1.7倍
practical_value: '- 工程实现Semantic ID约束时优先选择CPU侧做前缀树遍历，无需开发自定义CUDA kernel，与GPU模型前向并行可降低65%以上的单token延迟，性价比远高于GPU侧优化

  - 前缀树叶子节点统一采用深度优先编号，可将准入校验、去重、嵌套从属校验等所有规则转化为有序数组的二分查找，逻辑简洁易维护，可直接复用该设计

  - 整页生成的动态约束不要适配XGrammar等静态语法约束引擎，这类工具无法支持逐token变化的规则，实测性能比自定义方案低100倍

  - 上线前必须同时测试轻载（每步1-2个请求）和满载（队列打满）两种场景，不同约束实现的性能表现会出现反转，仅测单场景容易做出错误选型'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐已开始支持单次LLM解码直接输出整页推荐结果（含商家、商品嵌套结构），但生成的Semantic ID需满足三类动态约束：仅准入当前请求合法候选（如配送范围、库存）、已输出内容不可重复、嵌套从属关系正确（如商品必须属于上方商家）。现有约束解码方案要么无法适配逐请求、逐token变化的规则，要么性能损耗过高，直接使用会让解码速度降至无约束的5倍，达不到上线要求。
### 方法关键点
- 离线构建2个前缀树（商家、商品Semantic ID）+3个索引（地理位置到商家、商家到商品、商家到品牌），前缀树叶子按深度优先编号，每个节点对应一段叶子ID区间，所有规则校验转成有序数组的二分查找
- 约束校验逻辑放在CPU侧执行，和GPU模型前向计算并行，无需自定义CUDA kernel，每步批量将合法token列表传输到GPU对logits加掩
- 新增内层子树压缩、每行已输出集合缓存、前缀树状态增量携带等优化，避免重复计算
### 关键结果
基于Uber Eats真实搜索流量，6亿参数Qwen3模型、单B200 GPU、vLLM连续batching环境下测试：
- 最优全CPU栈方案较GPU侧直接遍历前缀树的基准实现，轻载下单token耗时降低65.9%，仅为无约束解码的1.7倍
- 满载场景下吞吐量提升96.9%，p95延迟降低97.5%
- 所有生成页面100%通过合法性校验，无不存在、超范围、重复、从属关系错误的候选
### 最值得记住的一句话
生成式推荐动态约束校验的核心瓶颈不是计算量，而是GPU kernel启动和CPU-GPU同步开销，把轻量前缀树遍历放到CPU侧与模型前向并行的收益，远高于在GPU侧做复杂优化
