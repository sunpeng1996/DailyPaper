---
title: Optimal Mixture-of-Experts Model Averaging for Conditional Generative Models
title_zh: 面向条件生成模型的最优专家混合模型平均框架
authors:
- Shijin Gong
- Baihua He
- Xinyu Zhang
affiliations:
- University of Science and Technology of China
- Academy of Mathematics and Systems Science, Chinese Academy of Sciences
arxiv_id: '2607.04360'
url: https://arxiv.org/abs/2607.04360
pdf_url: https://arxiv.org/pdf/2607.04360
published: '2026-07-05'
collected: '2026-07-07'
category: Training
direction: 条件生成模型 · 专家混合模型聚合
tags:
- MoE
- ModelAveraging
- MMD
- ConditionalGeneration
- AsymptoticOptimality
one_liner: 提出基于样本MMD的静态/输入自适应条件生成器聚合方法，兼具理论保证与多模态性能增益
practical_value: '- 多生成模型融合场景可直接复用MoEMA架构：无需候选模型暴露密度或内部参数，仅需生成样本即可完成自适应权重学习，适合聚合不同架构、不同域训练的电商文案生成、商品图生成、生成式推荐模型

  - 样本MMD损失可直接作为黑盒生成模型的融合目标，无需修改原有模型的训练逻辑，仅需新增百KB级轻量softmax门控网络即可，工程改造成本极低，适合快速上线多模型融合的生成类业务

  - 若候选模型为不同用户群/场景训练的领域专家，MoEMA可自动根据输入（用户特征、场景特征）匹配合适的模型，相比固定权重融合最高可降低70%以上的生成误差，适合多域/多场景的广告、推荐生成任务'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前条件生成模型迭代速度快，业务场景中常面临多个候选生成器选型难题，单个模型无法在全输入空间保持最优性能；传统模型平均方法依赖可计算的模型似然，无法适配扩散模型、自回归LLM等无显式密度的黑盒生成器，亟需不依赖模型内部结构的通用聚合方案。
### 方法关键点
- 提出两类无侵入聚合方案：静态权重StaticMA通过二次规划求解全局固定的融合权重；输入自适应MoEMA通过轻量softmax门控网络学习随输入动态变化的权重，全程无需修改候选生成器的结构与训练逻辑
- 采用基于样本的条件MMD作为聚合优化目标，仅需候选模型输出的生成样本即可计算损失，无需访问模型似然或内部参数，适配所有黑盒条件生成器
- 从理论上证明了两类方法的样本内/样本外渐近最优性，以及MoEMA权重函数的一致性，保证融合效果渐近不弱于最优单模型
### 关键实验
覆盖表格、图像、文本三类模态任务，对比最优单模型、等权平均等基线：表格回归任务上MoEMA相比最优单模型最高降低68%的误差；图像条件生成任务上FID最高降低90%以上；多域文本续写任务上相比静态权重融合降低5%左右的MMD，困惑度降低40%左右。
### 核心结论
不需要修改原有生成模型、仅依赖样本的输入自适应模型融合，是低成本提升生成类任务效果的高性价比方案。
