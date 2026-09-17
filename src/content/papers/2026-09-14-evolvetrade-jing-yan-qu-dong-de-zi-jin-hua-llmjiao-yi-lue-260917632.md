---
title: 'EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading
  Agents'
title_zh: EvolveTrade：经验驱动的自进化LLM交易Agent策略优化框架
authors:
- Sehee Kim
- Yumin Choi
- Minki Kang
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2609.17632'
url: https://arxiv.org/abs/2609.17632
pdf_url: https://arxiv.org/pdf/2609.17632
published: '2026-09-14'
collected: '2026-09-17'
category: Agent
direction: Agent自进化 · 策略在线优化
tags:
- LLM Agent
- Self-Evolution
- Policy Optimization
- Tool Calling
- Prompt Tuning
one_liner: 通过独立Policy Agent在线迭代工具调用策略，无需微调LLM即可提升交易Agent收益表现
practical_value: '- 可复用低代码Agent自进化架构：无需微调底座LLM，仅通过独立策略Agent迭代工具调用/决策流程的system prompt，即可适配非稳态业务环境（如电商大促、用户偏好漂移），大幅降低模型重训成本

  - 反馈闭环设计技巧：将决策轨迹（含每步推理依据）和事后业务反馈绑定作为策略迭代输入，解决稀疏/延迟反馈下的优化歧义问题，可迁移到广告投放、权益分配等延迟反馈场景

  - 迭代频率调优经验：每N个决策周期迭代一次策略（最优为5个周期）优于高频更新，避免过拟合短期噪声，可直接复用在推荐系统、广告投放的策略迭代周期配置上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具调用型LLM Agent的信息采集、证据验证、决策规则都由部署前人工编写的固定prompt控制，无法适配市场风格切换、用户偏好漂移等非稳态环境；固定策略会限制Agent主动激活场景适配的分析能力，比如金融下跌行情下不会自动调用VaR等尾部风险指标，电商大促场景下不会主动调用转化率预估工具，导致表现大幅下降。
### 方法关键点
- 把业务Agent的system prompt作为文本化可优化的策略参数，底座LLM和工具接口全程冻结，无需任何微调即可完成迭代
- 每N个决策周期（最优为5天）收集一批决策轨迹（含每步推理依据、工具调用记录）和实际业务反馈，交给独立的Policy Agent迭代生成新的策略prompt
- 策略迭代要求Policy Agent基于真实反馈做具象化修改，禁止泛泛改写，比如新增「新闻信号必须搭配价格验证才可调高仓位」这类可落地的规则
### 关键结果
在美股6种不同市场风格（横盘、下跌、上涨等）下，测试GPT-5-mini和Gemini-2.5-Flash两个底座，对比固定策略工具调用Agent、固定策略无工具Agent等基线：
- GPT-5-mini在2025年9月上涨行情下，累计收益达6.84%，超过所有规则基线和LLM基线，夏普比达2.01
- 2025年1月NVDA回调案例中，优化后的策略自动降低NVDA仓位从10.7%到2.9%，躲过次日17%的暴跌，单日相对收益高1.33个百分点
- 策略迭代后代码工具调用量从日均1次提升到2.6-4.5次，主动激活了固定策略从未调用的VaR、EMA、RSI等场景适配指标
> 最值得记住的一句话：对于工具调用型LLM Agent，优化其决策流程的system prompt，往往比新增工具、提升底座能力更能适配非稳态业务环境，且成本极低
