---
title: 'When Agentic Retrieval Fails Silently: Framework and Production Evidence from
  a Creative AI Assistant'
title_zh: 智能体检索静默失效分析框架及创意AI助手生产实践证据
authors:
- Yan
- Liang
- Anuj Agarwal
- Aditya Reddy Cheruku
affiliations:
- Adobe
arxiv_id: '2610.30423'
url: https://arxiv.org/abs/2610.30423
pdf_url: https://arxiv.org/pdf/2610.30423
published: '2026-10-21'
collected: '2026-10-23'
category: Eval
direction: 智能体检索 · 可观测性评估
tags:
- agentic retrieval
- retrieval attribution
- production metrics
- RAG evaluation
- LLM observability
one_liner: 提出三层LARA评估框架与四字段溯源方案，解决智能体检索归因gap无需额外建模
practical_value: '- 搭建Agent/RAG系统的检索评估体系时，直接废弃全局CTR/改写率等传统检索指标，仅在检索实际触发的会话轮次计算检索相关指标，同时将用户query改写拆分为检索需求调整和生成效果调优两类分别统计，避免指标误导

  - 优先在日志中新增`retrieval_id`、`returned_asset_ids`、`consumed_asset_id`、`source_retrieval_id`四个字段，无需额外建模即可解决跨多轮/跨会话的检索归因问题，工程投入极低收益极高

  - 检索评估按LARA三层拆分：第一层离线计算检索本身的precision/NDCG定位检索质量问题，第二层统计用户/Agent对召回结果的实际使用率定位生成层过滤问题，第三层关联最终业务转化（电商加购/下单、内容消费/分享）定位全链路效果，可快速排障

  - 新增路由层可观测指标：统计应当触发检索但未触发的漏召回率，以及不该触发检索却触发的误召率，避免检索模块本身达标但上游路由错配导致的业务效果下降'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统检索指标CTR、MRR、NDCG依赖三个核心假设：用户直接看到召回结果、用户行为紧跟检索发生、后续行为直接反映检索质量。但在Agent/RAG场景下，召回结果先被LLM处理用户不可见、用户行为可能跨多轮/跨会话发生、最终效果是检索能力与生成能力共同作用的结果，三个假设全部失效，出现检索静默失效（LLM凭自身知识弥补了检索错误，业务侧无感知但检索质量实际不达标）和严重归因偏差，传统指标完全无法指导检索模块优化。

### 方法关键点
- 三层LARA评估框架，各层独立计算互不干扰：Layer1 检索质量层，检索触发时直接用离线标注/LLM-as-judge计算null rate、precision@K、NDCG@K，可检测被生成层掩盖的静默失效；Layer2 参与度层，分开统计GPR（用户使用召回资产比例）、ACR（Agent内部使用召回资产比例）、ORF（观测到的检索失败率）、UOR（无明确正负信号的检索占比），不把无行为默认判定为失败；Layer3 业务成功层，关联最终业务转化指标（如电商下单、创意工具导出），通过溯源字段绑定到对应检索事件。
- 四字段溯源schema：仅需在日志新增4个字段，无需额外建模即可解决跨轮/跨会话归因问题：`retrieval_id`（检索事件唯一ID）、`returned_asset_ids`（检索触发时的全量排序列表，过滤前）、`consumed_asset_id`（被使用的资产ID）、`source_retrieval_id`（资产对应的检索事件ID）。

### 关键实验
基于Adobe Express 2026年8月生产数据验证，同一套检索架构同时服务传统画廊搜索和Agent助手，用户群体完全一致：1）Agent场景仅0.31%的prompt会触发检索，全局CTR接近0完全失效；2）Agent chat用户改写率44.4%远高于画廊搜索的33.1%，但其中绝大多数是对生成结果的调优而非检索效果差，传统改写率指标完全误导；3）当前会话级归因会将跨会话导出的用户统计为abandonment，导致chat abandonment率虚高至59.5%。

### 核心结论
在Agent场景下，不要用全局会话级指标衡量检索模块效果，检索质量必须在检索触发的时刻独立评估，才能发现被LLM掩盖的静默失效。
