---
title: Revision-Aware Independent Agent Graphs for Dynamic Reasoning
title_zh: 面向动态推理的修订感知独立智能体图（RIAG）框架
authors:
- Yan Luo
- Selim-Antoine Lali
- Jeremy Moebel
- Iliass Khoutaibi
- Ahmadou Aidara
- Mengyu Wang
affiliations:
- Harvard University
arxiv_id: '2610.01249'
url: https://arxiv.org/abs/2610.01249
pdf_url: https://arxiv.org/pdf/2610.01249
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 多智能体动态推理 · 时序任务路由
tags:
- MultiAgent
- Dynamic Reasoning
- Task Routing
- Caching
- LLM Agent
one_liner: 提出时序解析与推理分离的RIAG多智能体框架，动态路由场景精度翻倍、调用量降为1/29
practical_value: '- 电商/广告推荐的动态规则场景（促销生效、价格调整、规则撤回）可复用确定性时序解析器，先做版本路由再执行业务逻辑，避免错用过期规则，该解析器可直接接入现有推荐/审核链路，无需改动原有推理模块

  - 可复用版本+配置绑定的缓存机制：用文档版本、模型配置、prompt版本、解码参数的哈希作为缓存key，相同版本的任务直接复用结果，在商品详情页内容生成、活动规则问答等场景可大幅降低LLM调用量，本文实测MATH数据集缓存命中率达76.9%

  - 多智能体协作架构可借鉴：先执行两次无暴露的独立推理，结果一致就返回，不一致才触发审计/修复，最多4次调用，比反复辩论/refine的架构调用量低60%以上，适合推荐候选生成、内容审核等高吞吐场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多智能体推理框架默认任务固定，无法适配规则修订、延迟生效、历史回溯等动态事件流场景：全量重算会浪费大量LLM调用与延迟，直接复用历史结果则容易返回过期结论，且现有基准也无法评估动态任务路由能力。

### 方法关键点
- 构建动态任务路由基准：将MMLU、MATH、HumanEval等6个常用推理基准改造为31119个动态事件流片段，包含373428个时序查询，覆盖规则生效、过期、撤回、历史回溯等典型场景
- RIAG三层架构：1）无LLM调用的确定性时序解析器，根据事件的到达时间、生效时间、撤回状态，直接计算当前查询对应的合法文档版本；2）版本绑定缓存：将文档版本、模型配置、prompt版本、解码参数等序列化后取SHA256作为缓存key，命中直接返回结果；3）边界感知推理图：缓存未命中时先执行2次无暴露的独立推理，结果一致则返回，不一致才触发审计与修复，单新任务最多调用4次LLM

### 关键实验
对比Debate、Self-Consistency、Mixture-of-Agents、Graph-of-Agents等8个SOTA多智能体框架：同质RIAG联合精度达54.24%，较最强baseline Debate的32.22%提升22pp，每query平均调用量仅0.62次，为Debate的1/29；历史查询场景下传统方法精度下降24~29pp，RIAG精度波动小于0.7pp。

### 核心结论
可靠的时序绑定与选择性复用，对动态场景的收益远高于多轮deliberation或模型多样性。
