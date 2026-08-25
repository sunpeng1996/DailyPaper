---
title: Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervision
title_zh: 基于概念缩放与稠密监督释放图像编辑能力潜力
authors:
- Long Cui
- Xiaoqian Liu
- Qi Qin
- Yi Xin
- Tao Lin
- Jianguo Li
- Linfeng Zhang
affiliations:
- Shanghai Jiao Tong University
- Ant Group
arxiv_id: '2608.16812'
url: https://arxiv.org/abs/2608.16812
pdf_url: https://arxiv.org/pdf/2608.16812
published: '2026-08-16'
collected: '2026-08-25'
category: Other
direction: 多模态图像编辑 · 数据集与训练优化
tags:
- Diffusion Model
- Image Editing
- Dense Supervision
- Dataset
- Evaluation Benchmark
one_liner: 构建12M规模图像编辑数据集、稠密监督训练策略与细粒度评测基准，全面提升编辑性能
practical_value: '- 电商商品图批量美化场景可复用1000+细粒度编辑概念分类体系，定制换背景、调光影、加卖点标签等场景的标准化指令集，降低人工标注成本

  - 多任务AIGC模型训练可借鉴稠密监督策略，将互不干扰的多个编辑任务合成到单训练样本，大幅提升训练效率，减少训练算力开销

  - AIGC能力评估可参考ConceptEdit-Bench的构建思路，按场景、按任务维度拆解细粒度评估指标，避免粗粒度评估带来的效果偏差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像编辑框架直接沿用文生图扩散模型的训练范式，存在两个核心缺陷：对编辑概念的细粒度划分关注不足，且稀疏监督信号导致训练效率低下。
### 方法关键点
1. 构建包含1000+细粒度编辑概念的层级分类体系，通过优化的合成框架生成1200万高质量编辑对数据集ConceptEdit-12M，有效缓解生成数据分布坍塌问题，保证数据保真度；
2. 提出稠密监督训练策略，将多个互不干扰的编辑概念合成到单组图像对中，提供更丰富的学习信号，同步提升训练效率与模型性能；
3. 推出细粒度评估套件ConceptEdit-Bench，覆盖大量真实场景，可精准诊断模型各维度编辑能力。
### 关键结果
训练后模型效果显著优于此前SOTA图像编辑方案。
