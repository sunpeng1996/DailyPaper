---
title: 'DK-VLM: Geometry as Position for Spatial Reasoning in Vision-Language Models'
title_zh: DK-VLM：以几何为位置的视觉语言模型空间推理方法
authors:
- Han Su
- Meng Tian
- Tianyu Huang
- Mingyu Gao
- Lennox Wei
- Dongxu Li
- Jianhua Han
- Hang Xu
- Xiaohe Wu
- Wangmeng Zuo
affiliations:
- Harbin Institute of Technology
- Yinwang Intelligent Technology
- Huawei
arxiv_id: '2610.22356'
url: https://arxiv.org/abs/2610.22356
pdf_url: https://arxiv.org/pdf/2610.22356
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态大模型 · VLM空间推理优化
tags:
- VLM
- Spatial Reasoning
- Attention Mechanism
- 3D Vision
- Multimodal Learning
one_liner: 提出双内核注意力与参考系组合监督，显著提升VLM跨视图3D空间推理能力
practical_value: '- 开发AR试穿/试戴、商品3D交互类Agent时，可复用双内核注意力架构，融合几何位置信息提升空间感知准确性，避免3D特征与预训练语义表征对齐困难的问题

  - 做多视角商品短视频的内容标签生成、语义理解任务时，可引入Reference-Frame Composition (RC)监督，提升连续视角变换下的内容推理效果

  - 做具身Agent实物操作、室内导航类任务时，可借鉴「将几何信息作为位置编码而非特征融合」的设计，降低空间监督不足场景下的模型训练成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM难以理解跨视图3D空间关系，也无法随观察者移动更新空间判断；传统3D重建特征融合方案在有限空间监督下，很难与预训练语义表征对齐。
### 方法关键点
1. 提出Dual-Kernel Attention，语义内核保留预训练模型原生注意力与位置编码，几何内核基于3D点估计与相机位姿，通过点位移与相对视图变换直接调制注意力，再用可学习门控融合两路输出，将几何信息作为位置信息而非融合特征引入注意力计算
2. 新增Reference-Frame Composition (RC)监督，基于验证后的单步标注生成逐步转向与航向目标，训练模型跨连续判断更新参考系
### 关键结果
DK-VLM-8B在6个空间基准上平均得分最高，VSI-Bench得分74.33、ReVSI-32得分58.28均为最优；RC监督进一步提升多步空间推理能力，且完整模型保留通用视频理解能力
