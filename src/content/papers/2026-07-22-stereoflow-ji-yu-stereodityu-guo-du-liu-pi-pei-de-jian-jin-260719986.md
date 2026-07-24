---
title: 'STEREOFLOW: Progressive Stereo Matching with StereoDiT and Transition Flow
  Matching'
title_zh: STEREOFLOW：基于StereoDiT与过渡流匹配的渐进式立体匹配
authors:
- Hao Wang
- Haoran Geng
- Xiaotong Yang
- Jing Tang
- Songlin Wei
- Linlong Lang
- Yeying Jin
- Zheng Zhu
- Zhaoxin Fan
- Biao Leng
affiliations:
- Beihang University
arxiv_id: '2607.19986'
url: https://arxiv.org/abs/2607.19986
pdf_url: https://arxiv.org/pdf/2607.19986
published: '2026-07-22'
collected: '2026-07-24'
category: Other
direction: 3D视觉 · 生成式立体匹配
tags:
- Stereo Matching
- Diffusion Transformer
- Flow Matching
- Zero-shot Generalization
- 3D Reconstruction
one_liner: 提出融合确定性回归与生成式建模的立体匹配框架，多基准达SOTA
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有立体匹配范式将任务建模为确定性回归问题，把多模态分布建模压缩为单点估计，存在回归均值偏差，在模糊区域匹配表现较差。
### 方法关键点
1. 提出先验引导的生成式框架，融合确定性匹配回归与生成式分布建模，实现二者能力互补
2. 核心包含3个组件：双阶段渐进级联匹配网络生成多分辨率互补匹配条件；采用频率解耦架构的像素Diffusion Transformer（StereoDiT）建模对应歧义；设计少步过渡流匹配目标实现高效优化
### 关键结果
在病态区域、不连续区域及零样本泛化场景下具备强几何一致性与丰富细粒度细节，在Scene Flow、KITTI、ETH3D、Middlebury多个基准上取得SOTA结果
