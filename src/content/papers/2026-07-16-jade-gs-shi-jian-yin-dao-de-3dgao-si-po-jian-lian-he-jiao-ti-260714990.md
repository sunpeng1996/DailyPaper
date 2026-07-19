---
title: 'JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting'
title_zh: JADE-GS：事件引导的3D高斯泼溅联合交替去模糊方法
authors:
- Haoyu Fu
- Jiafeng Huang
- Yuchen Wang
- Shengjie Zhao
affiliations:
- 上海大学机电工程与自动化学院
- 上海宝山尚大通用智能机器人研究院
- 同济大学计算机科学与技术学院
arxiv_id: '2607.14990'
url: https://arxiv.org/abs/2607.14990
pdf_url: https://arxiv.org/pdf/2607.14990
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 3D高斯泼溅 · 事件相机去模糊
tags:
- 3D Gaussian Splatting
- Event Camera
- Deblurring
- 3D Reconstruction
- Novel View Synthesis
one_liner: 提出事件引导的双向闭环去模糊框架，大幅提升运动模糊场景下3D高斯泼溅重建性能与训练效率
practical_value: '- 像素级自适应门控融合互补先验的思路可迁移至多模态搜推特征融合场景，比如用户行为特征与大模型生成语义特征的动态加权，避免单一特征偏差

  - 预处理器与下游任务双向闭环约束的架构可复用在Query改写/文案生成等前置模块和下游排序/召回的联合优化中，阻断预处理误差传导到核心链路

  - 低显存高效训练的参数分离、轻量化约束设计可参考，降低生成式搜推方案在消费级/边缘GPU上的部署门槛'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
快速移动拍摄产生的运动模糊会破坏3D重建所需的帧内运动信息，现有事件辅助去模糊方案存在两大痛点：物理事件积分先验保边缘但易漂移、学习网络先验复现纹理但边界扭曲，且单向流程会把事件噪声、2D伪标签偏差直接传导到3D几何重建结果。

### 方法关键点
1. 设计像素自适应路由门，动态融合物理先验与学习网络先验的互补优势；
2. 构建2D去模糊器与3D高斯泼溅模型的双向闭环训练架构，用多视角一致渲染结果、物理重模糊约束正则化去模糊器，将固定预处理器升级为几何感知预测器。

### 关键结果
在合成、真实两类基准数据集上LPIPS、CLIP-IQA指标领先，PSNR、SSIM性能极具竞争力；单消费级GPU仅需5GB显存、1小时即可完成训练，且保留实时渲染能力。
