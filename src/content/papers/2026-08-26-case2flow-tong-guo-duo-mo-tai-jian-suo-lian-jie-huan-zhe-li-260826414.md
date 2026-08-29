---
title: 'Case2Flow: Bridging Patient Cases and Guideline Flowcharts through Multimodal
  Retrieval'
title_zh: Case2Flow：通过多模态检索连接患者病例与指南流程图
authors:
- Jiale Wei
- Yufan Chen
- Alexander Jaus
- Zdravko Marinov
- Julian Friedrich
- Simon Reiß
- Jens Kleesiek
- Rainer Stiefelhagen
affiliations:
- Karlsruhe Institute of Technology
- Helmholtz Information and Data Science School for Health
- University Hospital Essen
arxiv_id: '2608.26414'
url: https://arxiv.org/abs/2608.26414
pdf_url: https://arxiv.org/pdf/2608.26414
published: '2026-08-26'
collected: '2026-08-29'
category: Multimodal
direction: 多模态图文检索 · 无训练优化
tags:
- Multimodal Retrieval
- Image-Text Alignment
- Training-free
- Dataset Construction
- Cross-modal Matching
one_liner: 提出病例匹配指南流程图的多模态检索任务、FlowAtlas数据集与无训练优化方法CRISP
practical_value: '- 电商多模态商品检索/推荐场景可直接复用CRISP的无训练优化思路，抑制商品图冗余背景、降低模糊关键词匹配权重、加入双向图文对齐，无需重训模型即可提升跨模态匹配效果

  - 构建跨模态图文匹配训练数据集时，可借鉴其自动合成对齐pair的流水线，大幅降低人工标注成本

  - 做跨模态召回bad case分析时，可重点排查「关键词过度依赖」「非信息区域误匹配」两类共性问题，针对性优化召回逻辑'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
医疗指南内置的流程图可直接指导临床决策，但医务人员难以从海量指南中快速定位匹配具体病例的流程图，现有多模态检索存在过度依赖关键词、流程图无意义背景引发虚假匹配的问题。
### 方法关键点
1. 定义Case2Flow任务：输入患者病例，从指南库中检索最相关的决策流程图；
2. 构建FlowAtlas数据集：包含从2080份指南提取的202张流程图，以及自动合成的1911个病例-流程图对齐pair；
3. 提出无训练的CRISP打分方法：通过抑制无信息图像patch、降低模糊token匹配权重、引入双向图文对齐优化晚交互检索效果。
### 关键结果
CRISP将Recall@1最高提升18.71pp，盲态医师评估验证了其在真实病例场景的可行性。
