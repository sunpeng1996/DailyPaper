---
title: Structural Segmentation for Brazilian Legal Document Retrieval
title_zh: 巴西法律文档检索的结构化切分方法研究
authors:
- Leandro Carísio Fernandes
- João Alberto de Oliveira Lima
- Hudson de Martim
- Eduardo Seiti de Oliveira
- Roberto Lotufo
- Jayr Pereira
affiliations:
- Câmara dos Deputados, Brazil
- Senado Federal, Brazil
- Universidade Estadual de Campinas (UNICAMP), Brazil
- Universidade Federal do Cariri (UFCA), Brazil
arxiv_id: '2610.18622'
url: https://arxiv.org/abs/2610.18622
pdf_url: https://arxiv.org/pdf/2610.18622
published: '2026-10-13'
collected: '2026-10-18'
category: RAG
direction: RAG 文档切分策略优化
tags:
- Document Segmentation
- Dense Retrieval
- Lexical Retrieval
- RAG
- Legal IR
one_liner: 对比4种结构化切分策略，验证带元数据的核心chunk可提升法律文档dense检索效果
practical_value: '- RAG场景长文档切分无需保留完整层级结构，核心chunk+文档元数据的组合就能实现媲美全层级的检索效果，可降低切分复杂度和索引存储成本

  - 结构化切分仅对dense检索增益显著，lexical检索（如BM25）收益不稳定，混合检索场景需针对性设计切分策略，避免lexical侧效果下降

  - 电商商品详情页、政策类帮助中心长文档检索可复用该思路，按商品规格/条款核心模块切分后挂载商品ID、分类等元数据，提升召回准确率'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
长文档整体索引会稀释核心内容语义，导致dense检索召回准确率下降，现有切分多采用固定长度滑动窗口，未利用文档原生层级结构，检索增益有限。
### 方法关键点
基于法律文档原生层级结构做结构化切分，对比4种表征策略：全层级结构表征、核心chunk+完整元数据、核心chunk+精简元数据、仅核心chunk，在两个巴西法律公开数据集上分别测试lexical、dense检索效果。
### 关键结果
结构化切分相比全文档索引，dense检索效果提升明显，即使索引单元数量大幅增加也无负面影响；lexical检索无稳定增益；无需保留完整层级结构，核心chunk挂载文档元数据的方案取得最优或次优效果，比全层级方案更轻量化。
