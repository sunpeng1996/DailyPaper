---
title: Strategic Buying Agents
title_zh: 策略性购物智能代理的决策框架设计
authors:
- Mingyang Fu
- Ming Hu
affiliations:
- Rotman School of Management, University of Toronto
arxiv_id: '2607.04708'
url: https://arxiv.org/abs/2607.04708
pdf_url: https://arxiv.org/pdf/2607.04708
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: 购物Agent 购买时机优化
tags:
- Shopping Agent
- Purchase Timing
- Optimal Stopping
- Bayesian Learning
- Robust Policy
one_liner: 针对代客购物Agent提出三种信息场景下的最优购买时机决策框架
practical_value: '- 做代客购物Agent的购买决策模块时，不要让LLM直接输出买/等决策，改为让LLM选择三种策略类型、校准输入参数，最终决策交由OR规则执行，效果远优于LLM直接判断

  - 商品历史价格数据充足的场景优先选用平稳域动态阈值策略，仅需解简单ODE即可实现，平均消费者剩余表现与更复杂的贝叶斯策略相当，工程落地成本极低

  - 新品、冷启动商品等价格历史稀疏的场景，采用鲁棒域随机阈值策略，可保障10分位消费者剩余最优，降低极端价格波动下的用户投诉率

  - 该策略可直接对接Keepa等第三方价格监控工具，作为电商价格提醒、代买服务的核心决策组件，适配3C、家电等价格波动较大的品类'
score: 9
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
Agent AI技术发展让代客购物成为可能，消费者可委托智能代理在指定截止日期前监控价格、完成指定商品购买，核心痛点是如何将价格观测数据、购物窗口期约束、未来价格波动的不确定性转化为可落地的最优买/等决策，过往研究大多侧重卖家端动态定价策略，极少从买家Agent视角覆盖不同信息完备度场景的决策设计。

### 方法关键点
- 划分三类信息场景构建策略菜单：①平稳域：已知价格调整泊松到达率、价格分布，最优决策为动态阈值策略，阈值随剩余购物时间变化，满足常微分方程可快速求解；②贝叶斯域：已知价格调整率、价格分布未知，阈值随观测到的价格数据更新后验信念动态调整，同时给出了分布未知带来的信息损失上界；③鲁棒域：仅知晓价格上下界，采用随机阈值策略，可同时保证最优竞争比和最小最大后悔。
- 提出LLM+OR混合架构：LLM仅负责策略类型选择、参数校准，核心买/等决策由OR规则执行。

### 关键实验
数据集采用Keepa跟踪的亚马逊367个商品、48933条带时间戳的价格观测数据，对比baseline包括立即购买/截止日购买、固定阈值（历史最低/均值/中位数）、LLM直接决策三类：平稳和贝叶斯策略的平均归一化消费者剩余比简单baseline高16%，鲁棒策略在10分位剩余上表现最优，LLM+OR方案比LLM直接决策的剩余高23%。

### 最值得记住的结论
LLM更擅长决策框架选择、参数校准这类认知类任务，而非数值敏感的时序最优决策。
