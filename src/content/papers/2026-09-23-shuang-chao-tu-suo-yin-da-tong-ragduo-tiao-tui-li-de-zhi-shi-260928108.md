---
title: 'Dual-Hypergraph Indexing: Bridging Knowledge Islands for Multi-Hop Reasoning
  in Retrieval-Augmented Generation'
title_zh: 双超图索引：打通RAG多跳推理的知识孤岛
authors:
- Qi Sun
- Xingliang Hou
- Caibo Li
- Yijia Zhang
- Qiang Li
- Yu Guo
affiliations:
- 西安交通大学软件学院
- 西安交通大学人机混合增强智能国家重点实验室/人工智能与机器人研究所
- 中国南方电网超高压输电公司
arxiv_id: '2609.28108'
url: https://arxiv.org/abs/2609.28108
pdf_url: https://arxiv.org/pdf/2609.28108
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: 检索增强生成 · 多跳推理优化
tags:
- RAG
- Hypergraph
- Multi-hop Reasoning
- Knowledge Representation
- Information Retrieval
one_liner: 提出双超图索引框架DHI，通过双路径聚合解决超图RAG的知识孤岛问题，多跳推理性能达SOTA
practical_value: '- 可复用5维度实体重要度评估+P90归一化方案，优化电商场景下用户/商品核心hub识别，过滤无效关联，降低召回冗余

  - 双路径聚合思路可迁移至长时序用户行为建模：静态hub聚合捕捉长期兴趣核心，时序链聚合捕捉近期行为演进，提升多步推荐逻辑连贯性

  - 电商导购/客服Agent的RAG系统可直接复用双层超图架构：底层存商品/规则原子事实，上层存预聚合的场景化解决方案（如优惠叠加规则、售后链路），减少幻觉并降低token消耗

  - 长文档多跳检索场景（如电商合规审核、说明书问答）可借鉴时序链聚合的滑动窗口+实体重叠约束，打通跨片段关联逻辑，避免检索碎片化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有超图RAG将提取的超边作为孤立事实断言，存在结构碎片化的「知识孤岛」问题，多跳因果推理、时序追踪、叙事合成能力受限，LLM需实时推断跨片段依赖，极易出现注意力分散、幻觉级联错误，无法满足复杂多跳查询需求。

### 方法关键点
- 架构设计双层耦合超图：底层事实超图$H_K$存储实体、多实体关系及原子洞察，上层深度洞察超图$H_D$的顶点与$H_K$的高阶超边一一映射，存储跨超边聚合的合成洞察；
- 双路径聚合算法：① 重要度驱动的hub聚合：通过5维度拓扑特征（顶点度、关联超边数、平均超边规模、累积语义权重、邻居覆盖度）+P90归一化计算实体重要度，肘部法则筛选核心hub，聚合生成全局洞察；② 时序链渐进聚合：滑动窗口内基于时序邻近、实体重叠、反hub惩罚三个约束，挖掘跨片段的时序因果链，聚合生成演进类洞察；
- 检索时先召回$H_K$的相关事实子图，再映射到$H_D$做1跳扩散获取聚合洞察，拼接后作为生成上下文。

### 关键实验
在Mix（多学科）、CS、农业、神经内科、病理学5个基准数据集上对比7个SOTA基线：DHI在所有数据集综合得分SOTA，Mix基准综合得分83.18，较Hyper-RAG高2.79分，逻辑连贯性较HiRAG高1.53分；病理学多跳推理任务得分85.78%，较GraphRAG高3.06分。

### 核心结论
静态hub聚类与时序链聚合是完全正交且相互增强的归纳偏置，预聚合跨超边的关联洞察能从根源上降低多跳推理时LLM的推断负担与幻觉风险。
