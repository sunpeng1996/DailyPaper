---
title: 'Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States'
title_zh: 超越记忆：基于显式信念状态的长周期Agent优化框架
authors:
- Yu Luo
- Jiamin Jiang
- Yimin Zuo
- Xidao Wen
- Rongchen Gao
- Yongqian Sun
- Shenglin Zhang
- Guiyang Liu
- Cheng Zhang
- Fang Situ
affiliations:
- Nankai University
- Alibaba Group
- Tsinghua University
arxiv_id: '2610.01415'
url: https://arxiv.org/abs/2610.01415
pdf_url: https://arxiv.org/pdf/2610.01415
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: 长周期Agent · 显式信念状态管理
tags:
- LLM-Agent
- Long-Horizon
- Belief-State
- Trapping-Recovery
- Context-Management
one_liner: 提出PoS推理框架，通过显式信念维护、一致性校验与陷阱恢复提升长周期Agent表现
practical_value: '- 电商导购/售后长会话Agent可复用PoS的信念建模逻辑，将用户状态、待解决需求拆解为实体-状态-关系结构+认知/达成缺口，避免会话偏离用户核心诉求

  - 长链路Agent任务（如多轮用户诉求处理、营销活动全链路调度）可复用Belief Trapping检测逻辑，通过缺口持久性、进度停滞、信念复发三个指标快速识别无效循环，及时调整策略

  - Agent成本优化可参考PoS的权衡思路：虽然信念维护会增加额外token开销，但能显著降低主Agent的无效交互token消耗，整体提升任务ROI'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期LLM Agent依赖历史记忆存储或压缩，无法保证对当前环境的连贯认知，容易出现信念冲突、无意义循环等Belief Trapping问题，上下文长度增长时性能下降尤为明显。

### 方法关键点
- 提出Progression of States（PoS）推理框架，显式维护结构化信念状态：包含任务相关实体-状态-关系的世界状态、任务目标、认知缺口（待明确信息）、达成缺口（待完成任务）
- 每步信念更新后通过Belief Sentinel做一致性校验，过滤内部冲突或与观测证据矛盾的错误信念
- 设计Belief Trapping检测机制，基于缺口持久性、进度停滞度、信念复发率计算信念健康分，识别无进展状态后按静态/循环/漂移三类动态模式+认知/达成缺口类型做因子化诊断，生成对应恢复约束引导后续动作

### 关键实验
在4个长周期基准（ALFWorld、LOCA-Bench执行类，RCA-100、ClinDiag诊断类）上用3个LLM backbone测试，对比6个主流基线，PoS在所有场景下均取得最优表现，相对最强基线最高提升22.68%（ALFWorld）、37.89%（RCA-100联合准确率），256K长上下文场景下领先基线10.67~16个百分点。

> 最值得记住的一句话：长周期Agent的核心瓶颈不是上下文记忆容量，而是对当前世界状态与待完成任务的清晰、一致、可校验的显式认知
