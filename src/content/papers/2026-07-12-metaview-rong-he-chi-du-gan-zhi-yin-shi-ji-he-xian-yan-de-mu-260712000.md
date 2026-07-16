---
title: 'MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry
  Priors'
title_zh: MetaView：融合尺度感知隐式几何先验的单目新视图合成框架
authors:
- Yufei Cai
- Xuesong Niu
- Hao Lu
- Kun Gai
- Kai Wu
- Guosheng Lin
affiliations:
- Nanyang Technological University
- Kolors Team, Kuaishou Technology
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.12000'
url: https://arxiv.org/abs/2607.12000
pdf_url: https://arxiv.org/pdf/2607.12000
published: '2026-07-12'
collected: '2026-07-16'
category: Other
direction: 单目新视图合成 · 3D几何感知生成
tags:
- Novel View Synthesis
- Diffusion Model
- Implicit Geometry
- 3D Generation
- Monocular Vision
one_liner: 提出融合隐式几何先验与度量深度的扩散框架，实现大视角变化下高精度可控单目新视图合成
practical_value: '- 可复用该框架实现单张商品图生成多视角展示素材，降低3D建模成本，提升电商商品页沉浸感

  - 「隐式建模+轻量化显式3D约束」的融合思路可迁移到生成式推荐的内容一致性控制场景，平衡生成灵活性与可控性

  - 度量深度锚定生成尺度的trick可用于直播/短视频虚拟场景构建、AR试穿试戴素材生成，提升空间一致性'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有新视图合成方案存在明显矛盾：引入显式几何先验的方法空间一致性强，但大视角变化下泛化能力受限；采用隐式场景建模的交互生成方案灵活性高，但牺牲了精确相机控制能力与几何一致性，无法满足单图输入下大视角生成的需求。
**方法关键点**：基于扩散的MetaView框架核心采用「隐式几何+轻量化显式约束」的融合设计：1) 引入前馈几何感知网络输出的隐式几何先验做结构正则，无需依赖复杂的重建 pipeline；2) 引入度量深度锚定生成的物理尺度，同时兼顾几何一致性与生成可控性。
**关键结果**：在大视角变化的单目新视图合成任务上，性能显著优于现有SOTA方法，跨场景泛化性突出，代码已开源。
