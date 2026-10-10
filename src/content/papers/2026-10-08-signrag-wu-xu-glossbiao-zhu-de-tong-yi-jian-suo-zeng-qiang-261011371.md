---
title: 'SignRAG: Unified Retrieval-Augmented Gloss-Free Sign Language Translation'
title_zh: SignRAG：无需Gloss标注的统一检索增强手语翻译框架
authors:
- Zhi Rao
- Yucheng Zhou
- Qianran Sun
- Yiqing Huang
- Longcan Yuan
- Jiayi Hou
- Chengwen Yao
- Lin Cheng
- Donghui Sun
- Xiaoxin Chen
affiliations:
- 澳门科技大学创新工程学院
- 澳门大学SKL-IOTSC、CIS
- 中国科学院自动化研究所MAIS
- Yale University
- VIVO AI Lab
arxiv_id: '2610.11371'
url: https://arxiv.org/abs/2610.11371
pdf_url: https://arxiv.org/pdf/2610.11371
published: '2026-10-08'
collected: '2026-10-10'
category: RAG
direction: 检索增强生成 · 跨模态对齐优化
tags:
- RAG
- LLM Alignment
- Cross-modal
- Reinforcement Fine-tuning
- Multimodal
one_liner: 提出融合分层预训练、域内检索增强、检索感知强化微调的无Gloss手语翻译框架SignRAG
practical_value: '- 跨模态对齐场景可复用分层预训练策略：先学习模态内语义表示再对齐LLM，缓解优化不平衡，可用于图文跨模态推荐、多模态导购Agent落地

  - RAG落地可借鉴检索效用引导的强化微调思路：同时叠加任务效果和检索有用性双奖励，避免过度依赖错误检索结果，适配电商导购RAG、搜索query改写场景

  - 垂域LLM轻量适配可补充域内检索库：用实例级检索提示降低微调成本，适合商品文案生成、垂域客服Agent等场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有无Gloss标注的手语翻译预训练范式多基于编解码结构LM，无法直接适配仅解码器结构的主流LLM，跨模态优化易出现不平衡，且检索增强落地易出现过度依赖错误结果的问题。
### 方法关键点
1. 分层预训练：先学习具备语言学基础的手语表示，再联合对齐手语编码器与LLM，缓解跨模态优化不平衡；
2. 下游适配引入目标域检索库，提供实例级翻译提示补充参数微调效果；
3. 提出Retrieval Utility-Guided Reinforcement Fine-Tuning（RUG-RFT），同时结合翻译质量奖励和检索效用奖励，鼓励有效利用检索结果的同时抑制有害依赖。
### 关键结果
在多个SLT基准上达到SOTA，是首个在CSL-Daily数据集所有指标上超过有Gloss监督方法的无Gloss方案。
