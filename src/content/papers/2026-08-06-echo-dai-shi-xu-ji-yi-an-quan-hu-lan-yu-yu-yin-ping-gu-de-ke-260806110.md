---
title: 'ECHO: A Locally-Deployable Agentic Health Assistant with Temporal Memory,
  Safety Guardrails, and Speech Assessment'
title_zh: ECHO：带时序记忆、安全护栏与语音评估的可本地部署医疗Agent助手
authors:
- Abdulkadir Külçe
- Alihan Esen
- Cağla Fikir
- Berke Kurt
- Kuzey Arar
- Gökhan Ercan
- Faik Boray Tek
affiliations:
- Istanbul Technical University, Turkey
arxiv_id: '2608.06110'
url: https://arxiv.org/abs/2608.06110
pdf_url: https://arxiv.org/pdf/2608.06110
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 垂直领域可部署Agent 医疗场景优化
tags:
- Agent
- LangGraph
- Temporal Knowledge Graph
- Guardrail
- Multimodal
- Local Deployment
one_liner: 提出全本地运行的医疗健康Agent，整合时序记忆、两级安全护栏与多模态语音评估，性能优于零样本大模型基线
practical_value: '- 可复用两级安全护栏架构：先规则层（<1ms拦截明确风险如Prompt注入、违禁词）再轻量GNN分类边界case，平衡 latency
  与准确率，适合电商客服/内容审核等需低延迟安全过滤的场景

  - 时序知识图谱记忆的设计思路：用结构化SQL存储事务数据+时序KG存非结构化历史，冲突事实做时间戳版本更新而非直接覆盖，可迁移到电商用户长周期兴趣建模，避免过时行为标签干扰推荐

  - 多模态语音/文本融合的多任务学习框架：用预训练编码器分别提取声学+文本特征，跨注意力融合后接多任务头，不同标注数据集仅更新对应任务头，可复用在电商直播用户情绪识别、语音搜索语义理解等场景

  - 全本地部署的架构设计：用LiteLLM做模型路由支持本地/云端模型切换，核心数据全存储在本地避免隐私风险，可参考做企业内部私域Agent、合规要求高的金融/电商用户运营Agent'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前慢病长期管理缺乏院外连续支持，30天非计划再入院率达21.3%；现有数字健康工具存在三大痛点：LLM跨会话无状态易遗忘用户病史、提醒类工具被动无法响应复杂临床问题、通用大模型缺乏专用安全机制易给出危险回复，同时云端部署的医疗工具存在用户隐私数据泄露风险，不符合GDPR等合规要求。

### 方法关键点
- 核心Agent层：基于LangGraph实现ReAct循环，配备17种临床工具，对接SQLite结构化存储与Hindsight时序知识图谱，支持跨会话记忆持久化；记忆检索融合向量搜索、BM25、图链路扩展、时序过滤4种策略，用Reciprocal Rank Fusion排序，增加证据计数加权、时序衰减逻辑
- 两级安全护栏：第一层规则层用正则匹配，<1ms拦截Prompt注入、明确危机、无关请求；第二层带APPNP传播的符号GNN分类边界case，输出9类临床意图+二分类安全标签，训练加硬负样本挖掘、风险加权损失
- 多模态语音评估：Whisper提取声学特征+冻结的BERT提取文本特征，跨注意力融合后接情绪、抑郁、疼痛3个分类头，用多数据集部分标签训练，任务均衡采样避免偏置

### 关键结果
- 59个临床场景工具执行基准：GPT-5 Mini通过率94.9%、F1 0.977，开源Qwen3 32B也可达86.4%通过率，首Token延迟<3s
- 2537条标注土耳其健康数据集上，安全分类准确率88.8%、不安全请求召回率90.6%，性能优于Llama 3.3 70B等零样本大模型，推理成本低2个数量级
- 语音评估3任务平均macro F1 0.652，相比纯Whisper基线提升4.5pp，疼痛检测提升最显著达8.9pp

垂直领域Agent落地要优先做分层架构设计，用轻量规则解决高频明确问题、小模型解决边界模糊问题、大模型做核心推理，在保证效果的同时兼顾延迟、成本与隐私合规要求。
