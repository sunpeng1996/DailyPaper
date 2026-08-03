---
title: 'Know It, Act on It: Investigating Memory Utilization in LLM Personalization'
title_zh: LLM个性化场景下用户偏好记忆利用率的拆解与评估
authors:
- Zhaoxin Feng
- Jianfei Ma
- Emmanuele Chersoni
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2607.29433'
url: https://arxiv.org/abs/2607.29433
pdf_url: https://arxiv.org/pdf/2607.29433
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 个性化记忆利用率评估
tags:
- LLM Agent
- Personalization
- Memory Utilization
- RAG
- Agent Memory
- Evaluation
one_liner: 提出Know-Act配对评估范式，拆解LLM个性化场景下记忆存储与行为应用的差距
practical_value: '- 做个性化导购/陪伴Agent时，不能仅评估记忆召回率，必须补充Act类场景测试，比如用户提过对某成分过敏，需验证推荐时是否真的规避，避免虚假记忆达标

  - 内存架构选型优先考虑Mem0这类结构增强RAG，可将GPT-4o-mini的偏好利用率从16.3%提升至54.6%，远优于普通向量RAG的33%左右水平

  - 针对嵌入在任务对话中的Incidental类隐式偏好，需额外增加原子偏好抽取模块，这类信息是当前记忆系统召回率最低的场景，远低于需要推理的Inferential类偏好

  - 健康、过敏、情感类高风险偏好，除了记忆存储外需叠加规则校验层，这类偏好即使记忆正确，利用率也比普通偏好低30%以上，易引发安全问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM个性化Agent普遍存在「记得但不用」的问题：明明能正确回答用户的偏好提问，却在实际服务场景中忽略对应偏好，比如已知用户花生过敏仍推荐带花生的餐食。现有评估体系要么仅测记忆召回，要么仅测行为响应，无法定位故障根因，且未覆盖用户偏好多为隐式表达的真实场景，难以支撑系统优化。
### 方法关键点
- 设计Know-Act配对评估范式：对同一个用户偏好，分别做直接召回测试（Know，直接问用户是否有某偏好）和无提示场景应用测试（Act，给出需要用到该偏好的自然请求），定义利用率=Act通过数 / Know通过数
- 偏好按表达强度分为三类：直接陈述的Explicit、嵌入在其他任务中的Incidental、需要从行为推理的Inferential
- 设计三层故障归因框架：检索失败（没找到对应记忆）、理解失败（找到记忆但没提取出偏好）、应用失败（有明确偏好但没用到响应里）
### 关键实验
基于1000条用户偏好，覆盖5类偏好维度，测试16个系统、5种内存架构：
1. 全场景下Know-Act gap普遍存在，最优的Claude 4.6 Sonnet也仅能将65.1%的已记忆偏好转化为对应行为
2. 接入Mem0结构增强RAG的GPT-4o-mini，偏好利用率从原生的16.3%提升至54.6%，接近1M上下文Gemini 3.1 Flash的水平
3. Incidental类偏好召回率最低，健康医疗类偏好利用率仅15.58%，远低于普通偏好
4. 故障归因：53%为理解失败，30.7%为检索失败，16.2%为模型固有应用失败
### 最值得记住的一句话
LLM个性化的核心瓶颈不是记忆存储能力不足，而是已存储记忆的利用效率不足
