---
title: 'Training-Free versus Training-Based Intent Classification in LLMs: Accuracy,
  Robustness, and Failure Modes'
title_zh: 大语言模型免训练与基于训练的意图分类对比：精度、鲁棒性与失效模式
authors:
- Nan Chen
- Zhouhao Yang
- Soufiane Hayou
affiliations:
- Johns Hopkins University
arxiv_id: '2608.02415'
url: https://arxiv.org/abs/2608.02415
pdf_url: https://arxiv.org/pdf/2608.02415
published: '2026-08-03'
collected: '2026-08-04'
category: LLM
direction: LLM意图分类 · 路由模块选型
tags:
- Intent-Classification
- LLM-Routing
- Training-Free
- Robustness
- Activation-Statistics
one_liner: 系统对比LLM免训练与基于训练的意图分类方法，提出两款超轻量免训练方案并给出选型逻辑
practical_value: '- 电商客服/导购Agent的粗粒度路由（如商品咨询/售后/活动咨询）可直接用VecStat/NormStat，无需训练，新增意图仅需计算对应类的统计量，适配快速迭代的业务需求

  - 若业务输入噪声大（如用户乱输入、带混淆关键词的query），优先选用免训练分类方法，对抗场景下精度比训练得到的MLP头高40pct以上，减少路由错误

  - 细粒度意图分类（如区分不同品类的商品咨询）优先选择训练类方法，细粒度任务下精度比免训练方案高15-25pct，适合分类体系固定的场景

  - 工程上可实现分层路由：先用极轻量的NormStat做粗分类，高置信样本直接路由，低置信样本再调用MLP/VecStat做细分，兼顾推理效率与分类精度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM系统普遍采用路由架构，意图分类作为流量入口直接决定系统效率与效果，但现有方案存在明显缺陷：训练类分类头标注成本高、新增类别需重训，直接调用LLM做分类推理成本高、校准难度大，亟需明确不同场景下的选型逻辑，同时探索更低成本的分类方案。
### 方法关键点
- 免训练方案：提出VecStat与NormStat，均基于LLM prefill阶段的激活统计量实现分类，无需梯度更新，仅需少量校准样本计算各类别的基准统计量；其中VecStat用坐标级的均值/方差做匹配，NormStat仅用激活的归一化范数的均值/方差做匹配，存储成本极低。
- 对比基线：覆盖基于LLM最后层激活的Avg-MLP、Tail-MLP、线性探针三类训练类方法，以及零/少样本LLM直接分类方案。
- 构造混合意图数据集、3级难度的对抗重写数据集，系统测试不同方法的鲁棒性与失效模式。
### 关键结果
在1B-32B的Llama、Qwen系列模型上测试7个基准数据集：
1. 粗粒度分类任务（如文本/数学/代码区分）两类方法精度均可达99%+；
2. 细粒度分类任务（如数学子领域区分）训练类方法平均精度70%+，比免训练方法高15-25pct；
3. 混合意图场景下VecStat的校准RMSE比MLP低30%+，对抗样本场景下免训练方法精度比MLP高40pct以上；
4. NormStat仅需O(m)存储（m为类别数），千类场景下存储仅1.7MB，比MLP方案低3个数量级。
> 最值得记住：没有通用最优的意图分类方案，粗分类/高噪声场景优先选免训练方法，细分类/标注充足场景优先选训练类方法。
