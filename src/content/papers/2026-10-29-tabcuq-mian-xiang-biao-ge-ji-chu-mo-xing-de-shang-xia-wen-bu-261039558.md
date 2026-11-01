---
title: 'TabCUQ: Context-Uncertainty Quantification for Tabular Foundation Models'
title_zh: TabCUQ：面向表格基础模型的上下文不确定性量化
authors:
- Yuebei Shi
- Molei Liu
- Zijian Guo
affiliations:
- School of Mathematics, Zhejiang University
- Center for Data Science, Zhejiang University
- Department of Biostatistics, Peking University Health Science Center
- Beijing International Center for Mathematical Research, Peking University
arxiv_id: '2610.39558'
url: https://arxiv.org/abs/2610.39558
pdf_url: https://arxiv.org/pdf/2610.39558
published: '2026-10-29'
collected: '2026-11-01'
category: Eval
direction: 表格基础模型 · 不确定性量化评估
tags:
- Tabular Foundation Model
- Uncertainty Quantification
- In-Context Learning
- Wild Bootstrap
- Perturbation
one_liner: 提出扰动驱动的TabCUQ框架，同时量化表格基础模型的两类上下文不确定性
practical_value: '- 电商冷启动用户/商品的小样本转化预估、分群建模场景，可复用wild-bootstrap扰动方案量化上下文波动，规避传统bootstrap的高估问题

  - 小样本in-context learning场景下的模型偏差估计，可直接复用扰动预测与原预测的最大偏差指标，无需额外标注即可量化有限上下文偏置

  - 营销补贴、广告投放等高风险业务决策的可信评估环节，可引入该框架生成具备统计覆盖保证的置信区间，降低决策失误风险'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
表格基础模型基于in-context learning实现小样本条件期望、平均处理效应估计时，现有不确定性量化方法无法同时覆盖两类核心误差：推理阶段小样本带来的有限上下文偏差、上下文波动，且普通bootstrap会高估波动、子采样会低估波动，难以支撑高可信决策。
### 方法关键点
提出扰动驱动的TabCUQ框架：对观测输出注入噪声生成扰动上下文输入给基础模型，通过wild-bootstrap离散度估计上下文波动，用扰动预测与原预测的最大偏差量化有限上下文偏差，同时覆盖两类不确定性来源。
### 关键结果数字
模拟实验中覆盖度显著提升，平均区间宽度约为有偏先验基准的2倍；在7个真实世界任务中，对大样本训练得到的参考函数的覆盖度也有明显改善。
