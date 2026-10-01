---
title: 'cua-speedrun: Standardized Benchmarking of the Speed of Computer-Use Agents'
title_zh: cua-speedrun：计算机使用智能体（CUA）速度标准化基准测试
authors:
- Pranjal Aggarwal
- Lawrence Keunho Jang
- Sean Welleck
- Daniel Fried
- Ruslan Salakhutdinov
- Jing Yu Koh
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.40284'
url: https://arxiv.org/abs/2609.40284
pdf_url: https://arxiv.org/pdf/2609.40284
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent 计算机使用智能体效率评测
tags:
- CUA
- Agent Benchmark
- Efficiency Evaluation
- Pareto Frontier
- Standardized Infra
one_liner: 提出标准化CUA评测框架cua-speedrun，可公平对比不同Agent的性能、速度、成本trade-off
practical_value: '- 做电商自动化运营Agent、智能客服Agent等落地选型时，不要只看宣传的成功率，需搭建统一基础设施测试性能、速度、成本的Pareto最优配置，避免实际部署时效率不达标

  - 调优Agent推理参数时，默认「推理越少越快」的认知是错误的：适当调高推理努力可减少无效重复操作，反而能降低总耗时和成本，建议从低/中推理档位开始迭代调优

  - Agent与环境交互的I/O延迟不是越低越好：现有大模型未适配超高速I/O时，会因界面未加载完成增加额外观测请求，反而拉长总耗时，无需盲目投入资源优化到毫秒级I/O

  - 内部评测Agent效果时，可复用能量距离最小化的任务子集筛选方法，类似OSWorld的复杂任务场景下可减少84.9%的评测时间同时保持结果相关性≥0.95，大幅降低评测的GPU/API成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前计算机使用Agent（CUA）在多个基准上的成功率已超过人类水平，但速度与成本是大规模落地的核心瓶颈。现有CUA评测依赖异构基础设施、环境配置不统一，结果可复现性差，无法公平对比不同方案的效率，阻碍高效CUA的研发迭代。

### 方法关键点
- 标准化云原生评测基础设施：统一VM配置、执行管线与Agent接口，单Agent实现可无缝适配4类主流CUA基准，消除环境差异带来的评测偏差
- 代表性任务子集筛选：基于能量距离最小化算法选择最小任务子集，保证与全量评测的Spearman相关性≥0.95，大幅降低评测开销
- 多维度全链路埋点：拆分任务耗时为Agent计算、环境I/O、主动等待等模块，同时统计模型调用成本，输出性能-时间-成本联合Pareto前沿

### 关键结果
在OSWorld、OSWorld2等4个主流CUA基准上测试56种Agent配置，核心数据：① 无单一模型家族在性能、速度、成本三个维度均占优，所有评测的开源模型均未进入任意基准的Pareto前沿；② 适当调高推理努力可让Gemini 3 Flash的任务耗时降低45.5%、单任务成本降低58%；③ 超高速I/O反而使GPT-6 Astra的总任务耗时升高11%；④ 任务子集筛选可将OSWorld的评测时间降低84.9%，同时保持与全量评测的高相关性。

最值得记住的一句话：仅以成功率为核心的Agent选型完全脱离落地需求，必须结合业务的速度、成本约束，在统一评测框架下筛选Pareto最优配置。
