---
title: 'LOCKS: Page-Local Compact Key Summaries for Efficient Long-Context Decoding'
title_zh: LOCKS：基于页局部紧凑键摘要的高效长上下文解码方法
authors:
- Junsung Hwang
arxiv_id: '2607.24555'
url: https://arxiv.org/abs/2607.24555
pdf_url: https://arxiv.org/pdf/2607.24555
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: LLM长上下文推理 · KV cache优化
tags:
- KV cache
- long context
- LLM inference
- vLLM plugin
- spectral summary
one_liner: 无训练页级谱摘要KV缓存选择机制，作为vLLM插件实现长上下文解码2倍加速
practical_value: '- 直接复用LOCKS的vLLM插件优化长上下文RAG服务：电商商品/订单知识库查询、Agent长会话推理场景，1M上下文下解码时延降50%，不损失生成质量

  - 借鉴页局部低秩结构思路优化RAG召回排序：对召回文档块做局部谱摘要，无需读取全量文档即可快速计算与用户Query的匹配度，降低大批次召回的带宽开销

  - 量化选型参考：KV摘要用int4量化、秩取8的配置在精度和空间开销上达到最优平衡，可直接套用到业务侧的语义向量压缩场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM推理的核心瓶颈是KV cache读取带宽，单请求128K上下文的bf16格式KV缓存占16GiB显存，远大于模型本身权重。现有KV选择方案要么用全局共享低秩投影存在页内容盲spot，要么仅保留粗粒度统计量丢失关键载体页，小预算下推理质量大幅下降。

### 方法关键点
- 利用attention键局部低秩、全局高秩的特性，给每个KV页单独构造秩为8的谱摘要，仅占原KV页大小的1/10，无需训练
- 解码时仅读取摘要重建页内logit，通过log-sum-exp估算每页注意力权重，仅选择top页参与计算，无需读取候选页的KV内容
- 适配GQA分组注意力用份额平均规则合并多查询的页选择结果，减少重复计算，完整支持CUDA图加速，可作为无修改vLLM的插件直接部署

### 关键实验
在LongBench-v1长文档QA、AIME26/MATH-500长推理、InfiniteBench 100K+上下文等数据集上，对比Quest、ShadowKV、RocketKV等SOTA方案：2048-token预算下100K+上下文质量和全量KV持平，仅需访问2%的token；1M上下文下解码时延减半（2.0×加速），每步KV读取量降低9.8×；长推理任务上基线方案性能崩溃时仍接近全量KV效果。

最值得记住的一句话：Attention键的局部低秩结构比全局/序列级低秩投影的表征效率高一个量级，是小预算下兼顾长上下文推理质量和速度的核心抓手。
