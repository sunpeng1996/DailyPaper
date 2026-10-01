---
title: 'From Spectra to Joint Schedules in LLM Pre-training: 3+3(+2) Scaling-Law Regimes'
title_zh: LLM预训练频谱驱动的联合调度3+3(+2)缩放定律机制研究
authors:
- Yichen Wang
- Fanghui Liu
- Yudong Chen
affiliations:
- University of Wisconsin–Madison
- Shanghai Jiao Tong University
arxiv_id: '2609.40148'
url: https://arxiv.org/abs/2609.40148
pdf_url: https://arxiv.org/pdf/2609.40148
published: '2026-09-30'
collected: '2026-10-01'
category: Training
direction: LLM预训练 · 训练调度与缩放定律
tags:
- Scaling Law
- LLM Pre-training
- Learning Rate Schedule
- Batch Size Schedule
- SGD Dynamics
one_liner: 推导联合LR/Batch调度下的3+3(+2)缩放律区间，可跨调度预测LLM预训练损失
practical_value: '- 训练电商/推荐/Agent域内自定义小LLM时，可复用内在时间$T_t=\sum\eta_s$与$r=B/\eta$的等价性，固定$r$下灵活调整LR/Batch组合优化训练效率，无需重新调参

  - 跨调度损失预测的7参数forcing-memory surrogate可直接复用，仅在单种调度上拟合即可预测其他调度损失，大幅降低预训练调参试错成本

  - 公开数据集上验证得到LLM预训练$q_K≈1$的结论可直接复用，无需重新拟合即可快速完成小模型训练的损失预估与资源分配'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM预训练缩放定律默认指数是模型与数据的固有属性，但实际LR、Batch调度会显著改变损失曲线，无法跨调度做训练进度预测与资源分配，缺乏统一理论框架解释调度对缩放律的影响，也缺少可迁移的损失预测方法。

### 方法关键点
- 采用线性随机特征代理模型推导SGD训练的精确Volterra方程，将损失分解为传播未拟合目标误差的forcing项与传播随机误差的memory kernel项
- 定义两个调度核心坐标：衡量优化进度的内在时间$T_t=\sum_{s<t}\eta_s$，控制单位进度噪声注入的$r_t=B_t/\eta_t$
- 推导得到3+3(+2)缩放律区间：3个长记忆(LM)、3个可积记忆(IM)、2个有限块(FB)区间，给出不同区间下的最优训练调度速率公式
- 提出7参数forcing-memory surrogate模型，仅需在单种调度上拟合即可跨调度预测损失

### 关键实验
在124M、300M参数nanoGPT上验证，数据集采用OpenWebText、FineWeb、peS2o V2，对比8-1-1、WSD两种调度：① 相同$r$路径下，LR调度与Batch调度的损失在内在时间维度完全重合，预测误差<1%；② 单种调度拟合的surrogate零重训练预测其他调度损失的误差仅为最优拟合的1.03倍以内；③ 三个数据集拟合得到的$q_K$分别为1.017、0.952、0.995，均接近1，落在IM1/LM1边界。

最值得记住的一句话：LLM预训练的损失曲线由内在时间和Batch/学习率的比值唯一决定，与两者单独的取值无关。
