---
title: 'LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame
  Interpolation with Video Diffusion Models'
title_zh: LongE2V：基于视频扩散模型的长时序事件视频重建、预测与插帧
authors:
- Cheng-De Fan
- Chun-Wei Tuan Mu
- Chen-Wei Chang
- Chin-Yang Lin
- Kun-Ru Wu
- Yu-Chee Tseng
- Yu-Lun Liu
affiliations:
- National Yang Ming Chiao Tung University, Taiwan
arxiv_id: '2607.08770'
url: https://arxiv.org/abs/2607.08770
pdf_url: https://arxiv.org/pdf/2607.08770
published: '2026-07-08'
collected: '2026-07-10'
category: Other
direction: 视频生成 · 事件流时序建模
tags:
- Video Diffusion
- Event-based Vision
- Video Reconstruction
- Frame Interpolation
- Autoregressive Generation
one_liner: 基于预训练视频扩散先验，解决事件流长视频生成时序漂移问题，三任务均达SOTA
practical_value: '- 自回归展开+自适应上下文切换缓解长序列漂移的思路，可迁移到对话式推荐长轮次交互、生成式推荐长序列内容生成的时序一致性优化

  - 交叉残差校正保证双向一致性的方法，可用于用户行为序列缺失值插补、多模态广告素材生成的时序对齐

  - 针对输入数据密度做自适应增强的策略，可适配多源异构用户行为/搜索query数据的预处理'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
从稀疏事件流恢复高质量视频存在两大痛点：回归方法生成结果纹理模糊，现有生成模型长时序稳定性差、易出现时序漂移，且暂无方案可同时覆盖重建、预测、插帧三类任务。
### 方法关键点
1. 基于预训练视频扩散先验微调，仅需少量数据即可获得优异感知质量
2. 引入Autoregressive Unrolling、Adaptive Context Switching缓解极长序列时序漂移
3. 提出带Cross Residual Correction的重编码对齐，保证插帧任务双向一致性
4. 新增Event Voxel Density Augmentation，适配不同传感器分辨率输入，提升鲁棒性
### 关键结果
在真实世界基准测试中，视频重建、预测、插帧三类任务均超越当前SOTA方法，时序一致性表现优异，同时具备零样本泛化能力
