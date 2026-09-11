---
title: 'IAE-VTG: Interaction-Aligned Action-Entity Video Temporal Grounding'
title_zh: IAE-VTG：交互对齐的动作-实体视频时序定位方法
authors:
- Shiwen Zhao
- Qi Zhang
- Sezer Karaoglu
- Theo Gevers
- Martin R. Oswald
arxiv_id: '2609.09736'
url: https://arxiv.org/abs/2609.09736
pdf_url: https://arxiv.org/pdf/2609.09736
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 多模态视频理解 · 文本-视频时序对齐
tags:
- Video Temporal Grounding
- Multimodal Alignment
- Compositional Reasoning
- Cross-modal Matching
- Feature Disentanglement
one_liner: 通过细粒度解耦交互与交互敏感匹配策略，提升视频时序定位的语义准确性
practical_value: '- 可迁移到电商短视频搜索场景：将用户query拆分为动作、实体维度，分别与视频的运动、外观特征对齐，提升目标片段定位准确率

  - FDIM的细粒度特征解耦思路可复用至多模态召回任务，拆分query语义维度匹配对应模态特征，降低语义错配概率

  - ISA训练匹配策略可迁移至多模态排序模型训练，除重合度/相似度外增加语义兼容性约束，减少低质量样本干扰'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有Video Temporal Grounding（VTG）方法多整体编码查询或使用通用跨模态交互，未显式校验动作与实体的共现关联，易选出同时包含两个概念但不匹配查询描述事件的片段。
### 方法关键点
1. 细粒度解耦交互模块（FDIM）：拆分查询的动作、实体相关信息，分别与视频的运动、外观互补特征对齐，融合token级交互构建动作-实体关联表征；
2. 交互敏感分配（ISA）：将交互证据加入二分匹配逻辑，训练时同时基于时序重叠度和语义兼容性选择训练目标，降低时序合理但语义错误的候选框的监督干扰。
### 关键结果
在QVHighlights、Charades-STA、TACoS三个公开数据集上持续优于强基线，达到SOTA或可比性能，在相似动作/实体多次出现、复杂事件场景下提升效果尤为显著。
