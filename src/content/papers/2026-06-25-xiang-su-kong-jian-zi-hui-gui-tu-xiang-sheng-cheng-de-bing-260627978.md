---
title: Parallel Rollout Approximation for Pixel-Space Autoregressive Image Generation
title_zh: 像素空间自回归图像生成的并行Rollout近似方法
authors:
- Jiayi Xu
- Di He
- Guolin Ke
affiliations:
- Peking University
- DP Technology
arxiv_id: '2606.27978'
url: https://arxiv.org/abs/2606.27978
pdf_url: https://arxiv.org/pdf/2606.27978
published: '2026-06-25'
collected: '2026-06-30'
category: Multimodal
direction: 自回归生成 · 像素空间建模
tags:
- Autoregressive Generation
- Pixel-space Modeling
- Train-Inference Gap
- Parallel Rollout
- Image Generation
one_liner: 提出PRA框架解决像素空间自回归生成的误差累积与训练推理gap，取得SOTA性能
practical_value: '- 解决自回归生成任务训练推理gap时，可借鉴该思路：用并行方式近似推理rollout，同时兼顾训练效率和分布对齐

  - 高维输出生成任务可借鉴解耦设计：先生成低维中间状态再映射到目标输出空间，有效降低单步生成误差，适合生成式推荐、多模态生成场景

  - 保留原生输入输出接口的设计思路，可复用在需要兼容原有输入输出格式的生成任务改造中'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
像素空间连续token自回归生成直接将图像建模为原始像素块序列，无需离散化或单独预训练分词器，但存在两个耦合挑战：高维像素块生成导致单步误差大，teacher-forced训练带来训练-推理gap，误差会在自回归步间累积。现有修复方法仅能部分缓解问题，精确rollout训练虽匹配推理条件，但顺序采样速度过慢无法实用。

### 方法关键点
提出Parallel Rollout Approximation（PRA）可扩展框架，同时解决两个问题：1. 不直接生成高维像素块，先生成低维中间状态，再用像素解码器映射回像素空间token，保留像素进像素出的自回归接口；2. 沿各位置独立，用推理阶段相同的中间状态转像素路径构建类推理像素输入，在保留并行teacher-forced训练的同时，近似推理rollout的像素反馈接口。

### 关键结果
256×256分辨率类别条件ImageNet-1K生成任务中，135M参数的PRA-S FID达2.58，超过此前十亿参数级像素空间AR模型的3.60；511M参数的PRA-L FID进一步降至1.94，创下像素空间AR模型新SOTA；迁移到ImageNet分类任务，探针准确率也高于AR和扩散基线。
