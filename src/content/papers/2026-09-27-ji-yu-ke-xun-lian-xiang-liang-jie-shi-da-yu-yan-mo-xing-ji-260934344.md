---
title: 'Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large
  Language Models via Trainable Vectors'
title_zh: 基于可训练向量揭示大语言模型RLVR的几何特性与训练优化方法
authors:
- Yuchen Cai
- Ding Cao
- Qixiang Yin
- Xin Xu
- Kai Yang
- Siye Wu
- Pengyuan Wang
- Jiaxuan Wang
- Weijie Liu
- Saiyong Yang
affiliations:
- USTC
- Tencent Hunyuan
- BUPT
arxiv_id: '2609.34344'
url: https://arxiv.org/abs/2609.34344
pdf_url: https://arxiv.org/pdf/2609.34344
published: '2026-09-27'
collected: '2026-10-09'
category: Training
direction: 大语言模型RLVR训练稳定与几何机制
tags:
- RLVR
- LLM Training
- Activation Geometry
- Training Stability
- Vector Steering
one_liner: 发现RLVR增益对应激活空间低维有效流形，提出无额外参数的RL训练稳定框架Alpha-Stabler
practical_value: '- 电商导购Agent、推荐理由生成Agent等业务场景做RL微调时，可直接复用Alpha-Stabler框架，监控激活主空间侵入度提前预警训练崩毁，仅修改反向梯度即可稳定GRPO/DAPO等主流RLVR训练，无需新增参数，适配现有训练
  pipeline

  - 低资源大模型微调场景可参考向量steering思路：在中低层注入固定可训练向量即可还原85%+全参数RL微调增益，大幅降低训练/推理成本，适合将大模型的推理、文案生成能力蒸馏到小模型部署到业务端

  - 跨业务任务迁移可参考控制流形对齐特性：若两个业务任务（比如不同品类的商品文案生成、不同场景的搜索query理解）的steering向量余弦相似度高，则迁移增益高，可快速判断是否可复用已有RL微调权重，减少重复训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR已成为大模型提升推理能力的核心后训练范式，但高维参数更新过程黑盒化、训练易崩毁，内部增益机制不明确，缺乏可落地的训练稳定方案。
### 方法关键点
- 以向量steering为分析探针：冻结基础模型，仅在指定层注入输入无关的共享可训练偏移向量，蒸馏RL训练后教师模型的增益，定位激活空间的低维有效流形
- 提炼两个核心几何特性：①有效流形容量：极低维干预即可还原大部分RL增益，但不可无限压缩，效果随注入深度、师生分布gap动态变化；②控制流形分离：有效控制方向集中在激活主空间的低方差正交补空间，同任务下几何结构跨训练配置高度一致，跨任务对齐度与迁移增益正相关
- 提出Alpha-Stabler训练框架：Predictor模块监控激活主空间侵入度（PSI）提前预警训练崩毁，Controller模块反向传播时移除梯度的主空间分量、保留正交补分量，无额外训练参数，无需修改原有RL训练流程
### 关键结果
在1.5B~14B共5个LLM、数学/科学推理/代码/指令跟随共6类可验证奖励任务上验证：
- 每层单个固定steering向量即可还原85%+全参数RL微调增益
- 跨科学子任务的steering向量对齐度与迁移增益线性拟合R²达0.91
- Alpha-Stabler可稳定RL训练2000步，性能优于梯度裁剪等基线，无显著计算开销
> 最值得记住的结论：RLVR的能力增益本质是激活空间低维流形上的偏移，远离激活主空间的梯度更新才是有效更新，侵入主空间是训练崩毁的核心前兆
