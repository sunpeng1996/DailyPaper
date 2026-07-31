---
title: 'QQWorld: Quantile-Quantile Matching for World Model Regularization'
title_zh: QQWorld：基于分位数匹配的世界模型正则化方法
authors:
- Zhoushun Yu
- Xiaoyu Hu
- Xiangyu Xu
affiliations:
- Xi'an Jiaotong University
arxiv_id: '2607.28415'
url: https://arxiv.org/abs/2607.28415
pdf_url: https://arxiv.org/pdf/2607.28415
published: '2026-07-30'
collected: '2026-07-31'
category: Agent
direction: Agent世界模型 · 隐分布正则化
tags:
- World Model
- Distribution Regularization
- Quantile Matching
- Latent Space
- Planning
one_liner: 用分位数匹配替代EP正则化解决隐空间重尾问题，提升世界模型规划性能
practical_value: '- 隐空间正则化场景可直接替换原有MMD/EP类分布匹配损失为QQ匹配损失，能有效抑制重尾、提升梯度信号强度，无额外超参数，迁移成本几乎为零

  - 小batch训练场景可复用跨Batch的历史detached样本扩充分位数排序池，几乎不增加显存即可大幅提升小batch下的分布匹配精度，适配高维大模型训练

  - 生成式推荐/LLM4Rec的用户/物品表征分布对齐场景，可借鉴QQ匹配思路修正极端表征，解决召回排序结果不稳定问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于EP正则化的隐世界模型要求隐分布服从各向同性高斯，但EP损失的梯度对离群尾部样本会快速消失，导致隐空间存在严重重尾问题，多步规划时尾部极端隐值会放大预测误差，大幅降低规划成功率。

### 方法关键点
1. 提出QQ匹配损失，将投影后的一维隐向量排序后直接与对应秩的高斯分位点对齐，梯度大小与分位点偏差线性正相关，尾部样本也能获得有效修正梯度
2. 设计跨Batch QQ策略，用FIFO队列存储历史Batch的detached隐样本扩充排序池规模，梯度仅回传当前Batch样本，大幅降低显存开销
3. 理论证明QQ损失是比EP更强的分布约束，QQ损失收敛到0时EP损失必然收敛到0，反之不成立

### 关键结果
在Two-Room、PushT等4个控制环境测试，对比LeWM、Sub-JEPA等基线，QQWorld平均规划成功率达85.08%，较LeWM提升5.33个百分点；KS统计量降低15.8%，EP统计量降低31.4%，尾部概率大幅下降接近高斯参考值；跨Batch QQ用32的小batch仅需27%显存即可达到大batch 98%的性能。

> 值得记住：适合做分布差异度量的统计量不一定适合做训练目标，优化过程中全域的有效梯度信号比单纯的分布区分能力更重要。
