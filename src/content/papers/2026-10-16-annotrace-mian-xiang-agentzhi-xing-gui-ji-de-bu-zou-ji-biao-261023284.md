---
title: 'Annotrace: A Workbench for Step-Level Annotation of Agent Traces'
title_zh: Annotrace：面向Agent执行轨迹的步骤级标注工作台
authors:
- Arun Josephraj Arokiaraj
- Chenyi Huang
- Sahan Bulathwela
- Zekun Wu
- Bin Wu
affiliations:
- University College London
arxiv_id: '2610.23284'
url: https://arxiv.org/abs/2610.23284
pdf_url: https://arxiv.org/pdf/2610.23284
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 执行轨迹标注工具开发
tags:
- Agent
- Trace Annotation
- LLM Agent
- Observability
- Human-in-the-loop
one_liner: 支持多格式Agent轨迹解析的人机协同步骤级标注工作台，可100%复现人工标注结果
practical_value: '- 电商导购/推荐类Agent做故障归因时，可直接复用Annotrace的6种主流观测格式适配能力，对接现有LangSmith/Langfuse等观测链路，无需从零开发标注工具

  - 可借鉴其人机协同标注流程：先用低成本小模型预标注Agent轨迹的错误步骤/归因标签，再人工审核修正，可降低70%以上的标注人力成本

  - 做Agent离线效果评估时，复用其标注一致性校验逻辑，支持人/模型标注结果的Cohen’s κ计算，保障标注数据集的质量可靠性'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM Agent故障分析高度依赖人工标注的执行轨迹数据，但现有工具存在明显缺口：观测平台（LangSmith、Langfuse等）仅支持轨迹存储展示，无结构化标注能力；通用文本标注工具不识别Agent特有的步骤嵌套、工具调用、子任务委托等结构，打平成文本后会丢失错误定位的关键信息；各研究团队均自研一次性标注工具，复用性极低，浪费大量研发成本。
### 方法关键点
- 多格式适配层：内置6种主流Agent轨迹格式的转换器，自动识别格式并转换为统一的Step对象，保留原始嵌套层级、步骤类型、执行主体信息，支持从混合文本字段中拆分出Thinking-Action-Response循环
- 自定义标注schema：用户可可视化配置标注问题、可选标签、生效的步骤类型、条件跳转逻辑，无需硬编码修改源码
- 人机协同标注流：大模型先基于10条采样轨迹自动生成初始标注schema，再对全量轨迹做预标注，人工仅需修正错误结果，标注全程保留人/模型的标注主体信息
- 一致性校验：支持任意两个标注主体（人/模型）的标注结果对比，输出原始一致率和Cohen’s κ系数，识别分歧步骤
### 关键结果
在40条多Agent HotpotQA语料上，100%复现此前人工标注的235个Thinking-Action-Response单元；两个大模型标注同一轨迹的一致率达91%，Cohen’s κ=0.82；单schema生成耗时约4s，单条轨迹标注仅需3-5s，单条调用成本不到0.01美元。
### 核心结论
Agent故障分析的最小标注单元是执行步骤而非整条轨迹，打平轨迹会直接丢失错误定位的关键上下文。
