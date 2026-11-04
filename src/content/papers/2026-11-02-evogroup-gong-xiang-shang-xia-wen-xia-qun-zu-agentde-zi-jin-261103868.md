---
title: 'EvoGroup: A Self-Evolving Harness for Group Agents in Shared Contexts'
title_zh: EvoGroup：共享上下文下群组Agent的自进化管理框架
authors:
- Xinyi Xu
- Xiaoyang Li
- Yucheng Feng
- Wenqing Chen
- Youliang Yuan
- Wei Shi
- Rongxiang Weng
- Zibin Zheng
affiliations:
- Sun Yat-sen University
- Longcat Team, Meituan Inc.
arxiv_id: '2611.03868'
url: https://arxiv.org/abs/2611.03868
pdf_url: https://arxiv.org/pdf/2611.03868
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: 群组Agent · 自进化内存管理
tags:
- GroupAgent
- SelfEvolution
- AgentMemory
- AdaptiveHarness
- MultiUserCollaboration
one_liner: 通过四阶段自进化循环优化群组Agent内存框架，pass@1较基线提升超18个百分点
practical_value: '- 可复用自信度+正确性四象限轨迹筛选法，优先分析「自信错/不自信对/不自信错」三类高价值轨迹，大幅降低自优化计算成本，适合电商客服、商家协作等群组Agent迭代

  - 自适应渐进式披露(APD)轨迹分析方法可直接复用，仅按需加载可疑片段，比全量分析平均节省42.5%时间、41.5%Token，适配长会话推荐、多轮对话Agent的错误诊断场景

  - 四类标准化harness更新接口（表示/操作/干预/策略）可直接套用，优先优化策略与表示层能以最小改动获得最大收益，降低业务Agent自动化迭代的风险

  - 6个基础工具冷启动方案可复用，无需预先定义复杂内存规则，适合快速搭建小流量试错的群组Agent应用，如电商社群运营、用户群组服务Agent'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent内存系统多针对单用户设计，无法适配多用户共享上下文下的群组协作场景，预定义的内存规则难以适配动态变化的群组结构、任务需求，人工维护成本高且灵活性不足。

### 方法关键点
- 四阶段自进化循环：从仅含6个基础工具的最小harness冷启动，依次经过交互、轨迹筛选、分析、修订四个阶段持续迭代
- 轨迹筛选：结合Agent输出自信度与正确性标签，优先选取自信错误、不自信正确、不自信错误三类高信息量轨迹，过滤常规正确轨迹减少冗余计算
- 轨迹分析：用自适应渐进披露(APD)按需加载轨迹片段定位问题，再通过分桶聚合跨轨迹共性问题生成高层结论，比全量分析省40%+的时间与Token
- 标准化修订接口：将harness更新拆分为表示、操作、干预、策略四类接口，针对性优化避免无效修改

### 关键结果
在EverMemBench数据集上，DeepSeek-V4-Flash的pass@1从初始71.07%提升到89.58%，超过Claude Code的85.83%、Codex的82.62%；跨基准迁移到未见过的GroupMemBench，GPT-5.5下pass@1达63.89%，超过最优人工设计harness 8.46个百分点；迭代过程中能力保留率超91%，回归率低于9%。

最值得记住：Agent自进化的核心是用最少的高价值反馈信号低成本迭代核心规则，而非依赖全量数据或人工预先定义所有逻辑。
