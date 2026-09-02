---
title: 'GenFirst: Generation Before Reconstruction for Stable End-to-End Latent Generative
  Modeling'
title_zh: GenFirst：先生成后重建的稳定端到端隐变量生成建模
authors:
- Guangting Zheng
- Yiyuan Zhang
- Tao Yang
- Yunpeng Chen
- Rui Zhu
- Jiajun Deng
- Yanyong Zhang
affiliations:
- University of Science and Technology of China
- ByteDance Seed
arxiv_id: '2608.29335'
url: https://arxiv.org/abs/2608.29335
pdf_url: https://arxiv.org/pdf/2608.29335
published: '2026-08-28'
collected: '2026-09-02'
category: Training
direction: 隐变量生成模型 · 端到端训练优化
tags:
- Latent Generative Model
- End-to-End Training
- Latent Collapse
- Generative Prior
- Multi-modality Generation
one_liner: 提出先生成后重建训练策略，解决隐变量生成模型端到端训练的隐坍缩与目标冲突问题
practical_value: '- 生成式推荐的用户/物品隐表征端到端训练时，可复用「先弱生成目标塑形隐空间、再逐步加强重建损失」的训练顺序，避免表征坍缩

  - 多模态商品生成（主图+文案联合生成、商品Semantic ID建模）场景，可保留KL散度中的熵项约束，防止隐空间坍缩导致的生成多样性下降

  - 跨模态检索/推荐的共享表征训练，可参考不对称学习动态适配思路，动态平衡强监督快收敛任务与弱监督慢收敛任务的训练权重'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统隐变量生成模型两阶段训练存在重建最优隐空间不适配生成任务的缺陷，直接端到端联合训练易出现隐空间坍缩、生成与重建目标冲突问题。
### 方法关键点
1. 挖掘两个核心规律：KL散度中的熵项可抵消重建、先验拟合导致的后验收缩，避免隐坍缩；重建为强监督快收敛任务，生成为弱监督慢收敛任务，二者学习动态不对称。
2. 提出GenFirst训练策略：优先用生成目标在弱重建压力下塑形隐空间，再逐步提升重建损失权重恢复细节，实现无坍缩端到端训练。
### 关键结果
ImageNet-256数据集上SiT模型带CFG的gFID达0.97、不带CFG达1.45；文本生成图像任务MMDiT的GenEval得分达0.90；可拓展至多模态统一生成、生成与表征共享隐空间学习场景。
