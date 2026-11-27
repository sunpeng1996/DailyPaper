---
title: Hierarchical Semantic Learning for Multimodal Sentiment Analysis with Missing
  Modalities
title_zh: 面向模态缺失场景的多模态情感分析分层语义学习框架
authors:
- Chunlei Meng
- Rong Fu
- Zhan Chen
- Yi Liu
- Zhuo Zou
- LiDa Xu
- Chun Ouyang
- Zhongxue Gan
affiliations:
- 复旦大学
arxiv_id: '2611.34184'
url: https://arxiv.org/abs/2611.34184
pdf_url: https://arxiv.org/pdf/2611.34184
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态情感分析 · 模态缺失鲁棒性优化
tags:
- Multimodal Sentiment Analysis
- Hierarchical Semantic Learning
- Missing Modality
- Contrastive Learning
- Feature Reconstruction
one_liner: 提出分层语义学习HSL框架，解决多模态情感分析场景下模态缺失导致的性能劣化问题
practical_value: '- 电商多模态内容（图文/短视频/直播）情感识别场景，可复用分层语义解耦+跨模态跨层级重建思路，解决部分模态缺失（如直播无音频、商品图丢失）的特征鲁棒性问题

  - 多模态特征融合阶段可借鉴层级对比正则方法，约束不同层级特征语义一致性，降低特征重建的误差传播，提升下游召回/排序模型稳定性

  - 多模态用户评论/客服对话的情感分析场景，可直接复用HSL框架解决部分模态（如语音转写失败、表情包丢失）的识别准确率下降问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
真实场景多模态情感分析（MSA）常面临传感器故障、隐私掩码、传输不稳定导致的不可预测模态缺失问题，现有方法仅用单层扁平化编码器输出，忽略深度编码器的语义层级与模态内/间交互，易出现语义平均、映射病态问题，性能受限。
### 方法关键点
1. 分层语义解耦：从各模态编码器抽离低/中/高三个层级的特征流
2. 跨模态跨层级语义重建：以观测模态的高层语义为全局锚点，阶梯式重建缺失模态的中层结构与低层细节
3. 分层级联误差监督：用原型对比正则约束观测与重建特征的层级语义一致性，抑制误差传播
4. 分层交互融合：建模跨模态、跨语义层级的密集交互，输出鲁棒预测
### 关键结果
在CMU-MOSI、CMU-MOSEI、IEMOCAP、CH-SIMS四个公开数据集的各类模态缺失设置下，HSL性能在绝大多数场景超过现有基线。
