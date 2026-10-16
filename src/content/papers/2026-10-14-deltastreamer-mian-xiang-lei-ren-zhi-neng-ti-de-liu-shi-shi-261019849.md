---
title: 'DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding'
title_zh: DeltaStreamer：面向类人智能体的流式视频理解框架
authors:
- Boyuan Sun
- Deshui Miao
- Wenzhao Gao
- Shaoyong Jia
- Shaohui Jiao
- Chi Liu
- Yan Shu
- Derek Li
- Bryan Dai
- Shengsheng Qian
affiliations:
- VCIP, Nankai University
- ByteDance Inc.
- IQuest Research
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2610.19849'
url: https://arxiv.org/abs/2610.19849
pdf_url: https://arxiv.org/pdf/2610.19849
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 流式视频理解优化
tags:
- VideoAgent
- StreamingUnderstanding
- MemoryStructure
- QueryPlanning
- VideoQA
one_liner: 提出融合变化感知记忆、查询驱动规划与定向回放的类人流式视频理解智能体框架
practical_value: '- 流式时序数据记忆设计可迁移：电商用户行为流、广告曝光流可借鉴分层DAG记忆+delta增量记录机制，减少冗余存储同时保留事件转换关键信息

  - 查询驱动召回流程可复用：RAG/多轮对话推荐场景可借鉴一次性生成查询需求计划、跨记忆层回溯+原始数据回放校验的逻辑，降低 hallucination

  - 长序列记忆渲染策略可落地：用户行为建模可采用「长时摘要+最近窗口+按需召回中间记录」的拼接方式，平衡上下文预算与信息覆盖率

  - 多模块协同逻辑可参考：增量记录、分层记忆、查询规划三个模块协同比单模块优化增益更高，业务迭代可按该组合设计路径'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有流式视频理解方法多聚焦token压缩与KV cache复用，压缩历史时易模糊事件转换边界、丢失细粒度细节，且无原始帧回溯机制，后续查询需要的信息一旦被丢弃无法恢复，难以适配安防、直播、机器人等实时流场景的随机查询需求。

### 方法关键点
- 预查询阶段：对比相邻采样帧生成delta增量描述（记录帧间视觉变化），与当前场景结构化描述共同存入三层DAG结构的分层记忆（工作记忆/情节记忆/长时记忆），附带源指针关联原始帧与实体索引，支持全链路溯源
- 查询到达阶段：基于查询语义一次性生成包含目标、时间锚点、证据类型的持久化查询计划，全程指导记忆检索、后续帧观测与工具调用
- 证据不足时：通过源指针定向回溯匹配的历史帧，回放提取像素级缺失信息，校验多源记录一致性后生成答案

### 关键实验
在OVO-Bench、StreamingBench两个主流流式视频理解数据集上测试：OVO-Bench整体得分66.07%，较SOTA EventMemAgent提升5.32个百分点，超过Gemini 3 Flash 2.05个百分点；StreamingBench整体得分59.53%，较SOTA STRIDE提升1.95个百分点。消融实验显示移除回放功能后得分下降2.79个百分点，三个核心模块协同能带来最大增益。

### 核心结论
流式时序理解不能仅靠被动编码压缩历史，要结合主动查询驱动的证据检索与原始数据回溯能力，才能平衡存储效率和查询响应准确率。
