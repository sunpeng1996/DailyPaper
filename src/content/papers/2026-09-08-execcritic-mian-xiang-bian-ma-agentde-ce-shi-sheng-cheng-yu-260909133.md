---
title: 'ExecCritic: Learn to Test, Test to Improve for Coding Agents'
title_zh: ExecCritic：面向编码Agent的测试生成与修复分离优化框架
authors:
- Leitian Tao
- Baolin Peng
- Haorui Wang
- Hang Wang
- Hao Cheng
- Wenlin Yao
- Qianhui Wu
- Tao Ge
- Sharon Li
- Jianfeng Gao
affiliations:
- University of Wisconsin–Madison
- Microsoft Research
- Georgia Tech
arxiv_id: '2609.09133'
url: https://arxiv.org/abs/2609.09133
pdf_url: https://arxiv.org/pdf/2609.09133
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: 编码Agent · 双角色解耦训练
tags:
- Coding Agent
- Reinforcement Learning
- Multi-Agent
- Test Generation
- Code Repair
one_liner: 提出测试与修复解耦的双编码Agent框架，分角色RL训练提升代码修复准确率
practical_value: '- 多Agent分工解耦思路可迁移到生成式推荐校验场景：将「候选物料生成」和「合规/相关性校验」拆分为独立Agent，校验规则固定后禁止生成Agent修改，避免自验自批的假阳性问题

  - 分角色RL的差异化奖励设计可复用：针对不同任务角色设计对齐业务目标的奖励，比如校验角色奖励区分正负样本的能力，生成角色奖励最终业务效果，比端到端训练更易收敛

  - 低质量反馈反降效果的结论可指导业务迭代：上线Agent闭环前需先验证反馈源质量，低准确率的用户反馈、弱规则校验不要直接接入生成优化链路，否则会拉低整体效果

  - 「SFT初始化+RL微调」范式可复用在垂直Agent训练：先用高质量专家轨迹做SFT让模型掌握基础流程，再用RL优化垂直场景任务效果，比直接RL训练稳定性更高'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有编码Agent的测试生成与代码修复由同一链路完成，存在认知偏差耦合问题：测试和修复会共享同一个错误的需求理解，导致错误代码通过错误测试的假阳性问题；且低质量测试反馈不仅不能提升修复效果，反而会降低任务解决率。

### 方法关键点
- 框架解耦为Test Agent、校验harness、Repair Agent三个模块：Test Agent独立生成符合仓库规范的测试用例，harness校验测试用例在buggy版本上可正常失败后冻结，Repair Agent仅基于固定测试的执行反馈修复代码，无权修改测试用例
- 分角色训练：Test Agent先基于高质量专家轨迹做SFT，再用GRPO做RL训练，奖励核心是测试用例能区分正确/错误修复补丁；Repair Agent同时奖励无反馈下的直接修复能力和基于测试反馈的迭代修复能力
- 推理阶段完全不依赖Oracle测试用例，仅用其做离线训练的奖励信号，符合真实业务无标注部署场景

### 关键实验
在SWE-bench Verified数据集上测试：
- 原生Qwen-3.5-35B生成的低质量测试会将修复准确率从无测试基线的61.2%降到57.3%，而GPT-5.6生成的高质量测试能提升到65.3%
- Test Agent训练后Base-to-Gold成功率从22.2%提升到62.2%，Repair Agent训练后无测试修复准确率从61.2%提升到68.3%
- 训练后的双Agent组合准确率达72.6%，较原生无测试基线提升11.4个百分点

最值得记住的一句话：Agent系统中，独立、固定的校验反馈源质量直接决定了闭环迭代的效果，低质量反馈的危害远大于没有反馈
