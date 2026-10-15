---
title: 'Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models
  in Agent Loops'
title_zh: Agent循环中System One类快速决策模型的决策失败根因诊断
authors:
- Yubo Li
- Ramayya Krishnan
- Rema Padman
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.18579'
url: https://arxiv.org/abs/2610.18579
pdf_url: https://arxiv.org/pdf/2610.18579
published: '2026-10-12'
collected: '2026-10-15'
category: Agent
direction: Agent决策错误诊断 · 快速System One模型
tags:
- Agent
- System One Model
- Decision Failure
- LLM Evaluation
- Probe Testing
one_liner: 通过配对事实探针与决策任务，诊断出System One模型73%~85%错误源于事实读取正确但决策失误
practical_value: '- 做Agent决策模块错误排查时，可复用「事实探针+配对检测」框架，拆分上下文理解错误与决策逻辑错误，快速定位迭代方向，比如电商导购Agent错误可拆分为未读对用户历史、或读对后选错商品/回复两类。

  - 低延迟要求的Agent场景（实时推荐、客服快速响应）使用System One模型时，可加「置信度阈值+决策级联」优化：对低置信度决策先调用并行探针获取关键事实/子目标再决策，实测ALFWorld场景下JEV模型准确率可提升16+个点，仅增加少量轻量调用开销。

  - 给LLM决策模块加辅助信息时，优先补充明确的子目标信息比补零散事实收益高3~5倍，不要随意添加不完整的事实摘要，可能反而拉低决策准确率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前System One类快速决策模型（单遍打分选候选动作，无CoT输出，延迟仅为推理模型的1/10）在低延迟Agent场景中广泛应用，但决策错误时无法追溯根因，无法区分是上下文理解错误还是决策逻辑错误，严重阻碍模型迭代优化。

### 方法关键点
- 构建含65228条记录的冻结决策基准，覆盖模拟环境、客服政策、工具调用、网页导航、编码5类场景，每条记录关联决策任务和若干独立事实探针（如上一步动作是否成功、Agent当前状态等）
- 设计四象限归因框架：交叉「所有事实探针回答正确」和「决策正确」两个指标，拆分四类错误结果
- 提出探针充分性检验规则：只有当探针答案集合能唯一确定最优动作时，「事实对、决策错」才能归因于决策模块缺陷

### 关键结果数字
- 测试17种System One模型+GPT-6.1推理模型，准确率TOP6的System One模型73%~85%的决策错误都发生在所有事实探针全对的场景，且模型准确率越高，该占比越高
- 探针充分的场景下，将模型自身输出的正确事实拼接后决策，可修复15~28个点的准确率，直接用代码基于探针结果组合决策可达96%~100%准确率
- 真实场景下，给决策任务补充明确的下一级子目标，比补充零散事实的准确率增益高3倍以上，JEV模型在ALFWorld场景下单独加子目标即可提升16.3个点

**最值得记住的一句话**：快速决策模型的瓶颈早已经不是上下文理解，而是事实组合、子目标规划等决策层能力。
