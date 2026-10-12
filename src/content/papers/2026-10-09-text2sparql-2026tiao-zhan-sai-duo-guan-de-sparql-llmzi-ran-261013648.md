---
title: SPARQL-LLM in the TEXT2SPARQL 2026 Challenge
title_zh: TEXT2SPARQL 2026挑战赛夺冠的SPARQL-LLM自然语言转查询系统
authors:
- Panayiotis Smeros
- Vincent Emonet
- Ruijie Wang
- Ana-Claudia Sima
- Tarcisio Mendes de Farias
affiliations:
- SIB Swiss Institute of Bioinformatics
- University of Zurich
arxiv_id: '2610.13648'
url: https://arxiv.org/abs/2610.13648
pdf_url: https://arxiv.org/pdf/2610.13648
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM优化知识图谱自然语言转SPARQL
tags:
- LLM
- Knowledge Graph
- SPARQL
- TEXT2SPARQL
- KGQA
one_liner: 开源多语言TEXT2SPARQL系统SPARQL-LLM在2026挑战赛8个方案中夺冠，准确率最高超第二名59%
practical_value: '- 电商导购Agent场景可复用该架构，实现用户自然语言查询到商品/商家知识图谱SPARQL的自动转换，大幅降低图谱查询开发门槛

  - 多语言适配方案可直接迁移至跨境电商多语言站点的搜索、导购场景，覆盖英、德、西等主流语种的用户查询需求

  - 可参考其生产落地经验，基于开源代码快速部署到分布式异构业务图谱之上，支撑高并发的实时用户查询请求'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
知识图谱（KG）的SPARQL查询需使用者掌握专业语法、端点配置、Schema细节等，门槛极高，普通用户无法直接查询分布式KG数据，KGQA领域对自然语言自动转SPARQL的方案需求迫切。

### 方法关键点
基于LLM搭建开源SPARQL-LLM KGQA系统，兼容分布式异构KG的Schema差异，适配多语言输入的转换需求。

### 关键结果
在TEXT2SPARQL 2026挑战赛全数据集上排名总榜第一，参与对比的8个方案中，准确率较第二名最高提升59%；支持英、德、西三语问答；已完全开源，且已在生物信息学分布式KG的生产环境落地部署。
