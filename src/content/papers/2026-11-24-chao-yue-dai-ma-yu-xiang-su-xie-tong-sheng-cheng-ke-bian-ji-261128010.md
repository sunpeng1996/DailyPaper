---
title: 'Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations'
title_zh: 超越代码与像素：协同生成可编辑的富视觉演示文稿
authors:
- Wenrui Zhou
- Jiashun Liu
- Sujie Hu
- Bang Liu
- Ling Pan
affiliations:
- HKUST
- Tsinghua University
- Mila-Quebec Artificial Intelligence Institute
- Université de Montréal
arxiv_id: '2611.28010'
url: https://arxiv.org/abs/2611.28010
pdf_url: https://arxiv.org/pdf/2611.28010
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: 多智体协作 · 结构化内容生成
tags:
- Multi-Agent
- Diffusion Model
- Presentation Generation
- Hybrid Generation
- Editable Content
one_liner: 提出混合多Agent系统SlidesWeaver，同时保障演示文稿生成的视觉丰富度与原生编辑性
practical_value: '- 多Agent协作做结构化生成时，可借鉴「分阶段承诺」机制：先让视觉生成模型做像素级创意探索，再落地成结构化可编辑格式，平衡自由度与可控性，可迁移到电商
  landing page、营销素材生成场景

  - 针对内容保真与创意自由度的不同需求，可设计双路线调度：需要保留固定文案的场景用文本优先路线，需要视觉创意优先的场景用拓扑优先路线，适配电商不同营销素材的生成需求

  - 评估结构化生成多样性时，可复用Topo-Vendi指标，从拓扑结构维度量化生成结果的差异性，避免生成内容同质化，可用于推荐系统生成物料、Query的多样性评估'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有演示文稿生成方案分为两类：程序化生成路线输出可编辑内容但视觉效果僵硬同质化，图像生成路线视觉效果好但输出为像素级无法编辑，两类方案无法兼顾编辑性与视觉丰富度；且多Agent协作时存在内容、布局、视觉属性的决策依赖问题，过早固化任意维度都会限制下游优化空间。

### 方法关键点
- 提出分阶段多模态承诺协作机制，通过共享的Deck级、Slide级状态协调语言Agent与视觉Agent，避免决策冲突
- 设计双生成路线：Topology First路线先由低步Diffusion模型生成像素级布局提案，再根据布局容量生成适配文本，优先保障视觉创意；Text First路线先固定文案内容，再用Diffusion模型生成布局提案，优先保障文本准确性
- 最终将Diffusion生成的视觉提案落地为原生PPT格式，保留文本、几何参数的可编辑性，同时支持并行生成降低耗时

### 关键实验
测试集覆盖6个领域共72个演示文稿生成需求，对比AutoPresent、DeepSlides、DeepPresenter三类基线，共24种系统-模型配置。Text First路线相比最强基线，视觉表现力提升14.2%、指令遵循度提升15.9%、内容质量提升17.7%、布局有效性提升20.3%、拓扑多样性提升22.9%；Topology First路线比DeepPresenter成本低37.3%、速度快57.7%，8个Pareto最优配置中6个属于SlidesWeaver。

### 核心结论
将视觉生成能力嵌入结构化生成的全流程，而非仅作为素材获取工具，可同时兼顾生成结果的创意自由度与可控性。
