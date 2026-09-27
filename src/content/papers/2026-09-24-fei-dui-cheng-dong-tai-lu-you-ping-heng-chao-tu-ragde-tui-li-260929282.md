---
title: 'Asymmetric Dynamic Routing: Balancing Reasoning Depth and Computational Efficiency
  in Hypergraph RAG'
title_zh: 非对称动态路由：平衡超图RAG的推理深度与计算效率
authors:
- Qi Sun
- Yijia Zhang
- Xingliang Hou
- Caibo Li
- Qiang Li
- Yu Guo
affiliations:
- 西安交通大学软件学院
- 西安交通大学人机混合增强智能国家重点实验室
- 中国南方电网超高压输电公司
arxiv_id: '2609.29282'
url: https://arxiv.org/abs/2609.29282
pdf_url: https://arxiv.org/pdf/2609.29282
published: '2026-09-24'
collected: '2026-09-27'
category: RAG
direction: 检索增强生成 · 动态路由优化
tags:
- RAG
- Hypergraph
- Dynamic Routing
- Retrieval Efficiency
- Knowledge Graph
one_liner: 提出意图驱动的非对称动态路由框架，适配查询复杂度调整超图RAG遍历策略，兼顾效果与效率
practical_value: '- 电商客服、商品问答类RAG系统可直接复用查询分路思路：简单的SKU属性、物流查询走局部事实检索，复杂的搭配推荐、场景问题走跨层遍历，在不损失效果的前提下大幅降低token成本与延迟

  - 意图分类的保守 fallback 策略可直接复用，低置信度查询默认路由到中等复杂度路径，阈值0.75可直接作为初始配置，平衡路由准确率与效率

  - 分层双超图的知识组织方式适配电商知识库搭建：底层存储SKU参数、用户评价等事实数据，上层存储消费场景、人群偏好等抽象洞察，显著提升多跳推荐、场景化查询的召回质量

  - 高吞吐在线RAG场景优先做单 pass 动态路由优化，相比多轮迭代式自适应RAG，延迟开销降低一个数量级，更适合电商搜索、推荐的实时交互需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GraphRAG、HyperRAG等结构化RAG普遍采用静态拓扑遍历策略，不区分查询复杂度，会引发静态检索谬误：简单查询过检索导致token冗余、上下文信噪比下降，复杂查询欠检索导致证据链断裂、推理深度不足；而现有自适应检索多依赖多轮Agent迭代，延迟开销过高，无法适配高吞吐在线场景。
### 方法关键点
- 搭建分层双超图知识底座：底层HK存储细粒度实体、事实级关联，上层HD存储抽象洞察、高阶语义关联，两层通过预定义映射函数打通
- 轻量意图分类器将查询分为简单、中等、复杂三类，置信度低于0.75的查询统一fallback到中等复杂度路径，规避路由极端错误
- 三类查询对应差异化遍历算子：简单查询仅做HK局部事实锚定，无扩线；中等查询从HK向上扩散到HD获取关联洞察；复杂查询先在HD做顶层语义匹配，再反向映射回HK获取支撑事实
### 关键结果
在5个跨领域数据集上对比Zero-shot LLM、NaiveRAG、GraphRAG、Hyper-RAG等6种基线，效果优于最优基线DHI平均0.7~0.9分；对比固定复杂遍历模式，prompt token消耗降低48.7%，端到端查询延迟降低45.3%。
### 核心结论
静态检索谬误是结构化RAG落地的核心效率瓶颈，按查询复杂度做动态路由是兼顾推理效果与部署成本的最优路径之一。
