---
title: 'UNREAL: Unifying Retrieval and Long-Context with a Single Model'
title_zh: UNREAL：用单一模型统一检索与长上下文处理
authors:
- Edan Kinderman
- Elad Hoffer
- Yochai Blau
- Brian Chmiel
- Ron Banner
- Daniel Soudry
- Boris Ginsburg
affiliations:
- NVIDIA
- Technion
arxiv_id: '2610.08463'
url: https://arxiv.org/abs/2610.08463
pdf_url: https://arxiv.org/pdf/2610.08463
published: '2026-10-06'
collected: '2026-10-07'
category: RAG
direction: RAG优化 · 检索长上下文统一
tags:
- RAG
- Long-context LLM
- Evidence Selection
- Decoder-only LLM
- Contrastive Learning
one_liner: 在冻结LLM上仅加不到500K参数，实现跨语料检索与长上下文证据选择的统一机制
practical_value: '- 业务RAG系统可复用现有业务LLM主干，仅新增不到500K参数训练检索token与层混合权重，无需维护独立召回、重排模型，大幅降低多模型对齐与运维成本

  - 长上下文场景（如电商用户长会话理解、长商品说明书问答）可先用该机制筛选高相关chunk再生成，32K以上上下文即可降低FLOPs与time-to-first-token，同时避免无关内容干扰生成效果

  - 新增参数训练仅需业务域标注的query-正例chunk对，采用多正例InfoNCE损失训练即可，无需微调LLM主干，适配垂域的成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG依赖外部独立检索模型，需额外维护多套模型的训练、服务与对齐逻辑，成本高；长上下文推理则易受无关内容干扰，且计算开销随长度指数级上升。二者本质都是query驱动的证据选择任务，却长期作为独立体系建设，存在大量冗余。

### 方法关键点
- 基于完全冻结的Decoder-only LLM实现，仅新增<500K可训练参数（检索token、层混合权重α），无需微调主干
- 直接提取LLM中间层残差流状态编码chunk、生成检索query，采用MaxSim算子计算chunk与query的相似度
- 用多正例InfoNCE损失做对比训练，仅更新新增参数，兼容dense attention、linear attention、SSM等多种LLM架构
- 同一套参数可同时支持两类场景：语料库级检索直接从百万级chunk库召回，长上下文场景将全prompt拆分为chunk后筛选

### 关键结果
- 语料库检索：在21M chunk的Wikipedia索引上，4种测试主干均超越SOTA检索-重排系统，最佳模型HotpotQA recall@10从49.1%提升至73.2%，2WikiMultiHopQA从31.7%提升至60.1%
- 长上下文任务：无额外长上下文训练，NoLiMa 128K场景准确率从1.0%提升至24.83%，LV-Eval 256K场景F1从49.97%提升至54.66%
- 效率：32K tokens以上场景相比全上下文推理，FLOPs和time-to-first-token均降低，上下文越长收益越明显

### 最值得记住的话
语料库检索和长上下文推理本质是不同规模的同一类证据选择问题，冻结LLM的内部表示已经具备极强的原生检索潜力，无需构建两套独立系统。
