---
title: 'An Epistemic Position-Based Click Model: From Interactions to Epistemic Distributions
  of Relevance and Bias'
title_zh: 基于认知不确定性的位置点击模型：解耦相关性与位置偏差分布
authors:
- Oscar Rolando Ramirez Milian
- Harrie Oosterhuis
affiliations:
- University of Amsterdam
- Radboud University Nijmegen
arxiv_id: '2607.18712'
url: https://arxiv.org/abs/2607.18712
pdf_url: https://arxiv.org/pdf/2607.18712
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 推荐系统 · 点击建模与偏差去偏
tags:
- ClickModel
- EpistemicUncertainty
- PositionBias
- EvidentialDeepLearning
- UnbiasedLTR
one_liner: 首个基于证据深度学习的上下文认知点击模型，输出相关性与位置偏差的Beta分布并量化认知不确定性
practical_value: '- 业务点击建模可直接引入Beta分布输出相关性和位置偏差的不确定性，针对长尾query/商品/新流量位的低置信度估计单独做策略兜底，比如召回补充、排序降权或流量灰度

  - 优化证据深度学习类模型时，可复用本文的log-sum-exp数值稳定、低维变量条件采样降方差、梯度自归一化三个工程trick，避免训练不稳定或不收敛

  - 熵正则化权重推荐设置在1e-3量级，既能保持预测精度，又能避免模型坍缩成点估计，输出的置信度可直接用于排序结果的风险控制

  - 该认知PBM比传统点估计PBM收敛速度快10倍以上，测试集log-likelihood更高，可直接替换现有业务中的点击偏差估计模块'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有位置点击模型（PBM）仅输出相关性和位置偏差的点估计，无法量化认知不确定性，无法衡量估计的可靠度，尤其在长尾query、新商品、新流量位等数据稀疏场景下易出现严重估计偏差，也无法支撑下游排序策略的风险控制需求。
### 方法关键点
- 基于证据深度学习框架，为每个位置的偏差参数、每个query-item对的相关性参数各拟合一个Beta分布，分别捕获两者的认知不确定性
- 三大工程优化trick：用log-sum-exp运算解决似然值过小的数值下溢问题；对低维位置偏差变量条件采样降低梯度估计方差；梯度自归一化解决似然值接近0导致的梯度消失问题
- 加入按参数数量归一化的熵正则项，避免模型坍缩为点估计，平衡预测精度与不确定性表达能力
### 关键结果
在MSLR-Web10K、Istella-S两个公开排序数据集上做半合成实验，对比传统点估计PBM、朴素蒙特卡洛估计等基线：
- 采用本文优化trick的认知PBM测试集log-likelihood比点估计PBM高约5%，收敛速度快12倍（100轮 vs 1200轮收敛）
- 熵正则权重设为1e-3时，模型预测精度下降<1%，同时输出的不确定性分布校准度最优
- 下游排序评估任务上，认知PBM预测精度与点估计相当，同时可输出预测置信度用于风险衡量

**最值得记住的一句话**：引入认知不确定性的点击模型不仅不会损失预测精度，反而因为初始状态更中立，收敛更快、效果更优，还能额外提供置信度用于业务风险控制。
