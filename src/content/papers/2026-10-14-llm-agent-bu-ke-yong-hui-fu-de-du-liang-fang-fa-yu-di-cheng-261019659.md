---
title: Measuring and Reducing Unusable Replies of LLM Agents
title_zh: LLM Agent 不可用回复的度量方法与低成本优化方案
authors:
- Yilin Jiang
- Fei Tan
- Xuanyu Yin
- Guanchu Wang
- Xia Hu
- Yutao Yue
affiliations:
- 华东师范大学
- 香港科技大学（广州）
- 上海人工智能实验室
- 江苏省产业技术研究院深度感知技术研究所
arxiv_id: '2610.19659'
url: https://arxiv.org/abs/2610.19659
pdf_url: https://arxiv.org/pdf/2610.19659
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 交互回复可用性优化
tags:
- LLM_Agent
- Usability_Evaluation
- Response_Rewriting
- Prompt_Engineering
- Human_Agent_Interaction
one_liner: 提出LLM Agent回复可用性量化框架与两种低成本优化方案，大幅降低不可用回复占比
practical_value: '- 电商导购、广告投放类业务Agent可直接复用reader模型做回复可用性校验，过滤未解释的内部标识、专业术语，避免用户看不懂反复咨询，降低客诉率

  - 可直接在业务Agent的回复环节追加明确的回复要求prompt，零额外开发成本即可将不可用回复率降低约17%，同时减少事实错误与信息遗漏

  - 若无法修改上游Agent的系统prompt，可新增开源轻量模型作为二次改写模块，输入原始回复、任务上下文和规范要求，可进一步将不可用率降至36%

  - 多轮Agent的记忆模块在输出前需过滤内部生成的临时ID、工具调用标识、私有工作词汇，避免内部术语暴露给终端用户'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM Agent评估仅关注任务完成度与回复事实一致性，忽略了请求者未见过Agent私有执行过程（工具调用、临时记录、中间标识）的场景，超过半数的Agent执行完多步任务后返回的回复存在大量用户无法理解的内部词汇，完全无法落地使用。

### 方法关键点
- 定义回复可用性三判据：仅通过请求者可见上下文可解释、语言与请求者匹配、直接回应请求，违反任意一条即判定为不可用回复
- 构建reader模型模拟请求者视角：先针对回复生成需要解答的定义、指代、背景类问题，再在请求者可见上下文内检索答案，无答案即标记为信息缺口，自动完成可用性判定，与人类多数标注的Cohen's κ达0.60，达到单个标注员的标注水平
- 提出两种零额外开发成本的优化方案：在回复环节追加明确的回复要求prompt、用轻量二次模型对原始回复做重写

### 关键结果
在7个模型族8款模型的480条多任务回复上测试：基线不可用率达54%，最优模型也有30%的不可用率；追加回复要求prompt后不可用率从52%降至43%，事实错误+遗漏量从1.41/条降至1.07/条；二次重写方案可进一步将不可用率降至36%，人类盲测验证了优化效果。

### 核心结论
仅告知Agent「用户看不到执行过程」几乎无效果，明确列出回复必须包含的要素（先答核心问题、解释陌生名词、说明来源）才能有效降低不可用率
