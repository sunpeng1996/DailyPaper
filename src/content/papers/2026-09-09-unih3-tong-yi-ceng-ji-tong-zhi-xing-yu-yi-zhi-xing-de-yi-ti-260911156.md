---
title: 'UniH^3: Unifying Hierarchical Homogeneity and Heterogeneity for All-in-One
  Medical Image Restoration'
title_zh: UniH³：统一层级同质性与异质性的一体化医学图像恢复框架
authors:
- Zhiwen Yang
- Jiayin Li
- Chengyu Liu
- Hui Zhang
- Bingzheng Wei
- Yan Xu
affiliations:
- Beihang University
- Tsinghua University
- Independent Researcher
arxiv_id: '2609.11156'
url: https://arxiv.org/abs/2609.11156
pdf_url: https://arxiv.org/pdf/2609.11156
published: '2026-09-09'
collected: '2026-09-13'
category: Other
direction: 通用医学图像恢复 · 多任务统一建模
tags:
- Multi-Task Learning
- Universal Model
- Memory Module
- Attention Mechanism
- Medical Image Restoration
one_liner: 提出融合层级同质性记忆与异质性平衡的通用医学图像恢复框架，性能达SOTA
practical_value: '- 本研究属于医疗计算机视觉领域，与电商/广告/搜索推荐业务场景无直接关联

  - 核心方法为医学图像恢复专用技术，无直接可迁移到推荐场景的落地方案

  - 仅多任务均衡训练、通用先验蒸馏的思路可作为通用技术参考'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有一体化医学图像恢复方法仅聚焦任务间异质性（如不同数据分布、退化类型），忽略跨模态、跨任务共享的解剖结构等同质性先验，导致训练效率低、泛化性不足。
### 方法关键点
1. 设计Hierarchical Homogeneity Memory (H2M)模块，训练阶段从高质量图像中渐进蒸馏任务内、跨任务的同质性先验，推理时自适应检索匹配输入的先验引导恢复
2. 提出Homogeneity-Guided Attention (HGA)机制，将检索到的先验高效注入恢复流程
3. 设计Hierarchical Heterogeneity Balancer (H2B)模块，缓解优化过程中任务间、任务内冲突，实现均衡多任务学习
### 关键结果
在MedIR-2D-500K、MedIR-3D-3K两个大规模基准上，一体化及单任务医学图像恢复性能均达到SOTA。
