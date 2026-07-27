---
title: 'DWT-Fusion: A Signal-Based Framework for Training-Free LLM-Generated Text
  Detection'
title_zh: DWT-Fusion：基于信号的免训练大模型生成文本检测框架
authors:
- Mehmet Batuhan Özdaş
- Murat Osmanoğlu
affiliations:
- Ankara University, Türkiye
arxiv_id: '2607.22026'
url: https://arxiv.org/abs/2607.22026
pdf_url: https://arxiv.org/pdf/2607.22026
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: LLM生成文本检测 · 免训练零样本方案
tags:
- LLM-Detection
- Discrete-Wavelet-Transform
- Training-Free
- Zero-Shot
- Voting-Ensemble
one_liner: 基于离散小波分析token对数概率序列，搭配投票集成实现免训练跨域LLM生成文本检测
practical_value: '- 可复用离散小波变换提取token级log概率多尺度特征的思路，用于识别生成式推荐、Agent生成文案的真伪，防范UGC/PGC中的AI垃圾内容

  - 免训练校准加权投票集成方法可直接复用，无需额外标注数据即可快速上线低资源场景的AI内容检测能力

  - 跨模型泛化的检测思路可迁移到生成式推荐的内容质量校验环节，适配不同基座LLM生成的item文案、query推荐结果的合规校验'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有免训练LLM生成文本检测方法多依赖全局统计特征，未充分利用token级预测概率的局部、多尺度变化信息，跨数据集、跨域、未知生成器的零样本泛化能力较差。
### 方法关键点
1. 提出DWT-Fusion信号框架，对代理因果LLM输出的token级对数概率序列做离散小波多分辨率分析，从局部概率动态中提取检测信号；
2. 设计4种免训练投票变体（等权硬投票、等权软投票、校准加权硬投票、校准加权软投票）融合多小波配置结果，无需训练有监督元分类器。
### 关键结果
在HC3、M4、MAGE数据集上，单最优小波配置AUROC分别达0.9872、0.8185、0.7138；校准加权投票集成后AUROC进一步提升至0.9919、0.8477、0.7471。
