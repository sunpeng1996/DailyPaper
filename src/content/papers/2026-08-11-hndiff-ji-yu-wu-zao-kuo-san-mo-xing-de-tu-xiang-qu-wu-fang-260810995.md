---
title: 'HNDiff: Haze-Noise Diffusion for Image Dehazing'
title_zh: HNDiff：基于雾噪扩散模型的图像去雾方法
authors:
- Jin-Ting He
- Fu-Jen Tsai
- Yan-Tsung Peng
- Min-Hung Chen
- Chia-Wen Lin
- Yen-Yu Lin
affiliations:
- National Yang Ming Chiao Tung University, Taiwan
- National Tsing Hua University, Taiwan
- National Chengchi University, Taiwan
- NVIDIA, Taiwan
arxiv_id: '2608.10995'
url: https://arxiv.org/abs/2608.10995
pdf_url: https://arxiv.org/pdf/2608.10995
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 图像去雾 · 扩散模型物理先验优化
tags:
- Diffusion Model
- Image Dehazing
- Inductive Bias
- Latent Diffusion
- Physical Prior
one_liner: 将大气散射模型作为归纳偏置嵌入扩散框架，提出雾感知调度的雾噪联合扩散去雾方法及可即插即用的潜变量版本
practical_value: '- 电商户外商品图/直播带雾画面修复场景可直接复用HNDiff的雾感知噪声调度策略，根据雾浓度动态调整噪声注入强度，平衡内容生成与细节保留

  - 现有图像去雾业务管线可直接集成Latent HNDiff的干净latent prior，无需重构整个模型即可快速提升去雾效果

  - 扩散模型做图像修复类任务时可借鉴「将目标退化的物理形成原理作为inductive bias嵌入扩散正反过程」的思路，降低生成幻觉提升还原度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于diffusion的图像去雾方法普遍忽略雾形成的物理原理，从纯高斯噪声重建清晰图像，还原效果上限受限。
### 方法关键点
1. 将大气散射模型作为inductive bias嵌入diffusion框架，正反过程均贴合雾生成的物理机制；
2. 正向过程引入雾噪联合扩散+雾感知噪声scheduler，按区域雾浓度动态调整噪声注入强度：雾重区域加噪多促进内容生成，雾轻区域加噪少保留细节；
3. 反向过程设计物理一致的去雾去噪流程同步消去雾和噪声，同时推出Latent HNDiff版本，输出干净latent prior可无缝接入现有去雾网络。
### 关键结果
在公开去雾基准数据集上取得SOTA效果，可显著提升主流去雾骨干网络的性能。
