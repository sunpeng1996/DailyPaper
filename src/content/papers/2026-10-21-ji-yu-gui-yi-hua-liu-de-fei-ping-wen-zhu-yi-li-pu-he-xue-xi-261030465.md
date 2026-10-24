---
title: Flow-based Spectral Kernel Learning for Nonstationary Attention
title_zh: 基于归一化流的非平稳注意力谱核学习方法
authors:
- Zi Yang
- Ying Li
- Alejandro Lancho
- Darío C. Larese
- Pablo M. Olmos
- Michael Minyi Zhang
affiliations:
- 香港大学计算与数据科学学院
- 新加坡国立大学统计与数据科学系
- 马德里卡洛斯三世大学信号理论与通信系
arxiv_id: '2610.30465'
url: https://arxiv.org/abs/2610.30465
pdf_url: https://arxiv.org/pdf/2610.30465
published: '2026-10-21'
collected: '2026-10-24'
category: LLM
direction: LLM 高效注意力机制优化
tags:
- Attention
- Normalizing Flows
- Linear Attention
- Kernel Learning
- Parameter Efficiency
one_liner: 用归一化流学习非平稳注意力核，简化投影设计，降40%-47%参数同时性能超越主流基线
practical_value: '- 长序列用户行为建模、长文本召回排序等场景，可替换原生Transformer注意力为FSKA，在性能持平或提升的前提下减少40%左右的注意力层参数，同时线性内存缩放可适配万级token的长序列输入

  - 端侧小模型、电商轻量生成式推荐/Agent部署时，可复用移除QK可学习投影、固定正交V投影的设计思路，大幅压缩模型体积的同时保障核心表达能力

  - 线性注意力落地时，可直接复用ELU+1的正特征变换trick，解决随机傅里叶特征正负抵消导致的分母数值不稳定问题，无需大幅提升特征维度即可保证训练推理稳定性'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有核化注意力多依赖固定或平稳核，无法适配复杂的非平稳token交互模式；已有的可学习核方法要么采用GMM参数化，复杂度随组件数攀升，要么采用隐式神经网络参数化，缺少显式谱正则易出现过拟合或谱坍塌。同时标准Transformer的QKV投影占用大量参数，长序列下O(L²)的时空复杂度难以落地。

### 方法关键点
- 基于通用Bochner定理将非平稳注意力核学习转化为二元谱密度学习问题，采用RealNVP归一化流参数化谱密度，搭配NGSM谱先验做KL正则，从机制上避免谱坍塌
- 推导适配非平稳核的随机傅里叶特征（RFF）映射，实现O(L)线性时间注意力计算；新增ELU+1正特征变换，解决RFF特征正负抵消导致的注意力分母数值不稳定问题
- 理论证明足够表达能力的核可吸收QK投影的作用，直接移除QK可学习参数，仅保留固定正交V投影，多头V投影互相正交保证头间表达多样性

### 关键实验结果
在MNIST分类、6个句子分类数据集、4个长文档分类数据集上对比Transformer、Performer、Mamba、IKAN等10+基线：句子分类任务SST-2 F1较原生Transformer提升2.67个点，SST-5提升3.05个点；长文档分类任务在4个数据集上均取得最高macro-F1，较最强基线最高提升1.77个点；注意力层参数较主流基线减少40%-47%，序列长度为4096时训练内存仅10GB左右，远低于原生Transformer的80-120GB。

### 核心结论
当注意力核的表达能力足够强时，QK可学习投影并非必需，固定V投影即可实现性能与效率的双赢
