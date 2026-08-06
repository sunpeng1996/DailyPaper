---
title: 'Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory
  Systems'
title_zh: 借鉴灌丛鸦情景记忆原理的Agent长时记忆系统ScrubJay-MEM
authors:
- Kartikey Singh Bhandari
- Aarya Wadhwani
- Dhruv Kumar
- Pratik Narang
affiliations:
- Birla Institute of Technology and Science, Pilani
arxiv_id: '2608.04746'
url: https://arxiv.org/abs/2608.04746
pdf_url: https://arxiv.org/pdf/2608.04746
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent长时记忆 · 时序感知检索
tags:
- AgentMemory
- TemporalDecay
- EpisodicMemory
- RAG
- Retrieval
one_liner: 基于灌丛鸦认知原理为Agent记忆引入类型感知的时间衰减机制 提升时序推理性能
practical_value: '- 可直接复用记忆分类型衰减的设计：将用户行为/会话记忆分为稳定偏好（π低）、临时活动规则（π高）等类别，检索打分加入指数衰减项，过滤过期信息，减少电商推荐/客服Agent的事实错误

  - 可借鉴RCI（Retroactive Contextual Integration）的O(1)更新机制：当用户偏好/平台规则变更时，仅需1次LLM调用解析变更规则，批量更新相关记忆的衰减参数，无需逐条重分类，工程成本极低

  - 电商Agent/推荐的记忆检索可复用四要素自适应打分框架：语义相似度+场景匹配度+时序有效性+关联记忆传导，根据query意图动态调权，比如“今日优惠券”类query自动提权时序维度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent长时记忆系统对所有记忆采用统一留存/衰减策略，要么过度丢弃稳定知识，要么长期保留过期事实，随着记忆量增长，检索到过时信息的概率大幅上升，无法适配长周期运行的电商客服Agent、用户偏好建模系统等场景的需求。

### 方法关键点
- 每个记忆单元（EMU）存储为What（语义内容）-Where（场景上下文）-When（时间+有效期）绑定三元组，自动标注易腐性系数π_i和效用周期τ_i，分为4类：稳定知识（π=0.05~0.15，有效期月级）、流程知识（π=0.2~0.4，有效期周级）、任务特定知识（π=0.5~0.7，有效期天级）、临时信息（π=0.8~1.0，有效期小时/分钟级）
- 检索采用query自适应权重打分：根据关键词动态调整语义匹配、场景匹配、时序效用、关联图传导四个维度的权重，如带「最近/今天」的query自动提权时序维度
- 新增两个核心优化：RCI批量更新机制仅需1次LLM调用即可批量修改相关记忆的π/τ参数；PMB预取缓存提前加载下一个任务高概率用到的记忆，降低检索时延

### 关键结果
- 在EventQA-64k时序问答基准上，llama3.1:8b backbone下F1达61.58，比Mem0高2.66，比Qwen3-Embedding-4B高3.09；强backbone（qwen3:30b）下优势收窄，事实合并任务上劣于基线，仅适用于易过期事实的时序推理场景
- 自研TGT时序泛化基准上，是唯一取得正GenGap（+0.108）的检索类系统，移除类型感知衰减后GenGap下降5.7倍，验证该机制是泛化能力的核心来源

### 核心结论
不同类型的记忆衰减速度天然不同，统一全局衰减/分层记忆策略本质上是对时序信号的低效利用，按类型配置动态衰减参数是低成本提升Agent记忆时序准确性的核心路径
