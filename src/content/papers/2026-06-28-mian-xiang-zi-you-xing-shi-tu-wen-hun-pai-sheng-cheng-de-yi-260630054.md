---
title: Illuminating Unified Multimodal Model for Free-form Interleaved Text-Image
  Generation
title_zh: 面向自由形式图文混排生成的统一多模态模型ILLUME-X
authors:
- Chonghuinan Wang
- Zhikai Chen
- Chunwei Wang
- Yecong Wan
- Junwei Yang
- Zhixin Wang
- Wei Zhang
- Jiaqi Xu
- Renjing Pei
- Xiaohe Wu
affiliations:
- Harbin Institute of Technology
- Huawei Noah's Ark Lab
- Zhengzhou Advanced Research Institute of Harbin Institute of Technology
- Nankai University
arxiv_id: '2606.30054'
url: https://arxiv.org/abs/2606.30054
pdf_url: https://arxiv.org/pdf/2606.30054
published: '2026-06-28'
collected: '2026-06-30'
category: Multimodal
direction: 多模态生成 · 自由形式图文混排
tags:
- Multimodal Generation
- Text-Image Interleaving
- Unified Model
- Training Strategy
- Evaluation Metric
one_liner: 提出统一多模态框架ILLUME-X及配套训练策略、评估指标，实现高质量自由形式图文混排生成
practical_value: '- 电商商品详情页、营销种草内容生成场景可复用ILLUME-X的图文混排生成逻辑，自动生成图文穿插的活动页、种草笔记内容

  - 针对不定长多模态token序列的渐进式自适应目标训练策略，可迁移至多模态生成式推荐模型训练，解决训练不稳定问题

  - 提出的ILScore评估指标可直接用于图文混排生成效果的自动化评测，替代部分人工标注降低评估成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态生成模型大多仅支持单模态生成或固定格式图文输出，无法自主生成自由形式的图文穿插序列，同时存在多模态训练数据效率低、训练过程不稳定、缺乏统一评估标准的痛点。

### 方法关键点
1. 优化面向图文混排生成的扩展训练数据流水线，大幅提升多模态数据利用效率；
2. 针对不定长多模态token序列设计带自适应目标的渐进式训练策略，有效稳定多模态训练过程；
3. 提出面向图文混排序列的客观综合评估指标ILScore，解决该任务效果难以量化评估的问题。

### 关键结果
在风格迁移、图像分解、故事生成等多个图文混排生成任务上，ILLUME-X性能全面优于此前的SOTA统一多模态模型
