---
title: 'Procedura: Agentic 3D Modeling with Procedural Control'
title_zh: Procedura：具备程序化控制能力的智能体3D建模框架
authors:
- Youtian Lin
- Yikang Yang
- Zhanpeng Hu
- Mengqi Zhou
- Feihu Zhang
- Xun Cao
- Jiaheng Liu
- Yao Yao
affiliations:
- Nanjing University
- Envision
arxiv_id: '2608.26238'
url: https://arxiv.org/abs/2608.26238
pdf_url: https://arxiv.org/pdf/2608.26238
published: '2026-08-25'
collected: '2026-08-28'
category: Agent
direction: Agent 驱动程序化3D内容生成
tags:
- Agent
- LLM
- Procedural Generation
- 3D Content Generation
- Vision Critic
one_liner: 基于LLM搭建3D建模智能体，生成可编辑参数化装配程序，效果优于现有SOTA方案
practical_value: '- 逐部件生成+编译/校验通过才准入的逻辑，可迁移到电商Agent生成结构化商品参数、SKU组装场景，避免无效输出

  - 解耦的诊断式视觉critic单点迭代优化思路，可复用在生成式广告物料（3D商品图、短视频脚本）的多轮纠错流程，无需微调LLM即可提升质量

  - 把生成目标转化为可执行参数化程序的范式，适合电商虚拟展厅、3D商品定制场景，天然支持用户自定义编辑'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有原生3D生成器输出的密集网格存在硬表面边缘不锐利、无部件拆分、不可参数编辑的缺陷，无法满足工业级建模及后续二次编辑需求。

### 方法关键点
1. 提出「3D形状即代码」范式，基于LLM的代码能力搭建Procedura智能体框架，将物体建模为参数化装配程序，各命名部件通过可机器校验的接口拼接；
2. 智能体先规划装配图，逐部件编写代码，仅当编译、接口匹配、连通性校验全部通过才保留该部件，部件位置基于匹配框架计算而非盲猜；
3. 引入解耦的视觉评估模块，每次针对诊断出的问题做单点修正，最终输出带部件材质、支持模拟器验证的装配结构。

### 关键结果
在P3D-Bench和自研MechBench-36硬表面基准上，Procedura判定质量优于现有SOTA原生3D生成器及所有3D代码智能体，生成边缘最锐利，是唯一可输出可编辑、带部件结构程序的方法。
