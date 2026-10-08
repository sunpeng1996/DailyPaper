---
title: Cache the Encoder Within:Compact, Reusable Memory across LLM Queries
title_zh: LLM跨查询可复用紧凑内存：编码器隐状态缓存方案EncBank
authors:
- Hanzuo Liu
- Chunyu Liu
- Chaofan Lin
- Alex Lamb
- Mingyu Gao
affiliations:
- Tsinghua University
arxiv_id: '2610.10058'
url: https://arxiv.org/abs/2610.10058
pdf_url: https://arxiv.org/pdf/2610.10058
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: LLM推理优化 · 跨查询隐状态缓存
tags:
- KV-cache
- low-bit-quantization
- inference-optimization
- LoRA
- long-context
one_liner: 提出EncBank方案复用LLM低层编码器隐状态，低比特存储实现跨查询计算复用降本
practical_value: '- RAG场景可直接复用该架构：电商海量商品详情/知识库文档提前做低层编码后用4比特存储，显存占用仅为16比特的28.1%，精度损失可忽略，大幅降低长上下文RAG的推理成本

  - 长会话Agent场景可借鉴：客服/导购Agent的历史会话编码结果跨轮次复用，27B模型下Agent任务通过率比全上下文方案高10个百分点，同时避免长上下文的OOM问题

  - 工程落地方案参考：7B-14B量级模型选第12层作为分层切分点，平衡预fill速度和精度损失，一套LoRA适配多精度存储，无需针对量化额外训练，落地成本低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG、长对话场景下相同文档/历史被多次查询时会产生大量冗余编码开销，全层KV缓存存储成本过高（Qwen3-8B场景下达144 KiB/token），仅存储Token ID则完全无计算复用，亟需兼顾复用率与存储成本的中间方案。
### 方法关键点
- 对LLM做分层切分，低层作为语义编码器对文档分块独立编码，隐状态按H16/H8/H4三种精度量化持久存储，编码结果跨查询复用
- 仅对上层阅读器做自蒸馏LoRA微调，一套适配器同时适配三种存储精度，无需针对量化单独重训练
- 查询时通过BM25检索相关分块，仅重构选中分块的隐状态送入上层推理，仅缓存残差不存储全层KV
### 关键结果
- 基于Qwen3-8B在5个长上下文基准测试集上，H4存储精度相比H16精度损失不到1分，存储空间仅为后者28.1%，预fill速度比重新编码提升1.40×
- Qwen3.8-27B配置下，Terminal-Bench 2.1 Agent任务通过率达78.65%，比全上下文方案高10.11个百分点
- 存储成本仅为全层KV缓存的1/18，单Token存储开销降至8 KiB以下
### 核心结论
跨查询缓存的收益高度依赖查询复用率，32k上下文CPU驻留场景下至少需要9次以上重复查询才能抵消预编码的准备成本。
