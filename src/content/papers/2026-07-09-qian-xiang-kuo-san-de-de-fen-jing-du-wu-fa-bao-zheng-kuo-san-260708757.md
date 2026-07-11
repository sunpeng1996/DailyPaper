---
title: Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability
  in Diffusion Sampling
title_zh: 前向扩散的得分精度无法保证扩散采样的数值稳定性
authors:
- Yiwei Zhou
affiliations:
- The University of Texas at Austin
arxiv_id: '2607.08757'
url: https://arxiv.org/abs/2607.08757
pdf_url: https://arxiv.org/pdf/2607.08757
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 扩散模型采样数值稳定性理论研究
tags:
- diffusion model
- score matching
- numerical stability
- Euler-Maruyama
- denoiser projection
one_liner: 证明扩散模型前向边际得分误差小无法保证采样稳定性，提出紧支集数据下的去噪器投影修复方案
practical_value: '- 若使用扩散模型生成商品文案/图片/Semantic ID，不能仅以前向得分匹配损失作为收敛指标，需额外校验采样数值稳定性，避免偶发生成崩坏

  - 当生成内容为有限值域（如枚举类商品属性、固定范围embedding），可将去噪器输出投影到已知有界凸集，抑制罕见采样轨迹的数值爆炸

  - 扩散类生成式推荐模型上线前，需增加Wasserstein距离相关的采样效果校验，避免弱收敛达标但实际生成质量波动大的问题'
score: 4
source: arxiv-cs.LG
depth: abstract
---

## 动机
当前扩散模型普遍以前向边际的得分匹配误差作为训练收敛核心指标，未验证该指标是否能保证离散采样阶段的数值稳定性。

## 方法关键点
1. 构造反例证明：即便前向L2误差任意小、路径空间全变差任意接近真实过程、弱收敛成立，Euler-Maruyama离散采样的所有正阶矩仍会发散，所有p≥1的Wasserstein距离也会发散，且该问题在固定有限神经架构下同样存在。
2. 针对紧支集数据，将学习到的去噪器投影到包含数据支撑集的有界闭凸集，可在保留点精度的同时实现一致矩边界和Wasserstein收敛。

## 关键结果
小参数量DiT风格网络实验验证，去噪器投影可完全抑制罕见采样轨迹的数值爆炸，且整体轨迹误差无明显上升
