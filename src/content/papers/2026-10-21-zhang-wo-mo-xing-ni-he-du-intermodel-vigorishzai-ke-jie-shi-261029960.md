---
title: 'Mastering Model Fit: Applications of the InterModel Vigorish for Interpretable
  Machine Learning'
title_zh: 掌握模型拟合度：InterModel Vigorish在可解释机器学习中的应用
authors:
- Jiani Yan
- Pengyun Wang
- Klint Kanopka
- Ben Domingue
- Charles Rahal
affiliations:
- University of Oxford
- University of Chicago
- New York University
- Stanford University
arxiv_id: '2610.29960'
url: https://arxiv.org/abs/2610.29960
pdf_url: https://arxiv.org/pdf/2610.29960
published: '2026-10-21'
collected: '2026-10-23'
category: Eval
direction: 可解释机器学习 · 模型拟合度评估
tags:
- Interpretable ML
- Model Evaluation
- IMV
- SHAP
- Ablation Study
- Open Source
one_liner: 将IMV适配到可解释ML场景，推出3种衍生评估工具与配套开源库
practical_value: '- 可引入Ablate-IMV快速评估推荐/广告模型的特征组、架构模块对拟合效果的实际贡献，弥补纯AUC/ACC评估的盲区

  - 用SHAP-IMV做推荐特征重要性排序，相比普通SHAP可直接量化不同特征相对于基线模型的收益，指导特征迭代

  - 多分类场景可采用Multi-IMV评估商品/类目分类模型的类间区分能力，识别表现差的类目针对性优化'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
仅靠准确率、AUC等常规指标无法明确特征、模型组件对概率拟合的具体贡献，也无法量化不同模型相对基线的实际提升幅度，缺少统一可解释的拟合度对比标准。
### 方法关键点
将原用于二分类概率预测对比的InterModel Vigorish（IMV）适配到通用机器学习场景，推出3种衍生工具：① SHAP-IMV基于Shapley加权子集对比将拟合增益归因到单个特征；② Multi-IMV评估多分类场景下一对多、两两类别的区分能力；③ Ablate-IMV通过消融实验评估架构组件、特征组的贡献。
### 关键结果数字
在10组随机种子、6个图分类基准数据集上验证，200轮训练的时间剖面测试显示：高一对多准确率可能伴随相对于空模型的可忽略提升，固定训练预算下消融部分组件甚至可保留或提升拟合效果，配套开源imvpy库可直接复用。
