---
title: 'CodeGraph: Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding'
title_zh: CodeGraph：基于Wikidata对齐的开源代码开放分类知识图谱
authors:
- Federico Pennino
- Andrea Gurioli
- Stefano Zacchiroli
- Maurizio Gabbrielli
- Paolo Ferragina
affiliations:
- Università di Bologna
- Télécom Paris, Institut Polytechnique de Paris
- Sant’Anna School of Advanced Studies
arxiv_id: '2609.29474'
url: https://arxiv.org/abs/2609.29474
pdf_url: https://arxiv.org/pdf/2609.29474
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 代码知识图谱 实体对齐构建方案
tags:
- Knowledge Graph
- Entity Linking
- Agent
- Code LLM
- Wikidata
one_liner: 提出三阶段实体对齐流程，构建首个大规模开源代码开放分类知识图谱CodeGraph
practical_value: '- 三阶段实体对齐流程可直接复用：先通过确定性规则处理高置信度实体，再用Agent解决长尾歧义，最后补全层级关系，适配电商类目对齐、商品实体链接等场景

  - 小样本人工黄金集+LLM-as-judge的质量校验方案，可低成本量化大规模KG构建的标注精度，适合推荐系统物品图谱、用户画像的质量评估

  - 开放分类语义标注的构建思路，可直接迁移到技术社区内容推荐、开发者用户建模等业务场景'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有代码仓库分析工具仅支持语法、token级分析，无法提取代码隐含的算法、范式、应用领域等工程知识，大规模结构化知识沉淀困难。
### 方法关键点
1. 基于Code LLM实现代码的开放分类语义标注，提取算法、设计模式等概念实体；
2. 三阶段Wikidata实体对齐流程：确定性SPARQL处理无歧义实体、Deep Research Agent解决长尾实体对齐、层级上卷补全实体父类闭包；
3. 采用小体量人工黄金集+LLM-as-judge的校准协议，量化标注精度。
### 关键结果数字
在1.67亿文件的Stack-Edu语料上构建的CodeGraph含1.58亿节点、10亿条带类型边，覆盖14种编程语言，包含6.3万个概念实体、1.98万个对齐的Wikidata实体，是已知首个大规模开源代码开放分类知识图谱。
