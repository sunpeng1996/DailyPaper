---
title: Learning Bidirectional Causal Interactions with Heteroscedastic Neural Networks
title_zh: 基于异方差神经网络的双向因果交互学习
authors:
- Masahiro Tanaka
affiliations:
- Faculty of Economics, Fukuoka University
arxiv_id: '2607.22313'
url: https://arxiv.org/abs/2607.22313
pdf_url: https://arxiv.org/pdf/2607.22313
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 因果推断 · 双向交互效应估计
tags:
- causal-inference
- heteroscedastic-neural-network
- simultaneous-equations
- observational-data
- SEM-DNN
one_liner: 提出无需外部工具变量的SEM-DNN模型，可从观测数据识别双向结构因果交互效应
practical_value: '- 电商调价效果评估场景可直接复用SEM-DNN，无需寻找额外工具变量即可准确估计价格与销量的双向因果效应，避免内生性导致的效果错估

  - 搜索推荐场景中用户行为与曝光策略的双向反馈拆解可借鉴该方法，剥离循环反馈的干扰，得到真实的曝光策略增益，优化流量分配逻辑

  - 营销干预因果评估缺工具变量时，可尝试利用数据异方差特性套用该识别逻辑，降低因果推断的落地门槛'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
从观测数据估计同期双向因果交互存在严重内生性问题，传统灵活回归仅能捕捉简化形式的依赖关系，因果识别通常依赖难获取的外部工具变量。
### 方法关键点
提出SEM-DNN异方差神经联立方程估计器，利用条件协方差对角化实现因果识别，无需外部工具：当结构冲击满足零条件均值、给定协变量时条件不相关、条件方差非比例的假设时，仅真实交互系数可在全特征空间对角化条件残差协方差；模型通过引入联立系统雅可比的对角高斯拟似然，联合拟合非线性结构均值函数和特征依赖的方差。
### 关键结果
蒙特卡洛实验显示，随数据量提升，SEM-DNN比参数方法、核方法、单方程神经网络更可靠地还原结构效应，仅计算成本更高；在即食麦片扫描数据集上可有效估计价格-销量同期双向反馈，验证了识别有效性。
