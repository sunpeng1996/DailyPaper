---
title: 'LivingRAG: Augmenting Graph RAG with Experience'
title_zh: LivingRAG：支持可复用推理经验的Graph RAG增强框架
authors:
- Yuzhuo Cui
- Zongye Zhang
- Qingjie Liu
affiliations:
- State Key Laboratory of Virtual Reality Technology and Systems, Beihang University
- Hangzhou Innovation Institute, Beihang University
arxiv_id: '2608.25960'
url: https://arxiv.org/abs/2608.25960
pdf_url: https://arxiv.org/pdf/2608.25960
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: Graph RAG · 可复用经验增强
tags:
- GraphRAG
- Experience Reuse
- Multi-hop QA
- Retrieval Augmented Generation
- Inference Efficiency
one_liner: 为Graph RAG增加可写经验存储，通过双路复用提升多跳QA准确率、降低推理成本
practical_value: '- 电商商品咨询、售后QA等高频同模板query场景，可直接复用这套经验存储架构：存储历史查询的实体激活路径、推理模板，新查询无需从零检索推理，准确率提升的同时降低LLM调用成本

  - RAG落地可直接复用双门控写入机制：新增经验必须过NLI证据校验+和现有经验的相似度校验，避免错误、冗余经验污染记忆库，比直接存储对话历史的可靠性高很多

  - 大流量在线RAG系统可参考成本优化思路：平均仅增加3.5%的prompt token，就能降低22.7%的completion token，整体API成本降12.1%，ROI极高，适合推荐query改写、商品卖点生成等场景

  - 跨query的复用信号不要仅局限于实体匹配：新增图邻域激活路径、query模板两种复用维度，对电商场景下大量同结构不同实体的查询（如XX和YY哪个更适合干皮）适配性极强'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Graph RAG均孤立处理每个query，推理完成后直接丢弃所有中间推理信号，后续相关query必须从零开始检索、推理，不仅准确率上限低，还浪费大量LLM推理成本。分析在线QA流发现，90%以上的查询存在可复用信号（共享实体、同图邻域、同推理模板），仅靠实体缓存只能覆盖不到40%的复用场景，存在大量优化空间。
### 方法关键点
- 基于LinearRAG底座新增可写经验存储，每个验证通过的经验仅存储源query embedding、实体激活稀疏图、精简推理摘要、置信度等元信息，不存储全量推理trace，存储空间占用极低
- 经验双路复用：检索阶段将历史相似query的激活图与当前query的初始激活加权融合，引导图检索优先访问历史验证有效的邻域；生成阶段匹配相似度最高的推理模板作为脚手架，减少LLM重复推理
- 双门控写入机制：先校验候选经验的所有主张均有检索到的证据支撑（NLI模型做蕴含校验），再校验与现有经验的差异度足够高，仅27.4%的候选会被写入，避免错误、冗余经验积累
### 关键结果
在2Wiki、HotpotQA、MuSiQue等5个多跳QA数据集上对比7个强基线，LLM评估准确率较最优基线LinearRAG最高提5.71%；平均仅增加3.5%的prompt token，就能降低22.7%的completion token，整体API成本平均降12.1%，冷启动阶段（前10%流量）成本略高，经验积累后优势持续扩大。
> 最值得记住的结论：Graph RAG的优化不能仅停留在静态检索链路，在线积累经过验证的推理经验做双路复用，投入产出比远高于纯静态优化。
