---
title: 'TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces'
title_zh: TrawMem：面向任务的角色自适应Agent内存工作空间框架
authors:
- Mingyu Zhang
- Zixu Li
- Zhiheng Fu
- Zhiwei Chen
- Jinhe Bi
- Yupeng Hu
affiliations:
- Shandong University
- National University of Singapore
arxiv_id: '2610.36918'
url: https://arxiv.org/abs/2610.36918
pdf_url: https://arxiv.org/pdf/2610.36918
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent 内存系统优化
tags:
- LLM Agent
- Memory System
- Task-Oriented
- Role-Adaptive
- Retrieval Optimization
one_liner: 基于任务导向角色分配与互补记忆选择构建Agent内存工作空间，提效且降低上下文消耗
practical_value: '- 电商个性化客服/导购Agent可直接复用TrawMem的记忆组织逻辑：将用户历史交互按事件聚合为本地线程并构建关联图，解决多轮对话跨事件信息关联不足问题，降低上下文冗余

  - 长会话推荐、用户画像建模场景可借鉴角色分配+子模集选点思路：不再仅按语义相似度召回记忆，而是根据当前任务给记忆分配锚点/桥梁/上下文角色，优先选择互补信息减少冗余，提升推荐/画像准确性

  - 可通过调整线程邻域遍历深度H实现效果与耗时的trade-off：实时性要求高的场景（如实时导购）设H=1，复杂推理场景（如用户生命周期价值预判）设H=3，灵活适配业务需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent内存系统仅依靠语义相关性召回记忆，忽略了同一条记忆在不同任务中承担的差异化角色（如直接支撑答案/关联弱相关但必要的互补记忆），容易漏召回关键信息，同时上下文冗余度高，长周期多轮任务的推理效果不佳。
### 方法关键点
- 离线阶段：将交互历史按事件聚合为本地线程，每个线程包含摘要检索头+有序记忆单元，构建时序邻接+语义关联的线程图作为长期记忆
- 在线阶段：针对当前任务召回相关线程邻域，给候选记忆分配任务导向角色（锚点/桥梁/上下文），计算每条记忆的角色适配度
- 基于单调子模集优化选择记忆单元，最大化信息覆盖度同时控制冗余，最终组装为任务专属工作空间输入回答模型
### 关键结果
在LoCoMo、MemGallery两个长对话记忆基准上，与Mem0、LightMem、SimpleMem等主流内存系统对比，跨Qwen、DeepSeek、GPT系列4个 backbone 均取得一致提升：LoCoMo上LLM-Judge得分平均提升3.71个百分点，上下文token相比SimpleMem降低5.1%~12.8%；MemGallery上LLM-Judge平均提升2.94个百分点。记忆单元压缩率平均达89.2%，仅保留1/10候选单元即可满足推理需求。
### 核心结论
Agent记忆的核心不是寻找最相关的记忆，而是按照记忆对当前任务的支撑角色组织互补信息，用更少的上下文实现更好的推理效果
