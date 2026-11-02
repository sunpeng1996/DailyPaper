---
title: 'RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory'
title_zh: RoboArchitect：带持久内存的机器人Agent框架自动化设计
authors:
- Shengguang Wu
- Suning Huang
- Cherie Ho
- Ria Doshi
- Hao Zhu
- Serena Yeung-Levy
affiliations:
- Stanford University
arxiv_id: '2610.42141'
url: https://arxiv.org/abs/2610.42141
pdf_url: https://arxiv.org/pdf/2610.42141
published: '2026-10-29'
collected: '2026-11-02'
category: Agent
direction: Agent架构自动化优化 · 冻结策略适配
tags:
- Agent Harness
- Frozen Policy
- Persistent Memory
- Automated Iteration
- LLM for Robotics
one_liner: 无需更新模型权重，通过大模型自动迭代优化Agent Harness大幅提升冻结策略泛化性能
practical_value: '- 电商/推荐Agent业务可复用「冻结基座+自动迭代harness」范式：无需改动基座LLM/推荐模型权重，仅通过优化调用编排逻辑、工具组合策略适配新场景，大幅降低finetune成本

  - 迭代流程可直接迁移到badcase自动修复：用代码大模型分析业务badcase的trace，自动生成harness修复逻辑（如召回过滤规则、排序兜底逻辑），验证通过后自动上线，减少人工介入

  - 无预定义schema的持久内存机制可直接用到电商导购Agent：让Agent自动记录用户交互中的有效信息（如偏好价格带、禁忌属性），无需人工设计存储字段和读取逻辑，提升上下文感知能力

  - 动态平衡基座输出与程序化控制的逻辑可复用：自动识别基座模型输出无效的场景（如大模型推荐违规商品、生成错误话术），自动切到程序化逻辑兜底，提升系统鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前机器人Agent的harness（包裹冻结策略的控制编排层）依赖人工设计，每切换任务、硬件都要重新开发，成本极高；而通过finetune策略适配新场景需要采集大量标注数据，泛化性差且可解释性低，亟需更高效的策略适配方案。
### 方法关键点
- 全程不更新冻结VLA（视觉-语言-动作）策略的权重，初始harness仅透传策略输出，迭代过程完全基于harness代码修改
- 优化闭环：代码大模型分析每轮harness运行的完整轨迹，诊断失败模式，生成新版本harness代码，仅当训练集性能提升时才保留更新，最多迭代5轮
- 内置无预定义schema的持久内存，由大模型自动决定存储内容、格式和读取逻辑，支持跨Episode积累经验
- 支持自动调用目标检测、分割、姿态生成等辅助工具，可动态平衡策略输出与程序化控制的分工
### 关键实验
覆盖6个机器人操作基准、7种主流VLA策略，对比裸策略、同策略finetune版本：平均unseen场景成功率从9.7%提升到43.3%（4.5倍），unseen任务成功率从12.7%提升到40.2%（3.2倍）；跨基准/域外场景下平均增益达6-7倍，部分场景性能超过同策略finetune的效果。
### 核心结论
不更新模型权重的前提下，Agent编排层的优化存在巨大性能空间，可有效替代finetune适配新场景。
