---
title: 'VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes'
title_zh: VidaForge：面向视频预训练数据配方的开源研究基础设施
authors:
- Yan Ma
- Jiadi Su
- Zhulin Hu
- Ethan Chern
- Linhao Zhang
- Tiantian Mi
- Pengfei Liu
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Fudan University
- Shanghai University
- Generative Artificial Intelligence Research Lab (GAIR)
arxiv_id: '2609.06652'
url: https://arxiv.org/abs/2609.06652
pdf_url: https://arxiv.org/pdf/2609.06652
published: '2026-09-05'
collected: '2026-09-10'
category: Training
direction: 视频大模型预训练 · 数据流水线开源
tags:
- VideoFoundationModel
- DataPipeline
- Pretraining
- OpenDataset
- Infrastructure
one_liner: 开源可配置的视频预训练数据配方流水线基础设施，配套3.14M带细粒度标注的视频数据集
practical_value: '- 多模态电商/短视频推荐预训练数据流水线可参考其5阶段可配置范式，快速完成不同数据配方的消融实验，降低调优成本

  - 短视频内容召回的数据集构建可复用其场景级切片、细粒度标注方法，提升预训练数据的质量与匹配度

  - 做数据决策对模型效果的归因分析时，可参考「保留样本全链路生产路径」的设计，实现数据侧决策的可追溯可迭代'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前视频基础模型的端到端预训练数据流水线普遍闭源，研究者验证数据配方对预训练效果的影响需先搭建大量基础设施，研究门槛极高。
### 方法关键点
将视频数据配方抽象为从原始视频到训练数据集的5阶段可执行工作流，支持修改任意环节决策生成不同数据集，全程保留每个样本的生产路径可追溯。
### 关键结果
1. 在Wan 2.1、V-JEPA 2.1的从零预训练实验中，覆盖度更高的数据配方在下游基准取得最优效果，基于损失的评估则偏好其他配方
2. 同步开源VidaForge-3M数据集，包含314万场景级切片、总时长6475小时，附带细粒度标注和治理信号
