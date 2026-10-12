---
title: 'Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits'
title_zh: 拟人化MLE多智能体：会话交替机制突破单智能体性能上限
authors:
- Changye Li
- Zijian Zhang
- Muheng Li
- Yiduo Pang
- Tingjun Wu
- Menghan Li
- Yitong Liu
- Hongkai Guo
- Mengchi Chen
- Chenyu He
affiliations:
- Tsinghua University
- NVIDIA
- Zhejiang University
- MIT
arxiv_id: '2610.13494'
url: https://arxiv.org/abs/2610.13494
pdf_url: https://arxiv.org/pdf/2610.13494
published: '2026-10-09'
collected: '2026-10-12'
category: MultiAgent
direction: 多智能体长周期任务协作优化
tags:
- Multi-Agent
- Long-Horizon Task
- MLE Agent
- Workflow Optimization
- Context Reset
one_liner: 提出无需定制harness的多智能体会话交替框架HMA，突破单智能体长周期任务性能上限
practical_value: '- 长周期推荐策略迭代、广告A/B实验调优类Agent可直接复用HMA的会话交替逻辑：每运行k=3~5轮就切换不同基座的Agent、重置上下文，保留共享工作空间的产出，避免单Agent长期探索效率衰减，实测可提升6%+的任务达标率

  - 无需为不同模型定制prompt或harness，直接使用各厂商原生Agent即可通过协作获得增益，大幅降低多Agent落地的适配成本，尤其适合频繁升级LLM基座的业务场景

  - 最终交叉review环节可直接复用：所有候选产出交由非生成方Agent做最终选型，能提升2%+的最优结果保留率，可迁移到广告文案生成、推荐物料排序的结果校验环节'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
单智能体执行长周期任务时存在两个核心痛点：一是长程减速，推理强度随运行时间延长下降29.8%~45%，探索效率快速衰减；二是harness陈旧，定制的任务prompt、工具调度逻辑会随基座模型升级收益下降甚至反作用，依赖context engineering的优化方案无法跨模型版本复用。
### 方法关键点
- 将多智能体会话交替建模为上下文重置半马尔可夫决策过程（CR-SMDP），推导了交替策略超过单智能体性能上限的充分条件与实验预算边界
- 提出HMA框架：每最多k次实验后切换异质Agent、重置上下文，仅保留共享工作空间的所有历史产出，无需额外任务先验或定制harness
- 增加最终跨Agent review环节，由非执行方Agent从所有历史候选中筛选最优结果，提升最优结果保留率
- 实测k≤5时可保留97.8%的单会话增益，为最优会话长度阈值
### 关键结果
在包含75个Kaggle任务的MLE-bench数据集上测试：
- 最优配置（Claude Opus 5+GPT-5.6-sol）any-medal率达78.2%，超出最强开源基线8.0个百分点，仅用其四分之一时间预算
- 跨6种异质Agent对配置，HMA平均比单Agent基线提升6.4个百分点的any-medal率
- 48小时内核优化任务上，运行结果距离社区榜一仅差1.6%

最值得记住的结论：长周期任务中，无需改造单个Agent，仅通过固定周期交替不同基座Agent、重置上下文的极简协作模式，就能稳定突破单智能体性能上限。
