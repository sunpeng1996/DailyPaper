---
title: Local Sparsity Enables Unsupervised LLM Safety Detection
title_zh: 利用局部稀疏性实现无监督大语言模型安全检测
authors:
- Xin Chen
- Gil Kur
- Alexander Shevchenko
- Andreas Krause
affiliations:
- ETH Zürich
arxiv_id: '2609.20129'
url: https://arxiv.org/abs/2609.20129
pdf_url: https://arxiv.org/pdf/2609.20129
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: LLM安全检测 · 无监督异常检测
tags:
- Sparse Autoencoder
- Anomaly Detection
- LLM Safety
- Local Sparsity
- LoRA
one_liner: 基于稀疏自编码器局部稀疏特性，提出无需有害标注的无监督LLM安全检测框架
practical_value: '- 电商/广告场景的违规query、生成式推荐文案、Agent生成内容的合规检测可直接复用该框架，无需提前标注所有有害样本，适配新型垃圾广告、诱导话术等未知风险

  - SAE+局部稀疏掩码的特征降维trick可迁移到高维用户/Item表征的异常检测任务，仅需1-2%的神经元参与计算即可完成识别，大幅降低推理开销

  - 仅需1%异常样本做跨聚类校准即可获得接近监督模型的性能，适合冷启动违规检测场景，大幅减少标注成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM安全检测以监督方案为主，依赖预标注的有害样本，无法应对持续涌现的新型越狱攻击、未覆盖的有害类别，而直接对高维LLM激活做无监督异常检测受维度灾难制约效果极差。
### 方法关键点
- 基于线性表示假设，将LLM激活映射到稀疏自编码器(SAE)的过完备概念空间，利用局部稀疏特性：相近安全样本共享少量激活神经元，有效压缩有效维度
- 框架分为4个模块化阶段：SAE特征提取、K-means聚类划分安全样本邻域、每个聚类生成稀疏掩码筛选核心特征、基于掩码空间的质心距离或重构残差输出异常分
- 两种落地实例：训练免的FREQMASK-KM（全局频率选Top-k特征，L1距离打分，部署成本极低）、拟合per-cluster LoRA的LEARNEDMASK-LORA（重构残差打分，适配复杂模型结构）
### 关键结果
在6款主流指令微调LLM（含LLaMA3-8B、Qwen3-8B、Gemma 4-26B等）、三类有害数据集（BeaverTails、ToxiGen、HarmBench）上验证：无监督方案在≥8B参数模型上AUROC最高达0.937，仅用1%异常样本做校准后AUROC最高达0.99，性能接近监督线性探针，计算仅需1-2%的SAE神经元参与。
### 核心结论
利用LLM激活的固有局部稀疏结构，无监督异常检测可以在几乎不损失性能的前提下，摆脱对预标注有害样本的依赖，适配动态变化的安全风险场景
