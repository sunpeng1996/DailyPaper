---
title: 'BobFlow: Towards Human-Agent Collaborative Data Science Using Dataflows'
title_zh: BobFlow：基于数据流的人机协同数据科学系统
authors:
- Jiadong Bai
- Yicong Huang
- Chen Li
affiliations:
- University of California, Irvine
- University of Massachusetts Amherst
arxiv_id: '2611.05761'
url: https://arxiv.org/abs/2611.05761
pdf_url: https://arxiv.org/pdf/2611.05761
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 人机协同 · 数据流抽象优化
tags:
- LLM Agent
- Human-Agent Collaboration
- Dataflow
- ReAct
- Cost Optimization
one_liner: 提出结合数据流抽象与ReAct范式的人机协同数据科学系统，提准确率同时大幅降推理成本
practical_value: '- 开发业务分析/特征工程类Agent时，可封装领域通用的声明式算子（如filter、join、聚合、特征计算）替代让LLM直接生成Python脚本，既能降低输出token量，还能减少代码语法/逻辑错误，人也更容易快速理解Agent的处理逻辑

  - Agent调用工具返回执行结果时，用样本+维度统计量代替全量数据输入LLM上下文，可在不丢失关键数据特征的前提下降低输入token成本，适合电商大量表分析场景

  - 多轮人机交互场景下，可基于算子/模块的依赖关系剪枝无关历史上下文，仅保留当前修改节点的上游相关记录，大幅缩短上下文长度同时不影响推理准确性'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM驱动的数据科学Agent普遍采用自然语言、Python脚本、SQL作为计算抽象，三类抽象均存在缺陷：自然语言歧义性高，脚本语法复杂、人难理解调试，SQL不暴露中间处理步骤，导致人机协作时人很难快速对齐Agent的分析逻辑、提供精准反馈，同时全量代码/结果塞上下文也会推高推理成本。

### 方法关键点
- 采用数据流DAG作为人机共享的计算抽象：每个节点为声明式算子（含scan、filter、join、聚合、自定义算子），边表示数据依赖，同时满足语义精确、易理解、中间步骤透明三个要求
- 提出Dataflow ReAct框架：Agent基于数据流抽象迭代生成/修改算子、执行、获取结果，支持人机并行编辑同一数据流
- 两层上下文优化：一是算子执行结果用样本+统计量代替全量数据返回LLM，二是基于算子依赖剪枝无关历史观测，大幅降低token消耗
- 内置中断、跳转历史快照等交互原语，支持人随时介入修正分析流程、分支探索不同分析路径

### 关键实验
在PrepBench、KramaBench、LongDS-Bench三个数据科学基准上对比基于Python脚本的ReAct基线，覆盖8款主流闭源/开源LLM：BobFlow准确率最高提升18.6个百分点，推理成本最多降低64.7%，输出token量最多减少77.3%；用户研究显示，使用者排查分析错误的迭代次数减少57%，单任务推理耗时降低70%。

最值得记住的一句话：给Agent设计结构化的领域专属抽象，比让它直接生成无约束的代码，更容易实现低成本、高可靠的人机协同。
