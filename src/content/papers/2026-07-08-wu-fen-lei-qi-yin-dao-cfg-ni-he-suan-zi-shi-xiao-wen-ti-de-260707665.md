---
title: 'Guidance Breaks the Fitted Operator: A Terminal-Fitted Repair for Classifier-Free
  Guidance'
title_zh: 无分类器引导（CFG）拟合算子失效问题的终端拟合修复方法
authors:
- Shiheng Zhang
affiliations:
- University of Washington
arxiv_id: '2607.07665'
url: https://arxiv.org/abs/2607.07665
pdf_url: https://arxiv.org/pdf/2607.07665
published: '2026-07-08'
collected: '2026-07-09'
category: Other
direction: 扩散采样优化 · 无分类器引导（CFG）修复
tags:
- Classifier-Free Guidance
- Diffusion Model
- DDIM
- Sampling Optimization
- Stable Diffusion
one_liner: 提出零额外计算开销的CFG修复公式，解决高引导系数下扩散采样过饱和不稳定问题
practical_value: '- 生成式推荐场景用扩散做商品图、营销文案生成时，可直接替换原有CFG计算式，零额外成本解决高引导系数下生成结果过饱和、崩坏问题，无需增加采样步数降低推理速度

  - 对生成内容的类条件控制需求（如指定商品类别、风格生成），该修复可在高CFG权重下保持生成稳定性，提升条件匹配准确率

  - 扩散类生成服务部署时，无需调整原有采样链路，仅修改引导项计算公式即可落地，无额外推理开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Classifier-free guidance（CFG）是扩散、流匹配采样中增强类条件控制的标准方案，但高引导系数下会出现过饱和、不稳定问题，现有方案只能通过增加采样步长或限制引导区间缓解，会提升推理成本或降低控制效果。

### 方法关键点
从数值分析视角证明，引导操作会让判别子空间刚度提升至异常指数1+w，导致原有DDIM采样算子不再拟合，小噪声区间残差随σ_min趋近于0发散；提出零额外NFE的修复方案，仅需将CFG原有引导项计算从w(r-1)替换为r^(1+w)-r即可。

### 关键结果数字
在CIFAR-10和Stable Diffusion 1.5 DDIM测试集上，测试网格内9/9的点FID优于原生CFG，同时保留分类代理目标准确率，无额外计算开销，仅在部分场景下KID略逊于原生CFG。
