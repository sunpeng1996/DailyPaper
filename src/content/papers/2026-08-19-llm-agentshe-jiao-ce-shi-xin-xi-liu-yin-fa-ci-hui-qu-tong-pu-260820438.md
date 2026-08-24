---
title: Peer-Voted LLM-Agent Stress Tests Find Feed-Induced Lexical Convergence but
  No Reliable Matched-Exposure Advantage for Distributed Sources
title_zh: LLM-Agent社交测试：信息流引发词汇趋同，等曝光多源无额外说服优势
authors:
- Rana Muhammad Usman
- Dominic Williamson
affiliations:
- Codarossa.ai
arxiv_id: '2608.20438'
url: https://arxiv.org/abs/2608.20438
pdf_url: https://arxiv.org/pdf/2608.20438
published: '2026-08-19'
collected: '2026-08-24'
category: Agent
direction: LLM Agent 群体社交行为评估
tags:
- LLM Agent
- Social Simulation
- Stress Test
- Opinion Dynamics
- Testbed
one_liner: 提出PV-SST多Agent社交测试床，验证信息流词汇趋同效应与等曝光下多源无额外说服优势
practical_value: '- 做Agent群体行为模拟时可复用PV-SST的对照实验设计，固定曝光量后再对比不同内容分发/投放策略效果，避免混淆变量干扰

  - UGC内容推荐场景可参考结论：peer点赞排序的Feed会导致生成内容词汇趋同，做生态调控时可针对性调整排序策略避免内容同质化

  - 广告投放场景：相同曝光量级下，多账号分发同方向内容无额外说服优势，没必要为多账号额外付出运营成本，除非做内容差异化/受众分层覆盖

  - LLM Agent效果评估需按模型参数规模分层报告结果，不同大小的模型行为可能完全相反，不能直接迁移小模型结论到大模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent评估多聚焦单任务表现，无法刻画多Agent在社交场景下的递归交互闭环（内容生成、投票、排序反馈迭代），也无法验证两个行业普遍假设：信息流仅为内容载体不会影响群体行为，多来源协同投放比单来源说服力更强，需要可控的测试床完成因果验证。

### 方法关键点
- PV-SST测试床设计为：每轮实验包含12个预定义persona的Agent，运行6轮交互，每轮Agent接收场景反馈、生成≤180字结构化帖子、更新立场、对其他帖子投票，下一轮Feed按peer投票结果排序，全链路行为可追溯
- 设计4组对照：仅主题对照组、peer点赞排序Feed组、单来源攻击组、4分布式来源攻击组，两组攻击组总曝光量完全一致，仅来源数量不同
- 覆盖7个开源模型（4个小参数家族+3个大参数变体）、4个平台政策主题、4个随机种子，共448组预注册验证实验，避免数据窥探偏差

### 关键结果
- 相比仅主题对照组，peer排序Feed组的最终帖子TF-IDF余弦相似度提升0.0082（小模型组，p=0.000105）、0.0109（大模型组，p<0.000001），词汇趋同效应跨模型跨主题稳定存在
- 相同曝光下，分布式来源比单来源的说服效果在小模型组提升0.057（p=0.112，不显著），大模型组反而下降0.04（p=0.332，不显著），无可靠额外优势
- 少数派观点抑制效应仅在小模型组显著（下降3.9pp，p=0.0068），大模型组不显著，不具备通用性

### 核心结论
LLM Agent平台风险需要拆解为信息流曝光、排序、来源数量、内容多样性、触达范围等独立变量，通过配对实验验证，不能直接迁移小模型或单场景结论。
