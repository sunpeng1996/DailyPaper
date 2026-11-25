---
title: 'Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounded
  Policy Assistant'
title_zh: 基于RAG的移动端政策咨询助手JAMN Bot 解决考试缓办流程堵点
authors:
- Mark Farinas
- Alesandra Garcia
- Maria Reyes
- Jethro Nueva
- Nawaf Qureshi
- Mahmoud Elsaadany
- Shokry Shamseldin
affiliations:
- Department of Computer Science, MacEwan University
- MacEwan University, Edmonton, Canada
arxiv_id: '2611.32266'
url: https://arxiv.org/abs/2611.32266
pdf_url: https://arxiv.org/pdf/2611.32266
published: '2026-11-24'
collected: '2026-11-25'
category: RAG
direction: RAG落地 · 轻量化自托管垂直问答
tags:
- RAG
- Lightweight-LLM
- Self-hosted-Inference
- LLM-Evaluation
- Vertical-Chatbot
one_liner: 集成自托管Llama 3.2 3B RAG pipeline的移动端高校政策咨询机器人，兼顾回复准确性与隐私合规
practical_value: '- 做内部政策/规则类问答Agent时，可采用自托管3B级轻量LLM+RAG架构，在满足数据隐私要求的前提下控制推理成本，适合电商商家规则咨询、内部员工流程问答等高合规场景

  - 垂直场景RAG系统评估可复用「领域问题+隐私类问题+跨规则问题+对抗/OutOfScope问题」的benchmark设计思路，搭配LLM-as-judge+人工评估的组合方案，平衡评估效率与准确性

  - 可验证轻量开源LLM与前沿闭源模型在垂直场景的效果trade-off，在响应质量达标的前提下优先选用自托管方案，降低长期调用成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
高校考试缓办等行政流程规则复杂，传统人工咨询响应慢、解释口径不一致，且用户隐私数据无法上传至第三方闭源大模型，现有方案难以兼顾效率、准确性与合规要求。
### 方法关键点
1. 移动端APP Schedulater内置JAMN Bot政策咨询助手，采用Ollama自托管Llama 3.2 3B模型搭建RAG pipeline，全链路本地推理保证数据隐私，回复严格锚定官方政策；
2. 构建43条覆盖考试缓办、隐私、调度、跨政策、对抗/OutOfScope类问题的评估benchmark，采用人工标注+检索命中率+LLM-as-judge（GPT-5.4）的多维度评估方案，同时与Gemini 3.5 Flash、Qwen3.5 397B做效果对比。
### 关键结果
1. 验证了轻量开源LLM+RAG方案可满足垂直政策场景的咨询需求；
2. LLM-as-judge与人工评估一致性为轻到中等，随回答质量提升一致性显著升高；
3. 开源轻量模型与前沿闭源模型存在明确效果-成本-隐私的trade-off，垂直场景下轻量方案性价比更高
