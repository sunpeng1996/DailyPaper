---
title: 'ClearGS: Reliability-Aware Gaussian Splatting from Handheld Videos'
title_zh: ClearGS：面向手持视频的可靠性感知3D高斯溅射方法
authors:
- Xuanzhi Liu
- Xinyi Wu
- Hang Pan
- Wensi Huang
- Zhenyao Wu
- Ruize Han
- Song Wang
affiliations:
- Shenzhen University of Advanced Technology
- HONOR
- University of New South Wales
- Southern University of Science and Technology
arxiv_id: '2609.31509'
url: https://arxiv.org/abs/2609.31509
pdf_url: https://arxiv.org/pdf/2609.31509
published: '2026-09-25'
collected: '2026-09-28'
category: Other
direction: 3D场景重建 · 3D高斯溅射优化
tags:
- 3D Gaussian Splatting
- View Selection
- Video Restoration
- No-reference Supervision
- Novel View Synthesis
one_liner: 提出无需配对清晰监督的手持视频3DGS重建框架，多降质场景下性能达SOTA
practical_value: '- 电商商品3D重建场景可复用RVA分级权重分配逻辑替代二值帧筛选，避免有效几何信息丢失，提升手持拍摄素材的利用率

  - 无参考修复模块RIVR可直接迁移至UGC商品视频画质增强任务，无需配对清晰标注即可实现降质帧修复

  - 全轨迹修复巩固策略可借鉴到多帧序列特征融合任务中，避免早期有效细节被后续迭代覆盖'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有3D Gaussian Splatting (3DGS) 方法假设输入视角质量均匀，而手持视频存在视角覆盖不均、帧质量参差不齐问题，二值帧筛选逻辑过于粗糙，易丢失有效几何信息或引入降质伪影，传统修复依赖配对清晰监督数据，落地门槛高。
### 方法关键点
1. 提出Reliability-aware View Allocation (RVA) 模块，基于外观可靠性、降质风险、几何效用为每帧分配分级监督权重，弱激活被抑制的有效帧保障轨迹覆盖
2. 引入Render-Guided In-Video Restoration (RIVR) 模块，以当前3DGS渲染结果作为姿态对齐结构参考，调用冻结的无参考修复专家修复降质原始帧，通过无参考感知评分从渲染结果、修复帧、高频融合结果中选优
3. 加入全轨迹修复巩固机制，重访已采纳的修复结果，保留早期引入的有效细节
### 关键结果
在GS2E和GSOTM数据集上取得SOTA性能，多数降质场景下CLIP-IQA、MUSIQ指标一致提升，LPIPS指标下降，无需配对清晰监督或匹配的干净参考数据
