---
title: 'From Resource Flow to Executable Tests: Petri-Net-Guided LLM Test Generation
  for Concurrent Stateful Rust APIs'
title_zh: Petri网引导的面向并发有状态Rust API的LLM可执行测试生成方法
authors:
- Kaiwen Zhang
- Guanjun Liu
affiliations:
- Tongji University
arxiv_id: '2607.21530'
url: https://arxiv.org/abs/2607.21530
pdf_url: https://arxiv.org/pdf/2607.21530
published: '2026-07-23'
collected: '2026-07-27'
category: LLM
direction: LLM代码生成 · 形式化约束引导测试生成
tags:
- Petri Net
- LLM
- Test Generation
- Rust
- Concurrent API
one_liner: 基于Petri网建模API语义约束，引导LLM生成覆盖高冲突并发场景的合规Rust可执行测试
practical_value: '- 形式化模型（如Petri网）给LLM生成加硬约束的思路，可复用到Agent工具调用合规校验、推荐生成式文案的业务规则约束，降低幻觉

  - 「形式化模型管语义约束、LLM管具体语法实现」的分工架构，可迁移到带复杂业务规则的LLM生成任务，提升输出合规率

  - 分层判别器区分生成失败和实际业务逻辑违规的思路，可用于生成式推荐/Agent执行结果的错误根因定位'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
LLM直接生成并发有状态API测试时易违反API前置条件、覆盖场景浅、并发场景退化为随机串行路径，传统模型驱动测试则需要大量手写代码将抽象场景转换为可执行用例，两类方法存在明显gap。
### 方法关键点
1. 用有色Petri网建模API资源、生命周期条件、因果依赖，生成合法深状态、近合法、偏序并发场景作为LLM代码生成的约束中间表示
2. 引入局部保真契约和结构修复环路，保证生成过程不偏离建模意图，同时Petri引导的调度塑形优先探索高冲突并发骨架
3. 设计分层语义oracle，区分LLM合成失败和目标API预期行为违规两类错误
### 结果
面向Rust并发库实现原型，经评估可显著提升测试用例可执行率、结构保真度、深状态可达性与并发故障检出率
