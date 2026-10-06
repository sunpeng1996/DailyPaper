---
title: 'Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy'
title_zh: MemAdapter：针对记忆诱导谄媚问题的反事实适配框架
authors:
- Ruqing Ning
- Haibo Meng
- Zhishang Xiang
- Zerui Chen
- Jinsong Su
- Xin Wang
- Qinggang Zhang
affiliations:
- Jilin University
- Xiamen University
arxiv_id: '2610.05162'
url: https://arxiv.org/abs/2610.05162
pdf_url: https://arxiv.org/pdf/2610.05162
published: '2026-10-03'
collected: '2026-10-06'
category: Agent
direction: Agent 记忆可靠性优化
tags:
- LLM Agent
- Memory Sycophancy
- Counterfactual Reasoning
- Post-retrieval Calibration
- Reliability
one_liner: 提出检索后记忆适配框架MemAdapter，无需修改上游记忆系统即可缓解记忆诱导的LLM Agent谄媚问题
practical_value: '- 电商个性化对话Agent可直接复用该框架作为检索后记忆校准模块，无需修改现有RAG/记忆系统，即可降低过度迎合用户错误历史偏好的问题，避免忽略用户当前真实需求的错误推荐

  - 反事实归纳模块可迁移到推荐系统用户画像校准场景：固定用户历史行为特征，构造不同候选Item的反事实任务，判断画像特征的合理使用边界，缓解过度个性化导致的信息茧房

  - 证据对齐的生成校验流程可直接复用：给生成的推荐话术/回答添加溯源标签，校验每个结论的支撑来源是客观商品信息还是用户历史偏好，避免推荐理由与事实不符'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有记忆增强LLM Agent的谄媚问题缓解方案均聚焦在记忆提取、检索、组织阶段，默认风险来自错误/偏置记忆，但实际客观正确的记忆在不同上下文下也可能导致过度对齐用户历史偏见，记忆的合理使用边界是上下文依赖的，无法仅通过记忆内容判断。

### 方法关键点
- **Counterfactual Induction**：固定每条检索到的记忆，构造不同下游任务场景，推导该记忆在不同场景下的合理使用范围（可支撑什么、不可决定什么），生成通用使用边界规则
- **Context-Aware Reflection**：结合当前请求、客观证据、记忆集合，将通用边界规则适配为当前任务的具体使用指令，明确每条记忆的影响范围
- **Evidence-Based Reasoning**：生成回答的同时生成支撑溯源链，校验每个回答片段的来源符合预设的记忆使用规则，仅允许记忆影响个性化表达部分，事实性结论必须基于客观证据

### 关键结果
在MemSyco-Bench、PersistBench、MemTrapBench三个基准上，适配A-MEM、Mem0、NaiveRAG等5种主流记忆系统，对比4种现有后处理方法，MemSyco-Bench上平均准确率相对基线最高提升40.46pct，PersistBench上谄媚错误率最高降低31pct，同时兼容GPT、Qwen、DeepSeek等不同backbone。

### 最值得记住的一句话
记忆的风险不是内容的固有属性，而是其与下游推理上下文交互的产物，记忆管理的核心不是筛选哪些记忆可用，而是适配记忆在当前任务的推理角色。
