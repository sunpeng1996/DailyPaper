---
title: Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient
  Diffusion RLHF
title_zh: 面向样本高效扩散RLHF的选择性时间步加权与优势重放方法
authors:
- Eric Zhu
- Abhinav Shrivastava
- Soumik Mukhopadhyay
affiliations:
- Carnegie Mellon University
- University of Maryland, College Park
arxiv_id: '2607.07693'
url: https://arxiv.org/abs/2607.07693
pdf_url: https://arxiv.org/pdf/2607.07693
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: 扩散RLHF训练 · 样本效率优化
tags:
- RLHF
- Diffusion Model
- Sample Efficiency
- PPO
- Replay Buffer
- GRPO
one_liner: 提出时间步加权与优势轨迹重放策略，将扩散RLHF样本效率最高提升6倍且兼容现有管线
practical_value: '- 电商生成式推荐（图文/短视频/商品文案生成）的RLHF偏好对齐场景，可直接复用时间步加权trick，用扩散隐向量变化平方$|z_t-z_{t-1}|^2$作为权重，无需复杂计算即可提升对齐效率，降低奖励模型调用成本

  - LLM/多模态模型GRPO/PPO训练场景，可引入基于优势绝对值的轨迹硬挖重放机制，仅保留最近3轮高价值轨迹，既提升样本效率又避免分布偏移，适合标注/反馈成本高的业务

  - 现有扩散RLHF管线可直接将两个策略作为插件集成，无需修改模型架构即可获得2~6倍样本效率提升，同时不损失prompt泛化性与内容一致性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有扩散RLHF（如DDPO）给所有去噪时间步分配统一权重，且采样轨迹用完即丢弃，奖励反馈效率极低，在人力/奖励模型调用成本高的真实场景（如电商AIGC物料生成、内容偏好对齐）落地难度大。

### 方法关键点
- 时间步加权：理论推导PPO时间步优势与TD误差方差正相关，用去噪过程中隐向量变化平方$|z_t-z_{t-1}|^2$作为权重近似，动态给对最终结果影响大的去噪步分配更高训练权重，解决信用分配问题
- 优势轨迹重放：构建仅保留最近3轮轨迹的轻量回放池，按优势绝对值硬挖高价值轨迹复用，无需重复请求奖励即可获得更多有效训练信号，同时避免旧轨迹带来的分布偏移
- 两个策略完全即插即用，无需修改现有扩散RLHF的模型架构和训练流程

### 关键实验
基于Stable Diffusion v1.5，在JPEG压缩/反压缩、美学评分、HPS v2、Image Reward共5类偏好奖励函数上测试，对比DDPO、DPOK、B2-DiffuRL等基线，相同奖励查询预算下样本效率最高提升6倍；4k次奖励查询下新prompt泛化性平均提升12%以上，CLIP打分无明显下降。

最值得记住的一句话：扩散RLHF的训练信号天然分布不均，给高贡献时间步、高优势轨迹更高权重，是用极低工程成本换数倍样本效率提升的核心思路
