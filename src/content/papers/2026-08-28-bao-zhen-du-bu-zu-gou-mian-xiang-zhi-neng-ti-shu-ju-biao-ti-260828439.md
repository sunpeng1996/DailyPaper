---
title: 'Fidelity Is Not Enough: Dispatch-Level Instrumentation for Agentic Datasheet
  Extraction'
title_zh: 保真度不足够：面向智能体数据表提取的调度级可观测方案
authors:
- Qing Ye
- Meng-Hsuan Lin
affiliations:
- Infineon Technologies AG
arxiv_id: '2608.28439'
url: https://arxiv.org/abs/2608.28439
pdf_url: https://arxiv.org/pdf/2608.28439
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 工具调用可观测性与静默错误检测
tags:
- Agent Evaluation
- Tool Calling
- Silent Failure Detection
- Document Extraction
- Observability
one_liner: 提出基于工具调用日志的Agent静默错误检测方案，补全文档提取仅靠保真度评估的缺陷
practical_value: '- 业务部署Agent服务（如商品参数提取、商家资质审核、合同信息抽取）时，不要仅校验最终输出正确性，必须埋点全链路工具调用日志，可直接复用论文中的「无导航调用」「无交叉校验调用」两个规则低成本检测静默错误，实测零误报。

  - 跨模型部署Agent时不要仅验证SDK调用成功，必须额外做工具调用层的兼容性校验：JSON Schema输出约束可能被底层vLLM实现为token掩码，静默阻断工具调用，这类问题仅靠调度层埋点可发现。

  - Agent架构选型优先用单上下文窗口方案，仅当待处理文档/知识库超出上下文窗口时再切换带工具导航的Agent方案：工具层的核心价值是可观测性和长文档适配，而非提升准确率。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agent文档提取任务仅以**保真度**（输出与源文档匹配度）作为核心评估指标，无法识别模型未调用工具、完全依赖预训练知识/幻觉输出结果却碰巧匹配的静默错误。作者团队在内部上线电子元器件数据表提取生产服务时，就遇到某模型过了全量保真度校验、但实际从未打开目标数据表的问题，仅通过全链路工具调用trace才发现该故障。

### 方法关键点
- 构建含37个人工标注定量参数的电子元器件数据表提取基准，每个样本同时完成两类校验：与源文档比对的保真度校验、与物理实测结果比对的可复现性校验。
- 全链路埋点工具调用调度日志，基于日志设计无参数的静默错误检测器：无任何导航工具调用触发`tool-bypass`告警、有导航但无全文搜索/表提取交叉校验触发`verification-skipped`告警，全程不校验输出内容。
- 设计两阶段冻结的Agent执行流程：提取阶段仅开放文档侧工具，提交提取结果后才开放物理实测工具，避免信息泄露。

### 关键实验结果
- 测试3个工业级模型栈（Claude Sonnet 4.6、GPT-5.1、Qwen3.6-27B），207个通过保真度的干净样本上检测器零误报，50个人工植入的静默错误100%召回。
- 文档长度在上下文窗口内时，单轮LLM方案与Agent方案准确率一致，Agent仅带来1.2~1.8倍的成本上升；当文档超出上下文窗口时，Agent方案成本随所需提取页面数线性增长，远低于全量长文档输入成本。
- 物理实测仅能覆盖2/37的提取claim，给出了其余claim无法物理校验的分类体系。

### 核心结论
保真度对Agent提取任务是必要不充分条件，只有调度层的全链路工具调用埋点能发现保真度评估漏过的静默错误。
