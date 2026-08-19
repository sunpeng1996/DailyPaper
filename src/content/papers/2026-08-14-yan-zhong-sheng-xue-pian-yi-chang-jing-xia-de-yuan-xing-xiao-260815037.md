---
title: Prototype-Rectified Iterative Self-supervised Manifold Denoising under Severe
  Acoustic Shift
title_zh: 严重声学偏移场景下的原型校正迭代自监督流形去噪
authors:
- Ashish Anand Shukla
- Rini Smita Thakur
- Aryan Das
- Vinod K. Kurmi
affiliations:
- Indian Institute of Science Education and Research Bhopal
- Vellore Institute of Technology Bhopal
arxiv_id: '2608.15037'
url: https://arxiv.org/abs/2608.15037
pdf_url: https://arxiv.org/pdf/2608.15037
published: '2026-08-14'
collected: '2026-08-19'
category: Other
direction: 音文基础模型测试时自适应去噪
tags:
- Test-Time Adaptation
- Audio-Text Foundation Model
- Latent Space Correction
- Low-Rank Adaptation
- Denoising
one_liner: 提出训练无关、无数据源的TTA框架PRISM，解决音文基础模型强噪声下性能暴跌问题
practical_value: '- 低秩域偏移假设可迁移至搜索推荐场景，用户行为/query分布漂移时，可假设漂移能量集中在低秩主成分，用静态投影矩阵校正，避免梯度类TTA的噪声放大问题

  - 冻结类别文本原型作为几何锚点的思路，可用于生成式推荐冷启动item的语义嵌入对齐，无需额外训练即可校正无标注新item的嵌入偏差

  - 闭形式校正编译为单矩阵乘法的工程优化方案，可大幅降低在线推理延迟，适配低延时要求的搜索推荐、端侧Agent场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
音文基础模型（ATMs）在强声学噪声下性能灾难性下降，现有测试时自适应（TTA）方案要么基于梯度优化易放大噪声，要么依赖推理阶段不可获取的噪声标注prompt。
### 方法关键点
基于仿射噪声假设：强噪声在多模态隐空间引入低秩仿射偏移，90%以上失真能量集中在前60个主成分。PRISM为无训练、无数据源TTA框架：以冻结文本原型为几何锚点，从无标注目标批次估计并逆转隐空间失真，三类闭形式几何校正通过仿射偏差回归编译为单一静态投影矩阵；针对宽带类别子空间消去的Polyphonic Trap失效模式，引入置信度感知回归修复。
### 关键结果
UrbanSound8K数据集上较零-shot基线提升12.94pp，超Oracle辅助TTA基线9.41pp；推理仅需一次矩阵乘法，耗时0.0009ms，远快于梯度类TTA方案；置信度感知回归为受损最严重的类别最多恢复8.16pp性能
