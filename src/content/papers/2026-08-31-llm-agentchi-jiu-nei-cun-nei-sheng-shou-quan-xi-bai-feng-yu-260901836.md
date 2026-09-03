---
title: Agent Memory Is a Surface for Endogenous Authorization Laundering
title_zh: LLM Agent持久内存内生授权洗白风险与EAL-BENCH评估基准
authors:
- Tommaso Cerruti
- Mika Okamoto
- Ansel Kaplan Erol
affiliations:
- ETH Zurich
- Georgia Institute of Technology
arxiv_id: '2609.01836'
url: https://arxiv.org/abs/2609.01836
pdf_url: https://arxiv.org/pdf/2609.01836
published: '2026-08-31'
collected: '2026-09-03'
category: Agent
direction: Agent 持久内存授权安全评估
tags:
- Agent
- Memory Security
- Authorization
- Benchmark
- LLM Safety
one_liner: 识别Agent内存内生授权洗白故障，发布EAL-BENCH基准并验证风险与缓解权衡
practical_value: '- 电商客服、运营类Agent禁止用增量更新的自由文本内存存储用户/运营授权（如自动退款、大额下单权限），优先用带来源校验的结构化内存，避免授权被误放大导致资损

  - 涉及资金操作的Agent（如广告投放、供应链采购Agent）可参考两种缓解方案：权限存储强制绑定有效授权源事件、基于事件溯源追踪权限变更，根据业务对资损和效率的容忍度选择平衡点

  - 上线Agent前可复用EAL-BENCH的配对测试框架，针对业务授权规则构造仅单字段差异的合法/非法请求用例，提前验证内存更新对授权状态的保留准确率，降低上线后故障风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期运行的LLM Agent依赖持久内存跨交互保存权限、限制、撤销等状态，现有内存评估仅关注召回、对抗场景或下游任务性能，忽略了动态权限状态的保真度，无外部攻击时内存错误也会导致越权行为，比如曾出现邮件Agent因上下文压缩丢失「操作前确认」要求，误删200多封邮件的事故，这类内生授权洗白问题缺乏专门的量化评估手段。

### 方法关键点
- 提出EAL-BENCH开源基准，覆盖采购、网络安全、金融3个高风险域，每个用例包含动态演化的组织历史、隐藏的确定性权限账本，拆分内存写入器（将历史转为持久内存）和执行器（基于内存响应请求）两个模块，隔离权限错误生成与传播过程
- 对比4种内存配置：自由文本/结构化内存 × 全量一次性更新/增量更新，测试两种缓解方案：存储权限需绑定有效源事件、基于有界事件溯源追踪权限变更
- 设计配对测试用例，仅修改一个权限相关字段区分合法/非法请求，通过精确替换内存的干预方式定位故障根因

### 关键结果
测试5种LLM作为写入器、2种作为执行器，增量更新场景下写入器最多为50.2%的非法请求生成虚假权限，虚假权限存在时执行器98.6%的概率会执行非法操作，替换为正确内存后非法操作降为0；两种缓解方案分别将非法操作率从25.3%降至7.3%和9.0%，但合法请求通过率也从93.3%降至53.8%和64.7%，存在明确的安全-效用权衡。

**最值得记住的一句话**：Agent的持久内存不是单纯的性能组件，而是其有效授权策略的一部分，需要和身份访问管理系统一样做来源、生命周期、审计的严格管控。
