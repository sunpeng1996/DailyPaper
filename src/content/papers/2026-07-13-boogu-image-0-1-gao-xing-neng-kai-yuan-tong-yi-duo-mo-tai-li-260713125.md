---
title: 'Boogu-Image-0.1: Boosting Open-Source Unified Multimodal Understanding and
  Generation'
title_zh: Boogu-Image-0.1：高性能开源统一多模态理解与生成模型家族
authors:
- Guoxuan Chen
- Chufeng Xiao
- Haoran Yang
- Siyue Xie
- Binxiao Huang
- Ming Zhang
- Cheuk Him Chau
- Xinyu Fu
- Yingzhao Lian
- Tom S. Y. Li
affiliations:
- Boogu Team
arxiv_id: '2607.13125'
url: https://arxiv.org/abs/2607.13125
pdf_url: https://arxiv.org/pdf/2607.13125
published: '2026-07-13'
collected: '2026-07-16'
category: Multimodal
direction: 多模态大模型 · 图文生成与编辑
tags:
- Multimodal-LLM
- Text-to-Image
- Image-Editing
- Open-Source-Model
- Bilingual-Multimodal
one_liner: 推出4款变体的开源统一多模态模型，低训练成本下实现接近闭源系统的生成编辑性能
practical_value: '- 电商商品图生成、AI修图场景可直接调用Boogu-Image开源模型，替代部分闭源多模态API降低成本，其自带的中英双语渲染能力可直接适配跨境电商素材需求

  - 低算力预算下优化多模态模型可复用其核心思路：针对性优化模型理解能力、提升训练数据质量、优化训练pipeline，搭配推理端Agent scaling即可大幅提升效果

  - 多模态推荐、广告素材生成场景可根据时延要求选择对应变体（Turbo/Edit等），灵活平衡推理速度与生成质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
头部闭源多模态图文生成系统依赖系统级集成实现高性能，技术细节未公开，现有开源模型性能差距较大，且高训练成本阻碍中小团队落地。

### 方法关键点
推出含Base、Turbo、Edit、Edit-Turbo 4个变体的Boogu-Image-0.1模型家族，从模型理解能力、训练数据质量、训练pipeline三个维度做针对性优化，搭配推理端Agent scaling策略，在极低计算预算下提升生成与编辑性能。

### 关键结果
仅用208.62百万张独特图像训练，基础模型训练成本仅约40万美元；在Boogu Arena评测中ELO得分达1087，优于所有同期开源多模态生成模型，效果接近GPT-Image-2、Nano-Banana-Pro等头部闭源系统，同时支持中英双语文本渲染、指令驱动图像编辑、低延迟推理等能力，全系列代码权重已开源。
