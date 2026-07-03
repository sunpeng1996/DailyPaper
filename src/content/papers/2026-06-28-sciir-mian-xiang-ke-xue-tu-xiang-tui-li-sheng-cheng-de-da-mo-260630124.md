---
title: 'SciIR: A Large-scale Training Dataset and Benchmark for Scientific Image Reasoning
  Generation'
title_zh: SciIR：面向科学图像推理生成的大规模数据集与基准
authors:
- Zhiyuan Ma
- Zhengfeng Shi
- Yuning An
- Peize Li
- Jiabao Wei
- Ruijie Li
- Junhao Xiao
- Jianjun Li
- Bowen Zhou
affiliations:
- Huazhong University of Science and Technology
- Shandong University
- Tsinghua University
arxiv_id: '2606.30124'
url: https://arxiv.org/abs/2606.30124
pdf_url: https://arxiv.org/pdf/2606.30124
published: '2026-06-28'
collected: '2026-07-03'
category: Multimodal
direction: 多模态科学图像生成 · 数据集与评估基准
tags:
- Multimodal
- Text-to-Image
- Dataset
- Benchmark
- Chain-of-Thought
one_liner: 构建8.2万条标注科学图文数据集与三层维度评估基准，提升科学图像生成推理能力
practical_value: '- 分层维度+细粒度checklist的评估方法可复用在电商商品图、营销素材等垂类生成内容的效果验收，解决生成内容逻辑/合规校验难问题

  - 基于符号学分层的思维链标注思路可迁移到垂类多模态生成任务的微调数据标注，提升垂类生成内容的语义对齐与逻辑一致性

  - 将结果导向评价转为过程导向细粒度问答的方案，可用于广告/商品生成素材的自动效果评测，大幅降低人工标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有Text-to-Image（T2I）模型生成写实视觉内容表现优异，但无法满足科学图像对严格语义对齐、逻辑推理的要求，同时科学图像生成领域存在训练数据稀缺、缺乏统一评估基准的痛点。
### 方法关键点
1. 基于皮尔斯符号三元组将科学推理划分为实体结构、科学过程、科学定律3个核心维度；
2. 构建包含8.2万+高质量科学领域图文对的SciIR-82k数据集，配套Scientific Reasoning Chain-of-Thought（Sci-RCoT）标注显式建模底层视觉逻辑；
3. 推出SciIR-Bench评估基准，采用原子检查清单将结果导向的科学准确率校验转换为过程导向、可验证的细粒度问答。
### 关键结果
基于SciIR-82k微调的Qwen-Image-SciIR模型在基准上得分从35%提升至43%，实验验证现有通用多模态模型的科学推理能力存在显著缺陷。
