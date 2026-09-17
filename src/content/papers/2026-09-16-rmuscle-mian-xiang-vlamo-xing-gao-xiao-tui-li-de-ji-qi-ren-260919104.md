---
title: 'rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model
  Inference'
title_zh: rMuscle：面向VLA模型高效推理的机器人肌肉记忆框架
authors:
- Kaijun Zhou
- Zhiyang Li
- Le Chen
- Jinyu Gu
affiliations:
- Institute of Parallel and Distributed Systems, Shanghai Jiao Tong University
arxiv_id: '2609.19104'
url: https://arxiv.org/abs/2609.19104
pdf_url: https://arxiv.org/pdf/2609.19104
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: 具身Agent · VLA模型推理加速
tags:
- VLA
- Inference Optimization
- Cache Mechanism
- Embodied AI
- Edge Deployment
one_liner: 提出双阶段缓存的rMuscle框架，利用重复任务相似性实现VLA模型无精度损失推理加速
practical_value: '- 对于电商/推荐场景的高频重复请求（如爆款商品内容生成、Top Query召回），可借鉴双缓存思路，分别缓存前置特征（如视觉token、用户embedding）和中间激活状态，大幅降低重复计算量

  - 三个缓存优化trick：在线缓存重计算、滑动窗口检索、连续步骤掩码共享，可直接复用到大模型推理服务的KV cache优化中，降低内存占用与访问开销

  - 端侧部署导购Agent、多模态交互模型时，可复用该框架的相似请求复用逻辑，提升端侧推理速度，降低交互时延'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
工厂场景下具身机器人任务高度重复，当前VLA模型推理时延直接影响机器人响应速度与动作流畅度，现有推理框架未利用任务相似性，也未针对VLA推理不同阶段的瓶颈做优化。
### 方法关键点
1. 验证重复执行的任务相似性可延伸至模型内部状态，提出双阶段肌肉记忆缓存架构：Context Cache复用视觉token输出降低计算量，Action Cache复用神经元激活模式降低权重访问开销
2. 通过在线缓存重计算、滑动窗口缓存检索、连续去噪步骤掩码共享三个优化，控制缓存内存占用与访问开销
### 关键结果数字
在RTX 4090和Jetson Thor设备上，覆盖LIBERO、RoboTwin、实体操作任务，实现1.29-1.42倍推理提速，且完全保持原有机器人任务成功率
