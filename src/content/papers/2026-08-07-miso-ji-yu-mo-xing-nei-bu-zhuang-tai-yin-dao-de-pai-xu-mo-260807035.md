---
title: 'MISO: Model-Internal-State-Guided Optimization for Ranking Models'
title_zh: MISO：基于模型内部状态引导的排序模型优化框架
authors:
- Yongzhe Zhang
- Xiaoyu Deng
- Yifan He
- Mengying Sun
- Sheng Luo
- Yijia Liu
- Hao Yan
- Zhuo Li
- Yi Meng
- Huiping Yao
affiliations:
- Meta Inc
arxiv_id: '2608.07035'
url: https://arxiv.org/abs/2608.07035
pdf_url: https://arxiv.org/pdf/2608.07035
published: '2026-08-07'
collected: '2026-08-10'
category: RecSys
direction: 排序模型优化 · 迭代效率提升
tags:
- Ranking Model
- Model Optimization
- Ads Recommendation
- Model Internal State
- AutoML
one_liner: 提出模型内部状态引导的排序优化框架，大幅降低调参试错成本同时提升排序效果
practical_value: '- 可直接复用三类MIS聚合原语设计：通过神经元重要性排序指导模块裁剪/扩容、分布对齐得分指导Normalization模块调优、跨模型对比定位性能差异根因，替代盲目试错

  - 优化现有排序模型迭代流程：在固定模型架构的日常迭代场景下，引入MISO框架可减少80%+的训练试次，大幅节省GPU资源与迭代周期，尤其适配广告、电商排序的高频迭代需求

  - 适配工程团队现有工作流：MISO输出的优化建议直接对应模块级修改，可解释性强，无需推翻现有架构即可落地，可与专家经验形成互补'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界大规模广告、电商排序模型的迭代优化长期依赖专家经验试错或黑盒AutoML，前者可复现性差、效率波动大，后者需要消耗大量训练资源且优化逻辑不可解释；而已有训练完成的排序模型内部包含参数、激活值、梯度、归一化统计量等大量高价值信号，却未被系统性纳入优化决策链路，造成信号浪费与迭代效率瓶颈。
### 方法关键点
- 采用三层架构设计：MIS抽取层统一抽象多类型模型内部信号，屏蔽不同模型与训练框架的底层差异；分析聚合层通过三类可复用原语处理高维异构信号：排序类原语融合梯度与扰动信号计算神经元重要性得分，对齐类原语通过层激活分布与标准正态分布的KL散度判断模块稳定性，对比类原语跨模型/训练阶段对比信号定位性能差异根因；决策层将聚合信号映射为模块扩容、裁剪、替换等可直接落地的操作。
- 支持闭环自适应迭代：每次模型重训后重新抽取MIS，自动适配数据分布与系统需求的动态变化。
### 关键实验结果
在Meta十亿级样本的广告排序数据集上，对比专家驱动调优、黑盒容量扩容两个基线，在13x/20x/32x/50x多种模型规模下，MISO取得的相对Normalized Entropy（NE）提升是专家方案的2.0~2.5倍，所需训练试次仅3~12次，相比专家方案的50~92次减少84%~94%的探索成本；三类聚合原语叠加使用可取得最优效果。
### 核心结论
在固定模型家族的高频局部优化场景下，模型内部状态是介于人工经验与黑盒AutoML之间的高性价比优化信号，可在不损失可解释性的前提下大幅降低迭代成本。
