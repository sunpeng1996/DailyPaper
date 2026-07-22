---
title: 'Beyond Noisy Signals: Dual-Level Denoising for Multi-modal Sequential Recommendation'
title_zh: 面向多模态序列推荐的双层级去噪框架DDMSR
authors:
- Jie Luo
- Qi Jin
- Xinming Zhang
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.18786'
url: https://arxiv.org/abs/2607.18786
pdf_url: https://arxiv.org/pdf/2607.18786
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 多模态序列推荐 · 双层级去噪
tags:
- Sequential Recommendation
- Multi-modal Learning
- Denoising
- Graph Signal Processing
- Frequency Domain Modeling
one_liner: 从特征拓扑和序列频域双维度去噪，解决多模态序列推荐双重噪声痛点，性能最高提升19.33%
practical_value: '- 特征去噪可直接复用：无需引入复杂扩散模型，通过构建商品语义KNN图做拉普拉斯平滑，轻量实现预训练图文特征去噪，同时可通过邻居聚合补全长尾商品特征，适配电商多模态商品场景

  - 交互序列去噪落地方案：用FFT将交互序列转频域加可学习滤波器，自适应压制误点击、临时兴趣等异常信号，无需人工配置噪声过滤规则，适合电商/短视频高噪声交互场景

  - 跨模态对齐优化技巧：加入同商品图文特征的轻量对比损失，无需复杂融合结构即可缩小模态异质性gap，工程实现成本低收益显著

  - 超参数调优经验：语义图KNN邻居数小规模数据集选5，大规模选10-20，频域去噪层控制在1-3层，避免过滤波损失有效信息'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态序列推荐面临双重噪声困境：一是通用预训练模型提取的图文特征与推荐场景细粒度用户意图存在语义gap，冗余噪声多；二是用户交互序列中存在大量误点击、临时兴趣等虚假交互，两类噪声叠加严重限制推荐性能上限，现有方案多仅处理单层级噪声，或依赖扩散等高成本生成模型，落地性差。
### 方法关键点
- 图结构特征去噪：分模态构建Item语义KNN图，基于图信号处理的拉普拉斯平滑做低通滤波，自适应平衡自身特征与邻居聚合特征，抑制高频语义噪声，同时通过语义传播补全长尾Item特征
- 频域序列去噪：将交互序列通过FFT转换到频域，用可学习复数滤波器自适应调制频谱，压制异常交互对应的噪声分量后，再经IFFT转回时域输入序列编码器
- 跨模态对比对齐：加入同Item图文特征的InfoNCE对比损失，缩小模态间异质性gap，提升多模态特征语义一致性
### 关键实验结果
在Beauty、Sports、Toys、MicroLens四个公开电商/短视频数据集上，对比SASRec、BERT4Rec、UniSRec等10个SOTA基线，Recall@20最高提升19.33%（Sports数据集），NDCG@20最高提升10.68%（Beauty数据集），全指标显著优于基线。
**最值得记住的一句话**：多模态序列推荐的性能提升无需依赖复杂生成式模型，从特征和序列双维度做轻量信号去噪，即可获得远超基线的收益。
