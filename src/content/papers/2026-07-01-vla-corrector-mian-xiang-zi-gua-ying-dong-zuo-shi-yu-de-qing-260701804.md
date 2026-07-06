---
title: 'VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action
  Horizon'
title_zh: VLA-Corrector：面向自适应动作时域的轻量检测校正推理框架
authors:
- Yi Pan
- Miao Pan
- Qi Lu
- Jiaming Huang
- Man Zhang
- Siteng Huang
- Xin Li
- Jie Zhang
- Yongliang Shen
- Xuhong Zhang
affiliations:
- Zhejiang University
- Alibaba DAMO Academy
- ZJU ACES Lab OmniAI Group
arxiv_id: '2607.01804'
url: https://arxiv.org/abs/2607.01804
pdf_url: https://arxiv.org/pdf/2607.01804
published: '2026-07-01'
collected: '2026-07-06'
category: Agent
direction: 具身Agent · VLA推理优化
tags:
- VLA
- Embodied Agent
- Inference Optimization
- Action Chunk
- Adaptive Horizon
one_liner: 无需重训VLA骨干的轻量检测校正框架，破解固定动作时域鲁棒性与效率的权衡问题
practical_value: '- 推荐/广告开环预测场景可复用检测-校正架构：无需重训骨干模型，新增轻量监控模块对比预测结果和实际反馈的偏差，触发重排/重生成，平衡推理效率和效果

  - 长序列生成/批量执行类任务可借鉴自适应时域设计：结果可靠时保留长序列执行降低调用成本，漂移时触发短步长重规划，解决静态时域的鲁棒性效率权衡问题

  - 可复用Latent空间偏差检测思路：无需处理原始输入，直接对比预测和实际的隐层特征演化，计算成本低，适配在线低延迟业务场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA生成式策略为降低调用频率、保持时序连贯性，普遍采用固定时域动作chunk开环执行范式，接触丰富的交互场景下微小扰动会在开环盲区快速放大，累积误差最终导致任务失败，静态时域无法兼顾执行鲁棒性与策略调用效率。
### 方法关键点
1. 无需修改VLA骨干权重，新增轻量Latent-space Vision Monitor（LVM），在线对比预测与实际视觉特征演化，实现视觉动态偏差的实时检测；
2. 检测到持续偏差时截断剩余失效动作，通过Online Gradient Guidance（OGG）触发校正重规划，自然实现事件驱动的自适应动作时域。
### 关键结果
无需重训VLA骨干即可接入不同VLA模型，长时域接触丰富的机器人操作任务中鲁棒性大幅提升，同时保留动作chunk的大部分效率收益，有效缓解静态时域的固有权衡。
