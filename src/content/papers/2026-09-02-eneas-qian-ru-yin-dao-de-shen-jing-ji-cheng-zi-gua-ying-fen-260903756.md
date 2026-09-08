---
title: 'ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation'
title_zh: ENEAS：嵌入引导的神经集成自适应分割方法
authors:
- Javier del Pino
- Salvador Rodríguez
- Alejandro Garabito
- Javier Álvarez
- Chema Garabito
affiliations:
- SperidLabs
arxiv_id: '2609.03756'
url: https://arxiv.org/abs/2609.03756
pdf_url: https://arxiv.org/pdf/2609.03756
published: '2026-09-02'
collected: '2026-09-08'
category: Multimodal
direction: 多模态语义分割 · 实例跟踪
tags:
- Segmentation
- Instance Tracking
- VLM
- Text Prompt
- Semantic Verification
one_liner: 提出文本可提示的自适应分割框架ENEAS，解决SAM3等模型的幻觉、碎片化与语义误分类问题
practical_value: '- 多模态内容理解场景（如电商商品识别、虚假素材过滤）可复用「快速嵌入匹配+模糊候选VLM推理」的分层架构，兼顾准确率与低延迟

  - 直播/短视频商品跟踪场景可借鉴带时序记忆的跟踪优化思路，避免目标短暂消失、局部特写时的识别漂移问题

  - 电商相似款区分、真假货/虚拟素材（如雕像、画与真实商品）辨别场景，可复用语义验证层设计过滤视觉相似但本体不同的干扰项'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本提示分割模型（包括SAM 3）存在三大痛点：目标离开视野时未上报缺失、极端特写时仅分割局部纹理、优先匹配视觉特征导致本体误分类（如雕像、倒影被识别为真实目标），在3D重建等对准确率要求极高的场景下，单个误分类就会导致资产失效。
### 方法关键点
1. 统一架构支持两大能力：单实例精准跟踪分割、文本查询驱动的开放概念实例发现
2. 跟踪模块：为仅支持点交互的SeC架构新增文本提示适配器，复用其时序记忆，解决目标短暂消失漂移、特写分割碎片化问题
3. 语义验证层：先通过高速视觉嵌入匹配过滤明确候选，仅对歧义候选调用VLM语义推理，兼顾低延迟与本体错误过滤
### 关键结果
在视频、无时空序数据集上实现高质量语义跟踪与分割，可准确区分视觉相似但本体不同的目标，代码与模型已开源。
