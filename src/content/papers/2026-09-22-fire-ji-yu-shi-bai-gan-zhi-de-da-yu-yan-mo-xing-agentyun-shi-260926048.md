---
title: 'FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents'
title_zh: FIRE：基于失败感知的大语言模型Agent运行时可靠性优化框架
authors:
- Nikita Agarwal
- Nivedit Jain
affiliations:
- Failproof AI
arxiv_id: '2609.26048'
url: https://arxiv.org/abs/2609.26048
pdf_url: https://arxiv.org/pdf/2609.26048
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 运行时可靠性优化
tags:
- LLM Agent
- Runtime Policy
- Reliability
- Guardrail
- Failure-aware
one_liner: 无需微调模型或修改用户Prompt，仅通过运行时定向干预提升Agent任务执行的重复成功率
practical_value: '- 电商导购/售后Agent可复用该运行时干预逻辑：针对高频失败场景（如优惠券发放、地址修改后忘记校验），先沉淀失败前置状态，再在对应节点触发定向指令/操作拦截，无需微调模型即可降低重复错误率，成本远低于模型升级

  - 推荐系统的Agent化编排链路可参考该方法：针对召回/排序后物料拼接、权益叠加等高频流程类错误，配置轻量触发规则，在Agent输出最终结果前强制校验流程完整性，避免已生成的有效推荐方案因流程疏漏失效

  - 可复用五臂对照实验设计验证干预效果：通过同时测试真实干预、同时机sham干预、通用校验等对照组，可准确区分是干预内容生效还是仅打断流程生效，避免上线无效的通用自检逻辑浪费算力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent常出现「已生成有效解决方案但最终交付失败」的流程类错误，传统通用自校验、简单guardrail方法无法区分是干预内容生效还是仅打断流程的安慰剂效应，且微调模型/升级模型tier成本过高，无法低成本解决可复现的流程类失败。

### 方法关键点
- 从历史失败轨迹中提取运行时策略，每个策略由任务eligibility谓词（匹配任务描述）、运行时状态谓词（匹配失败前置状态）、干预动作（插入定向指令/拦截危险操作）、释放条件组成，不修改模型权重和用户Prompt
- 设计五臂随机对照实验分离干预效果：真实策略组、同触发时机的通用提示sham组、全量通用校验组、全量重思考组、基线组，准确验证干预内容的真实收益
- 提出pass∧2指标（两次尝试均成功的占比）衡量Agent任务执行的重复可靠性，区分「能做到」和「能稳定做到」的差距

### 关键实验
在Terminal-Bench 2.1的87个终端任务上测试3个GPT-5.6 tier模型（Luna/Terra/Sol）：
- 全量任务上，三个模型的pass∧2分别提升3.4、5.7、9.2个百分点，其中高端模型Sol的pass@2仅提升1.2个百分点，证明优化主要是将间歇性成功转化为稳定成功
- Terra模型在14个策略覆盖的任务上，成功率从35.7%提升至71.4%，超过无干预的Sol模型（64.3%），成本仅为后者的一半
- 五臂对照实验中，真实策略组在符合条件的任务上成功率达61%，显著高于基线组（39%）、sham组（36%）、通用校验/重思考组（39%-43%）

### 核心结论
模型升级解决的是「能不能做到」的能力边界问题，而针对性的运行时干预解决的是「能不能稳定交付」的流程可靠性问题，在可复现的失败场景下，后者的投入产出比远高于前者
