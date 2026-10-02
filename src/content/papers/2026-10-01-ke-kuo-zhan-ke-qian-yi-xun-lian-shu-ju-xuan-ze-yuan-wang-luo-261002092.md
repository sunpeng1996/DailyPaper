---
title: Scalable, Transferable Meta-network for Data Selection Requires a Different
  Loss (and Why the Obvious Choice is Problematic)
title_zh: 可扩展可迁移训练数据选择元网络TESS及专用损失设计
authors:
- Zilin Du
- Bowen Yang
- Boyang Albert Li
affiliations:
- Nanyang Technological University
arxiv_id: '2610.02092'
url: https://arxiv.org/abs/2610.02092
pdf_url: https://arxiv.org/pdf/2610.02092
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: LLM训练 · 可迁移数据选择元网络优化
tags:
- Data Selection
- Meta Learning
- LLM Training
- Bilevel Optimization
- Transfer Learning
one_liner: 提出基于Pointwise Value Matching损失的TESS框架，实现跨场景可迁移的LLM训练数据选择
practical_value: '- 垂直域LLM（如电商客服、商品文案生成LLM）微调场景，可直接复用TESS的PVM损失构造样本价值伪标签，避免传统MTS方法的权重抑制和捷径学习问题，提升数据筛选模型的跨域泛化性

  - 大模型微调成本受限的场景，可先用小参数模型训练TESS数据选择器，再迁移到大模型的训练数据筛选，可降低数据筛选成本5~6倍，保留70%以上的筛选性能

  - 推荐系统训练样本去噪、高价值样本筛选场景，可借鉴PVM的伪标签构造思路：用仅在训练集训练的模型和加入目标域信号训练的模型的损失差作为样本价值监督信号，无需额外人工标注'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于元学习的训练数据选择（MTS）方法存在两大瓶颈：一是样本/域级固定权重方案无法泛化到未见过的数据集，二是直接引入元网络输出权重时会出现优化不稳定、泛化性差的问题，根源是传统ScaleBiO损失存在权重抑制（大部分样本权重被压至0，失去价值区分度）和易学习特征主导（依赖训练集特有的捷径特征，分布偏移下性能骤降）两个固有缺陷，亟需更稳定的训练目标实现低成本、可迁移的大规模训练数据筛选。
### 方法关键点
- 采用顺序训练范式：先训练两个固定LLM，θ_U仅在训练集上优化，θ_W同时加入目标验证集信号优化
- 构造无监督样本价值伪标签Δ_i = ℓ(θ_U, x_i) - ℓ(θ_W, x_i)，差值越大说明样本对目标任务的价值越高
- 设计Pointwise Value Matching（PVM）损失，用MSE约束元网络输出的样本权重拟合伪标签，替代传统ScaleBiO的加权损失，从根源避免权重抑制和捷径学习
- 训练完成的元网络可直接对未见过的候选样本打分，无需额外优化，峰值内存占用比ScaleBiO低20%以上
### 关键实验
在LLM安全微调、目标指令微调两个核心场景验证：
1. 安全微调场景：跨数据集泛化下TESS的攻击成功率（ASR）比SBO、SEAL基线高22~24个百分点，性能仅比同数据集训练下降5.13%；用小模型训练的选择器迁移到大模型筛选可降低训练成本5.6~6.6倍，保留77%~83%的性能
2. 指令微调场景：仅用50K子集训练的TESS可泛化到200K全量语料筛选，Llama-2-7B在GSM8K+CodeX任务上平均准确率比随机选择高4.92个百分点，比LESS、RDS+等启发式方法高1.95~2.55个百分点，训练时间比样本级权重的SBO_w低3.46倍

最值得记住的一句话：训练数据选择元网络的泛化性瓶颈核心来自损失函数的固有缺陷，基于样本价值伪标签的点对匹配损失可以同时解决优化不稳定和泛化差的问题，大幅降低大规模数据筛选的成本。
