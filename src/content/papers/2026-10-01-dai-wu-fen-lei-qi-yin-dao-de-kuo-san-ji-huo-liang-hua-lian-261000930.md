---
title: Joint Branch-Space Transform Coding for Diffusion Activation Quantization with
  Classifier-Free Guidance
title_zh: 带无分类器引导的扩散激活量化联合分支空间变换编码
authors:
- Mingrun Jiang
- Yuejia Liu
- Zishan Shao
- Ting Jiang
- Qinsi Wang
- Hancheng Ye
- Yixiao Wang
- Rui-Feng Wang
- Kangning Cui
- Yixuan Chen
affiliations:
- Duke University
- Carnegie Mellon University
- University of Florida
- Wake Forest University
- University of Oxford
arxiv_id: '2610.00930'
url: https://arxiv.org/abs/2610.00930
pdf_url: https://arxiv.org/pdf/2610.00930
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 扩散模型训练后量化 · CFG优化
tags:
- Diffusion Model
- Post-Training Quantization
- CFG
- Activation Quantization
- GCBT
one_liner: 提出即插即用的GCBT分支变换，提升CFG引导扩散模型训练后量化精度无额外性能损失
practical_value: '- 电商生成式推荐场景中用扩散模型生成商品图、营销文案的需求，可直接将GCBT作为即插即用模块叠加到现有PTQ量化流程上，降低推理显存占用的同时保证生成质量

  - GCBT无梯度优化、无角度搜索的每层闭集解工程实现成本极低，无需修改原有量化pipeline即可快速上线

  - 所有带CFG引导的生成类任务（如个性化商品图生成、推荐话术生成的扩散/大模型），均可复用跨分支相关性建模思路优化量化损失'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有带CFG的扩散模型训练后量化方法，对条件、无条件两个分支的激活独立量化，未利用跨分支强相关性，固定比特预算下量化保真度受限
### 方法关键点
- 证明CFG匹配激活是强相关二维源，分支编码基的选择直接影响量化保真度
- 提出分支空间变换编码，通过离线计算的2×2正交矩阵旋转CFG匹配分支，仅需极小改动即可接入现有量化流程
- 推导GCBT变换，结合CFG引导方向和跨分支二阶矩，在等速率量化噪声代理下得到每层闭集解，无需梯度优化或角度搜索
### 关键结果
在W4A4精度下，GCBT叠加SVDQuant在PixArt-Σ上LPIPS从0.434降至0.333，在SANA-1.6B上LPIPS从0.282降至0.198，所有测试场景均无统计意义上的性能下降
