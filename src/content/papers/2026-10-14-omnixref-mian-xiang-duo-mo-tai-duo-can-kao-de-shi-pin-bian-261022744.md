---
title: 'OmniXRef: A Unified Framework for Multimodal Multi-Reference Video Editing'
title_zh: OmniXRef：面向多模态多参考的视频编辑统一框架
authors:
- Xiaoyan Cong
- Tianyu Wang
- Hyeonho Jeong
- Zhifei Zhang
- Yuqian Zhou
- Yijun Li
- Shaoteng Liu
- Zhe Lin
- Srinath Sridhar
- Soo Ye Kim
affiliations:
- Brown University
- Adobe Research
arxiv_id: '2610.22744'
url: https://arxiv.org/abs/2610.22744
pdf_url: https://arxiv.org/pdf/2610.22744
published: '2026-10-14'
collected: '2026-10-20'
category: Multimodal
direction: 多模态生成 · 视频编辑统一框架
tags:
- Multimodal Generation
- Video Editing
- Diffusion Transformer
- MLLM
- Benchmark
- Curriculum Learning
one_liner: 提出支持文本、图像、视频混合参考的视频编辑统一框架、配套数据集与评测基准
practical_value: '- 多模态混合参考的统一参考库接口+R²-RoPE设计，可迁移到电商商品营销视频定制场景，支持用户输入文本、参考图/视频的组合需求

  - 单流Diffusion Transformer交错处理源内容与MLLM多模态上下文的架构，可复用在生成式推荐的多模态内容生成模块

  - 合成数据集构建+Curriculum Learning逐步提复杂度的训练策略，可解决多模态生成类推荐任务训练数据稀缺的问题

  - 跨属性、跨模态的benchmark构建思路，可用于标准化评估生成式推荐的多模态产出效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频编辑方案仅支持单一模态参考输入，无法满足用户组合文本、参考图、参考视频表达创意的需求，同时缺乏多参考视频编辑的专用训练数据与标准化评测体系。
### 方法关键点
1. 设计带reference-bank接口的统一输入格式，引入R²-RoPE支持可变数量参考输入的泛化；
2. 采用单流diffusion transformer，交错处理源视频与MLLM输出的多模态上下文序列；
3. 构建OmniXRef-Data合成数据集，用curriculum learning逐步提升任务复杂度与训练分辨率；
4. 推出OmniXRef-Bench评测基准，覆盖相机、运动、内容、风格、VFX五大类视频属性迁移任务。
### 关键结果
在多模态多参考视频编辑任务上，效果全面优于特定任务基线模型与商用编辑工具。
