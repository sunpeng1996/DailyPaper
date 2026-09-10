---
title: 'Beyond Surface Imitation: Contrastive Modeling for Reasoning Path Alignment
  in Multimodal In-Context Learning'
title_zh: 多模态上下文学习中基于对比建模的推理路径对齐方法
authors:
- Mingbo Yang
- Wenqiang Wang
- Zhaolu Kang
- Peng Chen
- Yannan Chen
- Sunshang Wang
- Yan Xiao
affiliations:
- 中山大学
- 北京大学
- 鹏城实验室
- 天津科技大学
arxiv_id: '2609.10177'
url: https://arxiv.org/abs/2609.10177
pdf_url: https://arxiv.org/pdf/2609.10177
published: '2026-09-09'
collected: '2026-09-10'
category: Multimodal
direction: 多模态ICL · 推理路径对齐
tags:
- Multimodal-ICL
- Contrastive-Learning
- Reasoning-Path-Alignment
- MLLM
- Self-Refinement
one_liner: 提出COMIL多模态ICL框架，通过对比演示建模与推理路径对齐缓解表层模仿问题
practical_value: '- 可迁移到多模态商品理解、图文客服Agent场景，通过构造<次优回复/最优回复/修正推理路径>的对比样例库，提升MLLM的任务输出准确率

  - 响应条件检索的设计可以复用在RAG召回环节，除了输入相似度外额外增加当前生成结果与样例库次优回复的相似度匹配，召回更相关的修正指导

  - 轻量对齐控制器的设计可复用到生成式推荐、多模态内容审核等场景，用小成本的质量预测模型实现生成迭代的早停，平衡效果和latency

  - 对比样例库仅需300条左右样本即可达到接近最优效果，无需大规模标注，适合业务快速迭代场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模态ICL方法大多依赖对演示样例的表层特征模仿，无法对齐任务所需的推理路径，在需要细粒度跨模态证据匹配的复杂任务上性能瓶颈明显；常规正向演示仅给出目标输出，未提供从错误到正确的推理过程指导，无法修正模型的错误推理逻辑。

### 方法关键点
- 对比演示建模：将每条样例重构为<多模态输入、次优回复、最优回复、推理路径>四元组，明确告知模型次优回复的缺陷、修正所需的跨模态证据、修正逻辑
- 响应条件检索：迭代修正环节除了匹配输入相似度，额外增加当前生成回复与样例库次优回复的相似度权重，召回与当前错误模式更匹配的演示样例
- 轻量对齐控制器：用冻结的CLIP+BERT+三层MLP训练质量预测模型，预测当前生成结果的质量，实现迭代早停，避免无效修正

### 关键结果
在4个主流MLLM（Gemma-3-27B、InternVL3.5-14B、Qwen3.5-9B/4B）、4类多模态任务上测试：CIFAR10分类最高准确率98.4%，Flickr30k图文生成最高CIDEr 0.587，VQAv2问答最高准确率81.9%，16组实验中13组取得SOTA；比Self-Refine baseline latency降低29.2%，token消耗降低82.7%。

### 核心结论
对于需要推理的多模态任务，对比演示的效果远好于仅提供正向目标输出的常规ICL方法。
