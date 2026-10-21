---
title: 'HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention'
title_zh: HERA：harness-环境协同进化实现可靠的Agent拒答能力
authors:
- Han Luo
- Bingbing Wen
- Guang Yang
- Zora Zhiruo Wang
- Pan Lu
- Lucy Lu Wang
affiliations:
- University of Washington
- University of Leeds
- Carnegie Mellon University
- Stanford University
- Allen Institute for AI
arxiv_id: '2610.06563'
url: https://arxiv.org/abs/2610.06563
pdf_url: https://arxiv.org/pdf/2610.06563
published: '2026-10-04'
collected: '2026-10-21'
category: Agent
direction: Agent可靠性 · 拒答能力优化
tags:
- Agent
- Agentic Abstention
- Harness Evolution
- Co-Evolution
- LLM Agent
one_liner: 提出harness-环境协同进化框架，显著提升Agent拒答准确率且可跨19款LLM迁移
practical_value: '- 复用协同进化思路优化业务Agent：基于现有电商导购、售后Agent的失败case，针对性生成边界任务（如无库存、权限不足、信息缺失去重场景），同步迭代Agent控制逻辑，无需微调LLM即可提升场景可靠性

  - 直接复用harness优化模块：论文中提出的证据校验门、跨源证据核对、联合约束校验组件可直接嵌入现有业务Agent，适配多款LLM无需额外优化，大幅降低研发成本

  - 落地成本优化技巧：用HERA优化中小参数LLM的Agent harness，可实现接近大模型的拒答效果，最高降低85%API调用成本，适合大流量电商Agent场景落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent在工具调用场景中常无法识别任务不可行场景，强行执行会导致性能下降、额外API/计算成本甚至不可逆操作风险；现有Agent拒答优化方案多基于固定任务集迭代harness，对未知失败模式泛化性差，也未探索harness与任务环境的协同优化路径。

### 方法关键点
- 可验证任务对构造：先生成带结构化数据库、可执行工具的运行环境与可解任务，再通过可控环境突变（修改数据、权限、约束规则）生成配对的不可行任务，两类任务请求完全一致，仅环境差异决定是否需要拒答。
- 协同进化流程：每轮先基于当前harness的失败案例，针对性生成能命中现有弱点的新任务对加入训练池；再基于更新后的任务池迭代优化harness的提示词、内存、工具、控制逻辑等组件，仅当验证集上拒答准确率、可行任务完成率均不下降才更新harness版本。

### 关键结果
在60对人工校验的跨领域held-out测试集HERA-BENCH上对比5个基线：
1. 拒答准确率从基线的61.7%提升至83.3%，可行任务完成率从68.3%提升至76.7%，两项指标均为所有方法最优。
2. 优化后的harness无需模型专属微调即可迁移到19款不同LLM，平均提升拒答准确率15.3个百分点。
3. 中小参数LLM搭配HERA harness可匹配大模型基线性能，单任务API成本最高降低85%。

**最值得记住的结论**：Agent可靠性优化无需局限于LLM微调，通过harness与任务环境的协同进化即可实现跨模型的泛化性提升与成本下降。
