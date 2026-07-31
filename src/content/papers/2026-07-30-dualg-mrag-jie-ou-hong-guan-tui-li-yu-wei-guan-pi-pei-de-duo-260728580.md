---
title: 'DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented
  Generation'
title_zh: DualG-MRAG：解耦宏观推理与微观匹配的多模态检索增强生成框架
authors:
- Jiacheng Tao
- Qingyun Sun
- Haonan Yuan
- Ziwei Zhang
- Jianxin Li
affiliations:
- Beihang University
arxiv_id: '2607.28580'
url: https://arxiv.org/abs/2607.28580
pdf_url: https://arxiv.org/pdf/2607.28580
published: '2026-07-30'
collected: '2026-07-31'
category: RAG
direction: 多模态RAG · 图增强推理
tags:
- MM-RAG
- GNN
- Graph Reasoning
- Multi-hop QA
- Multimodal LLM
one_liner: 提出解耦宏观推理与微观匹配的双层图多模态RAG框架，提升复杂多跳QA性能
practical_value: '- 电商多模态商品RAG场景可复用双层图架构：宏观图做跨商品/内容的全局关联路由，微观图做商品属性、图片细节的精准匹配，既控制图膨胀又减少检索噪声

  - 处理多跳用户咨询（如「适合10岁男孩的防水登山鞋搭配什么袜子」）时，可借鉴query驱动的GNN消息传递机制，动态生成推理路径，降低下游LLM的推理负担

  - 生成检索结果时可复用路径解码逻辑，将召回的多模态片段拼接为结构化推理链，对小参数LLM的效果提升尤其明显，可降低部署成本

  - 可借鉴子图匹配的剪枝优化方案：通过Top-K向量召回缩小搜索空间+分支定界剪枝，在保持检索精度的同时将多模态检索latency控制在亚秒级，满足线上业务要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模态RAG在复杂多跳推理任务上表现不佳，传统单图层增强方案面临两难：引入细粒度视觉特征会导致图快速膨胀、检索噪声升高，用粗粒度表示又会丢失关键局部证据；同时静态图结构无法适配动态查询意图，召回的孤立片段也会增加下游MLLM的推理负担。

### 方法关键点
- 构建双层多模态图：宏观图存储全局实体与跨文档关联，用于全局拓扑路由；微观图存储图片、表格的细粒度特征与源文档指针，用于局部证据验证，两者通过实体对齐实现跨层映射
- 设计query驱动的GNN检索器：以查询关联实体为初始激活节点做定向消息传递，动态计算节点相关性，避免全局图计算带来的性能损耗
- 新增显式路径解码模块：通过动态规划从GNN的前向传播轨迹中提取最优推理路径，将孤立召回片段转化为结构化证据链输入下游MLLM

### 关键结果
在MMQA、WebQA、ScienceQA三个多跳QA数据集上测试，对比8个SOTA基线：MMQA数据集上4B参数版本EM达44.2%，较最优基线绝对提升7%；R@2、R@5分别达49.4%、61.9%，较最优图RAG基线提升17.6%、19.8%；平均查询latency仅0.44s，较同类型图RAG方案降低99%，实现性能与效率的平衡。

### 核心洞见
多模态RAG的图增强设计不需要追求统一的大而全的知识图谱，通过宏观推理、微观匹配的解耦架构，既能保留多跳推理能力，又能有效控制检索噪声和计算开销。
