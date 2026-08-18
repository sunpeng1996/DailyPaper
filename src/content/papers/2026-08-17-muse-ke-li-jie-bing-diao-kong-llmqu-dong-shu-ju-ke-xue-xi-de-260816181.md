---
title: 'MUSE: An Interactive Meta-Agent for Understanding and Steering LLM-powered
  Data Science Systems'
title_zh: MUSE：可理解并调控LLM驱动数据科学系统的交互式元代理
authors:
- Wei-Hao Chen
- Weixi Tong
- Yuan Tian
- Chenglong Wang
- Tianyi Zhang
affiliations:
- Purdue University
- Microsoft Research
arxiv_id: '2608.16181'
url: https://arxiv.org/abs/2608.16181
pdf_url: https://arxiv.org/pdf/2608.16181
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: 元Agent 调控LLM驱动数据科学系统
tags:
- Meta Agent
- Agent Observability
- Interactive Agent
- LLM Agent Debugging
- Human-Agent Interaction
one_liner: 提出分层语义解析、主动告警、上下文引导干预的元代理，提升用户调控LLM数据科学Agent的效率与信心
practical_value: '- 可复用多层级语义抽象设计，将推荐/广告Agent的底层执行日志（召回/排序逻辑、特征调用、工具调用）做L1到L5分层展示，降低运营/算法同学排查问题的成本，无需翻全量trace

  - 可借鉴主动告警+脚手架修复逻辑：针对推荐Agent常见异常（特征漏取、规则未触发、样本skew）预设启发式检测规则，告警同时给出可选修复方案，降低非算法专家的干预门槛

  - 可复用上下文锚定交互设计：支持用户拖拽指定异常步骤，系统自动关联上下游上下文生成干预指令，无需用户手动梳理历史信息，提升Agent调试效率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM驱动的Agent系统执行轨迹多为无结构低层级日志，非专业用户难以快速定位问题、干预流程，现有Agent调试工具多面向开发者，普通用户面临信息过载、干预门槛高的问题，亟需无需精通Agent开发即可理解、调控Agent执行流程的方案。

### 方法关键点
- 分层语义转换层：将底层Agent的推理轨迹、工具调用、代码、执行信号等原始日志按完成标记切分为语义块，生成从L1（阶段标题）到L5（全量原始trace）的5级抽象表示，支持按需查看
- 监控层：预设数据科学场景常见异常启发式检测规则，主动识别可疑步骤并挂载局部告警，支持点击查看告警原因、关联代码片段
- 验证层：支持用户拖拽指定步骤作为查询锚点，自动关联上下文回答问题；用户选中结果后自动生成可选验证方案，生成验证脚本在沙箱运行无需修改原流程
- 调控层：针对告警步骤给出可选修复方案，自动拼接修复指令与上下文传递给底层Agent，无需用户手动梳理历史信息

### 关键实验
15名不同背景用户的组间对比实验，对比基线为原始日志界面、DiLLS分层摘要工具，数据集为6个真实场景Kaggle数据科学任务。MUSE组任务平均耗时17分钟，比原始日志组降低35%，比DiLLS组降低9%；任务成功率达90%，与DiLLS组持平、是原始日志组的1.8倍；用户对结果的信心评分达4.2/7，远高于基线组的2.6/7；告警修复率达2.8个/人，是DiLLS组的3.5倍。

### 核心洞察
对Agent的可观测性设计不能只面向开发者，要按业务语义做分层抽象，同时提供从告警到修复的全链路脚手架，才能降低普通用户使用和干预Agent的门槛。
