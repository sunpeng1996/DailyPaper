---
title: 'Gaze as Evidence for Common Grounding: A Cross-Corpus Analysis of MapTask
  and MUNDEX'
title_zh: 视线作为共识构建证据：MapTask与MUNDEX跨语料分析
authors:
- Nan Li
- Albert Gatt
- Massimo Poesio
affiliations:
- Utrecht University
- Queen Mary University of London
arxiv_id: '2609.18011'
url: https://arxiv.org/abs/2609.18011
pdf_url: https://arxiv.org/pdf/2609.18011
published: '2026-09-15'
collected: '2026-09-20'
category: Other
direction: 多模态对话 视线特征与共识关联分析
tags:
- gaze feature
- common grounding
- cross-corpus analysis
- collaborative dialogue
- multimodal cue
one_liner: 跨两类信息不对称协作语料，分析视线特征与对话共识构建的关联规律，明确其弱辅助线索定位
practical_value: '- 做AR/VR电商导购Agent时，可将高任务注视占比、低视线熵作为用户理解商品说明的弱辅助特征，需结合对话上下文使用，不可单独作为判断依据

  - 跨场景行为特征分析可复用本研究的标签对齐思路：先将不同场景的异构行为标注映射为统一分类体系，再开展关联分析

  - 做用户行为特征的效果验证时，需同时检验对话维度、用户个体维度的显著性，避免忽略个体差异高估特征作用'
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
信息不对称的协作场景下，对话共识构建的可观测行为线索缺乏跨任务泛化验证，过往不同语料的视线标注体系独立，无法横向对比结论通用性。
### 方法关键点
将HCRC MapTask、MUNDEX两个协作语料的异构视线标注统一映射为「注视同伴/注视任务/看向别处」三类共享标签，提取对话相关单元的视线时序、占比、熵值、跳转次数等特征，分析其与共识达成状态的关联。
### 关键结果
两个语料中达成共识时均呈现更高任务注视占比、更低同伴注视占比、更低视线熵、更少视线跳转的规律，任务主导者的该关联更显著；最优视线特征组仅比对照组有小幅提升，效应量较小，用户个体差异会显著削弱相关性，仅能作为共识判断的辅助线索。
