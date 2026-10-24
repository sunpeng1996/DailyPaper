---
title: 'A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy,
  Evolution, and Future Directions'
title_zh: 长文档视觉问答的任务导向综述：分类、演进与未来方向
authors:
- Yufei Tong
- Guanjie Cheng
- Tianle Wu
- Leilei Zhang
- Hang Zheng
- Peihan Wu
- Jianwei Yin
- Shuiguang Deng
affiliations:
- Zhejiang University
- BWTON Technology Co., Ltd.
arxiv_id: '2610.31385'
url: https://arxiv.org/abs/2610.31385
pdf_url: https://arxiv.org/pdf/2610.31385
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 长文档多模态问答 · 综述与技术路径梳理
tags:
- Document-VQA
- Multimodal-RAG
- Information-Retrieval
- Agentic-Reasoning
- Visual-Document-Understanding
one_liner: 首个任务导向长文档VQA综述，拆解为4个核心模块并给出细粒度分类与未来研究方向
practical_value: '- 长文档VQA的四模块拆解框架（解析→检索→生成→评估）可直接复用至多模态电商商品说明书、商家资质材料的智能问答Agent开发

  - 证据优先的技术演进思路可迁移至多模态RAG系统优化，优先保障高保真证据召回而非盲目提升生成模型容量，降低推理成本

  - 预算感知的多模块协同方向可指导高并发场景下的多模态客服机器人架构设计，平衡回答准确率与响应时延'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有长文档VQA综述多聚焦技术架构本身，未建立任务瓶颈与技术选型、研究优先级的关联，落地参考性不足。
### 方法关键点
以任务为核心将长文档VQA拆解为文档解析、证据组织与检索、生成器组织与学习、评估4个核心模块，对每个模块构建细粒度分类体系，梳理不同技术路径的解决动机、技术方案与跨模块依赖关系，覆盖显式检索、直接读取两类主流技术路线，同步做领域发展时间线的演进分析。
### 关键结果
1. 领域研究重心已从早期多模态内容理解，逐步转向高保真证据获取、长时证据管理方向；
2. 明确证据充足性、可验证可纠错理解、预算感知协同三大核心未来研究方向
