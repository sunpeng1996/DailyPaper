---
title: 'WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge
  Routing'
title_zh: WorkSurface-Bench：面向企业Agent的多类型知识路由基准测试
authors:
- Hao Liang
- Meiyi Qiang
- Sizhe Qiu
- Linzhuang Sun
- Wentao Zhang
affiliations:
- Peking University
- Zhongguancun Academy
- University of Chinese Academy of Sciences
arxiv_id: '2607.25765'
url: https://arxiv.org/abs/2607.25765
pdf_url: https://arxiv.org/pdf/2607.25765
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: 企业Agent · 多知识面路由评测
tags:
- Agent
- Benchmark
- Knowledge Routing
- RAG
- Enterprise LLM
one_liner: 首个拆分知识面路由与回答正确性的企业级Agent基准，包含1151个可审计原子任务
practical_value: '- 开发电商/运营类Agent时，可拆分「知识类型选择→证据获取→答案合成」三个环节独立调优，避免端到端优化无法定位故障

  - 跨RAG、结构化运营表格、商品/内容依赖图的多源知识问答场景，可复用基准的可审计Gold构造逻辑：SQL执行结果、文档原文span、图路径作为标准答案，避免人工标注歧义

  - Agent路由调优可参考两个落地结论：1. 给模型明确所需知识类型提示可提升多数模型回答准确率；2. 移除无关工具可显著提升路由效率和F1，但不一定提升最终答案准确率

  - 多源知识问答效果评估可直接复用这套拆分指标：Route F1、Evidence、Answer、Efficiency，精准定位性能瓶颈'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有企业Agent基准通常仅端到端评测回答正确性或工具选择，未拆分「选择适配问题的知识形态（文档/表格/图）」和「基于知识正确推理回答」两个独立能力，导致故障无法定位，路由模块优化缺乏明确的评估标准。

### 方法关键点
- 基于Workspace-Bench-Lite的5个角色企业工作区，映射为三类可路由知识面：文档RAG库、DuckDB可查询结构化表格库、文件依赖图谱库，流程SOP仅作为任务元数据不单独作为路由目标
- 生成1151个原子任务，所有标准答案可审计：表格类答案来自执行后的DuckDB查询结果，文档类答案匹配原文span，图类答案来自原始依赖标注，无模型生成的自由文本标准答案
- 拆分4个独立评估指标：Route F1（知识面选择准确率）、Evidence（所需证据获取完整度）、Answer（最终回答正确率）、Efficiency（token使用效率）

### 关键实验结果
覆盖4类主流LLM backbone（GPT-4o-mini、DeepSeek-V4-Pro、Gemini-3.1-Pro、GPT-5.5）、6种Agent设置，共生成27624条无协议错误轨迹；给定黄金知识面约束的Agent Route F1可达98.7%~99.8%，但最终Answer准确率仅56.1%~75.3%；路由F1与回答准确率的相关系数仅为0.62，无强关联；移除无关工具可提升效率8.8~22.3个百分点。

> 最值得记住的结论：知识面路由正确不代表回答正确，Agent优化必须拆分路由、证据获取、答案合成三个环节独立调优
