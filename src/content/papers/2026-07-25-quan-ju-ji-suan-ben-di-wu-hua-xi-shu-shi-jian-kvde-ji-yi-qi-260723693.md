---
title: 'Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV'
title_zh: 全局计算本地物化：稀疏事件KV的记忆契约
authors:
- Zefeng Cai
- Zerui Cai
affiliations:
- Independent Researchers
arxiv_id: '2607.23693'
url: https://arxiv.org/abs/2607.23693
pdf_url: https://arxiv.org/pdf/2607.23693
published: '2026-07-25'
collected: '2026-08-05'
category: Agent
direction: Agent 长时序KV记忆机制优化
tags:
- KV cache
- Agent Memory
- Long Context
- Sparse Serving
- Semantic Materialization
one_liner: 揭示KV缓存删除源事件后仍保留隐含状态，给出稀疏事件KV作为Agent记忆的可程序化契约
practical_value: '- 做Agent类导购、客服会话时，可主动插入无答案的定向语义锚点事件，提前把用户偏好、会话核心结论写入下游KV，无需显式重复文本，降低上下文长度开销，提升长会话响应速度

  - KV eviction策略设计不能仅基于文本信息评估事件价值，删除源事件后下游KV可能仍保留其状态，评估eviction效果时不能仅靠下游准确率判断源事件是否冗余，避免误删关键依赖

  - 语义物化的触发和基座模型强相关，需针对业务所用基座做定向校准，优先选"follows/mirrors/copies"这类高写入率的句式构造锚点，同时保留显式文本作为降级方案

  - 长用户序列推荐场景可借鉴该机制，将早期用户行为的核心标签（如购买力、品类偏好）写入下游会话KV的锚点，减少召回阶段对超长历史行为的依赖，降低计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长horizon Agent普遍复用KV cache作为记忆载体，现有KV eviction、片段记忆方案均默认保留的KV仅携带可见文本信息，从未验证删除源事件后下游KV是否仍隐含源状态，导致eviction策略可能误删关键依赖，也缺乏可工程落地的KV记忆编程规范。

### 方法关键点
- 设计donor pair对照范式：两条历史仅源事件取值不同，服务时完全删除源事件，仅保留下游无取值表述的根事件（如"M mirrors S"），观测输出是否跟随被删除的源取值
- 覆盖16种不同语义的锚点句式、3款2025-2026年主流开源模型，测试语义物化的触发条件、落地位置、访问边界
- 分别在合成轨迹、真实长对话数据集（REALTALK、LoCoMo）上对比被动收获、主动构造锚点的效果

### 关键结果
- 源事件删除后，Qwen3-8B上99%的敏感输出仍跟随被删源取值，Ministral-3-8B为90:1，Gemma-4-12B为80:0
- 主动插入无答案的计算指令锚点，可将源状态恢复率从6%提升至51%（Qwen3-8B），被动从自然对话中收获的锚点无明显收益
- 仅二进制小状态可高概率恢复（准确率0.934），4/8分类状态恢复率接近随机，3位数字完全无法恢复
- 语义物化触发仅和表层句式相关，语义相同的不同句式写入率差可达40%以上，无通用跨模型有效句式

> 最值得记住的结论：删除源事件后观察到下游准确率无损失，不代表源事件是冗余的，它的状态可能已经被写入下游保留的KV中。
