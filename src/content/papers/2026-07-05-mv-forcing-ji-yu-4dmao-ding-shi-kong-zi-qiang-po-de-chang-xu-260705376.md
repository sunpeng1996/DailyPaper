---
title: 'MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal
  Self-Forcing'
title_zh: MV-Forcing：基于4D锚定时空自强迫的长序列多视角视频生成
authors:
- Gal Fiebelman
- Hadar Averbuch-Elor
- Sagie Benaim
affiliations:
- The Hebrew University of Jerusalem
- Cornell University
arxiv_id: '2607.05376'
url: https://arxiv.org/abs/2607.05376
pdf_url: https://arxiv.org/pdf/2607.05376
published: '2026-07-05'
collected: '2026-07-08'
category: Other
direction: 多视角长视频生成 · 扩散模型优化
tags:
- Video Diffusion
- Multi-View Generation
- Autoregressive Generation
- 4D Reconstruction
- Knowledge Distillation
one_liner: 提出MV-Forcing框架，通过4D几何桥实现任意长度、视角数的几何一致多视角视频生成
practical_value: '- 电商商品3D展示/多视角宣传视频生成场景，可借鉴4D几何桥对齐思路，解决不同视角内容拼接的几何错位问题，降低内容制作成本

  - 长时序视频生成任务可复用训练阶段双视角槽全噪声初始化的joint denoising技巧，突破预训练模型固定时序窗口限制

  - 自回归生成类任务可借鉴时空自强迫蒸馏方法，有效缩小时序、多维度序列的训练-推理曝光偏差，提升长序列生成稳定性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频扩散模型仅支持长时序单视角自回归生成，或短序列多视角双向注意力生成，无法同时输出长时序、多视角几何一致的动态场景视频，无法满足VR、内容创作等场景需求。

### 方法关键点
1. 提出MV-Forcing框架，在单个扩散模型中融合时序与视角维度自回归能力，引入4D几何桥连接顺序生成的不同视角：基于已生成的源视角重建3D结构，渲染出目标视角几何先验，再由扩散模型细化为高质量视频。
2. 训练阶段采用双视角槽全噪声初始化的联合去噪机制，突破教师模型固定时序窗口限制，支持无界时长生成。
3. 采用带时空自强迫的分布匹配蒸馏方案，消弭时序、视角双维度自回归的训练-推理曝光偏差。

### 关键结果
在合成与真实数据集上验证，仅需单个少步学生模型，即可生成任意长度、任意视角数量的几何一致多视角动态场景视频
