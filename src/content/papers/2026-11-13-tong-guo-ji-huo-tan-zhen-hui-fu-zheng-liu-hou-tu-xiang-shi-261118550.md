---
title: Restoring Diversity in Distilled Image and Video Generators by Probing Activations
title_zh: 通过激活探针恢复蒸馏后图像视频生成器的样本多样性
authors:
- Furkan Horoz
- Ozgur Kara
- Kaan Oktay
- Adil Kaan Akan
- Atakan Kara
- Anand Bhattad
- James Matthew Rehg
affiliations:
- University of Illinois at Urbana-Champaign
- fal
- Johns Hopkins University
arxiv_id: '2611.18550'
url: https://arxiv.org/abs/2611.18550
pdf_url: https://arxiv.org/pdf/2611.18550
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 扩散模型蒸馏 · 样本多样性优化
tags:
- Diffusion Model
- Knowledge Distillation
- Sample Diversity
- Activation Probing
- Adapter
one_liner: 定位蒸馏扩散模型多样性坍缩根因为激活方差方向集中，提出两类方案保质量恢复生成多样性
practical_value: '- 低延迟生成场景（如电商商品图/短视频批量生成）可复用ReDiverse方案，在少步蒸馏模型上同时保障生成质量与样本多样性，满足多素材投放需求

  - 大模型蒸馏部署时，可复用激活探针方法定位性能退化的核心层，无需全链路调优即可定位问题，大幅降低迭代成本

  - 生成式推荐模型蒸馏后出现的候选集多样性下降问题，可迁移ReDiverse-FT的轻量Adapter微调方案，以极低算力成本修复多样性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
扩散模型蒸馏为少步学生模型可大幅降低采样延迟，但会出现严重多样性坍缩：不同随机种子生成的样本差异极小，限制生成模型落地可用性。
### 方法关键点
1. 通过激活探针定位坍缩根因：学生模型总激活方差与教师相当，但方差集中在极少方向，且坍缩仅发生在初始去噪步骤的特定中间块，并非固有生成能力损失。
2. 提出两类修复方案：训练侧ReDiverse-FT微调轻量Adapter，将学生激活回归到教师分布，恢复特征方差特性；推理侧ReDiverse-TF无训练开销，沿预计算的教师主成分方向调整激活即可。
### 关键结果
在图像、视频多类蒸馏基准上，ReDiverse可完全恢复样本多样性，同时生成质量无损失，相关效果也得到用户研究验证。
