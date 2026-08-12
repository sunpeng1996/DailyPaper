---
title: 'Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human
  Design'
title_zh: 智能体系统协同进化：突破人工设计局限的自主进化路径
authors:
- Qing Zong
- Jiayu Liu
- Junhao Shen
- Zecong Tang
- Linsi Wu
- Yuxuan Liu
- Rui Wang
- Zhaowei Wang
- Weiqi Wang
- Cheng Qian
affiliations:
- 香港科技大学
- 伊利诺伊大学厄巴纳-香槟分校
- 香港中文大学
- 香港大学
- 北京大学
arxiv_id: '2608.10299'
url: https://arxiv.org/abs/2608.10299
pdf_url: https://arxiv.org/pdf/2608.10299
published: '2026-08-09'
collected: '2026-08-12'
category: Agent
direction: Agent系统 · 协同进化分类体系
tags:
- Agent
- Co-Evolution
- Multi-Agent
- Self-Evolution
- LLM-Agent
- Open-Endedness
one_liner: 首次提出智能体协同进化三阶段分类体系，系统梳理领域进展与落地挑战
practical_value: '- 推荐系统Agent闭环优化可借鉴Agent-Environment协同进化思路，根据模型当前表现动态调整召回/排序任务池，自动生成适配能力边界的难例训练集，减少人工标注成本

  - 多Agent导购/客服系统可复用Agent-Agent协同进化模式：用攻击Agent迭代优化客服Agent的合规拒答能力，用多角色协作的信用分配机制提升团队任务完成效率

  - Agent迭代工程落地可参考三阶段进化边界划分，优先落地固定环境下的智能体间协同进化，再逐步开放环境、进化机制的自适应能力，避免系统不稳定'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单实体自进化Agent受固定任务、反馈等静态上下文约束，容易进入性能瓶颈，当前缺少对多组件协同进化方向的系统性梳理，无法支撑突破人工设计局限的开放进化系统构建。

### 方法关键点
- 提出渐进式三阶段协同进化分类法，按进化自由度从低到高划分：①Agent-Agent协同进化：固定环境下多智能体通过对抗、协作、组织结构动态调整互相施加进化压力；②Agent-Environment协同进化：环境侧的任务、反馈、交互空间随Agent能力动态自适应；③Meta协同进化：进化规则（进化目标、触发时机、更新方式、评估逻辑）本身可自主迭代。
- 明确定义协同进化核心判定标准：至少两个进化单元存在双向进化压力，且互相重塑对方后续进化路径，区别于普通信息交互。

### 关键结果
跨文献汇总验证前两阶段协同进化在绝大多数场景下能稳定提升Agent性能，但随着进化推进收益逐渐收窄，Meta协同进化是突破性能瓶颈的潜在方向；同时梳理了当前领域在动态评估、规模化落地、安全可控三大方向的开放挑战。

### 核心结论
未来智能系统的进步不在于构建更强的静态智能体，而在于设计能通过协同进化持续自主迭代的系统框架。
