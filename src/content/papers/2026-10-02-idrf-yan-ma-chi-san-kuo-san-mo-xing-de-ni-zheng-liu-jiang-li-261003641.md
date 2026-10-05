---
title: 'IDRF: Inverse-Distilled Reward Fine-tuning of Masked Discrete Diffusion Models'
title_zh: IDRF：掩码离散扩散模型的逆蒸馏奖励微调框架
authors:
- Vladislav Gromadskii
- David Li
- Samson Gourevitch
- Yazid Janati
- Eric Moulines
- Maxim Panov
- Alexander Korotin
affiliations:
- Applied AI Institute (Moscow)
- MBZUAI
- CMAP, École Polytechnique
- Institute of Foundation Models
- LRE, EPITA
arxiv_id: '2610.03641'
url: https://arxiv.org/abs/2610.03641
pdf_url: https://arxiv.org/pdf/2610.03641
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 离散扩散模型 · 奖励微调效率优化
tags:
- Diffusion Model
- Reward Fine-tuning
- Inverse Distillation
- Discrete Generation
- Sampling Efficiency
one_liner: 提出逆蒸馏正则化的掩码离散扩散奖励微调框架，降采样步数同时规避奖励黑客
practical_value: '- 生成式推荐场景下若用离散扩散生成文案/商品序列，可复用IDRF的逆蒸馏正则替换KL罚，解决序列级KL难计算、采样慢的问题，降低推理延迟

  - 奖励微调场景（如推荐文案点击率优化、Agent工具调用成功率优化）可复用IDRF的轨迹级裁剪策略梯度目标，缓解奖励黑客问题

  - 低延迟少步生成任务可借鉴将生成过程建模为有限horizon MDP的思路，无需参考模型rollout即可完成高效微调，适配线上业务要求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
掩码离散扩散模型是自回归生成的高潜力替代方案，但存在两大痛点：迭代采样成本高，且序列似然不可导导致奖励微调难度大，纯奖励优化易出现奖励黑客问题，破坏原生样本质量。
### 方法关键点
提出IDRF奖励微调框架：用逆蒸馏正则替换不可解的序列级KL罚，理论证明该损失是与参考分布序列KL散度的上界；将少步生成建模为有限 horizon MDP，基于学生模型自身轨迹用裁剪策略梯度优化奖励，无需参考模型rollout，保留原少步采样器。
### 关键结果
跨DNA、图像、文本三类生成任务，IDRF在保持高奖励、样本质量的同时，去噪步数最多较基准减少32倍，有效规避奖励黑客问题。
