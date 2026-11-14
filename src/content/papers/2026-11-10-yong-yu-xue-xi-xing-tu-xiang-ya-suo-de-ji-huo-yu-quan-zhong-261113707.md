---
title: Joint Activation and Weight Quantization for Learned Image Compression
title_zh: 用于学习型图像压缩的激活与权重联合量化方法
authors:
- Yile Tu
- Heming Sun
affiliations:
- Yokohama National University, Japan
- Institute of Science Tokyo, Japan
arxiv_id: '2611.13707'
url: https://arxiv.org/abs/2611.13707
pdf_url: https://arxiv.org/pdf/2611.13707
published: '2026-11-10'
collected: '2026-11-14'
category: Other
direction: 模型量化 · 学习型图像压缩部署优化
tags:
- PTQ
- SmoothQuant
- GPTQ
- Learned Image Compression
- Model Quantization
one_liner: 提出结合SmoothQuant与GPTQ的联合量化框架，降低LIC模型PTQ的率失真损失
practical_value: '- 端侧电商商品图像压缩场景可复用两阶段量化思路，先做范围平衡再微调权重，降低PTQ精度损失

  - 对量化噪声敏感的端侧图像类模型（如商品图特征提取、超分模型）可借鉴联合优化思路，将业务目标（存储带宽、识别准确率）作为量化全局优化目标

  - 无需重训的PTQ方案可直接迁移到存量图像类模型的轻量化部署，降低算力与存储成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

> 动机：学习型图像压缩（LIC）模型率失真性能优异但网络规模大，端侧部署依赖量化降本；现有PTQ方法单独优化权重或激活，对量化噪声敏感的LIC模型会产生严重率失真退化，QAT方案则重训成本过高。
> 方法关键点：1. 采用两阶段量化pipeline：先通过SmoothQuant做数值变换，平衡激活与权重的动态范围，降低量化难度；再通过GPTQ调整变换后的权重，适配量化约束；2. 引入联合搜索框架，以率失真为全局优化目标同时调整两阶段参数，破解两个步骤的耦合问题。
> 关键结果：在多种LIC架构、不同激活量化位宽配置下验证，联合搜索策略可稳定降低量化后的率失真损失，PTQ精度逼近重训的QAT方案效果。
