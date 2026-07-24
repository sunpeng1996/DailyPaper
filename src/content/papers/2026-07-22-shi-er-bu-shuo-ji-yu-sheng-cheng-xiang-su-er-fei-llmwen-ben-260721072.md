---
title: 'Show, Don''t Tell: Evaluating Spatial Cognition in Generative Pixels Rather
  Than LLM Text'
title_zh: 「示而不说」：基于生成像素而非LLM文本的空间认知评估
authors:
- Xu Wang
- Kaixiang Yao
- Miao Pan
- Xiaohe Zhou
- Xuanyu Liu
- Wenqi Zhang
- Xuhong Zhang
affiliations:
- Zhejiang University
- OmniAI Group of ZJU ACES Lab
arxiv_id: '2607.21072'
url: https://arxiv.org/abs/2607.21072
pdf_url: https://arxiv.org/pdf/2607.21072
published: '2026-07-22'
collected: '2026-07-24'
category: Eval
direction: 多模态模型空间认知能力评估
tags:
- Spatial Cognition
- Evaluation Benchmark
- VLM
- Image Generation
- Agent
one_liner: 提出通用视觉评估框架ProVisE与空间认知基准SpatialGen-Bench，统一评估两类模型的空间认知能力
practical_value: '- 做电商多模态导购Agent、虚拟试搭/陈设空间生成类业务时，可复用ProVisE的协议化视觉输出解析逻辑，无需强制模型输出坐标文本，直接解析生成像素结果对齐业务指标，降低交互门槛

  - 搭建多模态模型能力评估体系时，可参考Agentic builder的思路，自动生成任务专属评估协议，快速适配不同业务评估场景（比如电商虚拟陈设效果评估）

  - 涉及家装布局推荐、线下店铺动线规划生成等空间类生成任务时，可优先用图像生成模型输出结果，组合推理环节叠加文本VLM，结合两类模型优势提效'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有空间推理基准要求输出坐标、选项或文本，和图像生成模型的像素输出接口不匹配，无法用同一任务语义对齐评估文本输出VLM和图像生成模型的空间认知能力。

### 方法关键点
1. 提出基准无关的ProVisE框架，引导图像生成模型输出协议约束的视觉答案，解析为兼容原有指标的结构化预测；自带Agentic builder可自动构建、验证新基准的任务专属协议。
2. 构建SpatialGen-Bench诊断基准，含470个样本，覆盖14个空间子任务、4个能力层级、多种答案形式。

### 关键结果
在6个外部空间基准验证了Agentic协议构建的有效性；图像生成模型在可直接像素输出的空间任务上表现具备竞争力，文本输出VLM在组合空间推理上优势明显。
