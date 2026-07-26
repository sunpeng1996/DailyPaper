---
title: 'SGA: Plug&Play Geometric Verification for Educational Video Synthesis'
title_zh: SGA：面向教育视频合成的即插即用几何验证模块
authors:
- Lopez Jhon
- Hinojosa Carlos
- Ghanem Bernard
affiliations:
- Universidad Industrial de Santander
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2607.18116'
url: https://arxiv.org/abs/2607.18116
pdf_url: https://arxiv.org/pdf/2607.18116
published: '2026-07-20'
collected: '2026-07-26'
category: Agent
direction: Agent 生成代码空间正确性校验
tags:
- Agent
- LLM Code Generation
- Spatial Verification
- Plug-and-Play
- Quality Metric
one_liner: 提出即插即用SGA模块与无渲染MVQS指标，解决LLM生成动画代码的空间冲突问题
practical_value: '- 电商生成商品展示短视频、活动页动画的代码生成管线中，可复用SGA即插即用的校验逻辑，无需改造原有LLM生成链路，仅新增中间校验修正环节即可解决元素遮挡、排版混乱问题

  - 做生成类内容质量评估时，可借鉴MVQS的无渲染代理指标思路，无需完成完整渲染/生成流程即可前置校验布局合理性，大幅降低算力开销

  - Agent生成可执行代码类任务（如活动页前端代码、商品陈列脚本）优化，可参考「拦截生成结果→部分执行提取结构化表征→定向修正」范式，提升输出正确性'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于LLM生成Manim教育动画代码的方案仅关注教学内容准确性，忽略几何遮挡等空间冲突问题，导致视觉可读性差，且传统质量校验需要完整渲染，算力开销极高。
### 方法关键点
1. 提出即插即用Symbolic Geometric Agent（SGA）模块，拦截LLM生成的动画代码，通过部分执行提取符号化场景图，检测到空间冲突后对代码做定向修正
2. 提出无渲染的确定性评估指标Manim Visual Quality Score（MVQS），无需执行完整渲染流程即可量化空间完整性
### 关键结果
在MMMC-Code基准上覆盖4种LLM backbone、2种Agent管线测试：SGA加持的Code2Video+GPT-5.1管线MVQS峰值达73.11，相对原始基线提升16.1%；8种backbone×管线组合中，有7种的MVQS获得明显提升
