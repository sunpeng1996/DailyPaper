---
title: Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM
  Agents
title_zh: LLM Agent多工具请求下的检索结构完备性与成本对比
authors:
- Shuyang Zhang
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2610.41905'
url: https://arxiv.org/abs/2610.41905
pdf_url: https://arxiv.org/pdf/2610.41905
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent工具检索 · 多工具场景性能评估
tags:
- Tool Retrieval
- Multi-Tool Agent
- Completeness Metric
- Retrieval Cost
- LLM Agent
one_liner: 对比6类工具检索结构在多工具请求场景的完备性、成本与失效模式
practical_value: '- 低延迟要求的业务（如电商导购Agent、实时客服Agent）：若有75-90条域内多工具请求标注数据，优先选择COLT这类训练型set-level检索器，query时间无LLM开销，AppWorld场景下完备性比无训练方法高2-3倍，直接提升多步任务成功率。

  - 可容忍高延迟的后台任务（如运营数据分析Agent、自动化内容生成）：无标注数据时可选AnyTool这类LLM引导的层级检索，单query 31-38次LLM调用，完备性接近训练型方案，无需提前标注即可上线。

  - 多工具场景下不要直接使用平层BM25、稠密检索、单次LLM查询拆分的方案，AppWorld上k=16时完备性最高仅9.6%，基本无法支撑多步任务。

  - 工具检索模块可将completeness@k作为核心上线指标，比传统recall更贴合最终任务效果：实验中检索集完备时Agent任务成功率100%，不完备时仅5.1%。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
主流工具检索方法的评估大多基于单工具请求，而实际Agent任务常需要调用多个存在依赖关系的工具，漏召任何一个都会直接导致任务失败。现有聚合评估分数完全掩盖了多工具场景下的性能差异，不同检索结构的效果、成本、失效模式也缺乏统一对比框架。

### 方法关键点
- 覆盖6类主流工具检索结构的代表性方案：平层词汇/稠密检索、LLM查询拆分、LLM导航层级检索、先匹配服务器再匹配工具、依赖图检索、训练型set-level检索；
- 公平对比控制变量：所有稠密检索统一用bge-base，所有LLM步骤统一用DeepSeek-V3.2；
- 核心评估指标采用completeness@k（召回全部必需工具的请求占比），同时统计query阶段的LLM调用次数、token消耗量、端到端延迟。

### 关键实验结果
在两个多工具专属测试集上验证：345条AppWorld查询（至少需要2个有依赖的API）、103条MCP-Bench任务（97%需要多工具）。
1. 无训练且单query LLM调用≤1的方案，AppWorld上k=16时完备性最高仅9.6%；
2. 训练型COLT仅需75-90条域内标注数据训练，AppWorld完备性达32.8%、MCP-Bench达58.3%，query阶段无任何LLM开销；
3. 无训练的LLM导航层级检索AnyTool，AppWorld完备性达30.1%、MCP-Bench达39.8%，但单query需要31-38次LLM调用，中位数延迟约5分钟；
4. 下游任务验证：检索集完备时Agent任务成功率100%（21/21），不完备时仅5.1%（2/39）。

### 最值得记住的一句话
多工具场景下工具检索的完备性没有免费午餐：要么用少量域内标注数据换低延迟，要么用query阶段大量LLM调用换免训练。
