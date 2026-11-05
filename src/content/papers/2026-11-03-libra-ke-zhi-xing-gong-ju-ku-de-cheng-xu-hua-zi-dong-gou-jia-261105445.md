---
title: 'LIBRA: Programmatic Induction of Executable Tool Libraries'
title_zh: LIBRA：可执行工具库的程序化自动构建框架
authors:
- Zekai Li
- Zhenke Liu
- Yonghao Li
- Junhan Liu
- Xulong Xiao
- Jiapeng Zhang
affiliations:
- Brown University
- University of Southern California
arxiv_id: '2611.05445'
url: https://arxiv.org/abs/2611.05445
pdf_url: https://arxiv.org/pdf/2611.05445
published: '2026-11-03'
collected: '2026-11-05'
category: Agent
direction: Agent 工具检索依赖关系自动构建
tags:
- Agent
- Tool Retrieval
- Dependency Graph
- Runtime Validation
- LLM
one_liner: 无需依赖标注与历史调用轨迹，通过沙箱执行验证构建工具依赖库，提升多工具任务检索精度
practical_value: '- 电商/广告Agent的工具检索场景可复用反事实验证思路：对工具链依赖不要仅靠语义匹配，可在沙箱中测试「有前置工具成功、无前置工具失败」的真实依赖，避免漏召回鉴权、格式转换类前置工具

  - 可复用离线预构建+在线传播的架构：离线阶段提前构建工具依赖库（LLM调用量与工具数线性相关，成本可控），在线检索时仅对语义匹配到的种子工具做1跳依赖传播，平衡效果和推理延迟

  - 多工具任务的召回优化可借鉴打分规则：上游依赖工具的得分取自身语义分和下游种子工具得分的平均值，避免纯传播导致无关工具得分过高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有工具检索多对工具独立打分，多工具任务下仅能召回与用户query语义匹配的目标工具，会遗漏鉴权、ID查询、格式转换等未在query中提及的前置依赖工具；传统依赖感知方法要么需要历史调用轨迹、标注数据训练，要么仅基于元数据推理未验证真实可执行性，依赖关系准确率低，无法适配无标注的新增工具库场景。
### 方法关键点
- 离线预构建可执行工具库：对每个工具仅用公开元数据，由LLM生成包含候选调用、可复用输出、成功/失败条件的执行合约，LLM调用量与工具数线性相关，成本可控
- 反事实沙箱验证依赖：对候选工具对先执行上游工具并将输出传入下游，若调用成功则重置沙箱状态，直接传入随机同类型值调用下游，仅当前者成功、后者失败时才保留真实依赖，排除仅类型匹配的假依赖
- 在线检索传播：先用密集检索召回和query语义匹配的种子工具，沿依赖图做1跳传播召回前置工具；依赖工具的最终得分为自身语义分和所有关联下游种子工具得分的平均值，避免传播打分过高
### 关键结果
在AppWorld、BFCL、SciToolEval三个工具检索基准上测试，对比BM25、QTS、ToolREX、Ego-Trip等基线：
- 单轮检索相比同基座密集检索，平均Recall提升7.9pp，NDCG提升3.7pp
- 集成到ToolReAGt多轮Agent检索框架中，10轮迭代后平均Recall提升4.5pp，NDCG提升2.9pp
### 核心结论
工具依赖的真实可执行性比语义相似性更重要，离线预构建的可验证依赖库可同时提升单轮和多轮Agent的工具召回效果，且成本可平摊到大量查询中
