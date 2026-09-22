---
title: 'Machine-Interpretable Information: Compiling Documents into Searchable and
  Readable Protocol States'
title_zh: 机器可解释信息：将文档编译为可搜索可读的协议状态
authors:
- Yifan Wang
- Dejing Dou
affiliations:
- NexusLumenLabs
- Fudan University
arxiv_id: '2609.23371'
url: https://arxiv.org/abs/2609.23371
pdf_url: https://arxiv.org/pdf/2609.23371
published: '2026-09-20'
collected: '2026-09-22'
category: RAG
direction: 长文档RAG · 跨模型编译协议
tags:
- RAG
- Long-Context
- Document-Compression
- A2A-Protocol
- Mamba
one_liner: 提出跨模型通用的A2A文档编译协议MII，大幅降低长文档RAG推理开销
practical_value: '- 电商商品知识库、售后手册、用户评价聚合等静态长文档RAG场景，可复用双时态Mamba编译架构，一次编译生成固定长度MII状态，多轮查询直接复用，降低长文本推理成本

  - Residual-MII分层缓存思路可直接迁移到电商客服Agent、商品问答场景：全局语义用编译态存储，精准实体/属性依赖稀疏片段检索，平衡推理效率和答案准确率

  - 轻量Translator适配逻辑可复用在多LLM混合部署的业务架构中，一次编译的语义状态可适配不同下游LLM，避免重复预处理开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统RAG存在固有索引-Payload割裂问题：稠密向量仅支持检索路由，推理时需重新加载全文带来O(N²)注意力开销，现有上下文压缩方案均绑定特定模型架构，无法跨模型复用，长文档场景下成本极高。
### 方法关键点
- 基于双时态Mamba构建Writer：慢分支偏向长距离语义集成，快分支捕捉局部语义变化，将任意长度文档编译为固定56 token的标准MII状态，拆分全局（16token）、事件（24token）、覆盖（16token）三个互补内存银行，兼顾全局结构、局部变化和覆盖度
- 轻量Translator仅需微调即可将标准MII状态映射到任意冻结Reader LLM的嵌入空间，实现跨Llama、Qwen、Mistral等异构LLM的兼容性
- Residual-MII架构融合编译全局状态与稀疏检索文本片段，解决固定带宽下的精确实体/词汇重建问题
### 关键结果
HotpotQA 7405条多跳问答测试集上，Residual-MII Exact Match超过全上下文基线，仅消耗≈7%的注意力FLOPs；28K token长文档场景下，Residual-MII仅消耗全上下文0.03%的FLOPs；单文档查询次数≥5时，编译成本可完全摊销，单查询latency稳定在132.8ms。
### 核心结论
将文档从人类可读的原生文本转换为机器原生的跨模型编译态神经协议，是实现长文档理解效率和泛化性双重突破的可行路径。
