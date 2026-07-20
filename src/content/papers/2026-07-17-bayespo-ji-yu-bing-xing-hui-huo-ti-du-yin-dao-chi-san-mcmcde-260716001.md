---
title: 'BayesPO: Bayesian Prompt Optimization via Parallel-Tempered Gradient-Guided
  Discrete MCMC'
title_zh: BayesPO：基于并行回火梯度引导离散MCMC的贝叶斯Prompt优化
authors:
- Junjie Zhou
- Zhijian Ou
affiliations:
- Tsinghua University, SPMI Lab
arxiv_id: '2607.16001'
url: https://arxiv.org/abs/2607.16001
pdf_url: https://arxiv.org/pdf/2607.16001
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 大语言模型 · 自动Prompt优化
tags:
- Prompt Optimization
- MCMC
- Parallel Tempering
- Bayesian Sampling
- LLM
one_liner: 提出结合梯度引导离散MCMC与并行回火的贝叶斯prompt优化框架，APE基准准确率提3.19个点
practical_value: '- 电商/广告场景的定制化prompt（如商品文案生成、query意图识别、广告定向话术）可复用BayesPO的后优化逻辑，以人工/APE生成的prompt为初始化，用少量业务标注样本构建能量函数迭代调优，降低人工调prompt的成本

  - 并行回火的多温度链探索机制可直接迁移到搜索推荐的离散优化场景（如query改写、短标题优化、标签组合召回），解决传统贪心优化容易陷入局部最优的问题

  - 能量函数设计思路可复用：将业务目标（如点击率拟合度、转化率匹配度）作为似然项、文本自然度作为LLM先验项，平衡优化目标的效果和可读性，避免生成生硬的prompt或文案

  - 小样本prompt优化需警惕过拟合风险：当优化样本少于10条时，即使训练能量持续下降也要做线上小流量验证，避免拟合样本噪声导致泛化效果下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自动prompt优化方法多为启发式搜索流程，要么做局部贪心编辑，要么依赖LLM生成候选，没有显式定义prompt的后验分布，容易陷入局部最优，且小样本下泛化性缺乏理论保障，亟需一套有概率理论支撑的离散prompt优化框架。
### 方法关键点
- 将prompt优化建模为离散token空间的贝叶斯后验采样问题，能量函数由两部分组成：任务似然项衡量prompt匹配输入输出样例的程度，LLM先验项约束prompt本身的流畅度，低能量对应高后验概率。
- 采用MH校正的Gibbs-with-Langevin（GwL）采样器，逐位更新prompt token，基于能量梯度生成离散候选，解决全序列更新接受率过低的问题，同时适配非权重绑定的主流LLM嵌入结构。
- 集成并行回火机制，运行多条不同温度的MCMC链，高温链负责宽范围探索、低温链保留优质候选，通过链间状态交换实现全局探索，跳出局部最优。
### 关键结果
在24个任务的APE指令诱导基准上，以APE生成的prompt为初始化，平均测试准确率从60.04%提升至63.23%，其中初始prompt语义偏差大的任务最大提升达53个百分点；控制实验证实并行回火可100%解决诗歌补全任务的局部最优陷阱。
### 核心结论
prompt优化中训练能量下降不必然对应测试效果提升，小样本下能量最小化容易过拟合优化集的噪声特征，能量函数设计和样本代表性是泛化效果的核心影响因素。
