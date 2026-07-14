---
title: 'Context by Distinct Information: An Auditable Dirichlet-Process Working Memory
  for Long, Redundant Context Streams'
title_zh: 基于差异化信息的上下文处理：面向长冗余流的可审计狄利克雷过程工作内存
authors:
- Siddharth Pal
- Viktoria Rojkova
arxiv_id: '2607.10441'
url: https://arxiv.org/abs/2607.10441
pdf_url: https://arxiv.org/pdf/2607.10441
published: '2026-07-11'
collected: '2026-07-14'
category: LLM
direction: LLM长上下文 · 可审计工作内存
tags:
- LongContext
- WorkingMemory
- KVCacheOptimization
- DirichletProcess
- AuditableAI
one_liner: 提出按任务依赖拆分三类上下文并匹配对应内存结构，长冗余场景性能持平全注意力且缓存开销减半
practical_value: '- 电商用户长行为序列建模可引入新奇度判定机制，仅缓存差异化行为事件（如新类目浏览、首次品类购买），无需全量存储所有token，降低KV
  cache开销同时保证召回准确率

  - 针对不同推荐任务适配存储策略：用户长期兴趣召回（recall-carried）用新奇度缓存，ctr预估统计特征计算（summary-carried）用状态空间模型，实时会话推荐（locality-carried）用滑动窗口，避免一刀切用全注意力

  - 可复用slot多属性记录设计，每个缓存slot存储内容来源、时间戳、合并记录，适合电商风控、广告归因等需要可解释性、合规审计的业务场景

  - 部署时优先为需要反复查询的持久化上下文（如用户长期画像）引入该缓存，单次短会话场景用滑动窗口性价比更高，无需盲目升级'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM上下文管理均以token为单位，无论固定状态循环模型、全注意力KV cache还是滑动窗口策略，都会对冗余信息重复计费，当上下文流存在大量重复实体、事件、记录时，内存和计算开销浪费严重，且无法做到上下文内容的可审计溯源。

### 方法关键点
- 按任务对历史信息的依赖拆分三类上下文，匹配对应存储结构：recall-carried类（需召回特定历史项）用基于狄利克雷过程的新奇度缓存，仅新增与已有slot余弦相似度低于阈值的KV对，相似内容合并到已有slot；summary-carried类（依赖长程聚合统计）用循环/状态空间模型；locality-carried类（依赖最近上下文）用滑动窗口
- 每个缓存slot存储key、value、首次位置、合并位置、使用次数、来源信息，天然支持审计溯源
- 支持固定阈值和突发自适应两种分配策略，自适应策略根据近期新奇内容占比动态调整缓存容量

### 关键实验
- enwik8字符级语言建模任务上，新奇度门控注意力性能与全注意力持平，仅需缓存49%的token；搭配状态空间模型的组合架构性能超过全注意力+状态空间组合，仅缓存53%的token；上下文长度扩展到1024时，组合架构比全注意力低0.3bpc
- 医保报销单next-code预测任务，1024事件长度下，组合架构比全注意力低0.311bit/事件，仅缓存45%的事件，远超滑动窗口、SnapKV、H2O等基线
- 日志、临床处方、KITTI地图等场景下，缓存自动对齐模板、药品、地点等实体，召回准确率最高达1.0

### 核心结论
上下文策略不能只由语料本身决定，必须匹配任务对历史信息的依赖类型，没有通用的最优内存结构
