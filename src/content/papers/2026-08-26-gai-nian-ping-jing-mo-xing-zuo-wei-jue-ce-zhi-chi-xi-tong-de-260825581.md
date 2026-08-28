---
title: Are Concept Bottleneck Models Effective as Decision-Support Systems?
title_zh: 概念瓶颈模型作为决策支持系统的有效性评估
authors:
- Alessandro Bogani
- Nicola Debole
- Emanuele Marconato
- Andrea Pugnana
- Katya Tentori
- Andrea Passerini
affiliations:
- DISI, University of Trento, Italy
- CIMeC, University of Trento, Italy
arxiv_id: '2608.25581'
url: https://arxiv.org/abs/2608.25581
pdf_url: https://arxiv.org/pdf/2608.25581
published: '2026-08-26'
collected: '2026-08-28'
category: Eval
direction: 可解释AI · 人机协作决策效用评估
tags:
- Concept Bottleneck Model
- Human-AI Collaboration
- Interpretability
- User Study
- Decision Support
one_liner: 通过705人规模用户实验，明确概念瓶颈模型在人机协作决策中的适用条件与效果边界
practical_value: '- 电商风控、广告审核、内容合规等需要人机协同决策的场景，可优先尝试CBM架构替代黑盒模型，提升人机团队整体准确率

  - 部署CBM前需验证三个前置条件：任务难度高、决策逻辑可拆解为人工可识别的明确概念、支持用户主动修改概念配置，不满足时落地收益极低

  - 需重点优化CBM的概念检测模块准确率，概念识别错误会大幅降低运营/审核人员对模型的信任，反而拉低协作效率'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
黑盒AI的可解释性不足是人机协作落地的核心障碍，Concept Bottleneck Models（CBM）作为天生可解释的模型架构被寄予厚望，但缺乏大规模用户研究验证其作为决策支持系统的实际效用。
### 方法关键点
开展两组大规模受控用户实验，覆盖705名参与者、累计6959条决策观测数据，在两类二分类任务中对比无AI辅助、非可解释AI辅助、带概念交互能力的CBM辅助三种模式下的人机团队决策表现。
### 关键结果
带交互功能的CBM可显著提升人机团队决策准确率，表现优于无AI辅助和非可解释AI辅助方案，但增益仅在三个条件下生效：任务感知难度高、决策概念易被人工识别、用户主动和模型交互；概念检测准确率不足会严重损害用户对模型的信任。
