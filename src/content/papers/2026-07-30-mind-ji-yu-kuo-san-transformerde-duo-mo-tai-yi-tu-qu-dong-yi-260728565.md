---
title: 'MIND: Multimodal Intent-Driven Network via Diffusion Transformers for Medical
  Image Fusion'
title_zh: MIND：基于扩散Transformer的多模态意图驱动医学图像融合网络
authors:
- Yunzhan Fu
- Xiangyu Shen
- Yifei Sun
- Yuhan Chen
- Jian Wu
- Hongxia Xu
affiliations:
- Zhejiang University
- Liangzhu Laboratory
- Hangzhou Institute of Technology, Xidian University
- Hangzhou Dianzi University
- Zhejiang Key Laboratory of Medical Imaging Artificial Intelligence
arxiv_id: '2607.28565'
url: https://arxiv.org/abs/2607.28565
pdf_url: https://arxiv.org/pdf/2607.28565
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 多模态医学图像融合 · 扩散Transformer
tags:
- Diffusion Transformers
- Multimodal Fusion
- Adapter
- Semantic Consistency
- Medical AI
one_liner: 提出融合诊断意图引导、多尺度隐层适配器的扩散Transformer医学图像融合框架
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有医学图像融合方法全局采用统一融合规则，缺乏对诊断意图、病理结构的深度理解；扩散Transformer（DiT）的1D序列打平操作会丢失2D空间连续性，图像输出与诊断意图解耦易产生语义偏移。
### 方法关键点
1. 调用BioMedGPT从源图像生成意图驱动的融合文本，用病理感知的诊断意图引导整个融合流程；
2. 设计多尺度Latent Adapter，在序列化前显式提取源图像多尺度特征，经严格维度对齐后注入DiT网络补充空间特征；
3. 新增医学语义一致性损失，锁定融合图像与融合文本的深层语义匹配关系，同时保证底层物理流形重建稳定性。
### 关键结果
在Harvard、BraTS、GFP三类公开数据集上融合质量优于现有SOTA方案，显著提升下游脑肿瘤分割任务精度，支持灵活的交互式融合。
