---
title: Visual Access Boundaries in Vision-Language Model Reasoning
title_zh: 多模态大模型推理中的视觉访问边界研究
authors:
- Hiroto Osaka
- Shohei Taniguchi
- Gouki Minegishi
- Kai Yamashita
- Masahiro Suzuki
- Yutaka Matsuo
arxiv_id: '2607.12815'
url: https://arxiv.org/abs/2607.12815
pdf_url: https://arxiv.org/pdf/2607.12815
published: '2026-07-14'
collected: '2026-07-15'
category: Reasoning
direction: 多模态大模型 · 推理机制研究
tags:
- VLM
- Chain-of-Thought
- Causal Intervention
- Visual Access Boundary
- Multimodal Reasoning
one_liner: 通过因果干预方法揭示VLM的CoT推理增益主要来自语言侧计算而非持续访问图像token
practical_value: '- 多模态商品理解/内容推荐场景的VLM推理可按VAB截断图像注意力访问，无需全程保留图像token注意力，有效降低KV cache占用、缩短推理时延

  - 多模态Agent执行商品属性识别、SKU计数等视觉任务时，优先优化前置视觉属性读出模块的准确率，比盲目增加CoT推理长度的收益更高

  - 对难识别的细粒度商品属性，可先通过线性探针从VLM隐层提取特征做预识别，再将结果作为文本输入CoT链路，可显著提升复杂属性判断、计数类任务准确率'
score: 8
source: arxiv-cs.AI
depth: abstract
---

### 动机
CoT prompting已广泛用于VLM推理性能提升，但长推理链的增益来源不明确，无法确定是来自全程持续访问图像token，还是依赖前向传播早期已提取的视觉信息。
### 方法关键点
提出Visual Access Sweep因果干预方法，按层深度和生成时序掩码生成token对图像token的注意力，定义Visual Access Boundary（VAB）为保留任务准确率的最小图像访问区域，在Qwen2.5-VL、InternVL3共6种模型配置上开展对比实验。
### 关键结果数字
1. 无论是否使用CoT，所有测试模型均存在有限VAB；CoT与无CoT的VAB层差异最多不超过2层，即使CoT生成长度远高于直接回答
2. CoT性能增益核心来自对已提取视觉隐状态的语言侧计算，而非全程访问图像token
3. 当视觉属性读出准确率低于60%时CoT无显著增益，输入真值属性文本后，CoT可将计数类任务准确率提升37%以上
