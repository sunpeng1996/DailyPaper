---
title: 'Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting'
title_zh: 面向开放世界的未来预测递归自进化智能体框架DeepEvolve
authors:
- Zhipeng Chen
- Yunsen Liang
- Yanxi Chen
- Hongkang Zhao
- Lingyun Feng
- Ruiyang Ren
- Guoxin Chen
- Jia Deng
- Feng Chang
- Chuan Hao
affiliations:
- Renmin University of China
- IQuest Research
- Nanyang Technological University
arxiv_id: '2610.29784'
url: https://arxiv.org/abs/2610.29784
pdf_url: https://arxiv.org/pdf/2610.29784
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: Agent 递归自进化与环境共优化
tags:
- Recursive Self-Improvement
- Agent Evolution
- Forecasting
- LLM Agent
- Open World
one_liner: 与开放世界共进化的递归自改进预测智能体DeepEvolve，在公开预测榜单连续三周登顶，性能最高提升195%
practical_value: '- 搜索-预测解耦设计可直接复用在电商大促销量预测、动态广告投放场景：在数据可获取的窗口期提前缓存实时特征，后续用离线更新的推理模块做决策，彻底避免数据泄露和环境污染问题

  - 参数+技能双路径进化思路适配生成式推荐系统迭代：高频更新轻量外部技能库（如选品规则、话术模板）适配动态变化的用户需求和平台规则，低频用RL更新模型核心参数，平衡迭代效率和计算成本

  - 动态环境进化机制可用于推荐系统冷启动与能力补全：基于现有模型的bad case自动生成针对性测试任务和训练样本，持续补全推荐系统的能力短板，避免静态数据集导致的过拟合和能力固化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI系统参数冻结、依赖人工更新迭代，递归自改进（RSI）是自主智能体的核心能力，但长期缺乏动态、可验证、有真实反馈的开放环境支撑。未来事件预测天然具备非静态、结果可验证、接地真实世界的属性，是RSI研究的理想测试场景。

### 方法关键点
DeepEvolve采用三模块闭环架构：
- Prometheus活数据环境实时接入新闻，生成结果可验证的动态预测任务
- Branchus智能体预测器拆分搜索/预测团队，提前缓存预测窗口期的证据，避免后续训练时的数据污染
- Athena递归进化引擎从预测轨迹中萃取能力，实现三层进化：参数层用真实结果作为奖励的RL、成功轨迹微调更新预测模块；行为层将推理轨迹蒸馏为可复用技能库，无需梯度更新即可在推理时调用；环境层从模型失败案例中蒸馏任务生成技能，自动生成针对性难例任务，持续驱动智能体能力提升。

### 关键结果
- 在每周更新的公开FutureX预测榜单上，连续三周排名所有系统第一，评分最高提升195%
- 自建动态预测评测集上，搭配4个不同基座LLM均进入Top3，Bradley-Terry得分最高超出最强基线10.7分
- 仅262条实时轨迹蒸馏的技能库即可将预测MAPE从2.80%降至2.28%，Brier score降低0.013；双路径进化+环境共进化的组合效果显著优于单一优化方式

最值得记住的一句话：AI进化方向正从固定数据集训练静态模型，转向开放动态环境中培育能从自身经验持续成长的智能体，环境的开放性是能力天花板的核心决定因素。
