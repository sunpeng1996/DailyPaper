---
title: Self-Supervised Learning of Structured Dynamics from Videos
title_zh: 从视频中自监督学习结构化动态表征
authors:
- Lukas Knobel
- Andrew Zisserman
- Yuki M. Asano
affiliations:
- Fundamental AI Lab, UTN
- VGG, University of Oxford
arxiv_id: '2607.21576'
url: https://arxiv.org/abs/2607.21576
pdf_url: https://arxiv.org/pdf/2607.21576
published: '2026-07-22'
collected: '2026-07-25'
category: Other
direction: 视频表征 · 自监督动态分解
tags:
- Self-Supervised Learning
- Video Representation
- ViT
- Motion Decomposition
- Weak Supervision
one_liner: 提出SDM模型基于预训练图像ViT冻结特征，自监督分离视频中相机与物体运动的结构化动态表征
practical_value: '- 短视频/直播商品理解场景可借鉴SDM的运动分解思路，分离镜头运动和商品动态，提取更精准的商品行为特征，提升短直内容推荐的相关性

  - 可复用「预训练图像大模型冻结特征+轻量下游动态建模」的范式，避免全量微调的高成本，快速适配视频类推荐任务

  - 采用合成数据+真实数据混合训练策略，用低成本合成数据补充弱监督信号，缓解真实视频场景标注不足的问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
视频帧间变化同时纠缠相机运动、物体运动两类动态因子，现有表征学习很少对二者解耦，且解耦需要的强监督标注成本极高；鲁棒运动表征需分离无关相机运动干扰，基于预训练图像ViT冻结特征能否提取结构化运动表征尚未被验证。
### 方法关键点
提出Structured Dynamics Model (SDM)，通过未来特征预测任务，显式将时序变化的主导分量（对应相机运动）和残差动态（对应物体运动）分离，避免使用单个纠缠隐变量或无结构化空间密集过渡token表征视频变化；训练结合真实视频自监督学习、Kubric合成数据场景动态弱监督两种信号。
### 关键结果
在全新构建的ProbeMotion评测套件（覆盖合成/真实视频的相机运动、物体运动、混合动态场景）上，SDM性能优于使用CLS token或平均池化特征的基线模型，在多个探测任务上效果比肩强监督的VGGT模型，且所用监督信号强度远低于后者。
