---
title: 'One Assistant, Many Memories: Benchmarking Real-World Group Assistance When
  Recall Is Not Enough'
title_zh: GROUPASSISTBENCH：真实群聊场景下群助手记忆使用评测基准
authors:
- Zhanghao Hu
- Linhai Zhang
- Qian Zhao
- Qi Zhu
- Yuan Hua
- Di Liang
- Jiasheng Si
- Xin Zhao
- Yulan He
- Zhumin Chen
affiliations:
- Tencent Yuanbao Team
- King's College London
- Qilu University of Technology
- Renmin University of China
- Shandong University
arxiv_id: '2611.04867'
url: https://arxiv.org/abs/2611.04867
pdf_url: https://arxiv.org/pdf/2611.04867
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent 群聊场景记忆能力评测
tags:
- Agent Memory
- Benchmark
- Group Chat
- Memory Recall
- RAG
one_liner: 首个基于真实部署群聊的记忆评测基准，同时覆盖记忆召回与开放服务场景下的记忆使用能力
practical_value: '- 做群场景Agent（如电商用户群助手、企业协作助手）时，不能只优化记忆召回精度，需额外加记忆约束绑定模块，避免召回正确信息但生成时未使用的问题，实测可提升2-6pp的服务准确率

  - 群记忆系统可添加Relational Evidence Refinement（RER）模块，显式构建记忆间关联，补充请求未明确提及的关联记忆，大幅降低分布式/冲突记忆场景下的召回错误

  - 开放场景Agent效果评估不要只做固定答案的召回题，要基于真实用户负反馈构建分场景打分规则，更贴近业务实际的用户满意度

  - 长上下文成本敏感的业务场景，优先选BM25/稠密检索这类轻量RAG方案，2k+查询量级下成本仅为全上下文方案的1/5，精度损失可控'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent记忆评测多聚焦单用户场景、仅考核固定答案的记忆召回，且数据多为合成生成，无法反映真实群聊场景下的核心痛点：群助手需要整合多用户信息、跟踪信息变更与冲突、输出符合所有成员共识的开放回复，仅召回正确记忆远不足以完成服务。

### 方法关键点
- 构建GROUPASSISTBENCH基准，基于腾讯元宝真实部署的50个群聊共8万条消息生成，包含2395个评测用例，总制作成本超5.3万美元
- 评测分两个正交维度：任务层分为L1记忆召回（有固定参考答案）、L2记忆使用（开放服务请求无固定答案）；记忆依赖层分为M1单记忆、M2多用户分布式记忆、M3冲突更新记忆
- L2场景的打分规则基于真实用户负反馈构建，针对错误使用记忆、违背共识、使用过期信息等场景设置惩罚项，评分与人类标注一致性达89.3%

### 关键实验结果
- 对比14种方案：全上下文、4种RAG、6种外部记忆系统，最强外部记忆系统EverMemOS的L1召回率0.621优于全上下文GPT-5.6-terra的0.570，但L2使用得分仅0.247远低于全上下文的0.431
- 全上下文方案的L2得分从M1的0.505降到M3的0.303，分布式与冲突记忆是核心瓶颈
- 加入RER+ACB两个模块后，所有测试记忆系统的L2得分提升1.7-6.3pp，可有效弥补召回后未使用的问题

### 最值得记住的一句话
群场景Agent记忆系统的核心瓶颈已经不是记忆召回精度，而是如何把召回的记忆正确应用到开放服务响应中。
