---
title: 'HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved
  Generation'
title_zh: HAM-RAG：面向结构保真交错生成的层级感知多模态RAG
authors:
- Yin Li
- Ziyang Hu
- Zhiyu Guo
- Xiangyu Liu
- Wenbin Li
- Boo-Ho Yang
- Rav Lawana
- Ziyue Li
- Wei Zeng
- Fugee Tsung
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- ASCETEX INTERNATIONAL LIMITED
- MOVENSYS Inc.
- Schneider Electric
- Technical University of Munich
arxiv_id: '2608.14032'
url: https://arxiv.org/abs/2608.14032
pdf_url: https://arxiv.org/pdf/2608.14032
published: '2026-08-14'
collected: '2026-08-17'
category: RAG
direction: 多模态RAG · 结构化文档图文生成
tags:
- Multimodal-RAG
- Hierarchy-Aware
- Structured-Document
- Interleaved-Generation
- Benchmark
one_liner: 提出层级感知多模态RAG框架及配套基准，大幅提升结构化文档图文生成的结构保真度
practical_value: '- 处理电商商品详情页、操作指南这类结构化多模态文档时，可复用层级感知索引思路：给文本/图片块拼接所属标题、章节路径、邻近上下文后再做嵌入，能大幅提升检索相关性

  - 做商品种草文案、使用教程类图文交错生成需求时，可借鉴HAM-RAG的prompt构造逻辑：给图片补充所属位置、上下文描述，引导大模型将图片插在语义匹配的文本位置，提升内容可信度

  - 自研多模态RAG评测体系时，可参考Img-CBS指标思路：除了判断图片是否选对，额外评估图片与周边文本的语义匹配度，更贴合真实业务的内容质量要求

  - 工业级结构化文档解析场景，可复用其层级树构建逻辑：从文档标记、标题层级、编号、图文关联、布局线索中恢复层级结构，无需完全依赖半结构化输入'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态RAG普遍将结构化文档拆分为孤立的文本、图片单元，丢失原文档层级结构、局部图文关联逻辑，易出现图片选对但位置错位、生成内容不符合原文档结构逻辑等问题，在工业SOP、运维手册、电商商品教程等需要严格对齐原文档结构的场景下，这类幻觉会直接影响内容可用性。
### 方法关键点
- 离线阶段先将结构化文档解析为层级树，每个文本/图片检索单元补充所属章节路径、祖先标题上下文、邻近图文关联关系等元数据，图片单元额外生成结合上下文的视觉描述，再嵌入存入向量库
- 在线检索阶段同时召回带层级元数据的文本、图片证据，构造prompt时完整保留来源、位置、关联关系信息，引导生成器按原文档结构逻辑生成图文交错内容
- 配套发布HAM-Bench评测基准，覆盖游戏攻略、维基页面、学术论文、食谱四类结构化文档，新增结构保真度、局部图文对齐等专属评测维度
### 关键结果
跨9种不同生成backbone测试，HAM-RAG的多模态平均得分较最优非层级基线提升17.3%；在Wukong游戏攻略数据集上，衡量图文局部对齐的Img-CBS指标较最优基线提升24.2%；整体生成失败率仅0.067%，单query推理成本低于普通多模态RAG方案。
**核心结论**：文档层级不是冗余元数据，而是多模态RAG实现结构保真生成的核心grounding信号
