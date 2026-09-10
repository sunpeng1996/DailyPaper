---
title: 'DSE-VTG: Dual-Side Enhancement for Training-Free Video Temporal Grounding'
title_zh: DSE-VTG：面向免训练视频时序定位的双边增强框架
authors:
- Zhuo Cao
- Bingqing Zhang
- Sen Wang
- Xue Li
affiliations:
- The University of Queensland, Australia
arxiv_id: '2609.08850'
url: https://arxiv.org/abs/2609.08850
pdf_url: https://arxiv.org/pdf/2609.08850
published: '2026-09-08'
collected: '2026-09-10'
category: Multimodal
direction: 多模态视频时序定位 · 免训练优化
tags:
- Video Temporal Grounding
- Training-Free
- Test-Time Adaptation
- Multi-Scale Fusion
- Vision-Language
one_liner: 提出无需任务训练的双边增强VTG框架，通过视觉多尺度融合与文本测试时适配刷新免训练方法SOTA
practical_value: '- 电商短视频带货场景可复用MSF多尺度相似性融合方法，提升文本query匹配视频片段的准确率，无需额外标注训练

  - 搜索场景中query歧义问题可借鉴Q-TTA轻量偏移优化思路，测试时动态适配query embedding，无需微调大模型backbone

  - OOD场景下的多模态匹配任务可参考双边增强架构，在不新增任务训练成本的前提下提升分布漂移下的鲁棒性'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
Text-guided VTG任务存在标注成本高、监督模型分布漂移下鲁棒性差的问题，现有免训练方案存在两个瓶颈：逐帧视觉编码忽略时序动态，固定query embedding无法解决歧义问题。

### 方法关键点
提出DSE-VTG双边增强免训练框架，无需任何任务专属训练：1. 视觉侧通过Multi-scale Similarity Fusion（MSF）融合帧级、clip级相似性，生成带时序感知的统一相似性特征；2. 文本侧通过Query-level Test-Time Adaptation（Q-TTA）优化轻量加性偏移，测试时适配query embedding到对应视频，无需微调backbone或调用外部LLM。

### 关键结果数字
在3个标准、2个OOD基准上实现免训练方法SOTA，Charades-STA数据集上mIoU比此前最优免训练方法高5.61点；分布漂移场景下Charades-CG Novel-Word数据集mIoU达50.86，比最强监督基线高2.76点。
