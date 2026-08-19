---
title: Conditional Evaluation of Language Models with Cheap Auxiliary Signals
title_zh: 基于廉价辅助信号的大语言模型条件性能评估方法
authors:
- Zhi Zhang
- Lingfeng Lyu
- Yue Kang
- Doudou Zhou
affiliations:
- University of California, Los Angeles
- University of Science and Technology of China
- Microsoft
- National University of Singapore
arxiv_id: '2608.16210'
url: https://arxiv.org/abs/2608.16210
pdf_url: https://arxiv.org/pdf/2608.16210
published: '2026-08-17'
collected: '2026-08-19'
category: Eval
direction: LLM评估 · 半监督廉价信号利用
tags:
- LLM Evaluation
- Semi-supervised Learning
- Control Variate
- Auxiliary Signal
- Performance Profiling
one_liner: 提出半监督评估框架LACE，利用廉价辅助信号实现无偏低标注成本的LLM细粒度条件性能评估
practical_value: '- 做LLM4Rec、Agent业务的效果评估时，可复用LACE的局部中心化思路，用LLM打分、置信度等廉价信号替代部分人工标注，大幅降低分场景、分人群的细粒度性能评估成本

  - 评估多版本推荐/Agent模型的分维度效果差时，可直接复用论文的配对模型gap estimator，不需要给全量样本打金标即可得到无偏的细分维度效果差统计

  - 业务上线前的模型灰度评估，可复用部署加权分数估计方法，结合线上流量分布特征，用少量标注得到更贴近真实线上表现的评估结果'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
聚合精度指标无法体现LLM在细分任务/属性维度的性能差异，仅靠金标估算条件性能剖面的标注成本极高；现有全量可收集的廉价辅助信号（LLM judge打分、置信度、配对比较结果等）普遍存在偏置、校准差的问题，无法直接用于无偏评估。

### 方法关键点
提出半监督条件评估框架LACE：1. 核心采用局部中心化操作，先减去目标剖面区域内廉价信号的条件均值，保证线性增强的条件均值为0，不改变待估参数；2. 用局部岭控制变量，结合标注子集的金标残差均值、全量样本池的廉价信号均值做估计，仅用增强系数提升评估效率，不引入偏置；3. 理论证明该方法无需校准、分组剖面无偏、在中心化线性增强类内达到局部oracle最优，还可扩展到配对模型差、部署加权分数两类评估场景。

### 关键结果
在MATH-500、ScienceQA、MMLU等8个主流LLM基准数据集上验证有效性，评估效率提升幅度由廉价信号与金标的局部R²决定，局部R²越高的剖面维度，标注成本节约越显著
