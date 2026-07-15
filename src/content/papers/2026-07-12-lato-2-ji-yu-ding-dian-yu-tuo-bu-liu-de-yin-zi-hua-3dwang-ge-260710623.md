---
title: 'LATO.2: Factorized 3D Mesh Generation with Vertex and Topology Flow'
title_zh: LATO.2：基于顶点与拓扑流的因子化3D网格生成方法
authors:
- Hang Long
- Tianhao Zhao
- Junkai Lin
- Youjia Zhang
- Huipeng Guo
- Rendong Liang
- Jiale Xu
- Jozef Hladký
- Matthias Nießner
- Wei Yang
affiliations:
- Huazhong University of Science and Technology
- Meshy AI
- Independent Researcher
- Technical University of Munich
arxiv_id: '2607.10623'
url: https://arxiv.org/abs/2607.10623
pdf_url: https://arxiv.org/pdf/2607.10623
published: '2026-07-12'
collected: '2026-07-15'
category: Other
direction: 3D生成 · 因子化流匹配
tags:
- Mesh Generation
- Flow Matching
- VAE
- 3D Generation
- Factorized Modeling
one_liner: 将3D网格生成拆解为顶点流+条件拓扑流两阶段，性能超越现有SOTA拓扑感知网格生成器
practical_value: '- 因子化解耦思路可复用：将生成任务中连续属性与离散结构拆分建模，降低多属性联合生成的学习难度

  - 两阶段条件生成架构可迁移到电商3D商品生成场景：先生成几何轮廓再补全拓扑，提升3D商品建模保真度

  - 共享粗粒度锚点的设计可复用：多阶段生成任务共享低维粗基座，保证各阶段输出的全局一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有拓扑感知网格生成方法在联合隐空间建模顶点与连接关系，连续几何信息与离散组合结构纠缠，流学习难度高，易出现顶点漂移、曲面破损问题。
### 方法关键点
1. 提出因子化流匹配框架LATO.2，将生成拆解为顶点流、顶点条件拓扑流两个串行阶段，两阶段共享粗体素基座锚定
2. 两阶段分别搭载专属VAE，实现亚体素精度的顶点还原、离散连接关系到连续隐空间的嵌入
3. 天然支持分块生成更高分辨率网格、修改顶点后无重优化自动适配拓扑两个特性
### 关键结果
几何保真度、连接质量指标均超越现有SOTA拓扑感知网格生成器
