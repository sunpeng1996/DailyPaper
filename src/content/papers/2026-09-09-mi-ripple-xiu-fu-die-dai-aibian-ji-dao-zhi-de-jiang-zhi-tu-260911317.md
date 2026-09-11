---
title: 'Mi-Ripple: Restoring Images Degraded by Iterative AI Editing'
title_zh: Mi-Ripple：修复迭代AI编辑导致的降质图像
authors:
- Jiayin Chen
- Yicheng Xu
- Muting Wang
affiliations:
- Miyang Technology (Shanghai) Co., Ltd.
- Key Laboratory of System Software (Chinese Academy of Sciences)
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Shanghai Jiao Tong University
arxiv_id: '2609.11317'
url: https://arxiv.org/abs/2609.11317
pdf_url: https://arxiv.org/pdf/2609.11317
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 多模态生成 · 迭代编辑图像瑕疵修复
tags:
- image_restoration
- AI_generated_image
- artifact_suppression
- structure_aware_filtering
- spectral_notching
one_liner: 提出诊断引导的Mi-Ripple工作流，抑制迭代AI编辑产生的数字波纹同时保护图像结构
practical_value: '- 电商AI生成商品图迭代修图场景可直接复用Mi-Ripple的瑕疵分离+修复工作流，消除网格/颗粒纹理，提升主图、详情页物料质量

  - 选择性频谱陷波+结构感知平滑的组合方案，可集成到内部AI图像生产管线的后处理模块，无需改动原有生成模型逻辑

  - 清洗后参考图再生的思路可迁移到多轮AI生成物料的质量校验环节，降低瑕疵物料的输出率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
迭代式参考条件图像编辑多次复用输出作为新参考时，会产生网格状、颗粒状的数字波纹瑕疵，现有修复方案易破坏原图结构或丢失合法细节。
### 方法关键点
1. 先分离周期性晶格伪影与内容耦合的颗粒纹理，针对不同类型瑕疵适配处理策略
2. 融合选择性频谱陷波、结构感知平滑、清洗后参考图再生三大模块
3. 频谱可隔离的伪影用低失真滤波，滤波会丢失细节的场景改用视觉重建
### 关键结果
14组仅陷波处理实验中，全图CIELAB亮度通道残差标准差仅0.08~0.44；配对再生实验中，参考清洗使输出碎屑密度降低45%，相比仅优化频谱指标的方案，视觉效果提升更显著。
