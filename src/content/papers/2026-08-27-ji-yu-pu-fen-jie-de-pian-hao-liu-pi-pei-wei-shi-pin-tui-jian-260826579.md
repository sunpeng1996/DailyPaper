---
title: Preference Flow Matching with Spectral Factorization for Micro-video Recommendation
title_zh: 基于谱分解的偏好流匹配微视频推荐框架PrismRec
authors:
- Xinxin Dong
- Haokai Ma
- Fei Hu
- YuZe Zheng
- Bin Wu
- Yonghui Yang
- Xiaodong Wang
affiliations:
- National University of Defense Technology
- National University of Singapore
- Zhengzhou University
arxiv_id: '2608.26579'
url: https://arxiv.org/abs/2608.26579
pdf_url: https://arxiv.org/pdf/2608.26579
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 微视频推荐 · 流匹配+频域特征分解
tags:
- Flow Matching
- Spectral Factorization
- Sequential Recommendation
- Micro-video Recommendation
- Multimodal Representation
one_liner: 提出融合谱语义分解与上下文校准流匹配的微视频推荐框架，性能较SOTA最高提升22.65%
practical_value: '- 短视频/微视频推荐场景可直接复用SSF模块，对帧级特征做时域FFT分解为静态语义、动态模态双因子，替代传统全局聚合的视频特征，提升内容信号区分度

  - 流匹配类推荐系统可参考CPM的结构化条件注入方式，将分解后的多模态特征作为独立条件引导生成轨迹，避免粗融合导致的信息损失

  - 高稀疏推荐场景（如新品/新视频冷启动）可集成本方法的内容驱动偏好建模逻辑到现有排序层，缓解交互稀疏问题，且推理延迟、内存占用优于现有生成式推荐方法'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有微视频推荐普遍将帧序列压缩为单一全局表示，混淆了共同决定用户偏好的静态视觉语义与动态时序模式；流匹配类推荐仅以粗粒度行为上下文作为生成条件，未利用视频内容的时序结构，内容仅作为辅助侧信息而非偏好生成的内在驱动，在交互稀疏场景下性能受限。

### 方法关键点
- 设计**Spectral Semantic Factorization (SSF)** 模块：对帧级表征做时域FFT变换，通过先验引导的可学习频率掩码分解出静态语义（低频）、动态时序（高频）双因子，再经分支独立精炼、不对称融合得到互补的内容表征
- 提出**Context-Calibrated Preference Matching (CPM)** 模块：基于用户历史交互序列计算对静态/动态内容的敏感度，加权融合双因子作为结构化条件，引导流匹配的偏好生成轨迹，将视频内容纳入偏好演化的内在驱动逻辑
- 端到端优化结合流匹配损失与排序损失，兼顾表征分布对齐与推荐判别性

### 关键实验
在MicroLens、Shortvideo共4个公开微视频数据集上，对比14个SOTA基线（含FMRec、IISAN-Versa等），所有16组数据集-指标对均最优，H@10最高提升22.65%，N@10最高提升22.14%；推理速度比最优基线快88%，峰值GPU内存低15%，对行为噪声、表征噪声的鲁棒性显著优于对比方法。

### 核心结论
将多模态内容做结构化分解再作为流匹配的引导条件，而非简单作为侧信息补充，能同时提升推荐性能、效率与鲁棒性，尤其适配交互稀疏的短视频/新内容推荐场景。
