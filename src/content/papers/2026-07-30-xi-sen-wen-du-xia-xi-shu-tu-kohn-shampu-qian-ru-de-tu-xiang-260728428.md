---
title: Kohn-Sham Spectral Embedding on Sparse Graphs at the Nishimori Temperature
  for Image Classification
title_zh: 西森温度下稀疏图Kohn-Sham谱嵌入的图像分类方法
authors:
- V. S. Usatyuk
- D. A. Sapozhnikov
- S. I. Egorov
affiliations:
- South-West State University (SWSU), Russia
- T8 LLC, Russia
arxiv_id: '2607.28428'
url: https://arxiv.org/abs/2607.28428
pdf_url: https://arxiv.org/pdf/2607.28428
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 物理启发 · 低参量稀疏图分类
tags:
- Sparse Graph
- Spectral Embedding
- Energy-based Model
- Low-parameter Model
- Image Classification
one_liner: 提出物理启发的KSSE稀疏图分类模型，参数量较Swin、ViT低10-30倍，ImageNet精度相当或更优
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有CNN、Transformer类图像分类模型参数量庞大，部署门槛高，亟需低参数量、高精度的替代分类方案。
### 方法关键点
1. 物理启发架构：将预训练特征映射到准循环LDPC稀疏图，构建正则化拉普拉斯作为Kohn-Sham哈密顿量，基于关联随机键伊辛模型的西森温度计算谱嵌入
2. 效率优化：通过星域手术调整图拓扑控制残余挫组，基于循环块FFT和低阶瑞利精化解谱问题，复杂度为$
\mathcal{O}(N\log N + k_{\text{mode}}^2 N)$
3. 收敛保障：通过多尺度分形分析验证损失面从粗糙regime到星域盆地的转变，仅需5个模态即可完成瑞利精化
### 关键结果
在ImageNet-1000采用冻结EfficientNet-B4特征，仅21.24M参数实现88.93% Top-1精度，优于197M参数的Swin-L，精度匹配632M参数的ViT-H/14，参数量分别降低10×、30×
