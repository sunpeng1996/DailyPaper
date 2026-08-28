---
title: 'Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion
  for Vision Transformer Encoders in JEPA World Models'
title_zh: 连续容量增长：JEPA世界模型ViT编码器的任务复杂度驱动宽深扩展
authors:
- Frederik Berenz
affiliations:
- 121-labs.com, Remscheid, Germany
arxiv_id: '2608.27367'
url: https://arxiv.org/abs/2608.27367
pdf_url: https://arxiv.org/pdf/2608.27367
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: Transformer自适应架构训练优化
tags:
- Vision Transformer
- JEPA
- Adaptive Architecture
- Function-Preserving Expansion
- World Model
one_liner: 提出任务复杂度驱动的ViT动态宽深扩展机制，显著提升JEPA世界模型的参数与计算效率
practical_value: '- 做Agent世界模型的视觉表征编码器时，可复用SCG动态扩缩机制，无需提前预置最大容量模型，大幅降低训练与推理成本

  - 推荐系统多任务场景下的Transformer基座训练可借鉴「功能保留扩展+试错回滚」逻辑，根据任务复杂度动态调整头数/层数，避免算力浪费

  - SIGReg正则化方法可直接迁移到多语义维度表征学习场景，有效防止表征坍缩，提升不同语义维度的独立性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
JEPA世界模型普遍采用固定尺寸ViT编码器，存在简单任务算力冗余、复杂任务容量不足，注意力头冗余度高的问题。
### 方法关键点
1. 提出连续容量增长(SCG)方法，从极小初始编码器（1头、2层、283K参数）起步，根据任务复杂度动态扩宽（新增注意力头提升低阶语义能力）或加深（新增Transformer块提升高阶语义抽象能力）；
2. 采用任务无关的试错验证机制，基于功能保留扩展安全测试架构变更，无收益则直接回滚；
3. 搭配SIGReg正则化，保证语义维度统计独立、贴合预测目标，避免架构扩张时出现表征坍缩。
### 关键结果
- 60维多物体动态任务：深度扩展后预测损失较固定小基线低20.3%，参数效率比固定大模型高56倍；
- 2D导航任务：单次宽度扩展后效果较固定大模型高23%；
- 3个复杂度递增环境下，自适应编码器效果持平或优于固定小基线，无错误扩张，功能保留精度100%
