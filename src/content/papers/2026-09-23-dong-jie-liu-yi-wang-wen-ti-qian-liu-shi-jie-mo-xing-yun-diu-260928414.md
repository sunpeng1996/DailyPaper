---
title: 'Frozen Flows Forget: Diagnosing and Restoring Lost Motion in a Latent-flow
  World Model'
title_zh: 冻结流遗忘问题：潜流世界模型运动丢失的诊断与修复
authors:
- Xiwen Chen
- Rigaudiere Z. Li
- Zhiruo Zhou
- Xiaojun Zhu
- Houde Liu
affiliations:
- 清华大学深圳国际研究生院
- 上海交通大学
- 武汉理工大学
arxiv_id: '2609.28414'
url: https://arxiv.org/abs/2609.28414
pdf_url: https://arxiv.org/pdf/2609.28414
published: '2026-09-23'
collected: '2026-09-25'
category: Other
direction: 世界模型 · 冻结潜空间运动修复
tags:
- WorldModel
- LatentDynamics
- FrozenEncoder
- Training
- MotionPrediction
one_liner: 提出解码增强Rollout训练法DART，修复冻结潜流世界模型的运动丢失缺陷
practical_value: '- 冻结预训练大模型（如LLM、多模态编码器）做下游时序动态建模时，不能仅依赖隐层损失，需补充解码路径监督信号，避免用户行为/商品动态等核心属性丢失

  - 时序类任务（如用户行为序列预测、广告投放效果时序预估）的评估不能只看单点误差，需额外校验时序结构合理性，避免模型输出静态/跳变的无效结果

  - 少参数微调冻结大模型的动态预测模块时，可复用DART的rollout+解码监督范式，无需解冻编码器即可提升动态建模精度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
冻结自监督潜空间的流模型训练稳定、计算成本低，但存在隐性运动崩溃问题：要么预测场景完全静止，要么物体瞬移，标准隐层损失无法感知该缺陷，根源是稀疏锚点、仅隐层的监督信号无法标记时序变化的对应位置。
### 方法关键点
提出解码增强Rollout训练（DART），全程保持编码器表征冻结，仅在流模块训练时加入解码路径的监督信号，无需修改原有模型架构。
### 关键结果
DART全面优于仅隐层监督的基线，恢复了运动的时序结构，将预测运动与场景重新耦合；扩规模后进一步提升预测质量，填补了与oracle插值参考之间近50%的性能gap；额外发现仅用像素误差的评估会奖励静态预测，存在显著评估偏差。
