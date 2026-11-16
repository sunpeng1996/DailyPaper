---
title: 'MeReader: An Offline, Privacy-Preserving, Progress-Aware AI Assistant for
  Narrative eBook Reading'
title_zh: MeReader：面向叙事类电子书的离线隐私保护进度感知AI助手
authors:
- Mohammed Efaz
- Udo Bub
- Itilekha Podder
affiliations:
- Eötvös Loránd University (ELTE), Budapest, Hungary
arxiv_id: '2611.18513'
url: https://arxiv.org/abs/2611.18513
pdf_url: https://arxiv.org/pdf/2611.18513
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: 端侧阅读Agent · 隐私保护进度感知RAG
tags:
- RAG
- On-device LLM
- Privacy-preserving
- Progress-aware Retrieval
- eBook Assistant
one_liner: 提出感知阅读进度的端侧混合RAG电子书助手，防剧透保隐私且性能对标大参数量模型
practical_value: '- 做端侧电商导购/内容阅读Agent时，可复用进度感知边界机制，仅召回用户当前浏览/阅读节点之前的内容，避免超前剧透（如新品未公开信息泄露、连载内容跳章剧透）

  - 端侧垂直场景RAG可参考混合检索方案，叠加vector similarity、BM25、摘要embedding三路召回，在小参数量模型下保障检索匹配准确率

  - 端侧模型选型可复用实验结论，2b-4b量级本地模型即可在垂直场景达到5b+大模型的理解效果，平衡响应延迟与输出质量'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有云侧LLM电子书助手全量上传、全量处理文本，既存在用户隐私泄露风险，还易返回未读内容造成叙事剧透，缺乏同时兼顾进度感知、隐私保护的本地化方案。
### 方法关键点
1. 设计进度感知边界机制，检索、生成全链路严格限制在用户当前阅读位置之前的文本范围内；
2. 采用混合RAG架构，融合vector similarity、BM25、摘要embedding三路召回，提升上下文匹配精度；
3. 全功能端侧运行，无需上传任何用户数据到云端。
### 关键结果数字
在经典英文书籍数据集测试，2b-4b量级端侧模型可达到与5b+大模型相当的理解准确率；进度感知机制可100%避免未来内容泄露，且不降低检索质量。
