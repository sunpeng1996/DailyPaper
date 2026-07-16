---
title: 'Compos3D: Interactive Part-Based Composition for Creative Control in Generative
  3D Models'
title_zh: Compos3D：生成式3D模型中支持创意控制的交互式部件组合方法
authors:
- Faraz Faruqi
- Sean J. Liu
- George Fitzmaurice
- Justin Matejka
affiliations:
- Autodesk Research
arxiv_id: '2607.12193'
url: https://arxiv.org/abs/2607.12193
pdf_url: https://arxiv.org/pdf/2607.12193
published: '2026-07-13'
collected: '2026-07-16'
category: Other
direction: 生成式3D建模 · 创意交互控制
tags:
- Generative 3D
- Compositional Generation
- Creative Control
- Interactive Workflow
- 3D Content Generation
one_liner: 提出基于部件混搭的生成式3D建模工作流，提升创意可控性与结果对齐度
practical_value: '- 电商3D商品生成、虚拟样品设计场景可复用「多候选生成+部件混搭组装」的工作流，大幅降低反复重生成的算力与时间成本

  - 面向C端的AI定制化商品设计工具可借鉴部件级选择拼接的交互逻辑，降低普通用户的3D创作门槛，提升结果满意度

  - 生成类任务Agent可参考该分阶段任务拆解思路，将“生成符合要求的内容”拆分为候选产出、要素筛选、整合优化三步，提升输出可控性'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有生成式3D建模工作流依赖多次重生成，可控性弱、输出不可预测，难以精准对齐用户的创意意图。
### 方法关键点
1. 提出Compos3D系统，将3D生成拆分为候选生成、部件混搭两个阶段：用户基于文本/图像prompt生成多个3D候选后，可通过2D图像区域或3D网格段选取不同候选中的目标部件，拼接为初步组合方案。
2. 系统自动将用户组合的部件合成为统一的精细化3D模型，在保留用户高层创意意图的同时，自动解决低层几何兼容问题。
### 关键结果
受控用户研究显示，相比传统重生成工作流，该混搭工作流的用户创意控制度、意图对齐度、用户满意度均显著更优。
