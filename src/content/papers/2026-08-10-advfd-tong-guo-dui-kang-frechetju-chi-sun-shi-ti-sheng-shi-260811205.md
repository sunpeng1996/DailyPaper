---
title: 'AdvFD: Boosting Visual Generation via Adversarial Fr''echet Distance Loss'
title_zh: AdvFD：通过对抗Fréchet距离损失提升视觉生成能力
authors:
- Mingju Gao
- Jingkai Zhou
- Kun Gai
- Changqian Yu
- Hao Tang
affiliations:
- Peking University
- KlingAI Research
arxiv_id: '2608.11205'
url: https://arxiv.org/abs/2608.11205
pdf_url: https://arxiv.org/pdf/2608.11205
published: '2026-08-10'
collected: '2026-08-12'
category: Training
direction: 生成模型训练 · 对抗损失优化
tags:
- Adversarial Loss
- Fréchet Distance
- Diffusion Model
- Generative Model
- Post-training
one_liner: 提出对抗Fréchet距离损失AdvFD，解决FD优化的Fréchet黑客问题，提升视觉生成器后训练表现
practical_value: '- 电商营销素材/商品图生成场景的生成器后训练环节，可替换原有FD损失为AdvFD，避免指标虚高但实际生成质量下降的Fréchet黑客问题

  - 推荐/多模态领域做分布对齐任务时，可借鉴「静态预训练表征+对抗自适应表征」的组合思路，减少分布对齐偏差

  - 实现min-max对抗优化时，可复用真实特征白化trick，归一化特征尺度与协方差结构，避免优化不稳定'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有FD损失作为扩散、流匹配等生成模型后训练的分布级优化目标，存在Fréchet黑客问题：目标指标持续提升，但实际生成质量、其他特征空间的FD对齐效果停滞甚至下降，根因是FD依赖的静态预训练特征空间对真实与生成分布差异的表征不全且固定。
### 方法关键点
1. 提出AdvFD损失，在原有静态FD目标基础上新增可学习对抗表征：对抗侧最大化真实/生成样本的FD差异，生成器在自适应特征空间最小化该差异
2. 引入真实特征白化机制，归一化特征尺度与协方差几何结构，解决对抗表征特征放大导致的优化不稳定问题
### 关键结果
在JiT、pMF两种骨干网络、不同模型尺度的一步生成器后训练任务上，AdvFD均带来一致的效果提升
