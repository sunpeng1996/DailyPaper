---
title: 'F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level
  Object Pose Estimation'
title_zh: F2G-Pose：面向直接RGB-D类别级物体位姿估计的几何感知基础特征提升框架
authors:
- Jinyu Zhang
- Haitao Lin
- Jiashu Hou
- Xiangyang Xue
- Yanwei Fu
affiliations:
- Fudan University
- Shanghai Innovation Institute
arxiv_id: '2610.31623'
url: https://arxiv.org/abs/2610.31623
pdf_url: https://arxiv.org/pdf/2610.31623
published: '2026-10-21'
collected: '2026-10-24'
category: Other
direction: 计算机视觉 · RGB-D类别级物体位姿估计
tags:
- Pose Estimation
- RGB-D Perception
- MoE Transformer
- DGCNN
- Foundation Feature
one_liner: 提出单前向传播的实时类别级RGB-D物体位姿估计框架，在多个基准达SOTA精度与28FPS推理速度
practical_value: '- 若业务涉及电商AR导购、商品3D自动化建模，可复用该框架单RGB-D输入快速位姿估计能力，降低3D素材生产的人工成本

  - 面向实体场景的商品拣选/盘点Agent开发，可借鉴DGCNN局部几何编码+MoE Transformer融合多模态特征的思路，提升实体物体识别鲁棒性

  - 需落地实时多模态推理的业务，可参考其冻住通用预训练backbone仅微调任务专用网络的训练范式，平衡效果与训练成本

  - 纯线上推荐/广告/搜索业务无相关3D视觉/实体Agent场景的，该论文主要为学术贡献，可借鉴点有限'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
类别级RGB-D物体位姿估计无需实例CAD模型/参考视图，但存在类内差异、物体对称、局部观测带来的歧义性，现有方案要么中间结构易出现误差传播，要么基于扩散模型的方案推理延迟高、后处理复杂，无法兼顾可靠性与效率。
### 方法关键点
1. 单前向传播框架，单次输入RGB-D即可同步输出类别级位姿、公制尺寸、相机坐标系下补全形状
2. 将稠密视觉基础特征映射到部分点云，用DGCNN tokenization编码局部几何，结合MoE Transformer整合物体级结构
3. 联合尺寸预测与相机帧形状补全任务，通过稠密几何监督保证度量一致性
4. 仅用带位姿标注的合成SOPE数据训练任务专用网络，冻住预训练RADIO backbone
### 关键结果数字
在SOPE、ROPE基准上达到SOTA精度，纯位姿推理速度达28FPS；在HouseCat6D上表现出优秀的相机帧几何建模能力，在HANDAL数据集上实现强真实物体迁移效果
