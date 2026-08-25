---
title: 'The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration
  in Generative Search'
title_zh: 生成式搜索上下文分配规律：因果测量与闭环编排框架
authors:
- Peiyang Liu
- Xi Wang
- Di Liang
- Wei Ye
affiliations:
- 北京大学
- 腾讯
arxiv_id: '2608.23252'
url: https://arxiv.org/abs/2608.23252
pdf_url: https://arxiv.org/pdf/2608.23252
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: RAG 上下文分配优化与因果评估
tags:
- RAG
- Generative Search
- Causal Inference
- Context Allocation
- Closed-loop Orchestration
one_liner: 提出因果归因探针校准RAG证据利用率，多轮窄上下文编排提升生成式搜索召回效果
practical_value: '- 电商多意图商品导购、搜索问答场景的RAG系统，可直接复用多轮窄上下文分配策略，替换现有单轮长上下文方案，同等算力下提升多维度答案覆盖率15%以上

  - RAG证据归因评估可落地因果留一法探针，替代传统语义相似度指标，在同query硬负样本场景下避免诊断幻觉，准确率提升40%以上，优化知识库召回结果筛选逻辑

  - 生成式推荐的多候选内容生成场景，可迁移闭环反馈调度思路，通过归因反馈动态调整下一轮输入的候选集，有效突破LLM注意力惯性，提升生成结果的多样性和信息覆盖度'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG向多答案生成范式演进时面临两大核心瓶颈：一是传统语义相似度、BM25等相关性代理指标仅能区分跨主题负样本，在同query硬负样本（主题相关但无有效答案）场景下完全失效，无法准确衡量LLM对上下文证据的真实利用率，存在严重的诊断幻觉；二是主流的单轮宽上下文分配策略受LLM固有注意力稀释特性限制，证据利用率随上下文宽度扩张显著衰减，多意图query的答案覆盖率难以突破天花板。
### 方法关键点
- 因果留一法（LOO）探针：通过反事实消融（移除单篇文档后观测生成文本的对数似然下降幅度），精准隔离LLM对单篇文档的真实依赖度，仅需并行教师强制前向传播，无自回归解码开销，计算效率高。
- 校准上下文稀释定律：通过去混淆因子实验得到上下文宽度弹性为-0.68，即上下文宽度每提升1倍，单篇文档的证据利用率平均下降68%，证明单轮宽上下文是架构陷阱。
- 闭环子模块调度器Ascp：结合因果归因反馈，动态选择未被充分利用的语义簇文档构成每轮窄上下文，搭配归因导向的对比解码器突破LLM注意力惯性，强制新证据融合。
### 关键结果
在ASQA、QAMPARI、ELI5等多答案生成基准上，对比7种基线（vanilla RAG、MMR、DPP-RAG等），相同算力预算下，多轮窄上下文编排比单轮宽上下文的portfolio recall绝对提升16.8~20.5个百分点，Ascp调度器比所有选择式基线提升3.3~8.1个百分点，效果稳定适配到32B大模型。
### 核心结论
同等推理预算下，多轮窄上下文+因果反馈闭环编排的效果远优于单轮最大化上下文宽度的策略，是生成式搜索/RAG系统的更优架构范式
