---
title: Research Entity Extraction and Topic Detection from UKRI Grant Proposals
title_zh: UKRI资助提案的研究实体抽取与主题检测方法研究
authors:
- Xingran Ruan
- Angelo Salatino
- Rosa Filgueira
- Kara Moraw
- Alexandru Marcoci
- Gemma Derrick
- Sarah Callaghan
affiliations:
- EPCC, University of Edinburgh, UK
- Knowledge Media Institute, The Open University, UK
- Institute for Technology and Humanity, University of Cambridge, UK
- Centre for Higher Education Transformations, University of Bristol, UK
- University of Oxford, UK
arxiv_id: '2606.30304'
url: https://arxiv.org/abs/2606.30304
pdf_url: https://arxiv.org/pdf/2606.30304
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: 大模型信息抽取与主题分类应用
tags:
- LLM
- Entity Extraction
- Topic Detection
- Mistral
- GPT-4o
one_liner: 对比三种实体抽取与主题分类方案，验证Mistral在敏感文本处理上兼具精度与效率优势
practical_value: '- 电商场景下的敏感用户文本、商品评价、交易数据结构化抽取可优先测试Mistral系列模型，平衡精度、成本与数据安全性

  - 实体抽取、类目分类类任务可复用「大模型初提取+映射到标准词表」的三级流水线架构，降低定制算法开发成本

  - 资源有限场景可采用Mistral替代GPT-4o做实体抽取、主题打标类任务，效果接近但推理成本、数据可控性更优'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
各国政府需从海量资助提案中识别新兴研究领域信号，优化公共科研投资分配，传统定制算法存在效果差、碎片化问题，亟需高效高准的信息抽取与主题分类方案。
### 方法关键点
设计三级处理流水线，基于Mistral完成核心实体抽取，将结果映射到OpenAlex主题词表实现分类；同时对比GPT-4o、自研DSIT-Taxonomies定制算法三种方案的效果，测试集覆盖42份不同领域的资助提案摘要。
### 关键结果
Mistral与GPT-4o输出的实体集语义重叠度高、效果相当，均显著优于定制算法；Mistral的主题分类准确率达90.5%，较DSIT-Taxonomies流水线的71.4%高出19.1个百分点，同时运行效率高、适合敏感数据大规模处理。
