---
title: 'HyperErase: Scale-Calibrated Hypernetwork for Multi-Concept Erasure in Text-to-Image
  Models'
title_zh: HyperErase：基于尺度校准超网络的文生图多概念擦除框架
authors:
- Yi Sun
- Xinhao Zhong
- Zhiqi Zhang
- Yimin Zhou
- Junhao Li
- Yuxia Qiao
affiliations:
- Harbin Institute of Technology, Shenzhen
- Tsinghua Shenzhen International Graduate School, Tsinghua University
- Jilin University
- Peng Cheng Laboratory
- South China University of Technology
arxiv_id: '2609.31154'
url: https://arxiv.org/abs/2609.31154
pdf_url: https://arxiv.org/pdf/2609.31154
published: '2026-09-25'
collected: '2026-09-28'
category: Multimodal
direction: 多模态安全 · 文生图概念擦除
tags:
- Hypernetwork
- LoRA
- Text-to-Image
- Concept Erasure
- Safety Alignment
one_liner: 用超网络生成prompt专属LoRA实现文生图无梯度多概念擦除，平衡擦除效果与生成质量
practical_value: '- 超网络动态生成prompt专属LoRA的思路可迁移到生成式推荐场景，无需为不同品类/场景预存多套LoRA，大幅降低存储与运维开销

  - LoRA的模式-尺度子空间解耦+平方根缩放trick可直接复用，解决多LoRA合并时的参数干扰、效果过溢问题，适配多目标生成需求

  - 无梯度动态参数适配的思路可用于电商Agent的用户指令响应场景，无需推理时微调即可快速适配不同用户的个性化生成需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文生图概念擦除方法依赖静态权重范式，生成的固定适配器难以适配多样prompt变体，扩展至多概念擦除时存在严重参数干扰，且需逐prompt梯度优化或手动合并LoRA，效率极低。

### 方法关键点
1. 将概念擦除重构为prompt条件的参数摊销任务，训练超网络直接将文本描述映射为对应prompt专属的LoRA更新，消除推理时梯度优化与手动LoRA合并的需求；
2. 提出解耦校正策略：将LoRA token拆分为模式、尺度两个子空间，通过平方根变换抑制乘性过缩放，推理阶段引入教师模型的规范先验做校正。

### 关键结果
跨主流概念类别实验显示，HyperErase在擦除有效性、图像质量、语义对齐三者的trade-off上表现更优，性能比肩单概念擦除的金标基线，且推理时单前向即可为任意prompt生成专属LoRA，无需梯度更新。
