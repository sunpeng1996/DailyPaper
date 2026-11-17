---
title: Continuation-Guided LLM Evolution of Program Policies and Goal Compilers in
  Craftax
title_zh: Craftax环境下基于延续性引导的LLM程序策略与目标编译器演化框架
authors:
- Víctor Gallego
affiliations:
- Komorebi AI Technologies
arxiv_id: '2611.19537'
url: https://arxiv.org/abs/2611.19537
pdf_url: https://arxiv.org/pdf/2611.19537
published: '2026-11-13'
collected: '2026-11-17'
category: Agent
direction: Agent 代码策略优化与复用
tags:
- CodingAgent
- ProgramPolicy
- ContinuationFeedback
- GoalCompiler
- ZeroShotTransfer
one_liner: 基于延续性反馈级联与策略拆分，将编码Agent生成的游戏策略达标率从<1%提至50%且支持零样本任务迁移
practical_value: '- 长链路转化类任务（如电商多步转化、推荐长周期留存优化）可复用反馈级联思路，放弃单一最终信号或局部单步信号，用「当前状态后的全链路目标达成概率」作为优化反馈，避免局部最优陷阱

  - 业务策略复用时可参考拆分思路：将成熟策略拆分为固定通用执行层（如用户建模、基础召回/排序逻辑）和可编辑规则层，再训练轻量化编译器将上层业务需求直接翻译为规则层代码，无需全链路重训即可适配新任务

  - 代码类Agent/规则引擎的迭代验证可采用配对快照对比法：修改后的候选策略与原策略从相同状态/种子运行，消去环境方差，快速验证局部修改的全链路效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
编码Agent可基于模拟器反馈生成可直接部署的代码策略，推理时无需调用LLM，成本低且可审计，但长周期任务存在两大痛点：局部优化易损害最终目标达成，新任务需重新做全量策略合成，成本极高。
### 方法关键点
- 5级反馈级联优化：从全episode结果、单里程碑通过率、快照分支对比、内部子目标延续性评估到模型信念精度校验，分层递进优化代码策略，规避短视问题
- 策略拆分机制：将单任务成熟策略拆分为固定领域通用执行器I（含环境感知、记忆、基础技能）和可编辑规则程序p0，通过严格动作一致性校验保障拆分后性能无损失
- 可复用目标编译器：仅用短任务训练编码Agent优化编译器Cθ，可将结构化任务直接编译为适配执行器I的新规则程序，推理无需LLM调用也无需任务特定调优
### 关键实验结果
在Craftax游戏2048个随机世界测试集上，仅用全episode反馈的策略最终关卡到达率仅0.29%，引入反馈级联后提升至50.49%，最终BOSS击败率达28.37%；目标编译器在48个未见任务（含长度超训练2倍的长任务）上零样本成功率达71.30%，是仅加约束基线的2倍，效果与单任务单独优化的策略相当。
> 最值得记住：长周期任务中局部子目标完成率不等于对最终目标的贡献，用子目标执行后的后续全链路成功率作为反馈才能避免局部最优，通用能力与任务逻辑拆分可大幅降低新任务适配成本
