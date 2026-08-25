---
title: 'GrOIL: Graph-Grounded Domain Ontology Induction with Constrained LLM Mediation'
title_zh: GrOIL：基于图锚定的受限LLM调解领域本体归纳方法
authors:
- Maruf Ahmed Mridul
- Abid Talukder
- Oshani Seneviratne
affiliations:
- Rensselaer Polytechnic Institute
arxiv_id: '2608.22135'
url: https://arxiv.org/abs/2608.22135
pdf_url: https://arxiv.org/pdf/2608.22135
published: '2026-08-22'
collected: '2026-08-25'
category: Reasoning
direction: 领域本体构建 · LLM受限推理
tags:
- Ontology Learning
- Knowledge Representation
- LLM
- Constrained Generation
- Graph Grounding
one_liner: 提出七阶段图锚定pipeline，用受限LLM生成全链路可审计的领域本体，性能优于直接/多Agent LLM基线
practical_value: '- 业务领域知识图谱/类目体系构建可复用「先做结构化图编码→再用LLM做窄场景调解」的思路，减少LLM幻觉，提升结果可解释性

  - 垂直领域Agent的知识库构建可借鉴全链路可审计的设计，每个生成的知识节点都关联原始来源，方便人工修正和迭代

  - 类目、属性等结构化知识自动生成场景，可限制LLM仅做对齐、归类等窄任务，比端到端生成的准确率更高、稳定性更强'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有自动领域本体构建方案无法同时满足语料锚定、词汇一致性、公理表达性、全链路可追溯的要求，人工构建成本极高。
### 方法关键点
提出7阶段图锚定pipeline，无任意无约束生成步骤：1）将文档编码为统一语篇超图（UDH）捕捉实体关联与语篇依赖；2）基于图证据逐层生成类层级、属性、限制公理，LLM仅被用于窄范围、图锚定的调解任务；3）配套ABox实例填充流程，所有生成术语自带从原始文本到各处理阶段的全决策链路，支持审计和人工优化。
### 关键结果
在寿险领域测试，CQ覆盖度比直接/多Agent LLM基线高22~37个百分点（最高达0.85），关键短语覆盖度接近人工构建的参考本体，大规模语料下词汇会出现饱和，生成的领域表示稳定可复用。
