---
title: 'Towards Privacy-Preserving Federated Prompt Tuning under Data Heterogeneity:
  A Subspace-Decomposed Expert Approach'
title_zh: 面向数据异质性的隐私保护联邦提示微调：子空间分解专家方法
authors:
- Yuhua Wang
- Xiaodong Li
- Yihao Guo
- Yuxiang Jia
- Qinnan Zhang
- Yifan Sun
- Hainan Zhang
- Yongxin Tong
- Zhiming Zheng
affiliations:
- Beihang University
- Renmin University of China
- Beijing Jiaotong University
arxiv_id: '2607.21417'
url: https://arxiv.org/abs/2607.21417
pdf_url: https://arxiv.org/pdf/2607.21417
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 联邦训练 · 隐私保护提示微调
tags:
- Federated Learning
- Prompt Tuning
- Differential Privacy
- Multi-Expert
- Low-Rank Adaptation
one_liner: 提出子空间分解+实例感知融合的联邦多专家提示微调框架，在隐私约束下平衡个性化与泛化
practical_value: '- 多商家/跨域联合训练推荐/分类模型时，可复用「固定公共基+低秩共享因子+本地残差」的参数分解方案，仅传输低秩因子并施加DP约束，既降低通信成本，又避免DP噪声随参数维度放大，满足数据不出域的隐私合规要求

  - 多专家模型推理优化可直接复用logit层融合trick：提前缓存各专家的文本/特征表征，输入级路由预测权重后直接在logit层加权，避免重复编码，端侧/侧侧部署时能大幅降低推理时延

  - 跨客群/跨域联邦训练时，可增加专家多样性正则+路由负载均衡正则，避免专家坍缩，在数据异质性强的场景下能有效平衡个性化与跨域泛化性'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有联邦提示微调（FPT）依赖单全局共享prompt，在数据异质性场景下会过度平滑多源分布的差异化特征，无法平衡个性化与泛化；替换为多专家prompt又会导致通信成本线性升高，DP噪声随参数维度放大，还存在噪声下专家融合鲁棒性差的问题，而隐私合规要求下跨域联合训练不能泄露用户原始数据，迫切需要兼顾隐私、效率、效果的FPT方案。

### 方法关键点
- **Subspace-decomposed Expert Modeling (SEM)**：每个专家prompt拆解为三部分：低秩共享因子、固定全局公共基、端侧私有残差，仅对低秩共享因子施加DP-SGD并上传聚合，大幅降低通信量与DP噪声，固定公共基保证所有客户端的专家参数处于统一坐标系可直接聚合，额外增加专家多样性正则避免专家冗余坍缩
- **Instance-aware Expert Fusion (IEF)**：端侧轻量路由根据输入特征预测专家权重，提前缓存每个专家的文本特征，在logit层做加权融合，既避免硬选单专家的鲁棒性问题，又降低推理计算量，增加路由负载均衡正则避免赢家通吃

### 关键结果
在11个异质性基准（含5个路径标签偏斜、2个实际标签偏斜、4个域+标签偏斜数据集）上对比PromptFL、DP-FPL等7个SOTA基线，隐私预算ε=1约束下，路径标签偏斜场景的调和均值（HM，平衡本地个性化与跨端泛化）较最优基线最高提升28%，通信量从64KiB降至8KiB（降低87.5%），缓存优化后的推理时延较单prompt基线降低18.7%；成员推理攻击AUC稳定在0.55左右接近随机猜测，梯度反转攻击的语义相似度降至-0.013无有效信息泄露。

最值得记住的一句话：联邦多专家训练中，将可共享参数压缩到低秩子空间做隐私保护，仅保留残差与路由逻辑在本地，是兼顾效率、隐私、个性化与泛化的可行路径。
