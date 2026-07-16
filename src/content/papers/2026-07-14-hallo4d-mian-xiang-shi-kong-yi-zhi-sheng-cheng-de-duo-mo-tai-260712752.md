---
title: 'Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal
  Generation'
title_zh: Hallo4D：面向时空一致生成的多模态幻觉缓解框架
authors:
- Hongbo Wang
- Huaibo Huang
- Jie Cao
- Jin Liu
- Haoyang Tong
- Ran He
affiliations:
- 中国科学院自动化研究所MAIS&NLPR
- 中国科学院大学
- 上海科技大学
arxiv_id: '2607.12752'
url: https://arxiv.org/abs/2607.12752
pdf_url: https://arxiv.org/pdf/2607.12752
published: '2026-07-14'
collected: '2026-07-16'
category: Multimodal
direction: 多模态生成 · 3D/4D时空一致性优化
tags:
- MultiModal Generation
- Hallucination Mitigation
- LMM
- 3D Generation
- 4D Generation
- Consistency Optimization
one_liner: 提出无需重训的多模态幻觉缓解框架，提升3D/4D生成的时空一致性
practical_value: '- 可借鉴「生成-检测-修正」范式+多模型投票的思路，优化电商商品3D/动态短视频生成的一致性问题，避免重训成本

  - 运动感知关键帧采样、曝光感知优化的trick可直接复用在电商商品动态展示素材的自动化生成流程中，提升生成效率和视觉稳定性

  - LMM做生成内容一致性校验的思路可迁移到电商UGC/PGC素材的自动质检环节，替代部分人工审核'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前3D生成依赖2D扩散监督，无显式几何一致性约束，易出现结构重复、几何错位等空间幻觉；4D生成需同时保证跨视角与时序演化一致性，进一步加剧抖动、身份闪烁、结构漂移等问题，现有方案多需重训或修改模型结构，适配性差。

### 方法关键点
1. 模型无关的统一框架，采用生成-检测-修正范式，调用LMM识别多视图、多帧渲染结果中的时空不一致问题
2. 共识驱动的图像空间一致性优化，LMM选择器通过多模型投票评估候选修正方案，无需重训或修改原有生成架构
3. 融合运动感知关键帧采样、LMM引导初始化、外观对齐、曝光感知优化、可见性剪枝策略，提升时序一致性与优化效率

### 关键结果
在多种3D/4D生成设置下稳定优于现有强基线，实现可扩展、泛化性强的一致性感知内容生成
