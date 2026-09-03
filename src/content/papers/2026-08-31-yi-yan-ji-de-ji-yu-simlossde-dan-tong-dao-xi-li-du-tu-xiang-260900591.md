---
title: 'A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss'
title_zh: 《一眼即得：基于SimLoss的单通道细粒度图像字幕生成方法》
authors:
- Suryaansh Jain
- Rahasya Barkur
- Vishal G
- Ryan Rossi
- Franck Dernoncourt
- Jack Wang
- Koustava Goswami
- Nedim Lipka
- Puneet Mathur
- Samyadeep Basu
affiliations:
- University of Massachusetts Amherst
- Adobe Research
arxiv_id: '2609.00591'
url: https://arxiv.org/abs/2609.00591
pdf_url: https://arxiv.org/pdf/2609.00591
published: '2026-08-31'
collected: '2026-09-03'
category: Multimodal
direction: 多模态 · 细粒度图像字幕生成优化
tags:
- Image Captioning
- Contrastive Loss
- Vision-Language Model
- InfoNCE
- Inference Optimization
one_liner: 提出无参考嵌入空间损失SimLoss，实现单通道细粒度图像字幕生成，推理速度超多阶段方案20倍
practical_value: '- 电商商品图自动生成属性/卖点文案场景可复用SimLoss思路，无需标注细粒度图文对，直接用冻结商品图像embedding做对比监督，大幅降低标注成本

  - 低 latency 要求的实时图文生成场景（如直播商品实时打标、搜索结果图实时摘要）优先选用SimLoss FFT方案，精度接近多阶段方案但速度快20倍

  - 若侧重细粒度属性召回（如商品材质、纹理、空间关系标签召回）可采用SimLoss GRPO的黑盒奖励优化思路，提升召回表现'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态模型生成的图像字幕多为粗粒度，易遗漏属性、数量、材质、空间关系等细粒度信息；多阶段细粒度字幕生成方案推理延迟极高，落地受限，且依赖人工细粒度标注或多阶段管道生成的伪标签，成本高。
### 方法关键点
提出无参考嵌入空间目标函数SimLoss，通过InfoNCE对比损失，训练阶段将VLM的隐层投影表示与冻结图像embedding对齐，在文本解码前提供密集视觉监督信号，无需人工标注细粒度字幕也无需多阶段伪标签；共两种实现变体：
1. 全微分微调的SimLoss FFT：支持反向传播穿过本地embedding模型
2. 奖励优化的SimLoss GRPO：将embedding模型作为黑盒奖励信号
### 关键结果
SimLoss FFT精度最高，F1得分接近多阶段方案，保持单通道推理，速度比多阶段管道快20倍；SimLoss GRPO取得最优召回率。
