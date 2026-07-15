---
title: 'Learning to Forget: Satiation-Aware Long-Sequence Transducers for Mitigating
  Post-Purchase Redundancy'
title_zh: 学会遗忘：面向购后消冗的饱足感知长序列推荐模型
authors:
- Yipin Dai
- Ruocong Tang
- Xing Fang
- Yang Huang
- Jing Wang
- Zhentao Song
- He Guo
arxiv_id: '2607.12714'
url: https://arxiv.org/abs/2607.12714
pdf_url: https://arxiv.org/pdf/2607.12714
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 长序列推荐 · 购后冗余抑制
tags:
- Sequential Recommendation
- Long Sequence Modeling
- Post-purchase Redundancy
- Self-supervised Learning
- E-commerce RecSys
one_liner: 提出饱足感知序列推荐框架SAM，缓解电商场景购后重复推荐的冗余问题
practical_value: '- 可直接复用双路交叉注意力结构，对已完成购买意图关联的历史点击做反向抑制，快速降低现有长序列推荐模型的重复推荐率

  - 自适应饱足门控单元ASGU的时间敏感软掩膜逻辑，可直接适配复购类商品的兴趣唤醒规则，替代人工配置的复购周期阈值

  - 自监督TTNP辅助任务无需额外标注，可直接加入现有推荐模型的多任务训练pipeline学习商品隐式生命周期，降低标注成本'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有序列推荐模型默认所有用户交互都是偏好累积的正向信号，忽略电商场景下购买行为往往代表特定意图终止（兴趣退出）而非延续的特性，存在行为-意图不对称问题，导致严重的购后重复推荐冗余。
### 方法关键点
端到端饱足感知机制SAM针对性建模用户兴趣生命周期，包含三个核心模块：
1. 双路交叉注意力架构：反向抑制已满足意图关联的历史点击，同时从长期购买历史中检索个性化复购节奏；
2. 自适应饱足门控单元ASGU：生成时间敏感软掩膜，购后立即抑制已满足兴趣，在预测的复购周期临近时逐步唤醒；
3. 自监督Time-to-Next-Purchase（TTNP）辅助任务：无需人工标注即可学习商品隐式生命周期。
### 关键结果
工业数据集离线实验与线上A/B测试验证，SAM可将购后重复推荐率（PPRR）显著降低超60%
