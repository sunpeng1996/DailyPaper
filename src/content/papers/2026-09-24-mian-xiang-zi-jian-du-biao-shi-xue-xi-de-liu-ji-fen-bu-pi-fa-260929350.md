---
title: Learning a Flow to Self-Supervised Representations
title_zh: 面向自监督表示学习的流基分布匹配方法
authors:
- Yuling Jiao
- Wensen Ma
- Houduo Qi
- Defeng Sun
arxiv_id: '2609.29350'
url: https://arxiv.org/abs/2609.29350
pdf_url: https://arxiv.org/pdf/2609.29350
published: '2026-09-24'
collected: '2026-09-25'
category: Training
direction: 自监督表示学习 · 分布匹配优化
tags:
- Self-Supervised Learning
- Distribution Matching
- Flow-Based Model
- Representation Learning
- Efficient Training
one_liner: 提出非对抗的流基分布匹配FBDM框架，训练速度较DM提升1.48-1.83倍且性能相当
practical_value: '- 做用户/商品/内容表示自监督预训练时，可替换现有对抗式分布匹配方案，用FBDM降低训练成本，提速且GPU内存开销几乎无增加

  - 自监督训练中可复用「同一样本多视图绑定到同一目标+单参考中心分配样本数限流」的约束策略，避免表示坍缩

  - 球条件速度回归的非对抗分布对齐思路可迁移到多模态语义表示对齐任务，降低对齐训练复杂度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有自监督表示学习的对抗式分布匹配方法需承担编码器-判别器联合优化的高昂成本，多数SSL方法对表示全局分布的约束为隐式，易出现表示坍缩问题。
### 方法关键点
提出非对抗的Flow-Based Distribution Matching（FBDM）框架，通过球面条件速度回归学习参考导向的几何结构；采用ETF启发的参考分布，支持分量数超过辅助流维度仍保持结构化几何分离；绑定同一样本的增强视图到同一目标，限制每个参考中心可接收的样本数，新增显式对齐损失拉近不同视图的表示。
### 关键结果
在CIFAR到ImageNet基准上性能与DM相当，比肩主流SSL方法；相同训练成本下，速度较DM提升1.48~1.83倍，GPU内存开销几乎无增加；理论证明预训练损失可约束下游任务错分类率上界。
