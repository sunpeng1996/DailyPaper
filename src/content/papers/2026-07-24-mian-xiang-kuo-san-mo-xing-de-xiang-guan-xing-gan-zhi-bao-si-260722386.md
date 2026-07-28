---
title: Correlation-Aware and Gaussianity-Preserving Robust Latent Angular Watermarking
  for Diffusion Models
title_zh: 面向扩散模型的相关性感知、保高斯性鲁棒隐空间角域水印方法
authors:
- Yebin Zheng
- Haonan An
- Guang Hua
- Zhiping Lin
- Yuguang Fang
affiliations:
- Singapore Institute of Technology
- City University of Hong Kong
- Nanyang Technological University
arxiv_id: '2607.22386'
url: https://arxiv.org/abs/2607.22386
pdf_url: https://arxiv.org/pdf/2607.22386
published: '2026-07-24'
collected: '2026-07-28'
category: Other
direction: 扩散模型 · 隐空间鲁棒水印
tags:
- Diffusion Model
- Watermarking
- Latent Space
- Gaussian Preserving
- Robustness
one_liner: 提出保高斯性的隐空间角域水印LAW及变体，实现SOTA抗攻击能力与更高生成保真度
practical_value: '- 电商生成式商品图、营销素材可复用LAW方法嵌入隐形水印，不影响画质即可溯源盗版侵权内容，降低素材盗用损失

  - 隐空间编码保持高斯分布的设计思路可迁移到GenRec的Semantic ID嵌入场景，避免自定义标识注入后生成质量下降

  - 优先选择大范数稳定隐维度嵌入信息的trick，可用于LLM生成文案、推荐生成结果的不可见业务标识注入，抗干扰性更强'
score: 5
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散模型隐空间水印方法存在三大缺陷：一是破坏隐变量高斯性，对正常/恶意扰动敏感，易被检测或移除；二是破坏隐变量独立同分布假设，导致生成保真度下降；三是缺乏对加水印后隐变量内部相关结构的严谨量化刻画。
### 方法关键点
1. 基于各向同性高斯的旋转不变性，提出LAW将水印位编码为不相交隐变量对之间的±π/2对极角，严格保留隐变量高斯性；
2. 推导证明解码角误差方差与隐变量对的范数平方成反比，据此提出LAW-M变体，选择大范数的几何最稳定隐维度锚定水印位，进一步提升鲁棒性；
3. 理论推导得到加水印后隐变量的闭式自相关结构，证明相关退化仅局限于稀疏、结构化的固定±π/4非对角元。
### 关键结果
实验实现针对各类后处理、重生成攻击的SOTA鲁棒性，同时取得现有隐空间水印方法中的最优图像保真度，FID指标领先现有方案。
