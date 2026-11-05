---
title: 'Pathwise-Budgeted LLM Routing: Online Allocation with K-Bit Tail-Cost Learning'
title_zh: 路径化预算约束下的LLM路由：基于K位尾成本学习的在线分配策略
authors:
- Hanzhang Qin
- Sophie H. Yu
- Yuewei Zhang
- Zhi-Hai Zhang
affiliations:
- National University of Singapore
- University of Pennsylvania
- Tsinghua University
arxiv_id: '2611.05835'
url: https://arxiv.org/abs/2611.05835
pdf_url: https://arxiv.org/pdf/2611.05835
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM路由优化 · 预算约束在线分配
tags:
- LLM Routing
- Contextual Bandit
- Online Allocation
- Budget Optimization
- Tail Cost Learning
one_liner: 提出K位尾成本估计的ADP-HT在线路由策略，固定LLM调用预算下最大化任务完成数
practical_value: '- 大模型调用成本优化场景（电商智能客服、Agent批量内容生成、LLM驱动个性化文案生成）可直接复用K位尾成本估计思路，无需精确预测token消耗，仅将输出长度分2^K个区间预测超阈值概率，大幅降低预测难度，同时控制超长响应用尽预算的风险

  - 可复用双速控制器设计：用快速更新的影子价格响应单次调用成本波动，用慢速更新的EMA移动平均平滑长期成本趋势，平衡预算利用率和超支风险，适合业务侧有固定月度大模型调用预算的场景

  - 重试门控逻辑可迁移至多轮LLM交互场景（用户query改写重试、商品属性抽取纠错重试），重试门槛随重试深度、已消耗预算动态提升，避免无效重试浪费预算'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
企业规模化部署LLM时普遍受固定调用预算约束，现有路由策略多基于单请求期望成本-收益权衡优化，未考虑路径化硬预算的终止风险：LLM响应长度服从重尾分布，单次超长响应可直接耗尽剩余预算，导致后续所有任务无法处理，且精确预测响应长度难度极高，无法用期望成本直接决策。
### 方法关键点
- 建模为K位路径化上下文背包问题，ADP-HT策略包含四大模块：混合奖励学习器融合共享任务难度特征与模型专属调整项，输出任务成功率的UCB估计，平衡探索与利用
- 成本学习器采用K位分桶机制，将响应长度划分为2^K个区间，仅预测各区间阈值的超越概率，构造保守成本上界，规避精确预测难题，K可平衡估计精度与分辨率
- 双速控制器：影子价格随单次调用成本快速更新，pacing乘数随近期成本EMA慢速调整，动态分配单任务预算配额，平衡预算利用率与超支风险
- 重试门控：重试门槛随重试深度、当前任务已消耗预算动态提升，避免无效重试浪费资源
### 关键结果
在MATH500、GPQA、RouterBench、LiveCodeBench上测试，对比Budget-aware LinUCB、ParetoBandit等基线：预算最紧张时完成的MATH500、GPQA任务数是最优基线的2倍以上；RouterBench上14个预算点中10个取得最高累计得分；低预算场景下性能超过商用路由的默认与成本节省模式。
### 核心结论
固定预算下的LLM路由不能仅优化单请求期望ROI，必须考虑重尾响应的预算耗尽风险，K位粗粒度成本估计比精确点估计更适配硬预算约束场景。
