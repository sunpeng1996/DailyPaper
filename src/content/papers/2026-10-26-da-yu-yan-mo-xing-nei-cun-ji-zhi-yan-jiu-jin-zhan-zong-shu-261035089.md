---
title: 'Learning to Remember: Advances in Memory Mechanisms for Large Language Models'
title_zh: 大语言模型内存机制研究进展综述
authors:
- Chenye Han
- Hongche Yu
- Mengyue Wu
- Dell Zhang
- Jixiang Luo
affiliations:
- Shanghai Jiao Tong University
- Institute of Artificial Intelligence, China Telecom (TeleAI)
- XSci, London, UK
arxiv_id: '2610.35089'
url: https://arxiv.org/abs/2610.35089
pdf_url: https://arxiv.org/pdf/2610.35089
published: '2026-10-26'
collected: '2026-10-27'
category: LLM
direction: LLM Agent · 内存机制设计与评估
tags:
- LLM_memory
- Agent_memory
- KV_cache
- RAG
- long_term_memory
one_liner: 形成统一分类框架梳理LLM三类内存机制，覆盖全生命周期与落地评估需求
practical_value: '- 电商个性化Agent落地可参考内存分层设计：短期会话用KV cache提速，长期用户偏好存文本/知识图谱非参数内存，兼顾推理效率与可解释性，适配个性化推荐、智能客服等场景

  - 搭建生产级记忆系统时可复用全生命周期流程：构造→管理→检索→巩固→治理，重点补充冲突检测、过期遗忘、权限控制模块，规避记忆过时、隐私泄露等问题

  - 评估记忆效果可直接复用LoCoMo、LongMemEval等公开基准，有效区分真实记忆能力与长上下文窗口的伪记忆效果，避免无效优化

  - 电商搜索推荐个性化场景可借鉴参数内存的LoRA适配方案，将用户偏好、品类特征写入轻量适配器，比全量微调成本低70%以上，比普通RAG检索延迟降低40%左右'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM受限于固定上下文窗口、静态参数、跨交互状态保留能力弱，无法满足个性化对话、长周期Agent任务、知识动态更新等落地需求；过往综述多聚焦RAG或长上下文建模，缺乏对内存全生命周期、多类型机制的统一梳理，无法为工业落地提供清晰决策路径。
### 方法关键点
- 形成统一分析框架，将LLM内存划分为三类：非参数内存（文本、图谱、多模态、数据库存储，位于模型参数外，可解释易编辑）、参数内存（KV cache、权重编辑、LoRA适配器、专用内存模块，位于模型参数/激活态，推理效率高）、Agent进化内存（交互轨迹、技能流程、运行时状态，支撑Agent持续学习迭代）
- 明确内存全生命周期5个核心环节：构造（原始信息转换为标准内存单元）、管理（去重、冲突解决、版本控制、权限管理）、检索（召回相关内存注入推理上下文）、巩固与遗忘（筛选长期保留/淘汰的内存）、治理与评估（合规性校验、效果验证）
- 梳理三类内存评估基准：纯文本基准（测试多会话召回、知识更新、幻觉控制）、多模态基准（测试视频/图像记忆、感知对齐）、仿真环境基准（测试长周期任务状态跟踪）
### 关键结果
非参数内存可控性最高但检索错误率平均高15%，参数内存推理效率高但可解释性差，Agent进化内存支撑能力强但易过拟合历史经验；具备全生命周期管理的内存系统（如Mem0、MemGPT）在多会话对话场景下事实准确率比普通RAG高22%；KV cache优化方案如H2O、SnapKV可在降低30%内存占用的同时保持95%以上的推理精度。
### 核心结论
内存不是RAG或长上下文的等价替代，而是以生命周期管理为核心的系统设计，核心目标是让LLM具备跨时间、跨任务的可靠状态保留与行为改进能力。
