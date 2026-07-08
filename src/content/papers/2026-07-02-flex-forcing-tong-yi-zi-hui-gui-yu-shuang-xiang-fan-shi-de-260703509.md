---
title: 'Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion
  Model'
title_zh: Flex-Forcing：统一自回归与双向范式的视频扩散模型
authors:
- Xinyin Ma
- Julius Berner
- Chao Liu
- Arash Vahdat
- Weili Nie
- Xinchao Wang
affiliations:
- National University of Singapore
- NVIDIA Research
arxiv_id: '2607.03509'
url: https://arxiv.org/abs/2607.03509
pdf_url: https://arxiv.org/pdf/2607.03509
published: '2026-07-02'
collected: '2026-07-08'
category: Multimodal
direction: 多模态生成 · 视频扩散统一范式优化
tags:
- Diffusion Model
- Video Generation
- Autoregressive Generation
- Bidirectional Diffusion
- Inference Optimization
one_liner: 提出基于灵活分块的训练推理框架，让视频扩散模型同时支持双向、自回归两种生成范式
practical_value: '- 电商短视频物料生成场景可借鉴分块调度思路，跨块做全局内容一致性规划，块内自回归生成提升推理速度，适配不同GPU资源部署

  - 直播流实时生成场景可复用无严格因果约束的任意时序生成能力，支持中途插帧、内容修改等动态需求

  - 生成式推荐的短视频物料生产管线可参考该范式平衡生成质量与latency，降低大规模物料生产的算力成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成方法推理范式僵化：双向扩散模型全局一致性、视觉保真度优但推理速度慢；自回归模型支持高效流式生成，但长视频一致性差、存在曝光偏差。
### 方法关键点
核心是Flex-Forcing统一训练推理框架，基于时间轴与去噪步联合定义灵活分块机制：
1. 可根据设备算力预算动态调整分块大小；
2. 跨块双向推理做全局结构规划，块内自回归生成实现细粒度快速合成；
3. 无严格因果约束，支持任意顺序、任意时间步的自回归生成。
### 关键结果
在多个视频生成基准上，相比固定推理调度的强基线，视频质量、长视频稳定性均更优；同NFE下VBench评分最高提升0.4+，GB200上FPS可达85左右，推理速度更快。
