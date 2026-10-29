---
title: 'ScIntBench: Physical Interaction Plausibility in 3D Scene Generation'
title_zh: 《ScIntBench：面向3D场景生成的物理交互合理性评测基准》
authors:
- Wendi Ying
- Daochang Liu
- Leonid Sigal
- Ajmal Saeed Mian
affiliations:
- The University of Western Australia
- University of British Columbia
- Canada CIFAR AI Chair
arxiv_id: '2610.37326'
url: https://arxiv.org/abs/2610.37326
pdf_url: https://arxiv.org/pdf/2610.37326
published: '2026-10-27'
collected: '2026-10-29'
category: Eval
direction: 3D场景生成 · 物理交互评测基准
tags:
- Benchmark
- Text-to-3D
- Physical Interaction
- Evaluation Metric
- 3D Generation
one_liner: 提出首个面向文本生成3D室内场景的物理交互可靠性统一评测基准，量化静态性能与交互可用性差距
practical_value: '- 电商3D虚拟场景（家装试搭、AR商品交互、虚拟直播间）的评测可直接复用这套「静态校验+物理模拟交互+多维度指标」的框架，规避看起来合规但实际操作失效的bad
  case

  - 多模态生成类任务的评测体系设计可借鉴分层思路：先语义保真校验→静态规则校验→动态交互/模拟验证，逐层过滤无效生成结果，提升评测准确性

  - 涉及Agent与3D环境交互的业务（如虚拟导购引导用户操作虚拟商品），可参考其从场景描述自动推导可执行交互动作的逻辑，快速生成测试用例'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文本条件3D室内场景生成的评测仅聚焦语义保真度、静止状态下的物理有效性，缺少交互阶段的物理可靠性评估，无法衡量生成场景的实际落地可用性。
### 方法关键点
1. 推出ScIntBench统一评测基准，设计三层评估体系：多视角语义质量评估（真实度、功能、布局、完成度）、静态物理合理性校验（碰撞、边界、支撑、稳定性）、主动交互合理性评测（基于Isaac Sim物理引擎执行推、开、放置等预设操作，量化任务成功率、交互进度、交互后完整性、动态合理性4类核心指标）
2. 覆盖10类房间类型，完成12个SOTA 3D场景生成系统的系统性评测
### 关键结果
静态表现接近完美的系统仅能完成11.54%的交互任务，12个系统中有7个完全不支持任何交互，最优系统的交互任务成功率仅为36.92%，验证静态性能与交互可用性无强关联。
