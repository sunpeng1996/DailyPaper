---
title: 'Glance: The Generator Is Its Own Reranker'
title_zh: Glance：让生成大模型自身充当RAG系统的重排器
authors:
- Adilet Metinov
- Chingiz Arziev
affiliations:
- Airun Intelligence Labs
arxiv_id: '2610.40454'
url: https://arxiv.org/abs/2610.40454
pdf_url: https://arxiv.org/pdf/2610.40454
published: '2026-10-28'
collected: '2026-10-30'
category: RAG
direction: RAG系统 · 生成重排一体化优化
tags:
- RAG
- Reranking
- LoRA
- KV Cache
- LLM Serving
one_liner: 仅用单份生成大模型骨干加轻量LoRA适配器，实现共享Prefill的RAG重排，无需独立重排模型
practical_value: '- RAG系统可复用此架构砍掉独立重排模型，仅给生成LLM加0.1GiB级LoRA适配器即可支持重排能力，显著降低GPU部署成本，尤其适合多业务并行的Agent场景

  - 电商商品/内容搜索的召回后重排可借鉴共享Prefill的多探针设计，批量处理召回候选无需逐对编码，候选量达200时仍能保持nDCG提升，适合大候选集重排场景

  - 多技能LLM部署可参考LoRA动态切换方案，单份骨干支持聊天、决策、重排多任务，切换延迟仅毫秒级，适合电商客服Agent、导购Agent等多能力复用场景

  - HotpotQA实验显示生成器自选择的上下文比独立重排器选择的下游答案质量更高，可迁移到电商问答、商品详情摘要等RAG场景，优化最终输出效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RAG系统普遍采用独立重排器+生成器的双模型架构，需重复部署模型、重复编码候选文本，GPU资源开销高；长上下文下逐对编码候选的延迟随候选量线性增长，无法支撑大候选集的低成本高效重排。

### 方法关键点
- 给冻结的生成大模型加rank-16 LoRA决策适配器+256维指针头，新增参数量仅0.1GiB级，不影响原生成能力
- 所有召回候选仅做一次共享Prefill，从缓存上下文分支生成逐候选的相关性探针，单次批处理得到所有候选的重排分数，无需逐对编码query-passage
- 支持两种工作流：主流流重排后重新Prefill高分候选生成答案，Activated流仅探针阶段启用适配器，可直接复用原KV缓存继续生成，无需二次Prefill
- 单份骨干可动态切换LoRA，同时支持聊天、通用决策、重排三种能力，切换延迟仅毫秒级

### 关键结果
- 39分钟MS MARCO微调后，SciFact数据集nDCG@10达0.741，NFCorpus达0.345，超过bge-reranker-v2-m3的0.721和0.326
- 200候选（43k tokens）场景下，nDCG@10超出交叉编码器0.058
- HotpotQA 300样本测试，自生成器选择的上下文比交叉编码器选择的答案F1提升0.045（95% CI [0.014, 0.076]）

### 核心结论
生成器自身对上下文的偏好匹配度远高于独立重排器，一体化重排不仅能降本，还能提升下游生成质量
