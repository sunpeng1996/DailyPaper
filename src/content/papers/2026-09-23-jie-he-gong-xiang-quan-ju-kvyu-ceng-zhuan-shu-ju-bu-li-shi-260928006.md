---
title: Shared Global KV with Layer-Specific Local History
title_zh: 结合共享全局KV与层专属局部历史的Transformer缓存优化
authors:
- Xinglang Xian
arxiv_id: '2609.28006'
url: https://arxiv.org/abs/2609.28006
pdf_url: https://arxiv.org/pdf/2609.28006
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM推理优化 · KV cache 跨层共享
tags:
- KV cache
- Transformer Inference
- Cross-layer KV Sharing
- Perplexity
- Long Context
one_liner: 提出共享全局KV加层专属局部历史的KV缓存设计，实现推理效果与资源开销的更优权衡
practical_value: '- 部署LLM驱动的电商推荐文案生成、query理解、Agent推理服务时，可复用「全局共享KV+层级128token局部历史KV」的架构，在PPL仅损失不到1%的前提下，将KV缓存容量降低近一半，适配高并发场景

  - 预填充（prefill）占比高的短生成业务场景（如搜索query改写、推荐卡片短文案生成）可优先采用该方案，实测prefill耗时比CLA跨层共享方案低16.4%，满足低延迟响应要求

  - 推理侧可直接复用论文提出的精确后缀预计算调度策略，上层仅需计算局部窗口内的依赖，实测比全量预填充提速1.8倍，无需损失精度即可降低预填充阶段算力开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Decoder-only Transformer生成时的KV缓存需随层深、序列长度线性扩容，跨层共享KV可大幅降低显存占用，但会损失不同层的表征多样性，现有方案未解决共享全局KV下如何保留必要层级局部信息的问题，效果退化明显。
### 方法关键点
- 架构分层：Transformer拆为8层下层、8层上层，下层输出经归一化投影得到全局共享KV，所有上层复用该全量前缀KV，无需每层独立存储
- 层专属局部KV：每个上层额外维护长度为128的局部历史KV，与全局KV共同输入同一个softmax做注意力计算，通过注意力得分动态分配两部分的权重占比
- 相邻层输入共享：相邻上层可共享局部KV的输入表征，仅保留独立的归一化和KV投影，进一步缩短预填充依赖链
- 精确后缀调度：基于局部窗口的依赖边界推导各层所需的最小输入后缀长度，无需全量计算上层表征即可构造完整缓存，算术精度与全量计算完全一致
### 关键结果
126M参数模型在FineWeb-Edu数据集训练，2K上下文下：
- 比仅保留当前token的局部分支方案，测试集perplexity低1.4%
- 比GQA2、CLA跨层共享基线，perplexity分别低1.43%、1.15%，适配8K上下文后优势仍保持
- 资源开销：prefill耗时比CLA低16.4%，但128步长解码耗时高32.98%；精确后缀调度可将预填充速度提升1.8倍
### 核心结论
KV缓存优化需根据业务场景的prefill/解码占比做权衡，共享局部KV的输入源比直接共享投影后的KV，对模型效果的损伤更小。
