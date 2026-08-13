---
title: 'OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution'
title_zh: OpenART：通过开放环境演化规模化实现Agent红队测试
authors:
- Yunhao Chen
- Xin Wang
- Yixu Wang
- Yi Liu
- Jie Li
- Yan Teng
- Xingjun Ma
- Xia Hu
- Yu-Gang Jiang
affiliations:
- Fudan University
- Shanghai Artificial Intelligence Laboratory
- XSafeAI
arxiv_id: '2608.00677'
url: https://arxiv.org/abs/2608.00677
pdf_url: https://arxiv.org/pdf/2608.00677
published: '2026-07-31'
collected: '2026-08-13'
category: Agent
direction: Agent安全测试 · 开放环境演化
tags:
- Agent Safety
- Red Teaming
- Environment Evolution
- Benchmark
- Black-box Attack
one_liner: 提出支持环境演化的Agent安全测试框架OpenART，覆盖50领域1万+有状态交互场景
practical_value: '- 电商/广告Agent安全测试可复用「统一场景定义+轻量适配器」架构，无需为不同Agent runtime单独构造测试用例，大幅降低跨架构评估成本

  - 长链路业务Agent（如全链路导购、客服Agent）可采用EMHA黑盒反馈驱动的环境演化方法，无需调整模型参数即可挖掘静态测试漏检的长周期隐式风险

  - 复杂多工具Agent的风险挖掘可借鉴超图协调状态变更的思路，组合多个单点环境修改，定位工具/权限/记忆组合带来的复合安全漏洞

  - Agent上线前的安全验收可参考Strict ASR双校验逻辑，结合规则判定+LLM审核降低安全漏判率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent安全基准多聚焦短周期静态任务，无法覆盖动态演化环境下的累积风险；且不同Agent runtime的接口不统一，难以跨架构横向对比安全性能，长链路交互中延迟触发的隐式攻击难以被静态测试检出。

### 方法关键点
- 场景层：基于50万+Tools、MCP、Skills生成1万+经过验证的有状态场景，覆盖50个领域，单任务中位数需要97次工具调用，远高于现有基准的1-15次
- 适配层：设计目标无关的场景表示，通过轻量运行时适配器，将相同场景投射到15个已部署Agent、5个基座模型的75种组合上，支持8种攻击向量的统一评估
- 攻击层：提出黑盒攻击策略EMHA，无需参数更新，通过超图遍历协调合法状态变更，基于评估反馈迭代演化环境状态，全程保持任务目标和安全规则不变

### 关键结果
在75种Agent-模型组合上，EMHA的平均Strict ASR达85.0%；在最复杂场景下，比仅修改指令的演化方法ASR高17.2-17.6%；Agent运行时实现对ASR的解释度比仅考虑基座模型时额外提升7.6%。

### 核心结论
Agent安全不是单次交互的属性，而是长周期交互中Agent与演化环境共同作用的结果，短静态测试会系统性低估Agent风险。
