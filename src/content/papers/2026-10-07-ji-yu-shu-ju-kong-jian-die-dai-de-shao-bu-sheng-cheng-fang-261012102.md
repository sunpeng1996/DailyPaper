---
title: Few-Step Generation via Data-Space Iteration
title_zh: 基于数据空间迭代的少步生成方法
authors:
- Shanchuan Lin
- Yansong Peng
- Fu-Yun Wang
- Haoqi Fan
affiliations:
- ByteDance Seed
arxiv_id: '2610.12102'
url: https://arxiv.org/abs/2610.12102
pdf_url: https://arxiv.org/pdf/2610.12102
published: '2026-10-07'
collected: '2026-10-13'
category: Training
direction: 生成模型少步采样优化
tags:
- Flow Matching
- Few-step Generation
- DMD
- Generative Model
- Sampling Optimization
one_liner: 提出无需概率流时间步离散化的数据空间迭代框架，提升少步生成效果
practical_value: '- 落地生成式推荐场景（如商品文案、个性化海报、Semantic ID序列生成）时，可直接复用该框架，省去手动调时间步离散化schedule的高额成本

  - 现有基于DMD蒸馏的生成模型可无缝集成该迭代方法，无需大规模改造即可获得少步生成质量提升

  - 对生成质量要求高且latency受限的业务场景（如实时广告素材生成、个性化push文案生成），可优先采用该方法替代传统流空间迭代方案'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Flow matching 是当前高质量生成模型的主流训练范式，但采样需多次网络前向，蒸馏得到的1步生成质量损失严重，少步生成是实际落地的最优选择；现有少步方法依赖概率流固定时间步离散化，调参成本高，无法适配不同样本的差异化精炼难度。
### 方法关键点
完全移除流离散化约束，提出数据空间迭代少步生成框架：从噪声出发，共享生成器直接在数据空间迭代精炼预测结果，每轮迭代目标为产出当前容量下的最优样本；仅需少量修改即可兼容 Distribution Matching Distillation (DMD)，支持相同训练配置下的公平对比。
### 关键结果
在256×256类条件ImageNet生成任务上，效果优于标准离散化基线，与经过schedule搜索的最优变体效果相当甚至更优，无需针对特定schedule做训练。
