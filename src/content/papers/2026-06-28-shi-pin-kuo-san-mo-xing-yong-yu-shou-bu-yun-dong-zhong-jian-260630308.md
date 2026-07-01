---
title: The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction
title_zh: 视频扩散模型用于手部运动重建的惊人有效性
authors:
- Yuxi Wang
- Chengkai Jin
- Yufei Liu
- Wenqi Ouyang
- Tianyi Wei
- Zhiwei Zeng
- Siyuan Huang
- Zhiqi Shen
- Xingang Pan
affiliations:
- Nanyang Technological University
- Shanghai Jiao Tong University
arxiv_id: '2606.30308'
url: https://arxiv.org/abs/2606.30308
pdf_url: https://arxiv.org/pdf/2606.30308
published: '2026-06-28'
collected: '2026-07-01'
category: Other
direction: 具身AI · 4D手部运动重建
tags:
- Video Diffusion Model
- Hand Motion Reconstruction
- Egocentric Video
- Embodied AI
- 4D Pose Estimation
one_liner: 利用预训练视频扩散模型隐式先验，实现无检测器、抗遮挡的高精度4D手部运动重建
practical_value: '- 方法范式可迁移：利用大规模预训练生成模型的隐式通用先验解决下游任务标注稀缺问题，可复用至多模态生成式推荐、少样本广告文案生成等场景

  - 微调策略可借鉴：采用任务专属对齐目标微调大模型，同时保留预训练阶段习得的通用世界先验，平衡任务适配效果与泛化性能

  - 若业务涉及AR电商/具身导购：可直接复用该pipeline实现高精度手势交互识别，降低AR试穿、虚拟导购场景的交互开发成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有第一视角视频4D手部运动重建方案存在明显瓶颈：基于图像的pipeline重度依赖检测器，遮挡场景下极易失效；基于视频的方法仅能从稀缺的手部姿态标注中学习时序模块，单一信号不足以支撑运动动态建模、遮挡推理、人手交互能力学习，而大规模预训练视频生成模型恰好隐式习得了上述能力。
### 方法关键点
提出ViDiHand方案：1. 复用预训练视频扩散模型的表征能力做4D双手姿态重建；2. 设计手部叠加渲染目标微调模型，在保留通用世界先验的同时适配手部任务特征；3. 接入解码器从适配特征中恢复公制尺度姿态，全pipeline直接输入完整帧，无需检测器、补全模块或测试时优化。
### 关键结果
在ARCTIC、HOT3D、HOI4D三个行业基准数据集上，效果大幅超越此前SOTA方法。
