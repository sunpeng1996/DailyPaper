---
title: 'AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards'
title_zh: AesCode：基于解耦跨模态奖励的审美代码生成框架
authors:
- Xin Gao
- Yifan Yang
- Xin Li
- Pan Wang
- Yan Li
- Muzhao Tian
- Mingxi Cheng
- Bei Liu
- Kai Qiu
- Qi Dai
affiliations:
- Microsoft
- Yale University
- Nanyang Technological University
- University of Pittsburgh
- Shanghai Jiao Tong University
arxiv_id: '2610.18860'
url: https://arxiv.org/abs/2610.18860
pdf_url: https://arxiv.org/pdf/2610.18860
published: '2026-10-12'
collected: '2026-10-14'
category: Multimodal
direction: 多模态代码生成 · 跨模态奖励设计
tags:
- Multimodal Code Generation
- Reinforcement Learning
- Reward Design
- VLM
- Design Graph
one_liner: 基于设计图和解耦跨模态奖励生成兼具内容正确性与视觉美感的可编辑可视化代码
practical_value: '- 多目标RL优化时可复用GDPO思路：不同维度奖励分别做通道归一化，避免稠密规则奖励淹没稀疏审美/体验类奖励，适合推荐系统兼顾转化、美观、合规等多目标调优

  - 评估复杂多维度输出（如商品海报、营销落地页）时，可借鉴Visual Graph Rubric思路：将整体审美拆解为绑定元素的二元Yes/No问题，自动评估结果和人类判断一致性可达93%，大幅降低人工评估成本

  - 做落地页/商品海报生成类Agent时，可引入生成图像作为审美先验，同时用规则校验强制内容正确性（如价格、活动文案不能错），平衡创意和信息准确性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前代码模型生成可视化网页/海报/仪表盘时，无法感知渲染后的视觉效果，布局和审美质量差；图像生成模型视觉效果好，但输出不可编辑、内容易出错（如文字、数据乱码），无法直接用于生产。现有图像转代码方案强制像素级复刻，会继承参考图的内容错误，也无法适配灵活的设计需求。

### 方法关键点
- 引入Design Graph作为中间表示，拆分元素的内容属性（如文本、数据）和视觉属性（如位置、颜色），显式定义元素间层级、对齐等关系，实现不同属性的可归因评估
- 设计解耦跨模态奖励：6个确定性校验器（执行、文本、边界、图表、语义布局、留白）从代码和渲染结果中自动校验可解析属性；Visual Graph Rubric（VGR）将审美要求拆解为绑定图元素的二元问题，用VLM判断，避免整体评分不稳定
- 用GDPO算法优化多目标奖励：每个奖励通道独立归一化后再聚合，避免稠密规则奖励淹没稀疏的审美奖励

### 关键实验
- 构建300样本的信息图生成benchmark，分别评估内容正确性和视觉质量，自动评分和人类判断一致性达93.3%
- 对比同参数Qwen3-VL基线，AesCode-8B、32B视觉质量分别提升31.1、22.4个百分点，整体效果比肩GPT-5.5、Claude Opus 4.8等闭源前沿模型，内容错误率更低
- 消融实验显示GDPO比普通GRPO提升5.12个视觉分，VGR比整体VLM评分提升6.89个视觉分

### 最值得记住的一句话
图像生成模型不仅可以作为内容输出工具，还可以作为结构化生成模型的可扩展视觉设计老师
