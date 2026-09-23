---
title: 'SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue'
title_zh: SpeakerMem-R1：面向多方对话的说话人中心双轨记忆系统
authors:
- Haobo Zheng
- Tan Tang
- Yan Chen
- Weijie Wang
- Yingcai Wu
affiliations:
- State Key Lab of CAD&CG, Zhejiang University
arxiv_id: '2609.26780'
url: https://arxiv.org/abs/2609.26780
pdf_url: https://arxiv.org/pdf/2609.26780
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent长时记忆 · 多方对话优化
tags:
- Multi-Party Dialogue
- Long-Term Memory
- Dual-Track Memory
- GRPO
- Reinforcement Learning
one_liner: 设计双轨记忆架构与RL训练的本地Writer，解决多方对话长时记忆的归因和状态重构瓶颈
practical_value: '- 搭建多角色群聊场景（如电商客服群、用户社群）的Agent记忆系统时，可复用双轨设计：原始对话存储带说话人/时间标签的逐字内容，结构化层拆分个人/群组视图，大幅降低信息归因错误

  - 记忆写入模块训练可参考SpeakerLevenshtein损失+说话人条件GRPO的组合方案，仅需3B量级小模型即可逼近大模型Writer效果，显著降低部署成本

  - 多源证据融合类任务可借鉴Anchor-Separate-Resolve-Compose查询流程，按主体/事件/时间维度组织证据，提升下游问答、决策任务的准确率

  - 用户长程偏好记忆场景可复用非破坏性更新设计，保留偏好状态演变链，支持历史版本回溯和偏好变化趋势分析'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有通用LLM记忆系统在多方对话场景下易丢失人物/群组关系，无法整合跨成员、跨时间的分散线索，核心瓶颈为信息归因错误（分不清谁说了什么、内容针对谁）和交错历史的状态重构能力不足，扁平检索、通用图记忆等方案均无法适配多方对话的层级关系。

### 方法关键点
- 双轨五层记忆架构：System1为逐字记忆层，仅追加存储带说话人、时间、渠道标签的原始对话；System2为四层结构化派生层，分为个人维度的Core（稳定身份、立场）、Profile（他人对该主体的认知）和群组维度的Interaction（跨用户事件、决策）、Insight（群组共识、规则），所有结构化记录均带溯源指针
- 查询阶段采用Anchor-Separate-Resolve-Compose流程，按主体、事件、时间维度从双轨拉取证据，结构化数据为空时自动fallback到对应主体的原始对话
- 仅训练记忆写入模块Writer，采用SpeakerLevenshtein损失和说话人条件GRPO优化，检索、问答模块保持冻结，支持本地小模型部署

### 关键结果
在GroupMemBench、SocialMemBench、EverMemBench三个多方对话基准上，准确率分别达47.9%、69.2%、61.9%，较主流最优baseline分别提升3.3、12.4、9.4个百分点，登顶EverMemBench公开榜单；基于Qwen2.5-3B的Writer-R1准确率达68.2%，较SFT版本提升10.82个百分点，达到大模型Writer效果的95.4%。

### 核心结论
多方对话记忆的核心不是提升检索相关性，而是要保留信息的主体归属、范围标签和历史状态链，双轨设计可同时兼顾原始信息准确性和结构化查询效率。
