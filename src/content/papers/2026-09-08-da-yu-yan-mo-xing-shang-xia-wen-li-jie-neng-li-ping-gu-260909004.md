---
title: Evaluation of Contextual Understanding in Large Language Models
title_zh: 大语言模型上下文理解能力评估
authors:
- Subavarshana Arumugam
- Mamta Nallaretnam
- Kithuni Wickramasinghe
- Chamath Gunapala
- Pragatheeswaran Vipulanandan
- Uthayasanker Thayasivam
- Kamal Premaratne
affiliations:
- University of Moratuwa, Sri Lanka
- University of Miami, USA
arxiv_id: '2609.09004'
url: https://arxiv.org/abs/2609.09004
pdf_url: https://arxiv.org/pdf/2609.09004
published: '2026-09-08'
collected: '2026-09-10'
category: Eval
direction: LLM上下文理解评估 · 知识图谱度量
tags:
- LLM Evaluation
- Knowledge Graph
- Contextual Understanding
- Semantic Similarity
- QA
one_liner: 提出基于知识图谱的S3KG混合相似度评估框架，可量化LLM上下文理解能力并诊断推理错误
practical_value: '- 电商RAG/智能客服Agent的输出质检可复用S3KG的结构+语义混合相似度思路，替代单纯BLEU/准确率，减少幻觉回答的误判

  - 商品问答、订单咨询场景的LLM回答评估，可将回复与商品/订单知识图谱做S3KG匹配，量化回答的上下文忠实度

  - 优化LLM服务时可复用其错误分类诊断框架，定位上下文提取/整合/推理各环节的bad case，针对性调整Prompt或微调策略'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM评估依赖困惑度、BLEU、表层准确率等指标，无法量化模型对上下文的提取、整合、推理能力，无法区分回答是基于给定上下文还是记忆关联，在QA等需要上下文对齐的场景存在明显缺陷。
### 方法关键点
1. 提出基于知识图谱的评估框架，核心指标S3KG（Semantic Structural Similarity for KGs）融合KG结构相似度与语义相似度，输出连续评估分值；
2. 配套推理错误诊断框架，可对LLM上下文理解的错误类型做分类归因。
### 关键结果
在人工构建的QA基准上验证，S3KG相比传统指标能更准确衡量LLM生成响应的正确性、忠实度与可解释性。
