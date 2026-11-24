---
title: 'Ask Again: Answer-List Instability in Generative Engines'
title_zh: 生成式搜索引擎答案列表不稳定性研究与测量指南
authors:
- Björn Busch-Geertsema
- David Antony Selby
- Sebastian Vollmer
affiliations:
- University of Kaiserslautern–Landau (RPTU)
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2611.30819'
url: https://arxiv.org/abs/2611.30819
pdf_url: https://arxiv.org/pdf/2611.30819
published: '2026-11-23'
collected: '2026-11-24'
category: Eval
direction: 生成式搜索评估 · 结果稳定性测量
tags:
- generative-search
- answer-stability
- GEO
- measurement-reliability
- ranked-evaluation
one_liner: 基于6万次生成式搜索响应量化答案列表不稳定性，给出可见性测量的采样方案
practical_value: '- 电商品牌做AI搜索可见性（GEO）监测时，不要单次采样，至少执行8次重复请求，榜首竞争激烈的场景提升到25次，同时统计商品上榜率、榜首占比两个指标，不要只输出单一排名

  - 生成式推荐系统上线前需做稳定性校验，尤其是开放式推荐Query（如「适合送女生的礼物」），要通过多轮测试控制首Item波动范围，避免用户体验不一致

  - 跨生成式引擎做优化时不要复用策略，不同引擎的答案列表差异远大于同引擎多次运行的差异，需分引擎单独测效果、做适配

  - 做生成式搜索/推荐效果评估时，要单独统计首Item一致性指标，不能只用整体RBO/Jaccard，存在列表Item完全一致但首Item调换的特殊情况'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式搜索引擎、生成式推荐的输出排名直接决定品牌/商品可见性，是GEO（生成式引擎优化）的核心监测目标，但现有测量方案未考虑同请求多次运行的答案列表波动，测量结果可靠性不足，无法支撑优化决策。

### 方法关键点
- 覆盖ChatGPT、Gemini、Perplexity 3个主流生成式引擎，2个国家（德国、美国）、200个覆盖事实、商品、健康等领域的Query，每个实验单元（Query+引擎+国家）重复请求50次，累计收集6万条响应
- 用三个维度衡量稳定性：Jaccard指数（Item重合度）、RBO（排名一致性，头部加权）、Rank-one agreement（首Item一致性）
- 按榜首前两名的占比差分为clear leader（差距≥40个百分点）、close leader（差距≤10个百分点）两类，测试不同采样预算的识别准确率

### 关键结果
- 同请求两次运行，32%的概率首Item不同，74%的实验单元至少出现一次首Item变动；即使Item完全一致的两个列表，也有8.1%的概率首Item不同
- 8次采样可100%识别clear leader（占总实验单元的70%），但仅能识别50%的close leader，25次采样也仅能识别60%的close leader
- 不同引擎的答案列表差异远大于同引擎多次运行的差异：跨引擎的RBO penalty平均为0.18，开放式Query的跨引擎差异是确定性Query的2倍以上

**最值得记住的一句话**：生成式搜索/推荐的可见性测量不能依赖单次运行结果，必须分引擎多次采样，同时上报条目出现率和榜首占比两个带不确定性的指标。
