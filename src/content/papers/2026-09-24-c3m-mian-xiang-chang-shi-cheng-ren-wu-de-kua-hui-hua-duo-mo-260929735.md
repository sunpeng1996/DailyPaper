---
title: 'C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks'
title_zh: C3M：面向长时程任务的跨会话多模态记忆维护框架
authors:
- Xueshu Chen
- Yan Wang
- Zihao Xue
- Jiefu Li
- Zhenfang Liu
- Jayden Chen
- Zhen Bi
- Jungang Lou
affiliations:
- Huzhou Normal University
- Alibaba Group
- University of Waterloo
arxiv_id: '2609.29735'
url: https://arxiv.org/abs/2609.29735
pdf_url: https://arxiv.org/pdf/2609.29735
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: 长时程Agent · 多模态记忆管理
tags:
- Multimodal Memory
- Long-Horizon Agent
- Cross-Session
- Memory Maintenance
- RAG
one_liner: 提出关系感知更新与预算路由的多模态记忆机制，固定预算下保留跨会话细粒度证据区分度
practical_value: '- 跨会话用户兴趣建模可复用「冷存储原始图文+活跃索引存路由向量+指针关联」的分层架构，既节省热内存开销，又不丢失用户历史浏览的商品图、详情文本等原始证据

  - 记忆更新阶段可借鉴RAMU的四类关系（same/update/distinct/uncertain）判定逻辑，仅合并高置信度的相同事实，避免将用户不同时间浏览的相似商品错误合并，丢失兴趣演化信号

  - 多模态RAG查询阶段可参考BMER的联合预算控制方案，对索引页、原始节点、图片、文本分别设配额，平衡召回覆盖率和推理时延，适配电商场景的成本约束'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
长时程Agent任务需跨会话保留图文多模态证据，现有压缩方案易丢失细粒度视觉线索，或错误合并语义相似但实体、状态、时间维度存在差异的记录，且查询盲的预存记忆难以在固定预算下覆盖未来未知查询需求，导致证据丢失、检索失败。
### 方法关键点
- 分层记忆架构：持久化ColdStore存储不可变的原始图文Raw Nodes，有限容量的活跃索引仅存紧凑路由表示与指向原始节点的指针，不修改原始数据
- 关系感知更新（RAMU）：新会话到来时召回TopK相似历史条目，判定两者关系为same/update/distinct/uncertain，仅对高置信度same关系做合并、update关系做版本关联，其余保留独立条目，避免误删有效区分信息
- 预算路由（BMER）：查询时按相关性+覆盖增益召回索引页、条目，在页/节点/图片/文本的联合预算约束下选择最优证据集合，直接返回原始图文用于推理，平衡召回率与资源开销
### 关键实验
在MemLens多模态长时记忆基准的195个Agent问题（共789样本）上测试，对比ReSum、MovieChat等4类基线，32K/64K上下文长度下，搭载GPT-5.6 Sol的C3M整体准确率达73.33%/68.21%，较最优基线分别提升5.12/3.59个百分点；搭载Qwen 3.8 Flash的C3M在32K上下文下准确率达66.67%，较最优基线提升1.59个百分点。
### 核心结论
多模态记忆维护不能只追求压缩率，应优先保证原始证据的可追溯性和区分度，仅对确认安全的冗余做合并，避免为节省内存丢失下游推理必需的细粒度信号
