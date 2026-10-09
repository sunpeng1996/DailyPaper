---
title: 'Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under
  Knowledge Conflict'
title_zh: 知识冲突场景下LLM Agent的认知谦逊能力评估
authors:
- Kaiser Sun
- Bernal Jimenez Gutierrez
- Hongjun Liu
- Jingyu Zhang
- Jie Gao
- Mark Dredze
- Daniel Khashabi
affiliations:
- Johns Hopkins University
- New York University
arxiv_id: '2610.12360'
url: https://arxiv.org/abs/2610.12360
pdf_url: https://arxiv.org/pdf/2610.12360
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: Agent行为评估 · 认知谦逊
tags:
- LLM Agent
- Epistemic Humility
- Knowledge Conflict
- Trajectory Evaluation
- Agent Safety
one_liner: 提出ISE三维评估框架，揭示LLM Agent任务准确率与认知谦逊的负相关关系
practical_value: '- 搭建电商导购/售后Agent时，可引入ISE框架做轨迹质检，检测Agent遇到商品参数、活动规则冲突时是否会主动校验、告知用户不确定性，降低错误推荐导致的客诉

  - 优化Agent工具调用逻辑时，可在Agent识别到知识冲突后强制触发二次检索/跨源校验步骤，解决早期识别冲突但后续无跟进的普遍问题

  - 设计Agent评测体系时，不要仅考核最终回答准确率，可加入Escalate指标作为安全维度加分项，避免Agent为追求准确率盲目输出错误结论

  - 轻量优化Agent认知谦逊能力时，可直接在系统提示词中加入要求报告冲突和不确定性的指令，能大幅提升不确定性上报率，适合容错率低的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent评估仅关注最终任务准确率，完全忽略执行过程中遇到知识冲突（参数记忆与检索结果冲突、多源检索结果冲突）时的不确定性处理能力；在电商、政务等高容错要求场景下，Agent盲目输出错误结论的危害远大于主动承认不确定，因此需要系统评估认知谦逊（EH）能力。

### 方法关键点
- 提出ISE三维可观测行为框架量化认知谦逊：Identify（执行过程中识别知识冲突）、Solve（识别冲突后主动调用工具尝试解决）、Escalate（冲突无法解决时最终回应用户告知不确定性）
- 设计两类知识冲突评测场景：① 可控冲突：预设参数记忆与给定上下文冲突的QA任务，配对无冲突对照组；② 自然发生冲突：多步工具调用任务中自然出现的结果/记忆冲突，配对对照组
- 采用轨迹级评估而非仅看最终答案，用GPT-5作为裁判分别对三个维度打分，人类标注与裁判一致性达76%~85%

### 关键结果
在4类Agent框架、5个骨干模型上评测，核心发现：
1. 高准确率与认知谦逊负相关：高准确率配置下Escalate率不足10%，低准确率配置下可达38%
2. 90%以上的冲突相关信息提及发生在执行前10%的步骤，但多数Agent无后续跟进处理
3. 加入认知谦逊要求的系统提示词后，Escalate率最高提升59个百分点，但任务准确率平均下降7个百分点，二者存在明显trade-off

**最值得记住的一句话**：Agent的能力评估不能只看最终答案准确率，相同准确率的Agent在冲突处理、不确定性上报等安全维度的表现可能存在天壤之别
