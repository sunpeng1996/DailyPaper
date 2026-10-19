---
title: Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents
title_zh: 面向长程智能体的信念更新与世界建模故障恢复框架
authors:
- Xiyang Wu
- Zhichao Liu
- Shengxin zhang
- Zongxia Li
- Ming Li
- Tianyi Zhou
- Dinesh Manocha
affiliations:
- University of Maryland
- Google
- MBZUAI
arxiv_id: '2610.18082'
url: https://arxiv.org/abs/2610.18082
pdf_url: https://arxiv.org/pdf/2610.18082
published: '2026-10-12'
collected: '2026-10-19'
category: Agent
direction: 长程智能体 · 故障恢复与知识蒸馏
tags:
- Long-Horizon Agent
- Failure Recovery
- Belief State
- World Modeling
- Knowledge Distillation
one_liner: 提出BELIEFWEAVER结合持久信念与隐式世界模型，提升长程Agent故障恢复能力并蒸馏降本
practical_value: '- 电商全链路导购、多轮用户运营类长程Agent遇到链路故障时，可复用持久关系信念状态设计：跨回滚保留所有失败尝试的证据，关联更新各修复方向的优先级，避免重复踩相同的坑

  - Agent大模型成本优化可参考蒸馏方案：先通过SFT将教师模型的重复调用逻辑（故障诊断、候选修复方向评估等）迁移到小参数模型，再补充On-Policy Distillation适配真实运行场景的状态分布，相比纯SFT效果更优，可降低50%以上大模型API成本

  - 故障修复优先级逻辑可复用「信念打分+证据门控」两层架构：先基于历史反馈给候选修复方向打分，再加准入规则（必须有证据支持、目标未达成）过滤，大幅提升修复效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程Agent（多步任务执行、自主导购、用户全生命周期运营类Agent）的早期错误会沿轨迹传播，现有局部反思、单分支回滚方案无法解决跨分支的共享错误根源，且失败尝试的经验无法复用，导致反复重试效率低、大模型调用成本高。

### 方法关键点
- 设计持久关系探索图，跨回滚保留所有修复假设、尝试记录、观测结果、检查点，维护每个修复方向的活跃信念值，新证据可关联更新所有相关假设的优先级；
- 引入隐式世界模型（IWM），负责生成可测试的修复假设、诊断验证假设合理性、预估修复进度、关联不同假设的依赖关系，指导探索方向；
- 证据门控执行：只有获得一致证据支持、目标未达成的修复方向才允许执行，否则回退到普通执行逻辑；
- 用SFT+On-Policy Distillation（OPD）把IWM的4类重复调用逻辑蒸馏到9B小模型，降低大模型API成本。

### 关键实验
在3个终端类长程Agent基准（TB2、TB3、LHTB共113个任务）上测试，BELIEFWEAVER教师版比原生Terminus-2基线总分高5.1个百分点；蒸馏后的9B学生版比原生基线高9.8个百分点，同时比匹配教师版降低54.8%的API成本。

**最值得记住的一句话**：长程Agent的故障恢复不能只做单次回滚重试，要把失败尝试转化为可复用的证据，跨分支关联更新修复方向优先级，才能在提效的同时降本。
