---
title: A Spatiotemporal Semantic Importance-Guided Unified Compression and Editing
  Framework for AI-Generated Videos
title_zh: 时空语义重要性引导的AI生成视频统一压缩与编辑框架
authors:
- Xihua Sheng
- Dong Liu
- Chang Wen Chen
arxiv_id: '2610.05779'
url: https://arxiv.org/abs/2610.05779
pdf_url: https://arxiv.org/pdf/2610.05779
published: '2026-10-05'
collected: '2026-10-10'
category: Multimodal
direction: 多模态生成 · AIGC视频压缩与编辑
tags:
- AIGC Video
- Video Compression
- Semantic Guidance
- Prompt Editing
- Generative Prior
one_liner: 引入冻结生成先验，设计三种时空语义引导技术，实现AIGC视频高效压缩与保结构prompt编辑
practical_value: '- 针对电商AIGC营销视频的存储传输场景，可复用「优先保留时空语义结构、丢弃可再生随机纹理」的压缩思路，大幅降低存储带宽成本

  - 可借鉴统一压缩+编辑的架构，压缩后的AIGC视频直接支持基于prompt的结构保留式编辑，无需保留原始生成文件，适合电商视频快速改款、物料迭代的需求

  - 帧自适应比特分配策略可迁移到短视频推荐的码率自适应场景，给语义更重要的帧（如商品特写帧）分配更高带宽，提升用户观看体验'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
AIGC视频的体量、时长、分辨率快速增长，存储传输压力陡增；传统视频压缩逐像素还原的目标浪费带宽，同时AIGC视频存在保时空语义的prompt编辑需求。
### 方法关键点
1. 引入冻结的预训练视频生成器作为可复用生成先验，构建压缩、编辑统一框架
2. 基于时空语义重要性做创新点选择，优先传输语义不变量，丢弃可再生的随机纹理噪声
3. 采用帧自适应比特分配，给语义保留需求更高的帧分配更多传输资源
4. 可调侧信息权重，同一压缩表示既支持高保真重建，也可作为语义锚实现保结构prompt编辑
### 关键结果
在多个主流视频生成模型的输出上测试，码率-感知效果优于传统、神经、生成式视频编码方案，同时支持同码流下的保结构prompt编辑
