---
title: 'Inside the Trading Loop: Markets, Models, and Moves with LLM Agents'
title_zh: LLM多智能体混合交易系统的架构设计与性能评估
authors:
- Renee Jia
- Di Mu
- Yao Yu
- Tianrui Liu
affiliations:
- R2M AI
- Cornell University
- Carnegie Mellon University
- Shanghai Jiao Tong University
- University of California San Diego
arxiv_id: '2611.11657'
url: https://arxiv.org/abs/2611.11657
pdf_url: https://arxiv.org/pdf/2611.11657
published: '2026-11-07'
collected: '2026-11-18'
category: MultiAgent
direction: 多智体协作 · 金融决策系统优化
tags:
- MultiAgent
- LLM
- TradingSystem
- SelectiveInvocation
- StructuredResponse
one_liner: 设计融合LLM专业分析师、动量选股与规则执行的混合多智体交易系统，半年实盘收益超SPY 20个百分点
practical_value: '- 多智能体协作架构可迁移到电商大促选品/广告投放决策场景：将LLM专业分析师（用户舆情、大盘趋势分析agent）的结构化输出接入规则协调层，和传统统计策略（销量动量、价格弹性）加权融合，避免LLM输出不可控的问题

  - 选择性调用LLM的策略可直接复用：通过判断规则层输出距离决策阈值的距离，仅在边界场景调用LLM，既保留LLM增益又能降本70%以上，适合电商搜索推荐的query改写、商品打标等高频场景

  - 结构化响应合约的设计技巧可借鉴：缩短LLM输出字段、移除非必要解释性内容，能将解析失败率从27.7%降到0，同时要验证字段删减前后的决策一致性，避免输出合规但决策偏差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM驱动的决策系统多聚焦单智能体能力或工具调用，缺乏明确的LLM输出与传统统计策略融合的规则框架，难以平衡LLM的信息增益与决策的稳定性、可解释性要求，且相关研究多为回测验证，缺乏实盘运行的性能数据支撑。

### 方法关键点
- 采用分层混合架构：2个专用LLM分析师（公司舆情agent输出情感得分、宏观经济agent输出市场得分与仓位建议）+ 规则协调层 + 执行层，各层接口明确、权限可控
- 核心策略以集中动量选股为基准，LLM输出仅作为权重调整、仓位控制的增量输入，动量因子占权重的95%，LLM等复合信号仅占5%，严格限制LLM的决策影响范围
- 设计三级权限配置对比：L0纯规则无LLM、L1 LLM输出仅参与权重计算、L2 LLM宏观立场直接映射仓位，可量化不同融合方式的性能差异
- 提出阈值门控的选择性LLM调用策略，仅在规则得分接近决策边界时调用LLM，降低调用成本

### 关键结果
- 实盘运行周期2026.3.11-2026.8.28，纯规则版本收益34.5%，同期SPY收益14.4%、QQQ收益18.2%，最大回撤26.8%（SPY仅6.3%）
- 回测验证中L1、L2配置收益达55.5%~58.7%，均显著跑赢基准；仅在68%的日期调用LLM即可覆盖98%的LLM增益
- 精简LLM输出字段可将解析失败率从27.7%降至0，但会导致49%的宏观立场建议发生变化，需平衡解析成功率与决策一致性

### 核心结论
在LLM与传统规则结合的决策系统中，明确的权限边界、可控的影响范围比LLM的能力本身更重要，盲目放开LLM的决策权限反而可能带来不可控的风险。
