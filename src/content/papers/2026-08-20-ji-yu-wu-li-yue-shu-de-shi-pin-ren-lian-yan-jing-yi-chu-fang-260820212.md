---
title: 'Unwarping the Lens: A Physics-Grounded Approach to Video Glasses Removal'
title_zh: 基于物理约束的视频人脸眼镜移除方法
authors:
- Radim Spetlik
- David Futschik
- Radek Danecek
- Feitong Tan
- Ziqian Bai
- Rohit Pandey
- Yinda Zhang
affiliations:
- Czech Technical University in Prague
- Google
arxiv_id: '2608.20212'
url: https://arxiv.org/abs/2608.20212
pdf_url: https://arxiv.org/pdf/2608.20212
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 人脸视频属性编辑 · 物理驱动生成
tags:
- Video Editing
- Image Inpainting
- Physically Grounded
- Generative Prior
- Temporal Consistency
one_liner: 结合物理光学仿真与结构约束的视频眼镜移除框架，实现高保真时序稳定的编辑效果
practical_value: '- 电商直播人脸美化、AR虚拟试戴场景可借鉴三阶段结构滤波约束，避免人脸ID漂移、表情姿态错位问题

  - 时序生成类任务可复用平移等变约束，提升视频帧间一致性，解决短视频生成、直播剪辑的帧跳变问题

  - 缺乏配对训练数据的垂类编辑任务，可参考「商用大模型生成+物理仿真构造配对数据」范式，降低标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
视频人脸去眼镜是面部属性编辑核心难点，眼镜的折射distortion、高光会遮挡面部几何，现有基于生成先验的静态修复方法缺乏结构约束，易出现ID漂移、动态序列时序一致性差等问题。
### 方法关键点
1. 调用商用生成模型生成高保真合成人脸，经三阶段结构滤波保留人脸ID、表情、姿态属性
2. 训练阶段引入透镜光学物理仿真，自动生成多样化配对训练数据
3. 提出JFSnet架构，融合DINOv2语义特征与卷积解码器做空间重建，加入平移等变约束提升时序一致性与高频细节保留
### 关键结果
FFHQ 12163张图像子集测试推理速度达27.68 FPS；CelebV-Text视频主观评测中，眼部一致性、时序稳定性、整体修复质量均显著优于扩散、GAN类基线
