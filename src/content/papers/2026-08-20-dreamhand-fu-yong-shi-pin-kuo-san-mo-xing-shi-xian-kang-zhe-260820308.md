---
title: 'DreamHand: Repurposing Video Diffusion Models for Occlusion-Robust Egocentric
  3D Hand Motion Recovery'
title_zh: DreamHand：复用视频扩散模型实现抗遮挡第一视角3D手部运动恢复
authors:
- Yufei Liu
- Xixi Wang
- Hao Li
- Ganlong Zhao
- Kaitong Cai
- Chengkai Jin
- Chunxiao Liu
- Jianbo Liu
- Siyuan Huang
- Xingang Pan
affiliations:
- Shanghai Jiao Tong University
- Nanyang Technological University
- The Chinese University of Hong Kong
- ACE Robotics
arxiv_id: '2608.20308'
url: https://arxiv.org/abs/2608.20308
pdf_url: https://arxiv.org/pdf/2608.20308
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 第一视角3D手部运动恢复·扩散模型复用
tags:
- Video Diffusion Model
- Egocentric Vision
- 3D Motion Recovery
- Occlusion Robustness
- Embodied AI
one_liner: 将视频扩散模型改造为确定性几何编码器，实现抗遮挡抗出框的第一视角3D手部运动恢复
practical_value: '- 预训练扩散模型改确定性特征编码器的思路，可复用在多模态推荐的用户行为断档、商品属性缺失等缺失信息补全场景

  - 双向时空解码器的连续序列补全方法，可迁移到推荐系统用户长短期行为序列建模，提升行为断档场景预测准确率

  - 无额外依赖的轻量化部署思路，可参考用于端侧AR/VR电商交互场景的用户手势识别模块优化'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
第一视角视频是具身AI的海量操作数据来源，但严重物体遮挡、手部频繁出框导致度量级3D手部轨迹恢复难度高；现有单帧/窗口时序回归器在手出框时失效，现有视频扩散模型作为像素渲染器需多步采样、计算开销大。
### 方法关键点
1. 将视频扩散模型（VDM）改造为确定性几何编码器，仅需1次前向传播即可从干净潜变量中推理出遮挡、出框区域的手部信息
2. 离线clip级框架DreamHand，含确定性干净潜编码器提取特征、双向时空解码器解码连续双手轨迹，无需外部检测器
3. 新增基于光线的相机求解器配置，测试时无需输入相机内参
### 关键结果
在5个第一视角基准数据集上达到SOTA：重遮挡数据集ARCTIC上MPJPE-p降低30%，HOT3D上降低40%；包含出框手部的评估场景下收益达46%-61%
