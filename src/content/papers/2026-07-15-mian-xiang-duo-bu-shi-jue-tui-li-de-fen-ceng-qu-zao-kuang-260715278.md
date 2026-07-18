---
title: Hierarchical Denoising For Multi-Step Visual Reasoning
title_zh: 面向多步视觉推理的分层去噪框架
authors:
- Zezhong Qian
- Xiaowei Chi
- Chak-Wing Mak
- Tianze Zhou
- Ruibin Yuan
- Yuhan Rui
- Hengzhe Sun
- Zhuoqun Wu
- Yuming Li
- Siyuan Qian
affiliations:
- 北京大学
- 香港科技大学
- 北京航空航天大学
- 福州大学
- Muka Robotics
arxiv_id: '2607.15278'
url: https://arxiv.org/abs/2607.15278
pdf_url: https://arxiv.org/pdf/2607.15278
published: '2026-07-15'
collected: '2026-07-18'
category: Reasoning
direction: 多步视觉推理 · 扩散模型生成优化
tags:
- Diffusion Model
- Visual Reasoning
- Hierarchical Latent
- Sparse Attention
- Streaming Generation
one_liner: 提出分层去噪HDR框架，兼顾多步视觉推理的逻辑一致性与低延迟流式输出
practical_value: '- 分层粗到精推理设计可迁移到多步Agent任务规划模块，先做全局粗路径规划再精细化落地，兼顾效率与准确性

  - 稀疏分层注意力SHAP可直接复用到长序列推荐/多轮对话推理场景，大幅降低长时序注意力计算开销

  - 小样本训练优化策略可借鉴到少标注数据的垂类推荐任务，仅用2%训练数据保留80%+性能的思路值得复用'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前视频生成两类范式均存在短板：流式自回归扩散效率高但推理能力弱，双向扩散支持全局修正但逐帧去噪推理延迟高，无法同时满足复杂多步视觉推理的逻辑一致性和低延迟要求。
### 方法关键点
提出HDR分层去噪框架，将视频隐变量组织为树状分层结构，先完成粗到细的全局推理再流式输出；粗去噪层保留多假设做全局规划，细去噪层逐步生成具体视觉状态；搭配稀疏分层注意力模式SHAP降低时序注意力成本。
### 关键结果
在6类多步推理任务上，对比流式自回归扩散基线，成功率从34.22提升至60.29（相对提升76.2%），平均进度从76.00提升至89.56；单隐变量推理延迟仅0.7秒，比双向扩散快54.2倍；仅用2%训练数据就能保留82.9%的全数据性能，远优于双向扩散的52.0%。
