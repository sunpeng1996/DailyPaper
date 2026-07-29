---
title: 'UltraViT: Latency-Optimized On-device Vision Encoder for Large Vision-Language
  Models'
title_zh: UltraViT：面向大视觉语言模型的端侧延迟优化视觉编码器
authors:
- Ioannis Maniadis Metaxas
- Adrian Bulat
- Alberto Baldrati
- Anestis Zaganidis
- Yassine Ouali
- Hyeonuk Kim
- Georgios Tzimiropoulos
affiliations:
- Samsung AI Cambridge
- Technical University of Iasi
- Queen Mary University of London
arxiv_id: '2607.23373'
url: https://arxiv.org/abs/2607.23373
pdf_url: https://arxiv.org/pdf/2607.23373
published: '2026-07-24'
collected: '2026-07-29'
category: Multimodal
direction: 多模态大模型 · 端侧视觉编码器优化
tags:
- LVLM
- On-device Inference
- Vision Encoder
- Pre-training
- Multimodal Model
one_liner: 提出面向LVLM的端侧延迟优化视觉编码器UltraViT，搭配定制预训练策略，超基线且端侧速度提升1.7倍
practical_value: '- 端侧多模态Agent、实景搜商、端侧推荐等场景，可参考延迟感知的异构空间混合器金字塔架构，优化视觉编码器的端侧推理效率

  - 小体量视觉编码器预训练可复用两阶段策略：先蒸馏学习空间特征，再用冻结混合容量LVLM做生成式监督，比传统对比学习的多模态对齐效果更优

  - 端侧多模态商品理解、拍照搜同款等业务可尝试替换现有视觉编码器为UltraViT，在精度损失可控的前提下降低推理延迟'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LVLM端侧部署算力瓶颈显著，现有优化多聚焦视觉Token压缩、小语言模型侧，视觉编码器的端侧延迟优化长期被忽略，无专门针对LVLM的端侧定制视觉编码器方案。
### 方法关键点
1. 基于真实端侧延迟数据设计金字塔架构，在宏块层策略性集成适配异构空间混合器，平衡精度与推理速度；
2. 提出两阶段生成式预训练策略：先通过密集蒸馏获取丰富空间特征，再用冻结的容量混合LVLM提供直接生成式监督，相比传统对比学习、自监督学习更适配后续LVLM多模态对齐需求。
### 关键结果
在端侧LVLM编码任务上达到SOTA，效果显著优于现有编码器基线，端侧推理速度提升近1.7×
