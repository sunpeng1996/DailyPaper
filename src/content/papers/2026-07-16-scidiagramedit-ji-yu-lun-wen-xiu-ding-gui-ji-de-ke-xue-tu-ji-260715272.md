---
title: 'SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions'
title_zh: 《SciDiagramEdit：基于论文修订轨迹的科学图表智能编辑框架》
authors:
- Yasheng Sun
- Zezi Zeng
- Yifan Yang
- Chong Luo
- Wenyi Wang
- Ziwei Liu
- Jürgen Schmidhuber
affiliations:
- King Abdullah University of Science and Technology
- Microsoft Research
- Nanyang Technological University
arxiv_id: '2607.15272'
url: https://arxiv.org/abs/2607.15272
pdf_url: https://arxiv.org/pdf/2607.15272
published: '2026-07-16'
collected: '2026-07-19'
category: Agent
direction: Agent 技能进化与指令驱动内容编辑
tags:
- Agent Skill Evolution
- Instruction Tuning
- Benchmark Dataset
- Revision Mining
- Vector Graphics Editing
one_liner: 构建科学图表编辑基准，提出技能进化Agent框架，利用arXiv修订数据实现指令驱动矢量图智能编辑
practical_value: '- 可复用「从自然用户修订轨迹挖掘训练信号」的思路，训练电商商品详情页/海报自动编辑Agent时，无需人工标注，直接复用真实美工改稿前后对作为训练数据，大幅降低标注成本

  - 技能进化Agent迭代框架可直接迁移：从Agent执行轨迹中自动提炼技能规则、多轮迭代优化的范式，适配客服话术优化、商品主图自动裁切改色等有明确操作轨迹的业务场景

  - 矢量元素可编辑的Agent交互设计可借鉴：做内容生成类Agent时输出可分层编辑的原子元素（如商品海报的文字、背景、商品图层），支持用户二次协同修改，大幅提升落地易用性'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
科研论文图表修订是高频耗时的日常工作，现有指令驱动的自动编辑方案难以适配科学图表多元素、视觉语法严谨的特性，同时缺乏带天然意图的标注训练数据。
### 方法关键点
1. 挖掘arXiv多版本论文的图表修订前后对，构建带原作者真实修订意图的基准数据集；
2. 采用技能进化的Agent学习范式，由提议器从多轮执行轨迹中持续迭代优化技能规则；
3. 直接基于矢量图源文件操作，支持用户与Agent协同编辑单个图元。
### 关键结果
在留出验证集上，编辑成功率随进化迭代次数单调上升，验证了自然论文修订轨迹可作为指令驱动图表编辑的有效训练信号。
