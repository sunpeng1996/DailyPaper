---
title: 'Escaping Iterative Parameter-Space Noise: Differentially Private Learning
  with a Hypernetwork'
title_zh: 逃脱迭代参数空间噪声：基于超网络的差分隐私学习
authors:
- Naoki Nishikawa
- Shokichi Takakura
- Satoshi Hasegawa
affiliations:
- The University of Tokyo
- LY Corporation
arxiv_id: '2606.26772'
url: https://arxiv.org/abs/2606.26772
pdf_url: https://arxiv.org/pdf/2606.26772
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 差分隐私训练 · 超网络优化
tags:
- Differential Privacy
- Hypernetwork
- DP-SGD
- LoRA
- Diffusion Model
one_liner: 基于超网络实现仅单次低维空间注噪的差分隐私训练，效用显著优于DP-SGD
practical_value: '- 做用户隐私敏感的LLM/推荐模型DP训练时，可替换传统DP-SGD，仅在低维数据集表征加一次噪声，大幅降低噪声对模型效用的影响

  - 私有数据LoRA微调场景（如用户行为数据微调垂类生成/推荐模型），可复用该超网络映射私有数据到目标参数的框架，在保隐私前提下提升模型效果

  - 有公开同领域数据集的业务场景（如公开电商商品数据+私有用户行为数据），可先在公开数据训超网络再处理私有数据，平衡隐私约束和业务效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统梯度基DP训练（如DP-SGD）需在训练迭代过程中反复向高维参数空间注入噪声，噪声累积导致模型效用损失严重，隐私预算固定时效果难以满足业务要求。

### 方法关键点
1. 用公开数据集预训练超网络，直接映射私有数据集到目标模型参数，跳过参数空间的迭代优化过程；
2. 先将私有数据的每个样本嵌入为低维表征，聚合后仅单次注噪得到符合差分隐私要求的数据集嵌入；
3. 超网络基于带噪低维嵌入生成目标模型参数，大幅降低噪声对最终模型效果的负面影响。

### 关键结果数字
固定隐私预算下，合成场景中模型效用显著优于DP-SGD；扩散模型LoRA微调任务中，FID低于DP-SGD及其他公共数据引导的DP方法，生成质量更高。
