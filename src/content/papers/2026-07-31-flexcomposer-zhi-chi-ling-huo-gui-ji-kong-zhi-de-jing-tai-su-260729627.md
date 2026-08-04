---
title: 'FlexComposer: Unified Video Compositing from Images to Dynamic Footage with
  Flexible Trajectory Control'
title_zh: FlexComposer：支持灵活轨迹控制的静态到动态素材统一视频合成
authors:
- Songchun Zhang
- Sitong Guo
- Xianghao Kong
- Pengwei Liu
- Yuwei Guo
- Lvmin Zhang
- Anyi Rao
affiliations:
- HKUST
- ZJU
- CUHK
- Stanford University
arxiv_id: '2607.29627'
url: https://arxiv.org/abs/2607.29627
pdf_url: https://arxiv.org/pdf/2607.29627
published: '2026-07-31'
collected: '2026-08-04'
category: Multimodal
direction: 多模态生成 · 可控视频合成
tags:
- Video Generation
- Trajectory Control
- Generative Compositing
- Latent Injection
- Multimodal Content
one_liner: 提出轨迹引导的统一视频合成框架，支持静态/动态前景无缝插入，兼顾动力学保留与精确轨迹控制
practical_value: '- 电商短视频/直播内容生成场景可复用「前景固有运动与全局位移解耦」的表征思路，将商品静态图/动态素材按自定义轨迹插入背景视频，无需额外3D建模即可降低内容生产成本

  - 可借鉴无参数Spatial-Aware Latent Injection机制，降低多模态生成任务中特征空间迁移的训练成本，适配不同类型素材的位置控制需求

  - 合成到真实的课程学习策略可复用在多模态内容生成的数据集构建流程，显著提升生成内容的光照、阴影与背景的一致性，优化真实感'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有生成式视频合成方案存在控制与保真度的权衡：要么静态图生成的运动幻觉无法保留预动画资产的固有动力学，要么无法支持自定义轨迹的细粒度空间控制，且普遍依赖显式3D重建或额外可学习适配器，部署成本高、灵活性差。
### 方法关键点
1. 设计统一规范前景表征，解耦对象固有运动与全局位移，将静态图、动态视频等异构输入标准化到稳定的居中隐空间
2. 提出空间感知隐式注入策略，利用VAE隐空间的平移等变性，通过无参数机制将规范特征迁移到用户指定的目标轨迹
3. 采用混合数据集+合成到真实的课程学习范式，联合程序模拟数据、真实电影素材、生成数据，隐式学习物理合理的光照与阴影一致性
### 关键结果
实验验证其在视觉质量、时序一致性、轨迹贴合度三个维度均全面超越SOTA方法，无需显式3D重建或额外适配器即可适配商品图、动态主体等多类输入。
