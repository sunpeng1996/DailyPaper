---
title: 'SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid
  Agentic Layout Evolution'
title_zh: SceneMosaic：基于混合智能体布局演化的高效多样化3D场景生成
authors:
- Xingjian Ran
- Xiaoye Mo
- Sihao Liu
- Jianyu Zhang
- Li Luo
- Bo Dai
affiliations:
- The University of Hong Kong
- University of Electronic Science and Technology of China
arxiv_id: '2609.05594'
url: https://arxiv.org/abs/2609.05594
pdf_url: https://arxiv.org/pdf/2609.05594
published: '2026-09-03'
collected: '2026-09-10'
category: Agent
direction: VLM智能体 · 3D场景生成优化
tags:
- VLM Agent
- 3D Scene Generation
- Hybrid Generation Paradigm
- Layout Evolution
- Efficiency Optimization
one_liner: 结合图像先验初始化与VLM智能体布局演化，实现高效物理合规的多样化3D场景生成
practical_value: '- 混合范式架构可直接复用：先用工效更高的小模型/预训练先验输出粗结果，再用大模型Agent做精细化校验修正，平衡生成质量与 latency，可迁移到电商商品搭配、直播间布景生成、虚拟试穿场景生成等业务

  - 局部独立演化+全局笛卡尔组合的思路可迁移到多单元组合类任务（如多sku打包推荐、营销素材多元素组合生成），既保证局部逻辑合理性，又能快速批量生成大量多样化输出

  - 多样性生成优化技巧可复用：通过单元级并行演化替代全局迭代，大幅降低多样化生成的算力开销，适合需给同一用户/需求生成多套推荐/内容方案的场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D场景生成两类主流范式均有缺陷：VLM Agent驱动的方案生成质量高但迭代优化耗时极长；基于2D图像先验的参数化方案效率高但物理合规性差，且两类方案均难以针对单输入生成多样化输出，无法满足交互娱乐、具身AI的规模化场景需求。
### 方法关键点
1. 双阶段混合架构：先基于图像预训练先验快速生成初始候选布局，再用VLM Agent执行布局演化，兼顾效率与物理有效性；
2. 局部分治策略：将场景拆解为独立局部单元，各单元并行演化后通过笛卡尔乘积组合全局场景，大幅提升生成多样性。
### 关键结果
在SceneEval-100数据集上，语义布局质量与最优Agent基线持平，推理速度提升24x，物理违规问题大幅减少，人类偏好评分位列第一。
