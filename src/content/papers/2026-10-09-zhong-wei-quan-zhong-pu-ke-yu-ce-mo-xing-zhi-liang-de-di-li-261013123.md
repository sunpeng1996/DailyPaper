---
title: Why Heavy-Tailed Weight Spectra Predict Model Quality
title_zh: 重尾权重谱可预测模型质量的底层原理研究
authors:
- Joseph Wilson
- Chris van der Heide
- Liam Hodgkinson
- Zhichao Wang
- Fred Roosta
- Michael W. Mahoney
affiliations:
- University of Queensland
- University of Melbourne
- University of California, Berkeley
- ICSI
- LBNL
arxiv_id: '2610.13123'
url: https://arxiv.org/abs/2610.13123
pdf_url: https://arxiv.org/pdf/2610.13123
published: '2026-10-09'
collected: '2026-10-13'
category: Eval
direction: 模型质量评估 · 权重谱分析
tags:
- Model Evaluation
- Heavy-Tailed Spectra
- DNN
- LLM
- Generalization
- Overfitting
one_liner: 从统计视角解释重尾权重谱预测模型质量的机理，推导最优重尾参数可预测DNN与LLM过拟合
practical_value: '- 训练推荐/广告域DNN、LLM4Rec模型时，可统计输出层权重的重尾参数快速评估泛化能力，无需验证集即可提前发现过拟合，降低训练成本

  - 小样本微调推荐/Agent专属LLM时，可将权重谱重尾度作为早停指标，避免私有小数据集的验证集信息泄露风险

  - 选型第三方预训练LLM做推荐下游任务时，可通过权重谱指标快速筛选泛化能力优的基座，无需全量下游任务验证'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：现有依赖训练数据的DNN/LLM质量评估指标计算成本高，无训练数据时无法使用；已观测到的权重重尾谱可预测模型质量的现象缺乏严谨统计支撑。
**方法关键点**：1. 基于概率框架推导仅用最后一层权重即可计算的DNN边际似然作为模型质量预测指标；2. 推导服从重尾HTMP分布的谱的极限对数边际似然，证明其在重尾参数上为凸函数，得到最优重尾参数。
**关键结果**：在大规模卷积DNN、LLM上验证边际似然可有效预测模型质量，推导的最优重尾参数可准确预测模型过拟合状态。
