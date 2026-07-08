---
title: 'Graph Convolutional Attention: A Spectral Perspective on Graph Denoising and
  Diffusion'
title_zh: 图卷积注意力：图去噪与扩散的谱视角
authors:
- Shervin Khalafi
- Igor Krawczuk
- Sergio Rozada
- Charilaos Kanatsoulis
- Antonio G Marques
- Alejandro Ribeiro
affiliations:
- University of Pennsylvania
- King Juan Carlos University
- Stanford University
arxiv_id: '2607.06546'
url: https://arxiv.org/abs/2607.06546
pdf_url: https://arxiv.org/pdf/2607.06546
published: '2026-07-07'
collected: '2026-07-08'
category: Other
direction: 图学习 · 图去噪与扩散优化
tags:
- Graph Learning
- Graph Attention
- Graph Denoising
- Graph Diffusion
- Spectral Filter
one_liner: 提出基于谱设计的图卷积注意力GCA，突破线性注意力去噪局限，提升图任务性能且降低推理开销
practical_value: '- 电商用户-物品交互图去噪场景可替换原有线性注意力为GCA，通过图滤波的query/key实现谱去噪，提升用户/物品表征质量

  - 图Transformer用于推荐召回/排序链路时，可替换为GCA省去复杂结构特征计算，降低推理延迟适配高吞吐业务需求

  - 基于图扩散的生成式推荐场景，可复用GCA+PEARL位置编码的架构，避免显式特征分解，平衡效果与推理速度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
图去噪是图学习基础问题也是图扩散模型核心操作，现有注意力类图去噪的理论机制尚不清晰，线性注意力仅能学习训练分布的平均谱去噪滤波器，无法适配谱分布差异较大的异构输入图。
### 方法关键点
1. 提出直接利用输入图谱的Spectral Attention，理论性能优于线性注意力，增益由数据集的谱多样性决定；
2. 落地为排列等变的实用架构GCA，通过图滤波的query、key实现谱去噪，后续softmax可进一步将带噪特征投影至干净特征空间；
3. 结合PEARL位置编码可避免显式特征分解，降低计算开销。
### 关键结果
- 替换线性注意力为GCA后，合成/真实数据集的图去噪、扩散任务性能稳定提升，增益与谱多样性正相关；
- 在DiGress基准上无需计算昂贵结构特征即可匹配标准图Transformer效果，结合PEARL后推理速度更快且质量无损
