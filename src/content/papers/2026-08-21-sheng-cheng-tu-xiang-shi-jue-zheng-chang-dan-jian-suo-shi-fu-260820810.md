---
title: 'When Generated Images Look Right and Retrieve Wrong: Coverage-Guided Cross-Scale
  Re-Indexing for Knowledge-Faithful Generative Perception'
title_zh: 生成图像视觉正常但检索失效：覆盖度引导跨尺度重索引实现知识保真生成感知
authors:
- Guangyuan Dong
- Chuang Liu
- Yangchen Zeng
- Haoyu Wang
- Xiaoyang Yu
- Pinlong Zhao
- Yuchao Hou
- Ziwei Li
- Zheng Lin
affiliations:
- National University of Singapore
- Wuhan University
- ByteDance
- Nankai University
- JD Research, JD.com, Inc.
arxiv_id: '2608.20810'
url: https://arxiv.org/abs/2608.20810
pdf_url: https://arxiv.org/pdf/2608.20810
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态生成 · 检索保真索引优化
tags:
- Multimodal Generation
- Image Retrieval
- Semantic Alignment
- Closed-loop System
- Generative Perception
one_liner: 提出闭环多模态索引框架CERES，解决生成图像因尺度概念丢失导致的检索失效问题
practical_value: '- 电商商品AIGC主图/短视频封面生成场景，可复用软Jaccard覆盖度损失约束生成内容保留商品核心属性（如颜色、款式、logo），避免生成图视觉效果好但无法被用户搜索query召回的问题

  - 多模态内容索引链路可引入生成后重校验闭环，用冻结VLM回检生成内容的概念覆盖率，降低语义崩塌风险

  - 多尺度目标生成（如商品细节图+场景图融合）可参考三级语义金字塔+共现感知路由架构，兼顾不同尺度语义概念保留'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前多模态系统中，语言引导生成的图像常因全局池化文本嵌入丢失不同尺度的特定概念，出现像素质量高但无法被目标query检索到的语义崩塌问题，无法满足生成内容回库可检索的业务需求。

### 方法关键点
提出CERES闭环多模态索引框架：1）构建三级语义金字塔，通过共现感知路由挖掘隐式概念；2）将尺度路由的交叉注意力注入轻量化U-Net生成器，用冻结VLM重索引生成图校验概念覆盖度；3）用可微软Jaccard覆盖度目标给0.39M小参数生成器回传梯度，额外用DINOv2线性探针独立验证覆盖度。

### 关键结果数字
4个全色锐化基准7种设置下达到SOTA，尺度差异最大场景Q2n相对提升4.64%、DOTA检测mAP提升9.7；概念查询检索Recall@5较最优基线提升14.0个点，图文MRR提升0.19。
