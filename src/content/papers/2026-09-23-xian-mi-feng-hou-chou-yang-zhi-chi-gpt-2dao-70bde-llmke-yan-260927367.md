---
title: 'Seal, Then Sample: Sampled Layerwise Proofs for Verifiable LLM Inference from
  GPT-2 to 70B'
title_zh: 先密封后抽样：支持GPT-2到70B的LLM可验证推理分层抽样证明方案
authors:
- Youki Lim
- Sam Yong
affiliations:
- TrueOpen
arxiv_id: '2609.27367'
url: https://arxiv.org/abs/2609.27367
pdf_url: https://arxiv.org/pdf/2609.27367
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM可验证推理 · 零知识证明
tags:
- Verifiable Inference
- Zero-Knowledge Proof
- Batch Proving
- LLM Quantization
- Sampled Audit
one_liner: 提出SLP分层抽样证明协议，可在单2TB CPU主机完成70B级LLM推理可验证审计
practical_value: '- 对于调用第三方LLM做推荐文案生成、用户意图理解的电商/推荐场景，可借鉴SLP抽样审计框架，无需重跑全量推理就能以可配置成本校验第三方输出是否符合约定，降低合规风险

  - 大模型服务端优化可复用批量打包证明思路：当证明成本核心来自权重加载而非token数时，用块对角因果掩码打包多请求同批次证明，可将12请求总证明成本降低6.5倍

  - LLM量化落地可参考其LLM-aware观测器设计：保留残差流24bit精度而非统一用12bit，可将与f32模型的argmax匹配度从16%提升到90%，避免量化后生成质量崩溃'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业大量外包LLM推理服务，但无法验证服务商是否使用了约定的模型权重、精度、推理逻辑，全量重跑推理成本过高，现有零知识证明方案无法支撑70B级大模型的验证需求，亟需可配置成本的可验证推理方案。

### 方法关键点
- 先密封后抽样协议：先对推理trace所有块的边界激活值做承诺，再由验证方随机抽取部分块+输入输出锚点块做证明，审计覆盖率可在runtime动态调整
- 批量打包证明：用块对角因果掩码将多并发请求打包进同一条推理trace，共享权重证明开销，每个请求的prompt和输出绑定到独立slot，无跨slot信息泄露
- 磁盘流式权重加载：量化权重落盘，分批做多项式承诺，无需将全量70B模型权重加载到内存，可在2TB CPU主机完整运行
- LLM感知量化观测器：单独保留残差流24bit精度，修复通用12bit量化导致的生成质量崩溃问题

### 关键实验结果
基于WikiText-2数据集测试，对比全量证明、独立请求证明等baseline：
1. TinyLlama-1.1B上抽样7个块证明，耗时仅为全量证明的22.0%，证明大小仅为6.8%
2. 12个请求打包证明总耗时181.9s，比12次独立证明快6.5倍，单请求验证耗时仅0.6s
3. Llama-2-70B上单请求证明仅需1259s，验证耗时46.3s，无需加载全量模型权重
4. 优化量化后与f32模型的argmax匹配度达84.8%~84.9%

可验证推理的核心是在审计成本和作弊威慑之间做tradeoff，低覆盖率抽样审计配合足够高的违约惩罚，就能实现有效的外包推理合规校验。
