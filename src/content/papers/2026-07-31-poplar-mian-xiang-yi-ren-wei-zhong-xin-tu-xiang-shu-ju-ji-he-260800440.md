---
title: 'Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis'
title_zh: Poplar：面向以人为中心图像数据集合成的可扩展流水线
authors:
- Zhishan Zou
affiliations:
- Beijing University of Posts and Telecommunications
arxiv_id: '2608.00440'
url: https://arxiv.org/abs/2608.00440
pdf_url: https://arxiv.org/pdf/2608.00440
published: '2026-07-31'
collected: '2026-08-05'
category: Multimodal
direction: 多模态数据集合成 · 生成式数据构建
tags:
- Multimodal Dataset
- Image Generation
- Data Synthesis
- Diffusion Pipeline
- Quality Control
one_liner: 提出Specify-Render-Inspect可复现流水线，实现高质量可控的以人为中心图像数据集规模化合成
practical_value: '- 电商模特/商品图规模化生成场景可复用三段式Pipeline：先按常识约束采样属性生成摄影风格prompt，再适配写实生成模型自动重试故障结果，最后用多模态大模型做质检筛除错漏，大幅降本提效

  - 构建生成式训练数据集时，可参考结构化属性约束逻辑，避免生成不合理属性组合，同时保留可审计的生成与质检记录，满足业务合规要求

  - 生成商详图/营销素材时，可引入构图感知的aspect ratio适配策略，自动匹配不同电商场景的素材尺寸要求，减少人工裁切成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像生成模型可生成高质量单张人像，但规模化生成可用的以人为中心数据集存在多个痛点：需覆盖多元人物与场景、避免不合理属性组合、保留日常摄影质感，且要实现可追溯的规模化质量管控。
### 方法关键点
1. **Specify阶段**：在常识约束下采样结构化属性，转译为面向摄影场景的生成prompt
2. **Render阶段**：调用适配写实风格的图像生成器，适配构图感知的宽高比，自动重试存在明显技术故障的生成结果
3. **Inspect阶段**：用单轮结构化多模态审核校验候选样本，保留原prompt的同时剔除图像固有缺陷、与prompt不匹配的样本
### 关键结果
基于该流水线生成的Poplar-9K数据集包含9401条经过校验的人-图文对，候选样本审核通过率达79.9%，同时开源流水线、配置、生成prompt与可审计质检记录，支持定制化人像数据集构建
