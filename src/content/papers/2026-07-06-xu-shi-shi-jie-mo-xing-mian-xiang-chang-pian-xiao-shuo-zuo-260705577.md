---
title: 'Narrative World Model: Narratology-Grounded Writer Memory for Long-Form Fiction'
title_zh: 叙事世界模型：面向长篇小说创作的叙事学驱动Agent记忆系统
authors:
- Mohammad Saifullah
- Thomas Kornmaier
- Taaha Kazi
- Vasu Sharma
- Aditya Sanjiv Kanade
- Aanand Kumar Yadav
affiliations:
- PocketFM
arxiv_id: '2607.05577'
url: https://arxiv.org/abs/2607.05577
pdf_url: https://arxiv.org/pdf/2607.05577
published: '2026-07-06'
collected: '2026-07-08'
category: Agent
direction: Agent长时记忆 · 时序知识图谱
tags:
- Agent_Memory
- Temporal_KG
- Hybrid_Retrieval
- Multi-hop_QA
- Narratology
one_liner: 基于叙事学结构设计时序知识图谱与混合检索，大幅提升多跳叙事状态问答准确率
practical_value: '- 做Agent长时记忆时可复用「领域特定结构化Schema+查询感知混合检索」的架构，比通用时序KG/GraphRAG在垂直场景多跳问答上提升更明显

  - 垂直领域知识建模可参考该工作，将领域核心规则（比如电商的商品状态变化、用户权益时间范围）作为一等公民嵌入KG Schema，而非用通用实体关系

  - 评估记忆系统性能时可借鉴「固定回答LLM+仅提供对应系统检索结果」的协议，隔离记忆检索与生成能力的干扰，准确定位记忆模块效果

  - 时序场景下的检索可复用「BM25+向量+1跳图扩展+reciprocal-rank fusion」的混合检索策略，平衡召回的相关性与结构完整性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有通用RAG、时序KG Agent记忆系统无法建模叙事学特有结构（比如事件发生顺序和披露顺序的差异、角色认知边界、伏笔回收状态），在长篇小说创作的多跳叙事状态查询上准确率极低，频繁返回错误证据或无结果，无法支撑长文本生成的一致性校验。

### 方法关键点
- 存储层：定义叙事学导向的结构化Schema，将角色认知、事件/披露时序、剧情伏笔、戏剧功能等作为一等类型，构建带有效性时间区间的时序知识图谱，所有记录绑定来源章节与证据片段
- 检索层：采用查询感知混合检索策略，先做章节因果截断（仅返回查询节点前的内容），再用BM25+BGE向量+RRF融合排序核心节点，扩展1跳邻域后组装为异构证据包
- 验证层：新增递归LLM QA模块，分解复杂叙事查询、验证证据一致性，避免幻觉
- 评估协议：固定Opus 4.8作为回答器，所有系统仅能返回自身检索到的章节安全证据，隔离记忆与生成能力的干扰

### 关键结果
在私有176条多跳叙事QA基准上，NWM多跳准确率达0.898，是当前最优时序KG记忆系统Graphiti（0.574，和NWM用相同提取器控制变量）的1.56倍，p<10^-5；在公开576条叙事QA基准的110条多跳子集上，NWM准确率0.709，超过Graphiti的0.582，p=0.0001，性能优势完全来自结构设计而非提取器质量，GraphRAG、普通RAG等基线性能远低于上述两个系统。

最值得记住的一句话：垂直场景Agent记忆的性能提升核心来自领域特定的结构化表示与查询感知的检索设计，而非更大的图谱规模或更强的提取模型。
