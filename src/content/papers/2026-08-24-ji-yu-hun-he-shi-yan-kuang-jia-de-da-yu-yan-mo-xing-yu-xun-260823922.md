---
title: 'Data Mixing as Mixture Experiment: Response Surface Methodology and Optimal
  Design for Large Language Model Pretraining'
title_zh: 基于混合实验框架的大语言模型预训练数据配比优化方法
authors:
- Yicheng Mao
- Hongru Du
affiliations:
- University of Calgary
- University of Virginia
arxiv_id: '2608.23922'
url: https://arxiv.org/abs/2608.23922
pdf_url: https://arxiv.org/pdf/2608.23922
published: '2026-08-24'
collected: '2026-08-26'
category: Training
direction: LLM预训练优化 · 数据配比设计
tags:
- LLM Pretraining
- Data Mixing
- Response Surface
- Optimal Experimental Design
- Scheffé Model
one_liner: 将LLM预训练数据配比转化为混合实验，用响应面建模和最优设计降低proxy实验成本
practical_value: '- 垂直域LLM/SFT数据配比调优时，可复用稀疏二阶Scheffé模型拆解不同数据源（如商品描述/用户评论/客服对话）的加性与交互效应，快速定位互补数据源组合，降低配比试错成本

  - 做proxy小模型验证数据配比时，替换原随机采样策略为模型鲁棒I-最优设计选择实验点，可减少约25%的proxy训练量，大幅降低预训练/微调前的配比探索成本

  - 所有固定预算下的资源分配场景（如多模态训练模态占比、多任务SFT任务占比、Agent训练数据配比）都可套用该混合实验框架，替代黑盒调参提升可解释性与效率'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM预训练跨域数据配比直接决定模型效果与计算资源利用率，现有proxy-based配比优化方法多随机采样候选配比、用黑盒模型拟合性能，既无法解释域间交互效应，也存在大量冗余proxy实验，造成计算浪费。

### 方法关键点
- 将数据配比问题映射为经典混合实验框架：数据域为混合组分、token占比为组分比例、proxy训练为实验点、验证损失为 simplex 上的响应面
- 采用稀疏二阶Scheffé模型拟合响应面，可显式拆解单域加性效应与跨域两两交互效应，量化域间互补/竞争关系
- 采用模型鲁棒I-最优设计选择proxy实验点，降低全 simplex 上的平均预测方差，减少所需proxy训练次数

### 关键实验
基于公开RegMix数据集（含17个Pile数据域、512个1M参数proxy模型）验证，对比一阶Scheffé模型、LightGBM baseline：稀疏二阶Scheffé模型在1B规模下的Spearman秩相关达0.975，和LightGBM性能相当，可解释性大幅提升；模型鲁棒I-最优设计相比原随机Dirichlet采样，减少25%的proxy run即可达到原512次实验的排序精度。

### 核心结论
大模型预训练数据域的价值是高度关系型的，弱加性效应的域可通过和其他域（如web文本）的交互大幅提升整体效果，无需孤立评估单域质量。
