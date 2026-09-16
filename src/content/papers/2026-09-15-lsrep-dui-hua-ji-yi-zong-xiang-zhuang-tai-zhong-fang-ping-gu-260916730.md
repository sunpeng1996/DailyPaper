---
title: 'LSREP: A Longitudinal State-Replay Protocol for Evaluating Conversational
  Memory, with ICE v2 as an Audited Local-First Architecture'
title_zh: LSREP：对话记忆纵向状态重放评估协议与本地优先ICE v2架构
authors:
- Deepesh Sonar
affiliations:
- Thakur College of Engineering and Technology, Mumbai, India
arxiv_id: '2609.16730'
url: https://arxiv.org/abs/2609.16730
pdf_url: https://arxiv.org/pdf/2609.16730
published: '2026-09-15'
collected: '2026-09-16'
category: Eval
direction: RAG架构优化 · 对话记忆评估
tags:
- Conversational Memory
- RAG
- Evaluation Protocol
- Local-First
- Fusion Retrieval
- Long Context
one_liner: 提出纵向状态重放评估协议LSREP，同时给出经审计的本地优先对话记忆中间件ICE v2实测结果
practical_value: '- 对话类Agent的记忆评估可复用LSREP的纵向重放+动态真值范式，解决传统单点QA无法验证记忆更新、老化、跨会话一致性的问题

  - 高信息密度场景的RAG系统可借鉴ICE v2的动态token预算机制，避免无上限召回导致的上下文溢出失效，实测在高密度技术文档场景下可降低77%的prompt
  token量

  - 混合检索场景需验证RRF的增益：未经融合的额外检索支路（如BM25）可能引入负向干扰，加入RRF可抵消该损失，避免盲目增加检索支路

  - 多会话场景的RAG架构需额外优化跨会话信息聚合逻辑，ICE v2单会话纵向表现达标但在LongMemEval跨会话任务上准确率比纯向量RAG低26.5个百分点，可针对性补全该模块'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统对话记忆评估仅依赖端点问答，无法刻画持久记忆的积累、老化、更新过程，也难以定位架构组件的实际效用与缺陷，现存固定历史基准无法覆盖纵向状态演变的评估需求。

### 方法关键点
- 提出LSREP纵向状态重放协议：按顺序重放对话历史，在每个检查点重构记忆状态，采用随历史演变的动态参考真值，同步审计组件执行保真度，避免单一聚合分数掩盖失效模式
- ICE v2本地优先记忆中间件：包含4类结构化记忆存储（情景、语义图、过程、外部文档），采用BM25+向量的混合检索，通过加权RRF融合结果，设置动态token预算限制上下文长度，支持访问加权的记忆衰减与激活机制
- 双维度评估：私有LSREP数据集测试单会话纵向记忆表现，公开LongMemEval数据集测试跨会话记忆泛化能力

### 关键结果
普通密度数据集上，ICE v2与纯向量RAG平均得分近乎一致（4.26 vs 4.25），召回片段减少32%，但prompt token量增加6.6%；高信息密度技术文档数据集上，纯向量RAG 94.2%的请求因上下文溢出失效（得分1），ICE v2平均得分达4.33，prompt token量降低77%；公开LongMemEval跨会话任务上，ICE v2准确率显著低于纯向量RAG：证据仅场景50.8% vs 72.8%，全会话场景43.0% vs 69.5%，跨会话与时序推理存在明显缺陷。

最值得记住的一句话：单一的端点准确率无法完整衡量记忆系统的实际表现，纵向重放、保真度审计、跨场景测试三者结合才能暴露传统评估遗漏的失效模式。
