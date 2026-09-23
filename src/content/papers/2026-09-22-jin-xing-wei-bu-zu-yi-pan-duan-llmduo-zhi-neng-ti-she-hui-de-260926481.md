---
title: 'Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence
  in LLM Societies'
title_zh: 仅行为不足以判断：LLM多智能体社会规范涌现的机制化评估
authors:
- Rasika Muralidharan
- Haewoon Kwak
- Jisun An
affiliations:
- Indiana University Bloomington
arxiv_id: '2609.26481'
url: https://arxiv.org/abs/2609.26481
pdf_url: https://arxiv.org/pdf/2609.26481
published: '2026-09-22'
collected: '2026-09-23'
category: MultiAgent
direction: 多智体协作 · 社会规范评估
tags:
- Multi-Agent
- Norm Emergence
- LLM Alignment
- Social Learning
- Social Selection
one_liner: 提出融合行为与双维度期望测量的LLM多智体社会规范涌现评估框架，拆解核心机制的贡献
practical_value: '- 搭建电商/内容生态的多Agent协作系统（商家治理、客服群智、内容审核集群）时，可新增轻量的期望唤起模块，仅需私询Agent对行为的共识判断，即可全模型提升协作水平0.58~1.39个单位

  - 需稳定Agent协作行为时，优先设计social learning（群体讨论、经验共享）机制，其对低贡献Agent的行为矫正效果是social selection（动态组队、淘汰）的5.7倍，还可降低90%的Agent淘汰率

  - 做多Agent系统鲁棒性监控时，可将实证/规范期望差值作为稳态预警指标，期望恢复速度比行为快，能提前预判系统对抗恶意注入扰动的恢复能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM多智体社会规范研究仅以行为收敛作为涌现判定标准，无法区分协作行为来自模仿、策略激励还是群体共识，不同底层机制的系统鲁棒性差异极大，给多智体系统对齐与稳定性设计带来核心盲区。
### 方法关键点
- 新增期望唤起模块：每轮私询每个智能体的**实证期望（群体典型行为）**与**规范期望（群体应然行为）**，将不可观测的群体共识量化为可测量指标
- 消融实验设计：拆分期望唤起（E）、社会学习（SL，群体讨论共享经验）、社会选择（SS，基于评价的动态组队+低评分淘汰）三个核心模块，设置5组对照条件
- 鲁棒性测试：在实验第10/20轮注入低协作意愿的对抗Agent，测试不同机制下的系统恢复能力
- 覆盖4个主流模型族：GPT-4o-mini、Llama 3.1-8B、Qwen2.5-7B、Mistral-7B，每组条件做10次独立重复消除随机误差
### 关键结果数字
1. 仅加入期望唤起即可让所有模型的平均协作贡献提升0.58~1.39，是唯一全模型有效的正向干预
2. 社会学习对低贡献者的行为调整效果（β=0.390）是社会选择（β=0.068）的5.7倍，同时可降低90%的Agent淘汰率
3. 运行20轮的成熟规范被扰动后5轮即可基本恢复，运行10轮的早期规范被扰动后仍有显著残留偏差
4. 规范期望与行为的差值对后续行为调整的解释力比实证期望高24%，是更强的行为引导信号
### 核心结论
多智能体系统的协作稳态不能仅看行为收敛，背后的共识期望与形成机制直接决定了系统的抗扰动能力
