---
title: 'Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap
  in Offline Retrieval-Augmented Generation'
title_zh: 离线RAG文本-向量完整性缺口测量与修补方案
authors:
- Georgios Feretzakis
- Alexandros Papaspyridis
affiliations:
- securagen.ai, Athens, Greece
arxiv_id: '2611.06498'
url: https://arxiv.org/abs/2611.06498
pdf_url: https://arxiv.org/pdf/2611.06498
published: '2026-11-04'
collected: '2026-11-05'
category: RAG
direction: 检索增强生成 · 向量完整性校验
tags:
- RAG
- Vector Database
- Embedding
- Edge AI
- Security
one_liner: 提出margin law量化RAG向量篡改风险，给出跨设备可复现的代码级向量完整性校验方案
practical_value: '- 做离线RAG/向量库的业务不要仅靠签名校验向量：签名仅能证明来源，无法保证向量与对应文本一致性，可防范供应链/内部人员投毒风险

  - 若采用容忍度向量校验，可直接用业务query log和诚实向量通过margin law计算篡改暴露率，无需模拟攻击即可快速评估风险

  - 向量库使用SQ/PQ/二进制压缩格式的场景，直接采用代码级校验+规范化，不要做容忍度向量比对：后者对PQ格式几乎100%暴露，前者测试中100%拦截篡改且无误拒

  - 边缘端RAG的校验任务尽量调度到LLM空闲时运行，或采用独立算力，实测同CPU运行校验会使LLM解码速度下降23%-31%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
离线边缘RAG部署中，知识包通常携带预计算向量避免端侧嵌入的高耗时，但签名仅校验包的来源合法性，无法保证向量与对应文本的语义一致性；攻击者可篡改预计算向量操控检索结果，而现有容忍度校验方案的风险未被量化，压缩向量库更是缺乏有效的完整性校验方案。

### 方法关键点
- 提出margin law：最优攻击者在余弦容忍度τ下的查询劫持率，等于查询的角度检索余量小于arccosτ的占比，可直接通过诚实向量和query log计算暴露率，无需模拟攻击
- 针对压缩向量库提出代码级校验方案：校验端仅信任自身从文本重计算的嵌入，比对压缩编码而非原始向量，设置校准保护带处理跨设备浮点噪声，对校验通过的编码用自身结果规范化，彻底消除攻击者篡改空间
- 覆盖5种校验方案、3种硬件平台的全链路测试，验证各方案的安全性与性能开销

### 关键结果
- 容忍度校验暴露率极高：浮点噪声级容忍度暴露0-5.5%的查询，INT8级容忍度暴露98%-100%的查询；FAISS PQ压缩索引的容忍度校验下，25%的目标查询攻击者可将恶意文档排到首位
- 代码级校验在所有测试平台+所有压缩格式下，100%接受诚实样本，100%拦截攻击，经规范化后无残余暴露
- 端侧校验成本：树莓派CPU上同时运行校验和LLM，会让LLM解码速度下降23%-31%，调度到空闲时运行可规避影响

**最值得记住的一句话**：任何向量校验的容忍度本质都是攻击预算，压缩向量库不要做容忍度的向量比对，直接做代码级校验+规范化。
