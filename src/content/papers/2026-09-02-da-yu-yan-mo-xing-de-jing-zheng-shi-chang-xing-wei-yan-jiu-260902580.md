---
title: Competitive Market Behavior of LLMs
title_zh: 大语言模型的竞争市场行为研究
authors:
- Pawel Struski
- Jakub Swistak
- Inez Okulska
- Przemyslaw Biecek
affiliations:
- University of Warsaw
- Warsaw University of Technology
- Centre for Credible Artificial Intelligence (CCAI)
- Group for Research in Applied Economics (GRAPE)
arxiv_id: '2609.02580'
url: https://arxiv.org/abs/2609.02580
pdf_url: https://arxiv.org/pdf/2609.02580
published: '2026-09-02'
collected: '2026-09-03'
category: MultiAgent
direction: 多Agent系统 · 市场机制对齐
tags:
- LLM Agent
- Double Auction
- Market Alignment
- Multi-Agent Simulation
- Economic Agent
one_liner: 基于经典双拍卖实验验证LLM交易Agent的市场对齐性，开源可复用多Agent市场模拟框架
practical_value: '- 做电商动态定价、广告竞价类Agent时，需针对通用LLM过度逐利、仅做最小幅调价、不愿主动跨价差成交的特征做prompt工程或微调，平衡单交易利润与成交概率，避免整体交易效率下降

  - 用LLM Agent做多Agent模拟（如电商交易场景、竞价策略仿真）时，不可默认LLM能复刻人类行为，需先基于人类行为基准做校准，否则模拟结果不具备业务参考性

  - 检测LLM定价Agent串谋行为时，不能直接沿用人类市场的「高于均衡价+小幅调价」判定规则，非串谋的LLM Agent本身就难以收敛到均衡价，需先构建LLM专属的非合作行为基准'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM 已被广泛应用于定价、竞价、交易等经济类Agent任务，但面向人类设计的市场机制在LLM Agent参与时能否达到预期分配效率、LLM Agent是否与现有市场机制对齐，尚未得到充分验证，尤其是双拍卖这一股票、大宗商品、电力交易等场景普遍使用的核心机制，其效率变化直接关系到未来LLM参与真实市场的规则设计。
### 方法关键点
- 复刻1962年Smith的经典双拍卖实验，设置11个买家+11个卖家，保留价格区间为$0.75~$3.25，理论均衡价为$2.00、均衡交易量为6单/轮
- 实现带持久化订单簿的连续双拍卖机制：仅改善价差的报价可进入订单簿，跨价差报价直接成交，每轮最多300次报价迭代，共开展5轮交易
- 测试3款主流LLM：GPT Large、GPT Small、Gemini Large，每组实验重复10次消除随机性，以人类实验结果为基准
### 关键结果
所有LLM构成的市场均未完全收敛到理论均衡：表现最好的GPT Small第5轮价格 dispersion 为11.7，是人类基准3.5的3.3倍，分配效率最高达0.91；GPT Large因仅做$0.01的最小幅度调价、不愿跨价差成交，每轮平均交易量仅2.2~3.8单，分配效率最低仅0.36；分析Gemini Large的CoT trace发现，Agent决定成交时的思考词汇会从战略优化类转向 urgency、执行导向类。
### 核心结论
更小、能力更弱的LLM在市场行为上反而更接近人类，通用大模型的强逐利倾向会显著降低多Agent市场的整体运行效率
