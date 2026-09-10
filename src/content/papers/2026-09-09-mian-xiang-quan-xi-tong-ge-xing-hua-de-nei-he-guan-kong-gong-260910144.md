---
title: Kernel-Managed Shared Memory for System-Wide Personalization
title_zh: 面向全系统个性化的内核管控共享内存架构
authors:
- Ryan Lum
- Yongfeng Zhang
affiliations:
- Rutgers University
arxiv_id: '2609.10144'
url: https://arxiv.org/abs/2609.10144
pdf_url: https://arxiv.org/pdf/2609.10144
published: '2026-09-09'
collected: '2026-09-10'
category: MultiAgent
direction: 多Agent系统 内核级共享内存个性化
tags:
- MultiAgent
- SharedMemory
- Personalization
- RAG
- AIOS
- MemoryManagement
one_liner: 提出多Agent系统内核统一管控的共享内存架构，实现低成本高效果的全链路个性化
practical_value: '- 多Agent电商客服/导购系统可复用内核级统一记忆架构，避免各Agent重复开发记忆检索、隐私校验逻辑，降低研发成本与不一致风险

  - 给现有RAG记忆系统增加用户粒度的单调序列编号写屏障，解决异步写入的读写时序问题，避免个性化上下文丢失，大幅提升记忆准确率

  - 结构化用户/商品记忆转自然语言语句后再注入prompt，可显著提升小模型对上下文的利用率，适合端侧小模型Agent的推荐场景

  - 所有记忆条目增加owner、sharing_policy元数据，内核层统一做权限校验，从架构层面避免跨用户隐私泄露，符合电商用户数据合规要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多Agent系统的记忆由各Agent独立管理，存在逻辑重复、隐私校验标准不一、跨Agent上下文无法共享的问题；全量上下文拼接成本高、延迟大，普通RAG检索易丢失非query相关的重要个性化信息，无统一管控的记忆后端（如Mem0）实际个性化效果极差，亟需系统级的共享记忆方案支撑全链路个性化。
### 方法关键点
- 记忆管理从单个Agent剥离，统一由Agent系统内核负责：Agent仅写入带标准化元数据（用户ID、所有者、记忆类型、共享策略）的结构化记忆，内核统一管控读写排序、隐私过滤、召回排序、格式化注入全链路
- 实现用户粒度的写屏障：每个用户的写入操作分配单调递增序列编号，检索时等待当前快照序号前的所有写入完成，避免异步写入的时序竞态导致上下文丢失，超时后fail-open保障服务可用性
- 内核层统一做可见性校验：仅记忆所有者或标记为shared的记忆对Agent可见，默认隐私，从架构层面保障数据安全
- 结构化记忆转自然语言格式后注入prompt，解决小模型无法有效利用JSON格式记忆的问题
### 关键实验
在AIOS框架上实现，对比3类基线：全量上下文拼接（效果上限）、普通RAG、无内核管控的Mem0，覆盖GPT-4o、Llama-3.1:8B、Qwen-2.5:7B三个模型，共1800次试验。核心结果：比Mem0的个性化得分高2.4~4.0分（5分制，GPT-4o的profile使用得分从1.05提升到4.69）；比全量上下文拼接的端到端延迟降低15%~61%，2/3模型上个性化效果无统计差异，仅Llama-3.1:8B存在小幅模型特定差距。
### 核心结论
记忆管理从应用层Agent下沉到系统内核，能以极低的成本获得接近全量上下文的个性化效果，远优于独立Agent记忆或普通RAG方案。
