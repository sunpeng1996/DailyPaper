---
title: 'L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory'
title_zh: L3G-World：基于隐式3D高斯记忆的实时无限世界生成
authors:
- Jinhyeok Choi
- JoungBin Lee
- Jongmin Lee
- Minkyeong Jeon
- Jiyoung Kim
- Kaeun Han
- Yoonjin Yoon
- Seungryong Kim
affiliations:
- KAIST AI
- Ewha Womans University
- KAIST Urban AI Institute
arxiv_id: '2610.40614'
url: https://arxiv.org/abs/2610.40614
pdf_url: https://arxiv.org/pdf/2610.40614
published: '2026-10-28'
collected: '2026-10-31'
category: Other
direction: 3D内容生成 · 隐式高斯记忆
tags:
- 3D_Gaussian
- Diffusion_Transformer
- Memory_Efficient
- Real_Time_Generation
- Scene_Representation
one_liner: 提出基于隐式3D高斯记忆的L3G-World框架，实现高空间一致性的实时无限3D世界生成
practical_value: '- 可复用「记忆随场景范围而非序列长度增长」的设计思路，优化推荐系统用户长期兴趣记忆模块，避免记忆无限制膨胀，降低存储开销

  - 隐空间直接渲染跳过VAE重编码的trick，可迁移到生成式推荐多模态内容生成链路，降低重复编码耗时，提升内容生成实时性

  - 增量记忆更新（新区域新增+旧区域优化）策略，可用于交互Agent的用户偏好动态更新，减少全量重训成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有交互世界生成方案依赖时序上下文或显式3D记忆，存在记忆随生成序列长度无限制膨胀、重编码RGB渲染结果耗时过高的问题，无法实现长时序实时生成且空间一致性差。
### 方法关键点
1. 提出隐式3D高斯记忆（L3G），每个高斯存储VAE隐特征，可直接渲染到DiT隐空间，跳过VAE重编码步骤；
2. 设计记忆更新器，仅在新观测区域生成高斯、已观测区域优化高斯，记忆规模随场景范围而非序列长度增长；
3. L3G-World采用记忆更新器+视频Diffusion Transformer交替自回归生成，保障生成内容的空间一致性。
### 关键结果
实现SOTA生成质量与长时序空间一致性，相比最优3D记忆基线：3D基元数量减少38.6×，记忆更新速度提升3.2×，记忆渲染速度提升359×，可实现9FPS实时世界生成。
