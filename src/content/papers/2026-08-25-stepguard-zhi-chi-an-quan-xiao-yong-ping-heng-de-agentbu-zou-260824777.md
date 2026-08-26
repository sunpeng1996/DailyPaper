---
title: 'StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility
  Balancing'
title_zh: StepGuard：支持安全-效用平衡的Agent步骤级安全护栏框架
authors:
- Zhijie Zheng
- Yu Li
- Chen Qian
- Yuqian Fu
- Yanwei Fu
- Lu Sheng
- Jing Shao
- Dongrui Liu
affiliations:
- 上海人工智能实验室
- 北京航空航天大学
- 复旦大学
- 中国人民大学
- KAUST
arxiv_id: '2608.24777'
url: https://arxiv.org/abs/2608.24777
pdf_url: https://arxiv.org/pdf/2608.24777
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent安全 · 步骤级工具调用防护
tags:
- Agent Safety
- Guardrail
- Synthetic Data
- GRPO
- Safety Alignment
one_liner: 通过StepGen自动数据引擎和Balance-GRPO实现Agent步骤级安全与效用平衡
practical_value: '- 电商导购/营销类Agent的工具调用安全校验可直接复用StepGuard的前置拦截架构，在调用敏感工具（支付、用户信息查询、批量消息推送）前插入安全判断，降低过拦截对用户体验的影响

  - 训练类不平衡的二分类安全校验模型时，可借鉴Balance-GRPO的动态权重调整策略：根据当前批次正负样本的准确率gap动态加权优势值，无需手动调整样本权重即可缓解过防御/欠防御问题

  - 缺乏正负匹配的安全训练数据时，可复用StepGen的前缀对齐生成思路：固定上下文前缀生成同场景下的安全/不安全对比样本，同时补充同类工具的良性使用样本，避免模型把工具本身作为风险信号

  - 部署Agent护栏时可参考其性能表现：4B参数单调用延迟仅600ms，仅占任务总耗时7%，对业务链路延迟影响可控，小参数模型也能达到接近GPT-5.4的安全判断准确率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
基于LLM的Agent可调用外部工具完成复杂任务，但现有护栏多针对完整执行轨迹做事后审计，缺乏执行前的步骤级动作校验，且普遍存在防御偏差：要么过拦截大量正常动作牺牲任务效用，要么漏拦截高危动作牺牲安全；同时步骤级安全标注数据稀缺，人工标注成本高，无法覆盖多样工具、场景和风险类型。
### 方法关键点
- 数据层：推出StepGen自动数据引擎，先构造带指定风险锚点的不安全轨迹，再固定风险点前的上下文前缀，生成两个前缀对齐的安全分支（直接拒绝风险动作/识别风险后改用安全动作完成任务），同时补充同类工具的良性使用样本，避免模型将工具本身作为风险判断信号，自动生成高对比度的步骤级标注训练数据
- 训练层：提出Balance-GRPO训练策略，在标准GRPO基础上，根据每轮迭代中安全/不安全样本的实时准确率差，动态重加权优势值，给准确率更低的类别分配更高训练权重，无需修改prompt或原始奖励即可缩小两类样本的准确率差，有效平衡安全与效用
- 推理层：4B参数小模型，同时支持执行前的单步工具调用校验、执行后的完整轨迹审计两种场景
### 关键结果
在5个静态安全基准上，StepGuard是开源护栏模型中平均准确率最高的，性能接近GPT-5.4；部署为runtime护栏时，相对无防护设置在AgentDojo和AgentDyn上平均攻击成功率降低77.3%，平均效用仅下降2.8个百分点；Balance-GRPO相比普通GRPO将安全/不安全样本的准确率差从13.0降到8.0，效用最高提升6.7个百分点，ASR仅上升0.3个百分点。

最值得记住的结论：Agent安全护栏的核心价值不是追求零风险，而是在可接受的安全损失下尽可能降低对正常业务效用的影响，动态平衡的训练策略远比单纯增加训练数据更能解决过防御/欠防御问题。
