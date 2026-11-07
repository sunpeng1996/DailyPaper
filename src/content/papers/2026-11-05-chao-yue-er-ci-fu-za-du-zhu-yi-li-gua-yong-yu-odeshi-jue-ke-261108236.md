---
title: 'Beyond Quadratic Attention: Separable Gaussian Operators for ODE Vision Transformers'
title_zh: 超越二次复杂度注意力：适用于ODE视觉Transformer的可分离高斯算子
authors:
- Carlos Boned Riera
- David Romero Sanchez
- Oriol Ramos Terrades
affiliations:
- Universitat Autònoma de Barcelona
- Centre de Visió per Computador (CVC)
- Centre de Recerca Matemàtica (CRM)
arxiv_id: '2611.08236'
url: https://arxiv.org/abs/2611.08236
pdf_url: https://arxiv.org/pdf/2611.08236
published: '2026-11-05'
collected: '2026-11-07'
category: LLM
direction: 大模型注意力效率优化
tags:
- Attention Optimization
- SSoG
- Vision Transformer
- Neural ODE
- Computation Efficiency
one_liner: 提出次二次复杂度可分离高斯算子SSoG替代稠密注意力，兼顾效果、效率与理论保证
practical_value: '- 长序列用户行为建模、高分辨率商品图理解等推荐场景，可尝试用SSoG替代稠密Attention，降低长token输入下的计算与内存开销，提升推理效率

  - SSoG全局Lipschitz连续的特性可复用在搜索推荐排序模型设计中，降低极端输入下的输出波动，提升线上服务稳定性

  - 连续深度ODE+SSoG的架构思路可迁移到高并发大模型推理服务优化，进一步提升高吞吐场景的资源利用率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
Transformer稠密自注意力的O(N²)复杂度限制了输入分辨率/序列长度的扩展性，且点积注意力Lipschitz常数无界，连续深度ODE变体缺乏全局唯一解的理论保证。
### 方法关键点
可分离高斯和算子SSoG用轴分解高斯核的混合学习替代稠密注意力，将每层复杂度降到N的次二次级；固定核的SSoG具备全局Lipschitz连续性，可保证ODE ViT的解全局唯一。
### 关键结果
224×224分辨率CIFAR-100任务上，固定深度与训练策略，SSoG在3种模型宽度下Top-1精度提升2.2~4.1个点，参数量减少8.8~16.6%；循环Transformer场景精度提升5.4~8.1个点；1024×1024分辨率下，ODE架构中SSoG throughput最高提升154%，峰值内存降低超60%，离散/循环场景throughput提升超30%
