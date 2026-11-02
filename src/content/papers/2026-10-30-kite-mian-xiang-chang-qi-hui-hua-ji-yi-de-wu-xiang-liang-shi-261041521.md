---
title: 'KITE: Retrieval as a Decision Procedure for Long-Term Conversational Memory'
title_zh: KITE：面向长期会话记忆的无向量显式决策检索框架
authors:
- Feng Li
- Kailun Tan
- Zhibo Zhou
- Youxiang Wang
- Lejun Liu
- Huaigu Li
- Fei Du
- Huilong An
affiliations:
- Memoket AI Research
- Universität Stuttgart
- Georgia Institute of Technology
- Tsinghua University
arxiv_id: '2610.41521'
url: https://arxiv.org/abs/2610.41521
pdf_url: https://arxiv.org/pdf/2610.41521
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 长期会话记忆检索优化
tags:
- LLM Agent
- Long-Term Memory
- Retrieval
- Knowledge Index
- Vector-Free
one_liner: 提出无向量的KITE框架，将会话记忆检索转化为受控知识索引上的显式决策流程
practical_value: '- 电商/客服Agent的长期用户记忆系统可复用该框架的受控主题索引设计，避免嵌入检索的语义匹配偏差，准确召回用户历史偏好、咨询记录，提升对话一致性

  - 多轮对话/长文本RAG场景可借鉴其「记忆构建-查询编译」共享索引的设计思路，将用户Query转化为可执行的结构化检索计划，大幅降低输入LLM的上下文Token量，削减推理成本

  - 长会话检索模块可复用其受控主题词表扩展+合并策略，减少主题碎片化，同时搭配稀疏 lexical 检索补全结构化索引遗漏的细节，兼顾检索准确率和召回率

  - 对可解释性要求高的消费级交互场景，可复用其确定性检索流程，检索过程和结果可审计，避免黑盒嵌入检索的不可控问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent长期记忆系统多基于嵌入向量相似度检索，仅靠语义排序无法保证召回内容匹配查询的真实条件，易召回语义相近但无关的记忆，同时嵌入索引存储成本高、Encoder更新需全量重建，检索过程黑盒不可解释，难以支撑长会话场景的高准确率、可审计需求。

### 方法关键点
- 构建受控演化的知识索引：将会话拆解为带溯源、时间、类型标签的结构化记忆条目，主题词表从根节点逐步扩展，仅新主题跨多会话重复出现才正式收录，定期合并冗余主题，同时支持实体、时间、事件等多维度分面索引
- 查询编译与索引对齐：基于同一知识索引将自然语言Query转化为可验证的结构化检索计划，明确选择范围、过滤条件、排序规则，计划语法校验和索引匹配通过后才执行
- 检索转化为显式决策流程：按计划执行确定性查找、过滤、排序，无匹配结果时按预设规则逐步放宽条件，搭配稀疏 lexical 检索补全结构化索引遗漏的表面细节，检索过程可解释、结果可复现

### 关键结果
在LoCoMo、LongMemEval-S两个长会话记忆基准上对比Mem0、Zep、EverMemOS等主流方案：
- LoCoMo数据集准确率93.5%，优于EverMemOS 0.4pct，平均仅需1.5k reader context token，比全上下文推理少消耗18.8k token，准确率高2.6pct
- LongMemEval-S数据集准确率86.0%，优于EverMemOS 3pct，平均仅需1.6k reader context token，比全上下文推理少消耗103.5k token，准确率高29.2pct
- 时间推理场景优势显著，LongMemEval-S上时间推理准确率达85.7%，超出次优方案8.3pct

> 最值得记住的一句话：会话记忆检索不需要依赖黑盒相似度排序，通过统一记忆构建和查询编译的受控索引，可将检索转化为可审计的显式决策流程，兼顾准确率和成本效率。
