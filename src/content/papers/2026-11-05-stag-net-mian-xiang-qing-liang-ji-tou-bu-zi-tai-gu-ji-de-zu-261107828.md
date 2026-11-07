---
title: 'STAG-Net: Structure-Aware Attention over Landmark Groups for Lightweight Head
  Pose Estimation'
title_zh: STAG-Net：面向轻量级头部姿态估计的关键点组结构感知注意力网络
authors:
- Asiri Gawesha Lindamulage
- Sanka Mohottala
- Dharshana Kasthurirathna
- Nuwan Kodagoda
affiliations:
- 斯里兰卡信息技术学院工程学院
- 斯里兰卡贾亚瓦德纳普拉大学工程学院
- 科伦坡大学计算学院
- 斯里兰卡信息技术学院计算学院
arxiv_id: '2611.07828'
url: https://arxiv.org/abs/2611.07828
pdf_url: https://arxiv.org/pdf/2611.07828
published: '2026-11-05'
collected: '2026-11-07'
category: Other
direction: 轻量计算机视觉 · 头部姿态估计
tags:
- Lightweight_NN
- Head_Pose_Estimation
- Facial_Landmark
- TinyML
- Edge_AI
one_liner: 提出轻量结构感知注意力网络STAG-Net，基于人脸关键点实现高精度低开销头部姿态估计
practical_value: '- 电商直播互动、虚拟试穿/试妆等场景的端侧人脸姿态对齐任务，可复用其关键点分群+轻量注意力的设计思路，大幅压缩模型开销

  - 端侧人脸相关CV能力部署时，可参考「先提取结构化关键点再做下游任务」的范式，降低推理算力要求

  - 轻量模型设计中，引入领域结构化先验（如人脸关键点空间聚类分组）替代无差别注意力，可兼顾精度与推理速度'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有基于图像的头部姿态估计算法算力开销过高，难以在资源受限的端侧/边缘场景落地。
### 方法关键点
1. 基于人脸关键点输入，采用运动感知选择、空间聚类策略对关键点分组，结合DeepSet编码器、自注意力与全局几何描述符构建轻量回归网络；
2. 分别适配FaceMesh、FAN两类主流关键点提取器，输出两种场景适配版本。
### 关键结果
所有评测场景下MAE为同类型关键点方法最低，BIWI数据集FAN版本交叉评测MAE仅3.51°，单主体评测MAE仅2.39°；回归器参数量仅0.012M~0.043M，FLOPs比FSA-Net低3个数量级；Tesla T4上FaceMesh管线FPS达322.9，是最快图像基线的2倍，CPU上FPS达111.0；训练速度比FSA-Net快7~8倍，完整训练仅需28分钟。
