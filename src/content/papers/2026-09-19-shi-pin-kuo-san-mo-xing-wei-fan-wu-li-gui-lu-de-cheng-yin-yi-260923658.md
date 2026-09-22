---
title: Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention
  Mechanisms
title_zh: 视频扩散模型违反物理规律的成因：注意力机制缺陷解析
authors:
- Yueyan Li
- Haibo Wang
- Caixia Yuan
- Xiaojie Wang
affiliations:
- Beijing University of Posts and Telecommunications
arxiv_id: '2609.23658'
url: https://arxiv.org/abs/2609.23658
pdf_url: https://arxiv.org/pdf/2609.23658
published: '2026-09-19'
collected: '2026-09-22'
category: Multimodal
direction: 多模态生成 · 视频扩散模型优化
tags:
- Video Diffusion
- Attention Mechanism
- RoPE
- Interpretability
- Motion Generation
one_liner: 定位RoPE导致的注意力衰减为视频扩散物理失准根因，给出分降噪步缩放RoPE频率的轻量优化方案
practical_value: '- 电商短视频素材生成业务可直接复用分降噪步调整RoPE频率的trick，无需额外训练即可降低生成视频的违和/物理违规占比

  - 时序多模态推荐/内容生成场景可参考注意力头归因方法，快速定位模型生成缺陷根因，避免盲目做数据增广

  - Agent虚拟直播/世界模拟场景可借鉴RoPE动态优化思路，提升长时序动态内容的物理一致性，减少穿模等异常问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前SOTA视频扩散模型视觉生成质量优异，但常输出违反真实物理规律的内容，现有优化方案依赖外部物理先验、提示改写或特殊数据集，无法从模型内部机制层面解决根因。
### 方法关键点
1. 首次针对文生视频扩散模型的运动规划过程开展可解释性研究，发现早期降噪阶段已完成运动轨迹生成，符合「先形状、后细节」的生成规律；
2. 定位核心缺陷：RoPE会引发过度空间注意力衰减，导致早期候选区域过早锁定物理不合理位置，压制邻帧合理运动轨迹；
3. 对应轻量架构修改方案为：不同降噪步动态缩放RoPE频率，降低过度注意力衰减，帮助模型探索更合理的候选区域，构建连贯物理运动。
### 关键结果
无需训练和带训练的两类实验均验证，该方案可有效提升生成视频的物理常识符合度。
