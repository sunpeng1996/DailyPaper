---
title: 'FoMo: Forking Moment in Generative Trajectory as a Perceptual Distance'
title_zh: FoMo：将扩散生成轨迹分叉时刻作为图像感知距离度量
authors:
- Jaihyun Lew
- Mingi Jung
- Minjun Park
- Wooseok Song
- Sungroh Yoon
affiliations:
- Interdisciplinary Program in AI, Seoul National University
- Department of Electrical and Computer Engineering, Seoul National University
- AIIS, ASRI, INMC, and ISRC, Seoul National University
arxiv_id: '2609.25716'
url: https://arxiv.org/abs/2609.25716
pdf_url: https://arxiv.org/pdf/2609.25716
published: '2026-09-21'
collected: '2026-09-28'
category: Other
direction: 扩散模型 · 图像感知距离自动标注
tags:
- Diffusion Model
- Image Quality Assessment
- Automatic Annotation
- Perceptual Distance
- Generative Trajectory
one_liner: 利用扩散生成轨迹分叉时刻自动生成无人工标注的图像感知距离标签，训练更高性能IQA模型
practical_value: '- 电商商品图生成/优化场景可复用FoMo思路，无需人工标注自动评估生成图与原图的感知差异，大幅降低MOS标注成本

  - 多模态推荐的图像召回环节，可借鉴扩散分叉时刻计算的感知距离替代传统CLIP余弦相似度，提升语义匹配准度

  - 做生成内容质量评估任务时，可直接复用开源FoMo预训练指标，替代成本高噪声大的人工标注流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有参考型图像质量评估（IQA）高度依赖人工标注：MOS点式标注规模化采集成本极高、人工判断不一致导致噪声大；2AFC pairwise标注仅能输出相对比较结果，无法支持任意图像对的通用量化评估。
### 方法关键点
利用扩散模型的生成动力学特征作为感知距离代理：扩散生成早期步输出图像粗结构、后期步输出细粒度细节，定义生成轨迹分叉时刻（FoMo）作为感知距离标签：分叉越早的图像仅共享粗结构、感知距离越远，分叉越晚的图像仅存在细节差异、感知距离越近。无需任何人工标注即可生成任意图像对的点式感知距离标签，用于监督IQA模型训练。
### 关键结果
在多类骨干架构上验证标注pipeline有效性，多个IQA基准测试中性能超过基于人工标注数据集训练的模型
