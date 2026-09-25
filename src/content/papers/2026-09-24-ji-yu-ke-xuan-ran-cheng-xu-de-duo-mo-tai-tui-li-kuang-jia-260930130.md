---
title: Multimodal Thinking with Renderable Programs
title_zh: 基于可渲染程序的多模态推理框架SVGLM
authors:
- Sunli Chen
- Ding Zhong
- Ziqiao Ma
- Jiaxin Liu
- Zeyuan Yang
- Hao Zhang
- Lie Lu
- Joyce Chai
- Chuang Gan
affiliations:
- University of Massachusetts Amherst
- University of Michigan
- University of Illinois Urbana-Champaign
- Dolby Laboratories
arxiv_id: '2609.30130'
url: https://arxiv.org/abs/2609.30130
pdf_url: https://arxiv.org/pdf/2609.30130
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态推理 · SVG中间表示
tags:
- VLM
- SVG
- Multimodal-Reasoning
- Digital-Agent
- Vision-Language
one_liner: 提出以SVG为中间媒介的SVGLM框架，打通VLM文本推理与图像生成链路，提升多模态推理可解释性
practical_value: '- 可参考SVG作为多模态中间表示的思路，替换电商商品图、营销图表的像素级表示，降低多模态推荐/推理的存储与计算开销，同时提升可解释性

  - 可复用「文本-结构化图形描述-渲染」的范式，搭建电商Agent的自动作图、商品可视化讲解能力，支持直播脚本、商品详情页自动生成

  - 针对电商场景的图表/尺码表/说明书理解任务，可参考SVG微调VLM的范式，相比直接微调像素级VLM，数据标注成本更低、收敛速度更快'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM在视觉理解、文本推理上表现优异，但无法将图像自然嵌入推理链路，全模态模型依赖的栅格/隐式图像表示可解释性差，在数学图表、结构化报表等数字视觉场景推理表现受限。
### 方法
提出SVGLM框架，采用SVG矢量图作为文本与图像的统一中间表示，利用SVG兼具图像描述、可执行文本指令的双重属性，无需修改VLM架构即可为其赋予推理过程中生成图像的能力；配套开源大规模SVG图像编辑数据集，以及开源VLM的微调范式。
### 结果
在数学推理基准测试中，SVGLM的SVG生成准确率、多模态推理表现显著优于原生微调的同参数VLM，证明SVG可作为数字领域Agent打通文本思考与视觉表示的可靠媒介。
