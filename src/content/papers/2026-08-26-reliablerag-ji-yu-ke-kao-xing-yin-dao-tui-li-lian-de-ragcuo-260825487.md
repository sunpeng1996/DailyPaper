---
title: 'ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via
  Reliability-Guided Reasoning Chains'
title_zh: ReliableRAG：基于可靠性引导推理链的RAG错误信息对抗框架
authors:
- Jinpu Jiang
- Xuan Wu
- Wenhao Song
- Bo Yang
- You Zhou
- Hongwei Ge
- Heow Pueh Lee
- Yanchun Liang
- Chunguo Wu
affiliations:
- 吉林大学
- 大连理工大学
- 新加坡国立大学
- 珠海科技学院
arxiv_id: '2608.25487'
url: https://arxiv.org/abs/2608.25487
pdf_url: https://arxiv.org/pdf/2608.25487
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: 检索增强生成 · 多跳QA错误信息对抗
tags:
- RAG
- Multi-hop QA
- Misinformation Robustness
- Reasoning Chain
- Triple Extraction
one_liner: 首个细粒度三元组级可靠性驱动的RAG框架，在多跳QA场景下抵御欺骗性错误信息干扰
practical_value: '- 电商客服/商品问答类RAG系统可复用三元组级细粒度可信度评估逻辑，替换传统粗粒度文档级可信度打分，过滤虚假商品描述、不实评价等错误信息，避免误导用户

  - 多步推理类Agent（如电商购物决策助手、售后问题排查Agent）可借鉴推理链动态构造+beam search剪枝策略，每轮迭代只保留top-F高置信度推理路径，平衡推理准确率和计算开销

  - 可直接复用α超参数调优经验：UGC内容多、虚假信息密集的场景（如用户评价、种草内容）可降低α（调低语义相关性权重，优先保障可信度），官方内容为主的场景可适当提高α

  - 离线预抽取文档三元组+预计算可信度的工程架构，可大幅降低线上推理延迟，适合高并发的电商搜索、智能导购类RAG场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG在多跳QA场景下极易受检索到的欺骗性错误信息干扰，单条错误信息就会导致推理链全链路出错；现有隐式对齐/显式调控方案要么依赖大量训练数据泛化性差，要么仅做粗粒度文档级可信度评估，无法识别语义相关但事实错误的细粒度欺骗信息，亟需更细粒度的可靠性感知能力。

### 方法关键点
- 离线阶段：Triple Extraction模块将所有文档拆解为<主语,谓语,宾语>结构化三元组，通过LLM预评估每个三元组的可信度得分（0-10分），维度覆盖实体真实性、关系合理性
- 在线阶段：Triple Evaluation模块为每一条已有推理链生成专属查询，融合查询-三元组语义相似度、三元组预计算可信度两个维度，按权重α计算综合可靠性得分，筛选top-K高可靠非冗余三元组
- Chain Construction模块采用beam search策略自回归构造推理链，每轮判断是否终止推理或追加三元组，仅保留top-F高置信度候选链，直到所有链终止或达到最大跳数，最终将可靠链拼接为上下文输入LLM生成答案

### 关键结果
在HotPotQA、2WikiMultiHopQA、MuSiQue三个多跳QA数据集的错误信息注入场景下，对比9种SOTA方案，基于Llama3-8B的ReliableRAG-TBS在HotPotQA上EM达53.4%，较次优方案CrAM高2.6pct；2WikiMultiHopQA上EM达45.4%，较次优方案高14.7pct；即使注入3条低可信度文档，性能下降幅度仅为同类方案的1/3。

**核心结论**：细粒度三元组级的可靠性评估，比粗粒度文档级打分能更有效抵御语义相似的欺骗性错误信息干扰。
