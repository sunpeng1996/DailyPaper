---
title: 'Specification-first convergence with an AI coding agent: a case study of dismantling
  a core architectural invariant across 189 files in a 717k-line codebase with no
  test oracle and no human code review'
title_zh: 规范优先AI编码Agent实现无测试预言无人工审核的大规模代码重构
authors:
- Joel Abenhaim
affiliations:
- AI Sovereign Labs, Paris, France
arxiv_id: '2608.12440'
url: https://arxiv.org/abs/2608.12440
pdf_url: https://arxiv.org/pdf/2608.12440
published: '2026-08-11'
collected: '2026-08-14'
category: Agent
direction: AI编码Agent大规模重构作业协议
tags:
- AI Coding Agent
- Specification-first
- Large Scale Refactoring
- Loop Engineering
- Agent Protocol
one_liner: 提出5阶段规范优先AI编码Agent协议，完成无人工审核的高难度大规模架构重构
practical_value: '- 业务Agent落地可复用规范优先双循环架构：先迭代需求规范对齐现有系统再做实现验证，大幅降低人工审核成本，适合推荐系统Agent化重构场景

  - 复杂Agent任务收敛规则可直接复用：连续两轮无偏差即停止迭代，平衡实现效果与推理成本，适配广告/搜索的规则迭代类任务

  - 缺陷前置修正思路可迁移到LLM4Rec需求落地：需求规范阶段提前校验对齐现有逻辑，比功能开发后再改的成本低一个数量级'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI编码Agent落地普遍依赖人工审核代码与预定义测试预言，在跨数百文件的大规模架构重构场景下，人工审核的记忆上限成为性能瓶颈，且新增功能无历史测试用例作为校验基准，常规增量重构或重写成本极高，亟需可落地的无人工干预作业流程。
### 方法关键点
- 采用5阶段拆分的Agent作业协议：ideate明确意图→specify生成正式规范→refine多轮迭代规范对齐现有源码→code原子化实现冻结规范→verify多轮验证代码对齐规范
- 双收敛规则：规范迭代到连续1轮无问题即冻结，代码验证到连续2轮无问题即停止，全程无人工审核代码，仅确认阶段启动
- 各阶段采用独立会话运行，基于ChatGPT 5.6 Sol最大推理模式执行
### 关键结果
测试对象为71.7万行TypeScript生产级代码库，任务为拆解核心架构不变量（关闭面板不终止流式生成），无预定义测试预言。最终3天完成189个文件修改，累计新增34770行、删除16420行代码，提前修复201个缺陷（85个规范问题+116个代码问题），首次手动运行无bug，后续30次使用无故障，总推理成本2430美元。
### 核心洞见
缺陷越早修复成本越低，规范阶段的问题仅需修改文字，实现后再调整则需要改动大量关联代码。
