---
title: 'SCOPE-Router: Cost-Aware Open-Set VLM Routing for Execution-Oriented Tasks'
title_zh: SCOPE-Router：面向执行类任务的成本感知开集VLM路由框架
authors:
- Tao Yu
- Yifei Qu
- Zhiqing Cui
- Pengfei Zhou
- Zhongtian Luo
- Yujia Yang
- Shenghua Chai
- Haopeng Jin
- Zhenghao Zhang
- Xinming Wang
affiliations:
- CASIA
- UCAS
- NUS
- Tencent
arxiv_id: '2608.12127'
url: https://arxiv.org/abs/2608.12127
pdf_url: https://arxiv.org/pdf/2608.12127
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: Agent执行优化 · 多模型成本感知路由
tags:
- VLM Routing
- Cost-Aware
- Open-Set
- Dual-Tower
- Execution Task
- Benchmark
one_liner: 提出成本感知开集VLM路由框架与执行类任务基准，新增模型无需重训即可接入
practical_value: '- 双塔式开集路由架构可直接复用在电商多LLM/VLM流量调度场景，新增模型仅需跑校准集生成Profile即可上线，无需重训路由模型，大幅降低新模型接入成本

  - CRM+RCCR损失函数可直接替换现有路由模型的损失，将成本偏好编码进训练目标，无需事后加规则调整，对任意架构均适用，可带来1.25~6.21的Rank Score提升

  - 50%随机+30%诊断+20%多样性的混合校准采样策略，可复用在大模型冷启动评估环节，用最少样本覆盖最大模型差异场景，降低校准/评估成本

  - 执行类任务的三层拆分评估范式（路由输入/执行上下文/验证规则），可借鉴来构建业务Agent的效果评估体系，实现路由决策层与执行层解耦，更贴近真实部署场景'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前异构LLM/VLM生态下，不同模型的能力、成本、时延差异可达两个量级，单一模型无法兼顾全场景效果与成本。现有VLM路由方法仅适配传统VQA任务，开集支持弱（新增模型需重新训练整个路由），且训练目标未纳入成本约束，无法满足代码生成、工具调用Agent、多步搜索等执行类任务的路由需求。

### 方法关键点
- 发布首个执行类VLM路由基准VLM-ExecRouterBench，覆盖代码、Agent、搜索3个领域共34k样本，11个候选模型的定价差接近两个量级，样本统一拆分为路由输入/执行上下文/验证规则三层，解耦路由可见信息与模型执行逻辑；
- 设计双塔式SCOPE-Router，将路由转化为查询与模型Profile的匹配问题，模型Profile由混合校准集（50%随机+30%诊断+20%多样性采样）生成，新增模型仅需跑一遍校准集生成Profile即可接入路由，无需重训；
- 提出架构无关的CRM+RCCR训练目标：CRM将成本偏好编码为连续相关性目标，用逐对独立BCE替代softmax避免多正样本信号稀释；RCCR约束路由偏好相似的查询在特征空间更接近，提升泛化性。

### 关键结果
在VLM-ExecRouterBench、VL-RouterBench、MMR-Bench三个公开基准上Rank Score均排名第一，OOD场景超第二名1.84分，双OOD开集场景超第二名6.75分；CRM+RCCR损失替换到4种现有不同架构的路由模型，Rank Score提升1.25~6.21分；对比全局最强单模型基线，成本降低85%，精度仅下降5.21pp。

### 核心结论
多模型路由的核心不是选全局最好的模型，而是选对当前query性价比最高的模型，开集无感知接入能力是大规模异构模型落地的核心刚需。
