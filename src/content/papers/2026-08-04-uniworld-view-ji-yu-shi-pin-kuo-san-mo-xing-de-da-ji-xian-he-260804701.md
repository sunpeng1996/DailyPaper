---
title: 'UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models'
title_zh: UniWorld-View：基于视频扩散模型的大基线视角合成
authors:
- Haiyang Zhou
- Wangbo Yu
- Chaoran Feng
- Xunyu Zhou
- Yonghong Tian
- Li Yuan
affiliations:
- Peking University
- Rabbitpre AI
arxiv_id: '2608.04701'
url: https://arxiv.org/abs/2608.04701
pdf_url: https://arxiv.org/pdf/2608.04701
published: '2026-08-04'
collected: '2026-08-07'
category: Multimodal
direction: 多模态3D内容生成·视角合成
tags:
- Diffusion Model
- View Synthesis
- 3D Reconstruction
- 3D Gaussian Splatting
- NeRF
one_liner: 结合遮挡感知3D引导与视频扩散，实现单目输入下可控大基线新视角合成
practical_value: '- 电商3D商品素材生产：可复用遮挡感知点云渲染策略，仅需少量商品实拍图即可生成多视角高清素材，大幅降低3D建模成本

  - AR/VR导购场景：依托大基线视角合成能力，实现用户大角度移动时虚拟商品的几何一致性渲染，提升交互真实感

  - 直播内容运营：可基于单路直播流快速生成多机位视角内容，丰富用户观看选择，提升停留时长'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
社交媒体上单目视频/图像资源存量大，是沉浸式内容创作的核心素材，但稀疏输入下生成具备精确相机控制、几何一致的真实感新视角仍存在较大瓶颈：传统NeRF、3DGS等重建类方法在稀疏输入下效果严重退化，无法显式处理遮挡；生成式方法数据要求低，但几何引导不准/隐式，大基线视角合成效果差。
### 方法关键点
1. 统一框架UniWorld-View融合显式3D引导与生成式扩散建模，兼顾可控性与生成质量
2. 采用遮挡感知点云渲染策略，解决可见性歧义，为扩散合成提供准确几何先验
3. 耦合视频扩散主干，支持单目输入下的大基线新视角生成，还可输出多视角视频供下游动态3DGS重建
### 关键结果
在WorldScore基准、零样本NVS基准上，可控性、几何一致性、视觉保真度均显著优于现有方案。
