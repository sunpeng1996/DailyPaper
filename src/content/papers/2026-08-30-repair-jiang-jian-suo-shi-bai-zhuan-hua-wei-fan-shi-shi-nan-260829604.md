---
title: 'RePair: Turning Retrieval Failures into Counterfactual Hard Pairs'
title_zh: RePair：将检索失败转化为反事实难例对的训练框架
authors:
- Siyi Liu
- Xiaorong Zhu
- Enjun Du
- Xinyu Zuo
- Lisheng Duan
- Haijin Liang
- Jin Ma
- Junfu Pu
- Yongqi Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- The University of Hong Kong
- ARC Lab, Tencent
arxiv_id: '2608.29604'
url: https://arxiv.org/abs/2608.29604
pdf_url: https://arxiv.org/pdf/2608.29604
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: 跨模态检索 · 难例构造与对比训练
tags:
- Contrastive Learning
- Hard Negative Mining
- Cross-Modal Retrieval
- Counterfactual Editing
- CLIP
one_liner: 基于模型真实检索失败做最小反事实编辑，生成难例对提升跨模态检索的训练效率与精度
practical_value: '- 电商跨模态检索（以文搜图/图搜商品）微调阶段，可直接复用RePair的难例构造逻辑：挖掘现有系统的topK假阳性结果，通过LLM/多模态大模型做最小语义编辑生成配对难例，比随机生成难例的数据效率高26%以上，大幅节省合成成本

  - 对比学习训练可复用局部网格损失设计：将难正负对打包在同一个局部计算单元，避免全局batch打散难例对导致的监督信号稀释，同时保留全局InfoNCE损失保证特征空间均匀性，无需改动大架构即可涨点

  - 难例质量控制可复用双验证逻辑：先校验query与Ground Truth一致性过滤标注噪声，再校验假阳性是否为真实模型混淆而非合理匹配，可减少无效难例带来的梯度噪声'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有CLIP类双编码器跨模态检索的细粒度语义匹配能力不足，top级近miss错误占比高；传统难例挖掘仅能选择现有负样本，缺乏对应的正向监督信号；无误差感知的合成难例大量修改无关语义，数据效率极低，部分样本甚至带来负向迁移。

### 方法关键点
- 基于「脚手架-残差」假设：top级假阳性和query共享大部分语义（脚手架），仅在局部错误语义（残差）存在差异，是天然的难例生成基础
- 三大设计原则：Validity（双LLM校验过滤标注噪声和合理匹配，仅保留真实模型混淆作为种子）、Minimality（仅编辑错误残差，生成多个候选后选择与原假阳性embedding相似度最高的样本，保证语义改动最小）、Locality（将锚点、难正负对打包成3×3局部网格，单独计算局部对比损失，与全局InfoNCE损失加权训练，避免难例信号被全局batch稀释）
- 双向构造：同时覆盖图搜文、文搜图两个方向的失败样例，生成跨模态难例对。

### 关键实验
在Flickr30K、COCO30K数据集上，和NegCLIP、SugarCrepe、LaCLIP等10余个基线对比，仅用107K合成样本（比基线少26%~75%），Flickr30K图搜文R@1达90.13，比最优基线高1.18个点，文搜图R@1达76.35，比最优基线高1.71个点；去掉失败感知的难例挖掘后，R@1最高下降2.42个点，证实失败驱动的难例是核心增益来源。

**最值得记住的一句话**：检索失败不是需要丢弃的错误，而是定位模型能力边界的精准锚点，基于失败做最小反事实编辑的难例，数据效率远高于无差别的批量合成。
