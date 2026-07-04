---
title: 'DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation'
title_zh: DuoMem：基于双空间蒸馏的高性能端侧内存智能体框架
authors:
- Peyman Hosseini
- Ondrej Bohdal
- Ahmed Alajrami
- Andrea Maracani
- Ignacio Castro
- Matthew Purver
- Mete Ozay
- Savas Ozkan
- Taha Ceritli
affiliations:
- Samsung R&D Institute UK
- Queen Mary University of London
arxiv_id: '2606.29961'
url: https://arxiv.org/abs/2606.29961
pdf_url: https://arxiv.org/pdf/2606.29961
published: '2026-06-28'
collected: '2026-07-04'
category: Agent
direction: 端侧LLM Agent 双空间知识蒸馏优化
tags:
- LLM Agent
- Knowledge Distillation
- LoRA
- On-Device AI
- Procedural Memory
one_liner: 通过上下文+参数双空间蒸馏，将大模型程序记忆能力迁移到端侧小模型
practical_value: '- 端侧电商导购/搜索交互Agent落地时，可先用大模型离线生成领域流程记忆（如导购话术、下单引导逻辑），推理时直接召回注入小模型上下文，零训练成本即可提升小模型流程执行准确率，记忆库仅几MB，几乎不增加端侧存储负担

  - 小模型流程推理能力不足时，收集大模型的成功交互轨迹做LoRA微调，仅新增<10M参数即可大幅提升任务成功率，适配端侧部署的存储约束

  - 端侧部署优先选择非thinking模式小模型，搭配蒸馏后的记忆与LoRA，比带思维链的大模型推理速度快3-7倍，同时可追回大部分性能差距，满足实时交互的延迟要求

  - 记忆检索配置可根据场景选择：MemP（脚本+参考轨迹）模式下检索4条记忆即可达到性能饱和，纯脚本模式可配到10条，平衡上下文长度与推理延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM 基于记忆的多步流程推理能力依赖大参数模型、长上下文和多次推理调用，算力/内存开销极高，难以部署在智能手机、IoT 等端侧设备；而 2B-12B 量级的小模型本身流程推理能力弱，无法有效利用结构化记忆，达不到业务要求。

### 方法关键点
- **上下文空间蒸馏**：离线用大模型（教师）生成高质量的流程记忆脚本，推理时召回和当前任务最相关的教师记忆直接拼接到小模型（学生）输入上下文，无需修改学生模型参数，整体记忆库仅占几MB存储
- **参数空间蒸馏**：收集大模型执行任务的成功交互轨迹，仅微调小模型的 LoRA 适配器，学习教师的行为决策模式，新增参数量仅几M到几十M，远小于基础模型参数量
- 双机制互补：上下文蒸馏优化模型输入的知识质量，LoRA 优化模型对上下文的利用效率，两者结合增益远高于单一机制

### 关键实验
在 ALFWorld 具身决策基准上测试，覆盖 2B-72B 的 Qwen、Gemma 系列模型，对比原生小模型、单空间蒸馏等 baseline：4B Qwen 原生任务成功率仅 4.3%，加 DuoMem 后提升到 77.9%，追回 72B 教师模型（87.1%）89%的性能差距；推理速度比 72B 教师快 3.4 倍，单任务平均耗时仅 4.89 秒，LoRA 新增参数仅 5.9M，记忆库仅 4MB。

### 核心结论
端侧 Agent 落地不需要盲目堆叠大模型，双空间蒸馏可以用极低的存储和计算开销，让小模型追回大模型的大部分流程推理性能，满足实时部署要求。
