---
title: Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses
title_zh: 面向长程任务Agent的递归经验-工作记忆演化框架Recuris
authors:
- Zhaochen Yu
- Yingcheng Wu
- Zhenfei Yin
- Kaiyuan Chen
- Zhe Zhao
- Mengdi Wang
- Shuicheng Yan
- Ling Yang
affiliations:
- NUS
- Stanford University
- University of Oxford
- Princeton University
arxiv_id: '2608.24876'
url: https://arxiv.org/abs/2608.24876
pdf_url: https://arxiv.org/pdf/2608.24876
published: '2026-08-24'
collected: '2026-08-26'
category: Agent
direction: 长程Agent · 记忆架构优化
tags:
- LLM Agent
- Long-Horizon Task
- Memory Architecture
- Recursive Self-Improvement
- Skill Invocation
one_liner: 提出耦合经验与工作记忆的递归演化框架，无需微调LLM即可大幅提升长程任务成功率
practical_value: '- 电商客服/履约类长程Agent可直接复用EM-WM耦合架构，用结构化Working Memory跟踪用户未解决诉求+当前进度，避免长交互中遗漏需求、错用工具，实测可降低长任务失败率最高80%

  - 可复用本文的故障定位+验证门控更新机制，基于结构化执行轨迹定位Agent失败的具体组件（技能库/状态规则/调用策略/校验器），做局部补丁更新而非全量调优，降低迭代成本且避免性能回退

  - 电商跨场景Agent可借鉴验证式状态更新思路，给每个目标设置环境侧可验证的完成谓词（比如订单改地址必须拿到接口返回成功回执才算完成，不能只靠用户口头确认），降低流程类任务的执行错误率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程Agent任务中，交互历史不断膨胀会导致Agent丢失未完成目标、技能调用与当前状态错配，现有经验记忆方法依赖全量历史或初始指令检索，召回准确率随任务长度骤降，且仅靠最终成败信号无法精准定位故障点，难以实现稳定的递归自迭代。

### 方法关键点
- 双记忆耦合架构：用Working Memory（WM）跟踪结构化任务状态（每个目标的内容、进度、验证证据、阻塞原因），Experiential Memory（EM）存储可复用技能，仅基于当前WM状态触发技能调用，脱离全量交互历史
- 证据驱动状态更新：执行工具调用后，通过环境返回的实际结果校验状态变更，而非信任LLM的完成声明，仅提交验证通过的状态更新
- 跨任务递归演化闭环：基于结构化执行轨迹将失败定位到具体记忆组件（EM/WM/调用策略/校验器），仅对故障组件做局部补丁更新，更新需通过验证门控（修复目标失败且不在验证集回退）才会生效，全程不微调底层LLM

### 关键结果
在4个长程基准（含τ2-Retail电商场景、SkillFlow流程类任务）、10款从3B开源到前沿闭源模型上测试，37组模型-基准对中有35组获得提升；τ2-Bench上给GPT-5.6 Sol提+17.8pp、Claude Opus 5提+15.6pp（Opus 5达到87.9%成功率），SkillFlow上给Qwen3.6-27B/35B提+16.6/+13.5pp；任务越长提升越显著，最长任务上提升达+32.2pp，常见长程失败率最高降80%。

**最值得记住的一句话**：长程Agent的性能瓶颈往往不是技能库不足，而是不知道什么时候该调用什么技能，以及怎么验证目标是否真的完成。
