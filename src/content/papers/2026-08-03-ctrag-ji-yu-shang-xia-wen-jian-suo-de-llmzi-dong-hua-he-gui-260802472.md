---
title: 'CTRAG: An In-Context Retrieval-based Framework for Automated Compliance Checking
  using LLMs'
title_zh: CTRAG：基于上下文检索的LLM自动化合规检查框架
authors:
- Muhammad Roman
- Karen Rafferty
- Barry Devereux
affiliations:
- Bristol Research and Innovation Laboratory (BRIL), Toshiba Europe Ltd.
- Queen’s University Belfast
arxiv_id: '2608.02472'
url: https://arxiv.org/abs/2608.02472
pdf_url: https://arxiv.org/pdf/2608.02472
published: '2026-08-03'
collected: '2026-08-05'
category: RAG
direction: RAG落地 · 自动化合规校验
tags:
- RAG
- In-Context Learning
- Adaptive Chunking
- Compliance Checking
- LLM Application
one_liner: 融合自适应分块、动态检索、上下文学习的RAG pipeline，实现高准确率自动化合规检查
practical_value: '- 电商平台合规校验、广告素材合规审核场景可复用自适应分块+动态检索的RAG架构，替代部分人工审核降本

  - 长文档交叉校验类任务可借鉴「从规则文本提取控制问题再检索匹配业务文档」的逻辑，提升召回准确率

  - 复杂依赖场景（如第三方服务商合规校验、供应商资质核验）可参考其跨文档交叉核验方法，降低漏判率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
监管合规校验是金融、数据隐私、网络安全等高管控领域企业的必备流程，人工校验耗时久、一致性差，涉及第三方服务商的间接合规场景校验难度尤其高。

### 方法关键点
CTRAG RAG自动化合规校验pipeline核心优化点包括：① 自适应分块处理长监管文本与非结构化企业文档；② 动态调整检索配置适配不同合规校验需求；③ 结合in-context learning提升结果精准度。流程上先从监管文本提取控制问题，再与企业文档交叉核验，支持第三方间接合规场景。

### 关键结果
最终部署版本F1-score达78%、召回达85%，已在四大会计师事务所落地POC，漏判非合规案例极少，大幅降低人工审核工作量。
