---
title: 'LLM within MCP Matters: Measuring Inefficient Resource Utilization Driven
  by LLMs'
title_zh: MCP场景下LLM资源利用低效问题的量化分析
authors:
- Minhan Cho
- Soyoung Park
- Kihyeon Jeong
- Byeongkyu Jeon
- Daejin Choi
- Jinyoung Han
affiliations:
- Remember & Company AI Lab
- Sungkyunkwan University
- National Assembly Research Service
- AlphaBridge
- Ewha Womans University
arxiv_id: '2608.08467'
url: https://arxiv.org/abs/2608.08467
pdf_url: https://arxiv.org/pdf/2608.08467
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: Agent工具调用优化 · MCP协议
tags:
- MCP
- Tool Calling
- LLM Agent
- Prompt Engineering
- Instruction Following
one_liner: 通过5.4万次实验量化MCP场景下LLM的工具调用偏好，给出三类prompt干预优化方案
practical_value: '- 开发MCP服务端时，优先同时添加强制优先级指令、正反调用样例、工具描述前置提示三类干预，避免单类干预对部分模型反效果，可覆盖20/24款主流模型实现≥86%的调用效率提升

  - 针对电商/推荐Agent高频查询场景，可将Top N高频item ID/属性映射表嵌入系统提示，配合三类干预措施，减少不必要的召回/搜索工具调用，降低latency和Token开销

  - 选型Agent底座LLM时不要盲目追新，新一代模型反而可能存在工具选择偏好偏差，需针对业务场景做工具调用效率实测验证

  - 若服务面向多模型客户端，不要仅依赖prompt工程修复，可在Agent编排层加前置校验：调用工具前先匹配嵌入参考数据，从架构层面规避资源浪费'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
MCP协议已成为LLM Agent对接外部数据与工具的主流标准，业界常用将高频参考数据嵌入服务端系统提示的设计来降低调用开销，但目前缺乏对不同LLM实际利用这类嵌入数据效率的量化研究，工具选择偏好导致的资源浪费问题尚未被明确验证。

### 方法关键点
- 测试基于生产级法律信息MCP服务器LexLink，其系统提示嵌入Top20高频法律的ID映射表，理想情况下LLM应直接用ID调用查询接口，无需调用搜索接口
- 覆盖24款主流LLM（9款Claude、6款Gemini、9款GPT），设计3类指令干预：添加强制优先级指令（B）、补充正反调用样例（C）、工具描述加前置检查提示（D），共8种组合+无搜索工具对照组
- 核心指标hit ratio φ：首次工具调用为正确ID直查的占比，总实验量5.4万次

### 关键结果
- 无搜索工具时，23/24款模型φ≥98%，说明几乎所有模型都具备读取嵌入数据的能力
- 存在搜索工具的基线场景下，9款模型φ<15%，工具存在会触发LLM的调用偏好，而非能力不足
- 同时叠加B/C/D三类干预后，20/24款模型φ≥86%，但单类干预可能反效果（如GPT-5.2单独加B干预时φ从5%降到0%）

### 核心结论
LLM工具调用效率和模型新旧无关，prompt工程是临时 workaround，从MCP宿主层强制优先读取嵌入指令才能从根本解决资源浪费问题
