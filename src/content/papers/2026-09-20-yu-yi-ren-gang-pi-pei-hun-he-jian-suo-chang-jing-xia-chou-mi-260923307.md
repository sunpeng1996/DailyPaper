---
title: 'Semantic Candidate-Job Matching: A Comparative Evaluation of Dense Embedding
  Models in Hybrid Retrieval'
title_zh: 语义人岗匹配：混合检索场景下稠密嵌入模型的对比评估
authors:
- Sai Yashwant
- Siddhartha Jain
- Anurag Dubey
- Samaroha Chatterjee
- Gantala Thulsiram
affiliations:
- ManpowerGroup Services India Pvt. Ltd.
- Indian Institute of Technology, Hyderabad
arxiv_id: '2609.23307'
url: https://arxiv.org/abs/2609.23307
pdf_url: https://arxiv.org/pdf/2609.23307
published: '2026-09-20'
collected: '2026-09-23'
category: RecSys
direction: 语义匹配 · 混合检索模型评估
tags:
- Dense Embedding
- Hybrid Retrieval
- Contrastive Fine-tuning
- RRF
- LLM-as-Judge
one_liner: 对比不同稠密嵌入模型与微调策略在混合检索人岗匹配场景的效果，给出垂域最优配置方案
practical_value: '- 垂直领域语义匹配场景可复用「LLM结构化抽取query+RRF融合向量+全文检索」的混合召回架构，适配高吞吐量业务需求

  - 稠密嵌入微调可优先测试Cached MNRL损失，对比AnglE/CoSENT等损失在垂域的实际效果，减少调优成本

  - 垂域模型选型可复用「业务上线打分+LLM-as-Judge人工对齐」的双层评估框架，避免通用基准和实际业务效果脱节'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
通用嵌入模型基准与企业级人岗匹配的实际业务约束存在明显差距，缺乏真实业务场景下稠密嵌入模型的结构化对比评估框架。
### 方法关键点
1. 搭建混合检索pipeline：通过LLM解析职位描述生成结构化搜索文本与多语言关键词，对简历做语义增强索引，采用RRF融合向量相似度和全文检索相关性
2. 对比三类方案：原生EmbeddingGemma、基于Cached MNRL微调的EmbeddingGemma、MPNet基线，同时验证了AnglE/CoSENT等多种对比微调损失的适配性
3. 采用双层评估体系：结合已上线的AI-Match业务打分、独立LLM-as-Judge相关性打分，补充模型收敛诊断指标
### 关键结果
实测仅采用Cached MNRL微调的EmbeddingGemma效果最优，相较原生EmbeddingGemma、MPNet基线，在业务匹配分、LLM-as-Judge相关性分两项指标上均领先，可适配高并发招聘业务流需求
