---
title: 'From Topical Relevance to Answerability: Entailment Distillation for Conversational
  Retrieval'
title_zh: 面向对话检索的蕴含蒸馏框架：从主题相关到可回答性匹配
authors:
- Shuai Qin
- Guojia An
- Weikang Guo
- Pei Ke
- Jiwei Wei
- Yang Yang
- Jie Zou
affiliations:
- University of Electronic Science and Technology of China
- Southwest University of Finance and Economics
arxiv_id: '2609.03482'
url: https://arxiv.org/abs/2609.03482
pdf_url: https://arxiv.org/pdf/2609.03482
published: '2026-09-03'
collected: '2026-09-04'
category: RAG
direction: 对话检索 · 可回答性匹配优化
tags:
- Conversational Retrieval
- Entailment Distillation
- Reranking
- Dual-channel Recall
- NLI
- RAG
one_liner: 提出CLEAR对话检索框架，通过蕴含蒸馏和双通道召回缩小主题相关与可回答性的差距
practical_value: '- 电商对话式导购/客服的RAG检索环节可复用dual-channel召回方案：离线用LoRA微调小成本为商品/知识库文档生成可回答的候选query，构建反向索引，解决低语义相似度但高可回答性的商品/文档漏召回问题，无额外在线LLM开销

  - 检索后重排序阶段可引入蕴含蒸馏思路：离线用frozen NLI模型标注答案-文档的蕴含标签，蒸馏到轻量cross-encoder重排器，训练时加入相似度感知的标签校准策略，缓解负例排序倒置问题，在线推理不需要答案输入，提升头部召回准确率，尤其适合会话上下文存在主题漂移的场景

  - 多召回源融合优先采用RRF方案，无需额外训练，可直接在对话搜索、会话推荐场景下复用，融合主题相似召回和可回答性召回的结果，平衡召回覆盖和精度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有对话检索范式（会话query改写、稠密检索）均以主题相似度为核心优化目标，存在系统性可回答性gap：主题高度匹配的文档可能无法支撑当前问题的答案，甚至检索能力越强，语义陷阱（top1文档主题相似度高于所有正例但不可回答）的发生概率越高，在存在主题漂移的多轮对话场景下问题尤为突出，直接影响RAG系统的回答准确率。

### 方法关键点
- 双通道召回：常规稠密检索 + 溯因召回通道，离线用LoRA微调LLaMA 3.1 8B为每个文档生成5个可回答的候选query，构建query池，在线将会话上下文与query池做对称匹配，召回低相似度但高可回答性的文档，两通道结果用RRF融合后取top100进重排
- 可回答性感知重排器：基于RoBERTa cross-encoder的双头结构，上下文相关性头优化常规relevance损失，可回答性头通过KL散度蒸馏frozen NLI模型输出的答案-文档蕴含概率，训练时加入相似度感知的校准机制修正NLI模型的标签倒置问题，保留负例间的排序暗知识
- 推理时可调节相关性与可回答性的融合权重，全程无在线LLM调用

### 关键实验
在TopiOCQA（多主题漂移）、QReCC（单主题为主）、零样本TREC CAsT数据集上对比10+强基线，TopiOCQA上MRR达46.2，比最强CDR基线QRACDR提升19.4%；QReCC上MRR达69.3，比最强基线提升34.3%；在主题漂移场景增益最显著，在线延迟仅为LLM驱动query改写方案的1/4。

### 核心结论
对话检索的核心目标不是匹配会话上下文的主题，而是匹配问题需要的答案证据，主题相似度只是必要非充分条件。
