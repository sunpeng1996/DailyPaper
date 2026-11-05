---
title: Task-Efficient Agent Evaluation Using Cached Traces
title_zh: 基于缓存执行轨迹的高效Agent评估方法
authors:
- Ben Johnson
- Hayden Helm
affiliations:
- Jataware
- Helivan
arxiv_id: '2611.06803'
url: https://arxiv.org/abs/2611.06803
pdf_url: https://arxiv.org/pdf/2611.06803
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: Agent 低样本性能评估优化
tags:
- Agent Evaluation
- Trace Embedding
- Item Response Theory
- Efficient Benchmarking
- LLM
one_liner: 提出trubric任务专属轨迹表征，结合几何建模与IRT实现低样本下的高效Agent性能评估
practical_value: '- 电商/广告领域自研Agent（导购、客服、运营辅助、素材生成Agent等）做内部评估时，可复用trubric思路：针对业务任务定义专属评估维度，用LLM抽取轨迹结构化摘要再嵌入，过滤部署环境、基础模型家族等无关噪声，提升评估结果的可信度

  - 若内部积累了大量历史Agent的全量评估数据，可搭建「参考系统几何空间+IRT」的融合评估pipeline，新Agent仅需跑1-5个任务即可预测全量基准分，评估成本降低80%以上，适合快速版本迭代

  - 做Agent版本A/B测试前，可先用该方法做前置校验，单任务下两两Agent排序准确率可达88%，快速淘汰明显劣质的版本，减少全量测试的资源消耗'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent全量基准评估成本极高，单轮完整评估常超过2000美元；传统低样本评估方法仅依赖执行结果的二元正误标签，浪费了执行轨迹中包含的大量Agent行为信息；而直接嵌入原始轨迹会混入系统标识、模型家族、运行框架等无关噪声，无法准确表征Agent的真实能力。

### 方法关键点
- 提出trubric任务专属轨迹表征：首先针对每个具体任务用LLM生成专属评估字段（如问题理解、资源定位、修改验证等），再用LLM按字段抽取执行轨迹的结构化摘要，拼接各字段的语义嵌入得到最终表征，可有效保留任务、执行正误相关信号，过滤无关噪声。
- 基于trubric表征构建所有参考系统的低维几何空间，用回归模型预测新Agent的全量基准分；同时结合IRT（项目反应理论）的正误标签结果做加权融合，进一步提升不同任务预算下的预测精度。

### 关键结果
在SWE-bench Verified、Terminal-Bench 2.0两个主流Agent基准上测试，对比IRT、原始轨迹嵌入等基线：
- 仅用1个随机执行任务时，融合方案在两个基准上的MAE分别从0.13降至0.08、从0.14降至0.12，统计显著性p均小于1e-3；
- SWE-bench场景下达到MAE<0.1的评估成本从10-40美元降至2美元，单任务下两两Agent排序准确率达88%；
- 效果对文本编码器选择不敏感，7个主流开源/闭源嵌入器的MAE差异小于0.008。

> 最值得记住的一句话：仅依赖二元正误标签的低样本评估浪费了大量轨迹信息，结合任务专属的结构化轨迹表征可将Agent评估成本降低一个数量级
