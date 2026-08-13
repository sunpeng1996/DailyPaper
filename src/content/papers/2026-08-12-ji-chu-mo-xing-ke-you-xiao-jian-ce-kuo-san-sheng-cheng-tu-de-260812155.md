---
title: Understanding Why Foundation Models Work for Diffusion-Generated Image Detection
title_zh: 基础模型可有效检测扩散生成图像的底层原因探究
authors:
- Davide Cozzolino
- Giovanni Poggi
- Luisa Verdoliva
affiliations:
- University Federico II of Naples
arxiv_id: '2608.12155'
url: https://arxiv.org/abs/2608.12155
pdf_url: https://arxiv.org/pdf/2608.12155
published: '2026-08-12'
collected: '2026-08-13'
category: Multimodal
direction: 多模态生成内容检测 · 基础模型可解释性
tags:
- Foundation Model
- Diffusion Model
- Generated Image Detection
- Frequency Analysis
- Media Forensics
one_liner: 通过多维度分析实验揭示基础模型检测扩散生成图依赖非语义中低频分布差异
practical_value: '- 做电商AIGC内容质检时，可重点提取图像中低频特征做生成内容识别，比高频特征抗压缩、缩放等degradation效果更好

  - 搭建生成内容检测模型时，可优先选用预训练视觉基础模型做特征提取器，泛化性和鲁棒性优于传统人工设计的artifact特征

  - 自研扩散模型生成电商商品图时，可针对性优化中低频分布对齐，降低生成内容被检测为AI图的概率，规避平台合规风险'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
视觉基础模型在扩散生成图像检测任务上泛化性、抗图像降质表现优异，但作用机制尚不清晰，无法支撑检测/生成算法的针对性优化。

### 方法关键点
1. 基于DDIM反演构造语义完全一致、扩散合成痕迹梯度变化的对照图像序列，排除语义偏差干扰；
2. 开展频域交换分析，定位判别特征的频带分布；
3. 从隐空间维度对比真实图像与扩散生成图像的分布差异。

### 关键结论
- 基础模型检测决策不依赖语义缺陷，核心捕捉非语义特征；
- 判别线索集中在中低频段，而非传统认知的高频生成伪影；
- 扩散生成图像隐空间方差、有效维度显著低于真实图像，未完全拟合真实数据分布。
