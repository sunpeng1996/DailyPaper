---
title: 'Thinking While Speaking: Inference-Time Knowledge Transfer for Responsive
  and Intelligent Conversational Voice Agents'
title_zh: 说话时思考：面向响应式智能对话语音Agent的推理时知识迁移
authors:
- Vidya Srinivas
- Zachary Englhardt
- Shwetak Patel
- Vikram Iyer
- Maximus Powers
affiliations:
- University of Washington
arxiv_id: '2511.07397'
url: https://arxiv.org/abs/2511.07397
pdf_url: https://arxiv.org/pdf/2511.07397
published: '2026-06-22'
collected: '2026-06-30'
category: Agent
direction: Agent双模型协作 平衡延迟与能力
tags:
- Voice Agent
- Small Language Model
- Model Collaboration
- Latency Optimization
- Conversational AI
one_liner: 提出双模型协作的对话填充架构，同时实现Agent的毫秒级响应和大模型级能力
practical_value: '- 可直接借鉴双模型分工架构到电商智能客服/对话导购Agent：大模型Reasoner负责RAG检索、工具调用、复杂推理，小模型Talker负责前端实时对话响应，隐藏大模型延迟，解决交互卡顿问题

  - 动态上下文填充机制优于固定填充语：能适配RAG/工具调用的可变延迟，自动生成和上下文一致的无矛盾填充语，用户感知体验更好

  - 方案落地成本极低：微调135M~1.7B参数的Talker模型总成本仅约130美元，中小团队可快速复现适配业务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
语音对话Agent存在核心矛盾：大模型做推理、RAG检索、工具调用能力强，但过程迭代慢、延迟高，无法满足对话交互要求的毫秒级首响应；小模型能满足延迟要求但能力远不及大模型，现有方案只能在响应性和能力之间二选一，在RAG、工具调用等高延迟场景体验极差。

### 方法关键点
- 分工设计：轻量SLM做Talker直接对接用户，大模型做Reasoner异步执行推理、检索、工具调用；Talker在Reasoner出结果前生成上下文匹配的填充语隐藏延迟，拿到知识块后自然整合进回复，保持对话流畅
- 数据构建：生成290571条六领域训练样本，经过格式校验、时序对齐校验、蕴含验证、实体去幻觉四轮严格验证，保证数据质量
- 推理实现：用双队列做异步协作，用户query同时发给Talker和Reasoner，Reasoner流式推送知识块到队列，Talker逐块消费，无可用知识时自动生成填充，保证输出不中断

### 关键结果
- 基准测试：ConvFill准确率仅比纯大模型Reasoner低最多6.3%，相比原始未微调小模型准确率最高提升63.4%
- 端侧延迟：Apple M2上首响应时间平均500ms左右，相比纯大模型最高实现19倍加速，RAG场景平均加速9.2倍
- 用户研究：18名参与者评估，ConvFill整体体验和纯大模型持平，RAG场景用户显著偏好ConvFill，延迟评分显著高于纯大模型

最值得记住的一句话：通过推理时异步双模型协作，可以在几乎不损失大模型能力的前提下，实现对话Agent的毫秒级响应体验
