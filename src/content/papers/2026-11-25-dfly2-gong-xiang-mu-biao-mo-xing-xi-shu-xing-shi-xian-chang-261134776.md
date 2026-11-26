---
title: 'DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target''s
  Sparsity'
title_zh: DFly2：共享目标模型稀疏性实现长上下文推测解码加速
authors:
- Hong Liu
- Rui Cen
- Junhan Shi
- Lin Niu
- Runzhi Fan
- Zhaojing Zhou
- Haodi Lei
- Jiebin Zhang
- Saiyong Yang
- Junqiang Zheng
affiliations:
- Tencent Inc.
arxiv_id: '2611.34776'
url: https://arxiv.org/abs/2611.34776
pdf_url: https://arxiv.org/pdf/2611.34776
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: 长上下文LLM推理 · 推测解码优化
tags:
- Speculative Decoding
- Sparse Attention
- Long Context LLM
- KV Cache
- Inference Acceleration
one_liner: 面向原生稀疏大模型的无独立KV缓存推测解码器，无损加速长上下文推理
practical_value: '- 部署长上下文电商导购Agent、多轮用户对话推荐、长商品文案生成服务时，若使用DeepSeek-V4、GLM-5等原生稀疏大模型，可直接复用DFly2方案，无需维护drafter独立KV缓存，64K
  Agent场景吞吐量最高提升81%

  - 推测解码drafter设计可复用大模型已计算的中间结果：包括稀疏attention索引、已缓存KV、层初始化权重，大幅降低推理额外开销，该思路可直接迁移到生成式推荐（GenRec）的LLM推理优化

  - 长会话推荐/Agent场景下，放弃固定滑动窗口的上下文选择逻辑，复用大模型原生query-aware的稀疏attention选点，相比固定窗口方案接受token长度最高提升31.5%，长度泛化性更强'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
原生稀疏长上下文大模型（DeepSeek-V4、GLM-5等）已将attention开销压缩为线性，但主流推测解码方案仍面向稠密模型设计：要么维护独立KV缓存，占用大量显存、降低请求并发、损失前缀缓存命中率；要么采用固定滑动窗口裁剪上下文，在长上下文/Agent场景下接受率骤降，drafter选点开销也随上下文长度线性增长。
### 方法关键点
- **KV共享**：drafter每层直接读取配对的目标模型稀疏层已缓存KV，无独立KV缓存，32K上下文下请求并发提升1.73x，无prefill阶段额外开销
- **Index共享**：直接复用目标模型稀疏层已计算的query-aware top-k attention选点结果，无需额外索引计算，每步读取固定长度位置，开销不随上下文长度增长
- **权重初始化对齐**：drafter层权重从配对的目标模型层初始化，对齐query空间与特征分布，降低训练成本
- 新增目标模型最后一层隐状态注入、块内校正模块，提升token接受率
### 关键结果
在DeepSeek-V4.1-Flash、GLM-5.3-Flash、Hy4三个稀疏模型上测试，覆盖通用、128K长上下文、Agent三类benchmark，对比同训练配置的DFlash、DSpark baseline：
- 通用场景单步接受token长度提升3.9%~10.5%，长上下文/Agent场景提升10.0%~31.5%
- 高并发部署64K任务时，长上下文场景吞吐量提升62%，Agent场景提升81%
> 最值得记住：针对具备原生能力的大模型做推理优化，优先复用其已计算的中间结果而非新增独立模块，往往能实现无损大幅加速
