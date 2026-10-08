---
title: 'SOTA: Stock Options Trading Agents Guided by Option-Implied Return Distributions'
title_zh: SOTA：基于期权隐含收益分布引导的股票期权交易智能体
authors:
- Yizhen Xie
- Mengyang Liu
affiliations:
- Carnegie Mellon University
- Amazon
arxiv_id: '2610.10407'
url: https://arxiv.org/abs/2610.10407
pdf_url: https://arxiv.org/pdf/2610.10407
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent 金融交易策略优化
tags:
- Trading Agent
- Supervised Fine-Tuning
- Reinforcement Learning
- LLM
- Portfolio Optimization
one_liner: 提出结构化期权策略选择Agent框架，通过SFT+RL训练大模型实现更高交易收益
practical_value: '- 大候选集降维思路：可迁移到电商全量商品/广告推荐场景，先抽象为上层品类/场景级策略决策，再由确定性模块落地具体item选择，大幅降低Agent动作空间复杂度

  - 训练流程复用：先SFT对齐优质人工/规则策略轨迹，再做RL优化的两阶段范式，适合搜索推荐多目标优化场景的Agent训练

  - 特征分阶段消融：非结构化特征（如用户评论、热点新闻）可能在SFT阶段提效但RL阶段引入过拟合，可做分阶段特征有效性验证，避免负向收益'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有期权交易Agent要么单合约独立预测收益，要么限制策略为固定结构（如跨式套利），无法随市场动态调整，且单标的数千级合约的大决策空间难以直接优化。
### 方法关键点
1. 分层决策架构：将海量期权合约选择抽象为上层策略级决策，下层由确定性解析器完成具体投资组合落地，大幅压缩动作空间
2. 两阶段训练：先对Qwen3.8-27B做SFT对齐优质策略轨迹，再通过RL做策略迭代优化
3. 分阶段验证非结构化特征（新闻）的不对称作用
### 关键结果
6个月外样本测试期总收益18.3%，夏普率1.60，最大回撤8.96%；仅SFT阶段引入新闻、RL阶段移除的方案最优，RL阶段保留新闻会导致收益降至-2.7%。
