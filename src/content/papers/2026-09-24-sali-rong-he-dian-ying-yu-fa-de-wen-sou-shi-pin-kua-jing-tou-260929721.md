---
title: 'SALI: Shot-Aware Late Interaction for Cross-Shot Relation Matching in Text-to-Video
  Retrieval using Film-Grammar Knowledge'
title_zh: SALI：融合电影语法的文搜视频跨镜头关系匹配后交互方法
authors:
- Toya Oyama
- Rainer Lienhart
- Shin'ichi Satoh
affiliations:
- The University of Tokyo
- National Institute of Informatics
- University of Augsburg
arxiv_id: '2609.29721'
url: https://arxiv.org/abs/2609.29721
pdf_url: https://arxiv.org/pdf/2609.29721
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态检索 · 文搜视频效果优化
tags:
- Text-to-Video Retrieval
- Late Interaction
- Optimal Transport
- Film Grammar
- CLIP
one_liner: 提出融合电影语法的SALI镜头感知后交互方法，提升文搜视频多镜头关系查询召回
practical_value: '- 电商短视频/直播切片检索场景可复用拆分query主客体、逐镜头匹配的思路，提升含人物交互、多场景切换类query的检索准确率

  - 针对多片段结构化内容的召回任务，可引入领域先验规则作为微调惩罚项，在几乎不损失整体召回效果的前提下提升专项query表现

  - 多分段匹配算子可根据算力预算选择greedy max（低延迟）或最优传输（高精度），灵活适配在线/离线业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文搜视频（T2VR）方案通常将整段视频编码为单一embedding，忽略视频的镜头分切结构，无法捕捉跨镜头的人物交互等组合语义关系，导致影视剧、多场景短视频等内容的关系类查询召回效果差。
### 方法关键点
1. SALI镜头感知后交互框架：先从文本query中抽取主体、客体，分别将query整体、主客体的文本embedding与视频的每个镜头embedding做匹配
2. 匹配算子支持贪心取最大值（低算力）或最优传输（高精度）两种可选方案
3. 微调阶段加入电影语法先验惩罚项，对符合镜头切换逻辑的匹配结果做小幅修正
### 关键结果
基于CLIP4Clip-meanP基线构建，Condensed Movies、ActivityNet数据集整体召回与基线持平，多镜头关系查询R@1分别提升3、12个点，为对比方法中最高；MSR-VTT数据集该类查询效果提升，仅损失1.4的整体R@1
