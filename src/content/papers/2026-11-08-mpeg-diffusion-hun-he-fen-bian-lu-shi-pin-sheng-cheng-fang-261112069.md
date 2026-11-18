---
title: 'MPEG-Diffusion: Mixed-Resolution Video Generation'
title_zh: MPEG-Diffusion：混合分辨率视频生成方法
authors:
- Dennis Menn
- Tianpei Gu
- Guande He
- Aryan V S
- Yanke Song
- Nan Liu
- Desai Xie
- Xun Huang
- Chenfeng Xu
- Diana Marculescu
affiliations:
- UT Austin
- Roblox
arxiv_id: '2611.12069'
url: https://arxiv.org/abs/2611.12069
pdf_url: https://arxiv.org/pdf/2611.12069
published: '2026-11-08'
collected: '2026-11-18'
category: Other
direction: 视频生成 · 混合分辨率推理加速
tags:
- Diffusion
- Video Generation
- Mixed Resolution
- DiT
- Inference Acceleration
one_liner: 提出混合分辨率视频生成框架，仅用30%全分辨率token实现4.8倍去噪加速，质量接近全分辨率
practical_value: '- 电商商品短视频、广告素材生成场景可复用混合分辨率思路：对用户关注的核心主体（如商品、人像）用高分辨率生成，背景等非核心区域用低分辨率，在不损失感知质量的前提下大幅降本提速

  - 大模型推理优化可借鉴双分辨率注意力设计：query仅读取同分辨率K/V，显著降低attention模块计算开销，适配低算力端侧部署需求

  - 生成式推荐的素材动态优化场景可复用自选择HR区域逻辑：基于模型内置知识自动识别核心内容区域，无需额外人工标注即可实现重点内容突出效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
视频扩散Transformer（DiT）生成质量高但计算开销随分辨率、时长指数增长，现有混合分辨率方案存在视频质量骤降、需提前指定高分辨率（HR）区域的缺陷，难以落地。
### 方法关键点
1. 双分辨率注意力：每个query仅读取同分辨率的K/V，缓解混合分辨率下的效果劣化问题；
2. 混合分辨率解码器：解码前融合HR与低分辨率（LR）隐变量，解决生成畸变；
3. 基于DiT内置知识自动识别视觉重要区域作为HR区域，无需提前标注输入。
### 关键结果
仅处理30%全分辨率token，在Wan2.1 14B上实现4.8倍去噪加速（1.3B版本为3.8倍），全指标优于现有混合分辨率方案；用户调研中90%以上对比样本被用户偏好，生成质量接近全分辨率效果。
