---
title: 'Query-Side Attacks on GNN-Based KGQA: Tracing Failures from Entity Linking
  to Answer Generation'
title_zh: 面向GNN基知识图谱问答的查询侧攻击：从实体链接到答案生成的故障溯源
authors:
- Pankaj Kumar
- Subhankar Mishra
affiliations:
- National Institute of Science Education and Research
- Homi Bhabha National Institute
arxiv_id: '2608.25922'
url: https://arxiv.org/abs/2608.25922
pdf_url: https://arxiv.org/pdf/2608.25922
published: '2026-08-26'
collected: '2026-08-29'
category: Eval
direction: KGQA鲁棒性 · 分阶段故障溯源评估
tags:
- KGQA
- GNN
- Adversarial Attack
- Robustness Evaluation
- Subgraph Retrieval
one_liner: 提出分阶段隔离的KGQA鲁棒性评估框架，定位子图构建为查询扰动下核心失效点
practical_value: '- 搭建基于KG的电商导购Agent/搜索RAG系统时，鲁棒性优化优先投入子图检索模块，而非GNN推理模块，投入产出比更高

  - 多阶段pipeline的故障排查可复用文中的阶段隔离评估协议，避免单一端到端指标掩盖真实故障点，减少优化走偏

  - 电商搜索query改写/纠错的鲁棒性测试，可借鉴CR/RS两种保语义的扰动构造方法，覆盖用户句式变换、同义表达场景'
score: 5
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有GNN基KGQA pipeline的鲁棒性评估仅使用端到端指标，无法区分实体链接、子图检索、GNN推理、答案生成四个阶段的独立失效原因，难以定位优化靶点。
### 方法关键点
提出阶段隔离评估协议，设计两种经KG校验的保答案查询侧对抗扰动：Compositional Restructuring（CR，句式重组）、Relation Synonym Swap（RS，关系同义词替换），扰动不改变输入实体种子，可精准定位各阶段故障贡献。
### 关键结果数字
在ComplexWebQuestions、WebQSP数据集测试显示：子图完整时GNN推理精度接近基线水平；CR扰动下99%的端到端精度下降源于子图构建阶段，哪怕74%的检索子图中存在正确答案，仍因答案可达性问题失效，该差异无法被端到端指标识别。
