---
title: 'Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D
  Reconstruction'
title_zh: Scal3R：面向可扩展在线3D重建的高效多相对位姿查询学习
authors:
- Chin-Yang Lin
- Yang-Che Sun
- Cheng Sun
- Fu-En Yang
- Min-Hung Chen
- Yen-Yu Lin
- Wei-Chen Chiu
- Yu-Lun Liu
affiliations:
- National Yang Ming Chiao Tung University
- NVIDIA
arxiv_id: '2609.04201'
url: https://arxiv.org/abs/2609.04201
pdf_url: https://arxiv.org/pdf/2609.04201
published: '2026-09-02'
collected: '2026-09-06'
category: Other
direction: 在线3D重建 · 位姿估计优化
tags:
- 3D Reconstruction
- Pose Estimation
- Frozen Backbone
- Lightweight Fine-tuning
- Online Processing
one_liner: 通过冻结骨干+1%参数量轻量token做多参考位姿查询，大幅降低长序列3D重建漂移，单卡8小时收敛
practical_value: '- 冻结大模型骨干仅微调1%参数量的轻量可学习token、通过不对称注意力注入的微调trick，可直接迁移到推荐/广告系统LLM微调，大幅降低训练成本

  - 将全局预测拆分为多局部参考查询+后验全局优化的架构思路，可借鉴到长序列用户行为建模，解决长序列分布外推误差问题

  - 局部特征稳定仅全局预测头失效的解耦观察，可指导长序列推荐/广告系统的模块拆分设计，避免重复优化已收敛的局部特征模块'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有在线3D重建模型在长视频上表现极差，固定首帧为锚点回归全局位姿的方式迫使模型做训练分布外的外推，微小漂移累积放大为严重几何崩溃；同时观察到失效过程中逐帧深度输出稳定，骨干的局部几何能力完好，仅全局位姿头失效。
### 方法关键点
1. 重构问题为多参考帧相对位姿查询任务；2. 仅引入占参约1%的轻量可学习token，通过不对称注意力注入完全冻结的骨干，查询多个历史关键帧的相对位姿；3. 搭配带回环检测的在线位姿图优化模块抑制长程漂移。
### 关键结果
单GPU仅需8小时即可收敛；KITTI数据集上较在线基线平均ATE降低超60%，在Virtual KITTI、Sintel、TUM-Dynamic等6个数据集上达到SOTA。
