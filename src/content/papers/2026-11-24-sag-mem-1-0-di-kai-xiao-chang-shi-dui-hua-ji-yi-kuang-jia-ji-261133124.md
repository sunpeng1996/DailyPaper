---
title: SAG-Mem-1.0 Technical Report
title_zh: SAG-Mem-1.0 低开销长时对话记忆框架技术报告
authors:
- Yuchao Wu
- XingCheng Liang
- Xuanze Wang
- Yini Huang
- Yue Wu
affiliations:
- Zleap AI
arxiv_id: '2611.33124'
url: https://arxiv.org/abs/2611.33124
pdf_url: https://arxiv.org/pdf/2611.33124
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: Agent 长时对话记忆优化
tags:
- Conversational Memory
- RAG
- Lexical Expansion
- Temporal Grounding
- Agent Memory
one_liner: 提出无LLM预抽取的长时对话记忆框架，兼顾SOTA效果与低运算开销
practical_value: '- 电商客服Agent的记忆系统可复用对话全文存储方案，避免LLM预抽取的高成本和信息丢失，大幅降低多会话记忆运维开销

  - 跨会话用户行为/需求检索场景可借鉴证据引导词法扩展策略，补充传统语义检索漏召回的间接关联证据，提升多跳需求识别准确率

  - 涉及时间的用户需求（如「我上周买的衣服什么时候到」）可复用规则化相对时间标注方案，不用LLM即可降低时间推理错误率

  - 对延迟敏感的线上业务可选SAG-Mem-Lite配置，用预计算嵌入打分替代JEV评估，在精度损失很小的前提下实现低时延响应'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长时对话记忆方案多依赖LLM预抽取摘要、构建语义关系/知识图谱，写入开销高且易丢失原始对话细节，仅靠用户Query相似度检索易漏召回和原始Query关联度低但关键的互补证据，同时相对时间表达式的推理也增加了LLM负担。

### 方法关键点
- 记忆构建：无LLM推理，按512token软预算将完整对话切分为非重叠Chunk，保留原始文本、说话人、时间等元数据，仅构建词法索引，SAG-Mem-Lite额外预计算Chunk的bge嵌入
- 检索流程：先BM25召回初始候选，经JEV证据评估（SAG-Mem）或嵌入余弦相似度（SAG-Mem-Lite）筛选种子Chunk，提取种子非Query词做第二轮词法扩展检索，再结合已获证据重排序后返回Top20 Chunk
- 时间处理：检索后对选中Chunk的相对时间表达式做规则化日历标注，保留原始文本的同时降低LLM时间推理成本

### 关键实验
在LoCoMo、LongMemEval两个长时对话记忆benchmark上，以Qwen3.6-35B为backbone：SAG-Mem整体得分83.08（LoCoMo）、80.20（LongMemEval），超出最强基线7.2个百分点；SAG-Mem-Lite得分77.09、77.20，运算成本比Full Context和所有记忆基线更低，端到端latency优于多数对比方案。

### 核心结论
长时记忆系统优先保留原始信息、把关联推理延迟到查询时做，往往比预构建复杂语义结构的方案兼顾更高精度和更低总成本。
