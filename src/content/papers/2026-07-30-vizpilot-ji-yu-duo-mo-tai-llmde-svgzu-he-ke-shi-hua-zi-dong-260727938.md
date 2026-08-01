---
title: 'VizPilot: Automated Onboarding for SVG-based Composite Visualizations using
  Multimodal LLMs'
title_zh: VizPilot：基于多模态LLM的SVG组合可视化自动引导方案
authors:
- Nishaanthini Gnanavel
- Yong Wang
arxiv_id: '2607.27938'
url: https://arxiv.org/abs/2607.27938
pdf_url: https://arxiv.org/pdf/2607.27938
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 多模态LLM · 可视化自动用户引导
tags:
- MLLM
- SVG
- Composite Visualization
- User Onboarding
- Multimodal
one_liner: 基于多模态LLM逆向解析SVG组合可视化结构，自动生成交互式用户引导流程
practical_value: '- 电商数据看板、后台可视化报表的新用户引导可复用两阶段解析+元素映射pipeline，自动生成引导内容，大幅降低人工编写成本

  - 多模态LLM解析视觉元素并映射到DOM节点的思路，可用于前端交互类Agent自动识别页面元素，完成自动操作、智能答疑等需求

  - 双模式（引导式+自由探索）的用户引导设计，可复用在电商新功能上线、活动页的用户引导流程中，降低用户学习成本提升转化'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
组合可视化可高效表达复杂数据集，但复杂结构对新手用户初始认知负荷极高；现有可视化引导方案依赖特定平台、需大量人工编写、难适配组合可视化的结构复杂度，通用性差。
### 方法关键点
1. 整体分为组合可视化分析器、引导接口两大模块，以浏览器插件形式落地；
2. 基于MLLM的两阶段解析pipeline：语义推理阶段按5类分类体系拆分可视化组件生成原子解释单元，语义映射阶段通过层级DOM遍历将解释锚定到具体SVG元素，支持精准高亮交互；
3. 引导接口支持叙事滚动式引导、自由探索两种模式，开发者仅需提供简短可视化描述和可选交互源码即可自动生成引导内容。
### 关键结果
可自动化生成引导内容，有效降低人工编写成本，同时降低用户认知负荷，提升组合可视化的可用性与可访问性。
