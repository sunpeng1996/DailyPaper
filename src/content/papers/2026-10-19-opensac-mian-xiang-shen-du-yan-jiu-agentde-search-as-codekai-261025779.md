---
title: 'OpenSaC: A Python Library for Search as Code in Deep Research Agents'
title_zh: OpenSaC：面向深度研究Agent的Search as Code开源Python库
authors:
- Qi Liu
- Jiaxin Mao
- Fengbin Zhu
- Tat-Seng Chua
- Ji-Rong Wen
affiliations:
- Renmin University of China
- National University of Singapore
arxiv_id: '2610.25779'
url: https://arxiv.org/abs/2610.25779
pdf_url: https://arxiv.org/pdf/2610.25779
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: Agent工具 · Search as Code 开源框架
tags:
- Search_as_Code
- Deep_Research_Agent
- Python_Library
- Agent_Tool
- Programmatic_Retrieval
one_liner: 开源OpenSaC Python库，支持Agent以代码编排检索处理流程，降低Search as Code落地门槛
practical_value: '- 电商/广告检索类Agent可复用OpenSaC的批检索-重排-抽取组合范式，减少LLM多轮交互次数，降低推理时延和token开销

  - 业务侧自研检索Agent工具链时，可参考其可插拔Provider适配架构，灵活切换搜索、重排、LLM服务供应商，无需修改上层逻辑

  - 做复杂信息收集类任务（如竞品分析、舆情调研、商品参数爬取整合）时，可借鉴Search as Code思路，将固定流程的检索、过滤、解析逻辑封装为代码批量执行，仅将关键信息返回LLM决策'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统ReAct范式的深度研究Agent遵循「推理-单步动作」循环，每次检索、页面读取操作都需要触发LLM决策，大量无意义的中间交互会占用上下文窗口、提升token消耗与推理时延；现有Search as Code实现多为闭源服务，缺乏可扩展、可透明审计的开源框架支撑业务快速落地。
### 方法关键点
- 提供标准化可组合SDK接口，覆盖批搜索、批内容抓取、重排、LLM生成/结构化抽取、结果融合、去重等核心检索处理能力，统一不同后端的返回格式，全程保留证据溯源链路
- 采用可插拔Provider适配架构，不同搜索、重排、LLM服务可通过适配器接入，上层业务逻辑无需修改即可切换后端服务
- 配套Search as Code技能指引，引导Agent自动批量编排独立检索请求、处理返回结果、筛选关键证据返回给LLM，减少不必要的模型交互
### 关键实验
在BrowseComp事实发现、WideSearch信息收集两个基准数据集上，对比原生内置web搜索的Codex：
- BrowseComp任务：准确率提升2.96pp，执行时间降低30.3%，token消耗降低37.8%，推理成本降低36.4%
- WideSearch任务：执行时间降低29.5%，token消耗降低13.8%，推理成本降低12.6%，仅F1值小幅下降0.84pp
### 核心结论
将可批量执行的检索、数据处理逻辑封装为代码批量执行，仅将必要决策点返回LLM，是大幅降低Agent推理成本、提升执行效率的核心路径
