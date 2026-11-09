---
title: How Much Conversation History Does an AI Agent Need?
title_zh: AI Agent对话记忆预算的成本效果权衡与保留策略研究
authors:
- Danny Kim
- Fernando Koch
affiliations:
- Pembroke Pines Charter High School
- Florida Atlantic University
arxiv_id: '2611.09662'
url: https://arxiv.org/abs/2611.09662
pdf_url: https://arxiv.org/pdf/2611.09662
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 对话记忆预算优化
tags:
- ConversationalMemory
- ContextBudgeting
- LLMAgent
- TokenEfficiency
- BenchmarkEvaluation
one_liner: 量化对话Agent记忆预算的token成本与效果权衡，验证不同信息保留策略的适用边界
practical_value: '- 电商导购/客服Agent可优先采用「保留所有用户消息+最近3条上下文」策略，直接要求类query可省30%左右token，效果下降可控

  - 若业务query涉及历史offer引用（如用户说“就要你上轮推荐的那款”），不可仅保留用户消息，必须同步留存对应的系统回复上下文，避免信息缺失

  - 做Agent效果评估时，不能完全依赖LLM自动打分，需针对时间推理、优惠引用类场景增加原始上下文对齐校验，降低误判

  - 算力预算有限的场景，可将历史检索召回的passage数从10降至3，能节省67.8%的reader token，仅损失5.45分的基准评分，性价比突出'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前对话Agent的记忆管理缺乏量化的成本效果参考：全量保留历史会导致token成本高、推理延迟大，过度裁剪又容易丢失关键上下文导致回答错误；同时现有基准的自动打分与回答实际正确性的对齐度不明确，无法有效指导记忆策略优化。
### 方法关键点
- 固定检索排序、Reader模型、打分逻辑，仅调整传入Reader的历史passage数量（1/3/5/10/20共5档），控制变量测算成本-效果tradeoff
- 拆分可回答类、需拒答类两种问题类型，对比不同记忆预算下的效果差异，同时审计基准打分的有效性
- 构造控制实验，对比直接要求、历史offer引用两类场景下，用户消息保留、等token最近上下文两种策略的信息留存效果
### 关键实验结果
在BEAM基准的1100条问题上测试，Reader采用Qwen2.5-14B：
1. 召回passage数从10降至3，可节省67.8%的Reader token，仅带来5.45分的基准评分损失；若提升至20条，token消耗翻倍仅涨2.39分
2. 需拒答类问题缩小记忆预算时，评分反而提升11.4分
3. 控制实验中，用户消息保留策略对直接要求类场景的全状态匹配率达100%，对历史offer引用类场景匹配率为0
### 核心结论
对话记忆的最优预算没有通用解，必须匹配当前query所需的证据类型，同时效果评估必须关联原始上下文做正确性校验
