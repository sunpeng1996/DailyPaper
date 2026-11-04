---
title: 'Meta$^2$: Precomputing Reusable Knowledge for Online Harness Evolution in
  Long-Horizon Agents'
title_zh: Meta²：为长周期Agent在线Harness演化预计算可复用知识
authors:
- Lingzhi Yuan
- Yiguang Cai
- Weize Liu
- Siqi Yang
- Feijiang Han
- Yongkyun Lee
- Udari Madhushani Sehwag
- Furong Huang
affiliations:
- University of Maryland
- University of Washington
- University of Illinois at Urbana-Champaign
- Scale AI
- All Purpose AI
arxiv_id: '2611.05139'
url: https://arxiv.org/abs/2611.05139
pdf_url: https://arxiv.org/pdf/2611.05139
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: 长周期Agent · Harness在线演化
tags:
- Long-Horizon Agent
- Harness Evolution
- Contrastive Learning
- Meta Skill
- Online Adaptation
one_liner: 通过离线对比学习预计算可复用元技能，指导长周期Agent运行中本地优化Harness无需测试时验证反馈
practical_value: '- 电商导购/客服长交互Agent可复用「离线预计算通用演化规则+在线仅做任务本地编辑」架构，既避免跨任务干预污染，又降低在线决策时延

  - 推荐策略迭代可迁移三类对照范式：采集无干预/当前策略干预/最优干预三类轨迹，对比产出可复用干预规则，比仅用成功轨迹训练更覆盖难例

  - 线上大流量Agent服务可参考checkpoint间隔调优方案：选择适中的干预间隔（如实验中L=5）平衡性能与算力成本，实现降本提效'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长周期Agent依赖Harness（包含prompt、工具、记忆、钩子的执行框架）保障执行效果，现有优化方案存在明显缺陷：离线优化出的通用Harness容易过拟合训练任务，无法响应运行时暴露的新问题；在线演化方案要么干预时机滞后无法挽救当前执行，要么需要测试阶段不可用的验证器反馈，每次从零决策也会大幅提升在线时延与成本。
### 方法关键点
- 架构分层设计：离线阶段仅学习可复用的Meta-Skill，不输出固定通用Harness；在线阶段Meta-Skill全局冻结，仅基于当前任务运行轨迹做Harness本地编辑，编辑结果不跨任务传递避免污染
- 离线对比训练：对每个训练任务执行三类rollout：A（无演化器）、B（当前Meta-Skill指导的演化器）、C（仅训练时可用的带特权验证信息的演化器），对比5类轨迹结果提炼act/hold/avoid三类通用干预规则
- 在线低 overhead 演化：每固定L步做一次checkpoint，演化器结合Meta-Skill与当前轨迹决定保留Harness或做局部修改，修改仅作用于当前任务剩余执行流程
### 关键结果
在Terminal-Bench 2.1、DeepSWE 1.1两个长周期Agent基准测试，对比10个不同类别的基线方法，使用GPT-5.6-Terra时准确率分别达81.00%、44.44%，比最强Harness演化基线Meta-Harness分别高7.67、7.11个百分点；使用DeepSeek-V4-Flash时在Terminal-Bench也达到77.67%的准确率，领先所有基线。
### 核心结论
预计算「如何自适应」的规则，再随着任务推进做本地自适应，比预计算一个通用的固定执行框架效果更好
