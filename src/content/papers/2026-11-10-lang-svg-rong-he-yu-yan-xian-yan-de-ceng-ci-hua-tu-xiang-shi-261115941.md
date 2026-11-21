---
title: 'Lang-SVG: Hierarchical Image Vectorization with Language Priors'
title_zh: Lang-SVG：融合语言先验的层次化图像矢量化方法
authors:
- Xi Liu
- Chaoyi Zhou
- Run Wang
- Jiaang Li
- Feng Luo
- Junxiang Huang
- Siyu Huang
affiliations:
- Clemson University
- University of Copenhagen
- eBay
arxiv_id: '2611.15941'
url: https://arxiv.org/abs/2611.15941
pdf_url: https://arxiv.org/pdf/2611.15941
published: '2026-11-10'
collected: '2026-11-21'
category: Multimodal
direction: 多模态大模型 · 结构化SVG生成
tags:
- Multimodal LLM
- Image Vectorization
- SVG Generation
- Tree Structure
- Semantic Segmentation
one_liner: 提出融合语言先验的树形结构SVG矢量化方案，同时实现SOTA渲染保真度与语义层级可编辑性
practical_value: '- 电商场景可复用语义分层树结构，将商品图转换为带语义标签的SVG，大幅降低素材编辑、个性化素材生成的成本

  - 可借鉴「深度自适应简化+树引导剪枝合并+缺失区域补全」的Pipeline，优化多模态输入的结构化表示冗余问题

  - 可复用结构化语义对齐的评估思路，替代纯像素级指标，更合理衡量多模态生成内容的业务可用性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像矢量化方法仅优化像素级渲染保真度，输出SVG不符合人类感知的对象-部件层级结构，可编辑性差，且缺乏面向结构化质量的统一评估标准。
### 方法关键点
1. 设计带语义标签与父子依赖的显式树形结构组织SVG基元，引入粒度可控的开放词汇分割先验初始化对象-部件层级，调用MLLM结合SVG树上下文为未标注节点分配语义标签；
2. 采用深度自适应简化降低形状复杂度，通过树引导的剪枝合并消除冗余SVG节点，新增L1-SAM-Prompting补全缺失区域，兼顾结构精简与重建保真度；
3. 提出同时衡量结构质量、语义部件对齐度的新型评估协议。
### 关键结果
在渲染保真度、结构质量两个核心维度均达到SOTA性能。
