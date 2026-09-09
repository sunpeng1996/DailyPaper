---
title: 'MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance
  for Long-Horizon LLM Agents'
title_zh: MeClear：面向长周期LLM Agent的博弈归因与风险感知内存清理框架
authors:
- Boyu Yang
- Jiazheng Sun
- Zilong Lu
- Zhi Qiu
- Xin Peng
- Jun Zheng
affiliations:
- 复旦大学
- 北京理工大学
arxiv_id: '2609.09115'
url: https://arxiv.org/abs/2609.09115
pdf_url: https://arxiv.org/pdf/2609.09115
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: Agent 长周期内存管理优化
tags:
- LLM Agent
- Memory Management
- Shapley Value
- Cooperative Game
- Long-Horizon
one_liner: 基于合作博弈归因实现长周期LLM Agent的查询级可逆有害内存清理，任务恢复率较LOO提升25.5pp
practical_value: '- 电商个性化Agent、用户画像RAG系统可复用LOO初筛+采样Shapley归因的组合策略，定位对当前查询有害的冗余、过期用户行为记忆，解决多冲突记忆互相掩盖的问题，归因准确率远高于单条删除策略

  - 采用查询级可逆内存抑制而非永久删除的设计，可直接迁移到电商搜索推荐的用户兴趣记忆模块，避免永久删除用户行为记录导致的跨query推荐效果退化

  - 仅需16次排列采样即可达到稳定的Shapley归因效果，无需全排列枚举，计算开销可控，可落地到线上实时请求的后处理链路'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长周期LLM Agent依赖外部内存存储用户偏好、历史交互信息，但传统基于语义相似度的检索机制仅召回语义相关内容，无法识别过期、误导、冲突的有害记忆；多条冗余或联合有害的记忆会互相掩盖效用，单条删除（LOO）的归因方法完全失效，同时永久修改内存会导致后续任务效果退化，亟需可逆、可识别多记忆交互影响的内存清理方案。
### 方法关键点
- 作为检索后处理模块，不修改原有检索逻辑，先冻结召回的K条内存上下文，避免检索波动干扰归因结果
- 先通过LOO单条删除做初筛，过滤明确正向贡献的内存，再用采样Shapley值计算每条内存跨不同组合的边际贡献，解决冗余/联合伤害记忆的掩盖问题
- 按负贡献排序生成嵌套候选清理集合，逐个验证清理后的任务恢复效果，选择最小清理规模、最大任务收益的方案，仅对当前查询抑制有害内存，不修改持久化内存库
### 关键实验
基于10组长对话LoCoMo数据集，共745个因果验证测试用例、1115条故障内存，对比LOO、ContextCite、ProxySPEX等基线：MeClear实现85.9%的有害内存召回率、82.3%的整体任务恢复率，较LOO基线任务恢复率提升25.5个百分点；在冗余冲突场景下，LOO召回率仅12.3%、恢复率仅6.3%，MeClear仍保持83.2%召回率、68.4%恢复率。
### 核心洞见
基于语义相似度的内存检索不能保证下游任务收益，多记忆交互的因果归因是长周期Agent内存管理的核心瓶颈。
