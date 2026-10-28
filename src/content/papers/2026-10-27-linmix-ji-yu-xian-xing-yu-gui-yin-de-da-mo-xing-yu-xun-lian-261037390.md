---
title: 'LinMix: Data Mixing as Linear Domain Attribution'
title_zh: LinMix：基于线性域归因的大模型预训练数据混合方法
authors:
- Hubert Baniecki
- Przemyslaw Biecek
- Martin Pawelczyk
affiliations:
- University of Warsaw
- Centre for Credible AI, Warsaw University of Technology
- Faculty of Computer Science, University of Vienna
arxiv_id: '2610.37390'
url: https://arxiv.org/abs/2610.37390
pdf_url: https://arxiv.org/pdf/2610.37390
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM预训练 · 数据混合优化
tags:
- DataMixing
- DomainAttribution
- LLMPretraining
- ExperimentalDesign
- LinearRegression
one_liner: 提出无超参数的顶点采样数据混合方法，通过线性域归因实现LLM预训练数据配比优化，效果超Dirichlet采样基线
practical_value: '- 垂直域LLM微调场景可复用顶点采样方法快速估算各训练域的贡献度，替代网格搜索调混合比例，降低调参成本

  - 多任务推荐模型训练数据加权场景，可复用线性域归因框架，无需复杂非线性拟合即可快速定位高价值任务/数据域

  - 训练数据选型时可参考「仅保留正归因域」规则，快速过滤低价值训练数据，降低训练成本同时提升下游效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM预训练数据混合方法依赖Dirichlet采样训练小代理模型再拟合回归预测最优配比，需要大量超参数调优，且当域数量增长到上百级时线性拟合失效，归因误差高，无法高效得到最优数据混合比例。

### 方法关键点
1. 遵循D最优实验设计思路，在带上限约束的单纯形顶点采样混合比例，无超参数，每个域要么取采样上限要么占比为0，天然解耦域间效应
2. 拟合线性回归即可得到各域的归因系数，仅保留系数为正的域，最优混合比例直接按系数从高到低填充对应域的上限即可，无需额外候选集搜索
3. 支持引入曲率参数r适配数据重复的边际收益递减场景，r=1时对应对数效用，为所有正归因域分配非零权重

### 关键结果
在200B token的WebOrganizer语料上实验，对比RegMix、OLMix等SOTA基线：1B参数OLMo2模型在288细粒度域设置下平均准确率相对提升11%；4B参数Qwen3.5模型上MBPP代码基准相对提升46%，GSM8K数学基准相对提升14%。

**最值得记住的一句话**：数据混合优化的核心是尽可能解耦各域的效应，而非依赖复杂的非线性拟合模型，无超参数的顶点采样能大幅降低域归因的误差，线性模型即可达到SOTA效果。
