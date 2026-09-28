---
title: 'PIA: A Personal Intelligence Agent Turning Health Conversations into Records
  and Records into Understanding'
title_zh: PIA：将健康对话转为结构化记录并生成用户理解的智能Agent
authors:
- Jeonghun Yoon
- Dongchan Kim
- Hongyeon Yu
- Young-Bum Kim
- Jaegul Choo
affiliations:
- KAIST
- NAVER Corp.
arxiv_id: '2609.31255'
url: https://arxiv.org/abs/2609.31255
pdf_url: https://arxiv.org/pdf/2609.31255
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 长时记忆结构化与用户理解
tags:
- Agent Memory
- Structured Extraction
- User Profiling
- Longitudinal Data
- Knowledge Grounding
one_liner: 提出四控制记忆框架与HU2引擎，解决健康场景Agent长时记忆结构化缺失问题
practical_value: '- 采用双存储记忆架构：结构化关系库存储可聚合的标准化字段（如电商用户的尺码、消费等级、购买时间），关联语义记忆库存放模糊偏好内容，同时兼顾精确查询和语义召回需求

  - 落地确定性时间解析规则：对话中的时间表达式直接复制，不用LLM计算绝对时间，通过规则结合会话时间戳统一转换，避免时效类场景的时间幻觉（如用户提及的历史订单、优惠有效期）

  - 领域记忆设置准入Gate：核心实体（如电商商品名、属性、用户的明确偏好）采用精确别名匹配准入，不符合的内容进入待审核队列，避免错误记忆污染知识库

  - 离线预计算用户理解维度：将用户的偏好、约束、行为趋势等固定维度的画像异步生成更新，线上请求直接带入上下文包，大幅降低实时计算全量历史的延迟'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
通用Agent长时记忆多采用文本摘要+向量召回的模式，仅能满足简单偏好记忆需求，无法适配健康等对准确性要求极高的领域：结构化信息（如用药剂量、检测值）会被平化为文本，时间表达依赖LLM自主判断易出错，长周期趋势查询无法通过语义相似性召回得到可靠结果。
### 方法关键点
- 双存储架构：每轮对话同时写入结构化HUP健康用户档案关系库（含10类静态、13类episodic、5类衍生语义字段）和关联语义记忆库，分别支撑精确查询和语义召回
- 四控制记忆框架：提取控制采用schema约束抽取+确定性时间解析，禁止LLM自主计算日期；记忆控制设置精确别名匹配准入gate，结合医学知识图谱做字段标注；检索控制按请求类型路由结构化检索或关联召回，精确查询无匹配直接返回空不做相似fallback；理解控制离线异步运行HU2引擎，固定回答7个维度的用户特征问题，生成每轮请求的上下文包
- 三级个性化响应机制：1D仅注入查询相关记忆，2D加入用户静态快照，3D补充时间维度的趋势与因果关联，提升回答深度
### 关键结果数字
在20个合成用户的271个测试场景下，记忆准入gate精度100%、准确率94.9%，读操作召回率91%，检索MRR达0.785；部署环境中99.7%的检测结果记录带标准key，近1/3的候选因果关联为结构噪声，可通过规则直接过滤。
### 最值得记住的一句话
当领域需要精确可验证的记忆时，结构化存储+规则约束的效果远好于纯向量语义召回的通用记忆方案。
