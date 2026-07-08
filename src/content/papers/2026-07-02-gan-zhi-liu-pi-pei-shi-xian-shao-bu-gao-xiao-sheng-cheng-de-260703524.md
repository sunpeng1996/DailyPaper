---
title: Perceptual Flow Matching for Few-Step Generative Modeling
title_zh: 感知流匹配：实现少步高效生成的流匹配建模优化框架
authors:
- Chuyang Zhao
- Yifei Song
- Hongfa Wang
- Jianlong Yuan
- Yuan Zhang
- Siming Fu
- Zhineng Chen
- Huilin Deng
- Haoyang Huang
- Nan Duan
affiliations:
- Joy Future Academy
- Fudan University
- Tsinghua University
- USTC
arxiv_id: '2607.03524'
url: https://arxiv.org/abs/2607.03524
pdf_url: https://arxiv.org/pdf/2607.03524
published: '2026-07-02'
collected: '2026-07-08'
category: Training
direction: 生成式建模 · 流匹配少步推理优化
tags:
- Flow Matching
- Generative Modeling
- Few-step Inference
- Perceptual Supervision
- Inference Acceleration
one_liner: 将流匹配监督迁移到预训练感知特征空间，无需教师模型即可实现4-8步高质量生成
practical_value: '- 生成式推荐场景下若采用流匹配做商品海报/文案生成，可直接复用PFM思路，在CLIP等预训练语义特征空间做监督，无需蒸馏即可将采样步数压至4-8步，大幅降低推理延迟适配线上QPS要求

  - 放弃隐空间回归、切换到任务相关预训练特征空间做监督的思路，可迁移到Semantic ID生成、用户兴趣建模等任务，缓解平均预测带来的结果模糊/趋同问题

  - 无需教师模型的少步生成优化方案，可大幅降低生成式任务的训练成本，无需额外预训练大教师模型即可快速完成线上部署适配'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统流匹配模型需35-50步采样才能产出高质量结果，推理延迟高难以落地，现有蒸馏加速方案依赖教师模型或辅助分数网络，训练成本高、集成复杂度高。
### 方法关键点
1. 放弃传统VAE隐空间的速度回归逻辑，改用预训练感知模型提取的特征空间做流匹配监督；
2. 无需教师模型、辅助网络，仅需对标准流匹配训练pipeline做极少量修改即可集成；
3. 感知监督将回归目标从均值寻向转为模式寻向，预测偏向流形上的有效模式，少步粗粒度积分下仍能保持精度。
### 关键结果
采样步数从35-50步降至4-8步的同时完全保留生成质量，在图像生成、视频生成、图像编辑任务上效果优于现有蒸馏类方法，生成伪影数量显著降低。
