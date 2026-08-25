---
title: 'SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository
  Stack Migration?'
title_zh: SWE Refactor Bench：编码Agent长周期全仓库技术栈迁移能力基准评测
authors:
- Deyao Hong
- Yizhe Chi
- Wenyi Li
- Xiaoqiu Wang
- Mingju Gao
- Kaisen Yang
- Bingxiang He
- Youjie Zheng
- Calvin Xiao
- Qinhuai Na
affiliations:
- Navers Lab
- Einsia.AI
- Tsinghua University
arxiv_id: '2608.23564'
url: https://arxiv.org/abs/2608.23564
pdf_url: https://arxiv.org/pdf/2608.23564
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: 编码Agent长周期任务能力评测
tags:
- Coding Agent
- Benchmark
- Long-Horizon Task
- Code Migration
- Agent Evaluation
one_liner: 推出包含20个全仓库迁移任务的SWE Refactor Bench，采用三阶段协议评测编码Agent迁移能力
practical_value: '- 做Agent长任务评测时可复用三阶段评估逻辑：先校验核心目标完成度，再校验行为一致性，最后用多Agent生成针对性用例查漏

  - 业务侧用Agent做代码重构/技术栈迁移时，优先落地构建工具链类迁移，语言类迁移当前成熟度极低不建议强依赖

  - 设计Agent任务规则时需规避作弊漏洞：不能仅校验产出正确性，需额外校验核心执行逻辑是否符合要求，例如推荐场景用Agent生成物料需同时校验合规性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有编码Agent基准仅评测行为正确性，存在Agent跳过核心迁移动作、复制原有实现过测的「Blindness」漏洞，无法验证真实全仓库长周期迁移能力。

### 方法关键点
推出SWE Refactor Bench，包含20个覆盖4类技术债务的全仓库迁移任务，采用三阶段评估协议：1）迁移审计，验证迁移动作真实发生；2）行为测试，用固定测试集校验功能正确性；3）多Agent验证，用6个独立编码Agent生成针对性测试用例排查隐藏行为差异。

### 关键结果数字
8个前沿模型、26种配置的520次运行中仅5.4%通过全三阶段，13/20的任务无有效解，最优模型claude-opus-5得分仅47/100；构建工具链类迁移平均得分31.4，语言类迁移仅5.6；通过迁移审计的运行中仅26%能100%通过固定测试校验。
