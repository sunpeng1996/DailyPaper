---
title: 'HAMP-LIC: Hessian-Aware Mixed-Precision Post-Training Quantization for Learned
  Image Compression'
title_zh: HAMP-LIC：面向学习型图像压缩的Hessian感知混合精度训练后量化
authors:
- Yuefeng Zhang
arxiv_id: '2608.12239'
url: https://arxiv.org/abs/2608.12239
pdf_url: https://arxiv.org/pdf/2608.12239
published: '2026-08-12'
collected: '2026-08-15'
category: Other
direction: 模型压缩 · 训练后混合精度量化
tags:
- PTQ
- Mixed-Precision Quantization
- Model Compression
- Hessian Analysis
- Learned Image Compression
one_liner: 提出四阶段Hessian感知混合精度PTQ框架，实现LIC模型低损高压缩比跨平台部署
practical_value: '- 大模型部署阶段可复用Hessian迹估计层量化敏感度的思路，替代经验式位宽分配策略，显著降低低比特量化的精度损失

  - 多模态推荐/生成场景的模型PTQ可参考四阶段优化框架，结合业务目标调整敏感度权重，平衡模型压缩比与核心业务指标

  - 跨异构硬件平台部署AI模型时，可借鉴该框架的一致性优化思路，消除不同设备的推理结果偏差问题'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
预训练学习型图像压缩（LIC）模型计算复杂度高，异构硬件平台间编解码匹配性差；传统固定精度量化未考虑不同网络层的量化敏感度差异，低位宽部署时质量损失严重。
### 方法关键点
提出四阶段Hessian感知混合精度PTQ框架：1）基于Hessian迹估计块级量化敏感度，捕捉参数二阶重要性；2）任务感知优化模块联合量化失真与率失真性能调整敏感度权重；3）在全局模型大小约束下基于敏感度分配位宽，平衡推理效率与重建质量；4）用小规模校准集做块级重构，进一步抑制量化误差。
### 关键结果
在Minnen2018、Cheng2020等典型LIC模型上实现最高4.85倍模型压缩，BD-rate损失仅0.59%，性能优于现有所有固定/混合精度PTQ方法，完全消除跨平台编解码错误。
