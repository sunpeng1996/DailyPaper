---
title: 'Knowing the User Is Not Knowing What We Established: Grounding Awareness in
  Personal Agents'
title_zh: 面向个人Agent的共识感知能力：区分用户信息与双方达成的生效约定
authors:
- Jiajun Chen
- Xinyue Chen
- Yicheng Jiang
- Hua Shen
affiliations:
- Carnegie Mellon University
- New York University
- NYU Shanghai
arxiv_id: '2610.18684'
url: https://arxiv.org/abs/2610.18684
pdf_url: https://arxiv.org/pdf/2610.18684
published: '2026-10-13'
collected: '2026-10-16'
category: Agent
direction: 个人Agent · 记忆系统共识校验
tags:
- Personal Agent
- Memory System
- Grounding
- LLM Agent
- Common Ground
one_liner: 提出共识感知概念与无训练Grounding Layer，解决个人Agent误执行未授权提议的问题
practical_value: '- 电商智能客服/购物Agent可复用Grounding Layer设计，在现有记忆系统外新增共识台账，记录用户对Agent提议的接受状态、生效范围，避免未经确认自动执行优惠券领取、订单取消等高风险操作，降低客诉

  - 推荐系统的用户偏好记忆模块可新增交互状态标签，区分「用户明确表达的偏好」「系统猜测的偏好」「用户未确认的推荐策略」，避免过度推送未授权的内容/服务

  - Agent动作执行前新增拦截校验门，针对高影响动作（下单、退订、发消息）必须匹配共识台账的授权状态，无需改造原有LLM和记忆系统，落地成本极低'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有个人Agent的记忆系统仅关注存储用户的偏好、事实信息，不会区分「Agent提出的提议」和「用户已经确认接受的生效约定」，很容易把未授权的提议当成用户指令跨会话执行，造成越权操作（比如私自拒接电话、下单等）。现有记忆评测benchmark也完全没有覆盖跨会话的共识校验场景，导致这一风险被长期忽略。

### 方法关键点
- 定义**Grounding Awareness（共识感知）**能力：要求Agent能区分已接受、未确认、已修订、限定范围的四类约定，仅在授权范围内执行动作
- 构建160个场景、800个测试用例的跨会话共识评测benchmark，每个场景生成5组仅共识状态不同的对照对话，排除其他变量干扰
- 提出无训练的**Grounding Layer**组件：由共识台账（记录约定的提议方、接受状态、生效范围、对话证据）、执行门（高风险动作前校验授权）、溯源校验（回查原始对话补全缺失信息）三部分组成，无需修改原有模型和记忆系统

### 关键实验
在Mem0、A-Mem、MemOS、LangMem等主流记忆系统，以及GPT、Qwen、Gemini、DeepSeek等主流LLM上测试：现有系统的共识感知Sensitivity平均仅0.23，远低于偏好跟踪任务的平均0.64得分；给记忆内容增加共识状态标签可将Qwen的Sensitivity从0.09提升到0.34；叠加Grounding Layer后，LangMem搭配Qwen的Sensitivity从0.21提升到0.51，未授权执行率从0.44降到0.08。

### 最值得记住的一句话
更强的记忆性能和更大的信息访问量并不能保证Agent做出符合共识的决策，甚至可能提升未授权操作的概率
