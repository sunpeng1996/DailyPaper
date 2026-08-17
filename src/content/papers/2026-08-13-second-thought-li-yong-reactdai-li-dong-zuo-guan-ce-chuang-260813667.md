---
title: 'Second Thought: Reasoning in Parallel as LLM Agents Act and Observe'
title_zh: Second Thought：利用ReAct代理动作观测窗口的并行推理框架
authors:
- Zhensu Sun
- Chengran Yang
- Yunbo Lyu
- Jieke Shi
- David Lo
affiliations:
- Singapore Management University
arxiv_id: '2608.13667'
url: https://arxiv.org/abs/2608.13667
pdf_url: https://arxiv.org/pdf/2608.13667
published: '2026-08-13'
collected: '2026-08-17'
category: Agent
direction: Agent 并行推理效率优化
tags:
- LLM Agent
- Parallel Reasoning
- ReAct
- Inference Optimization
- KV Cache
one_liner: 无训练推理框架利用ReAct代理动作-观测空闲窗口并行生成辅助推理，优化延迟-精度权衡
practical_value: '- 可直接复用框架到电商导购Agent、客服Agent的ReAct链路：在工具调用/请求商品/物流/库存数据的空闲窗口并行跑辅助分支，既不增加主链路延迟，还能减少错误重试、降低交互轮次

  - 工程实现可复用2个核心trick：辅助分支共享主链路prompt前缀KV cache降低算力开销，用XML标签包裹原子化thought，即使被中断也能提取有效内容，无需复杂分支合并逻辑

  - 成本敏感场景可灵活裁剪分支：比如电商客服场景仅保留Recall（召回用户历史约束、平台规则）和Rehearse（预演用户常见疑问应答）分支，可将额外API成本控制在20%以内，ROI更高

  - 可复用结论：工具调用/外部观测延迟越高的Agent场景（比如调用推荐系统接口、跨系统查询数据），Second Thought的收益越大，空闲窗口越长可生成的有效辅助推理越多'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
ReAct范式的LLM Agent仅在Thought阶段生成推理，动作执行、等待环境观测的窗口无任何推理计算，属于算力浪费；现有并行推理方案均在Thought阶段内做多路径采样，需要复杂投票合并逻辑，还会增加主链路延迟，无法利用这段空闲窗口。

### 方法关键点
- 无训练推理框架：Thought阶段结束立刻fork4个辅助分支，与主链路的动作执行、观测等待并行解码，观测返回后立即截断分支，将有效thought拼入上下文供下一轮推理使用
- 4个互补分支设计：Check（校验当前计划的隐含假设）、Recall（召回历史关键约束避免遗忘）、Rehearse（预演下一步可能的应对方案）、Alternative（生成备选策略避免路径依赖）
- 原子thought设计：每个推理单元用<thought>标签包裹，单条不超过25词、无前后依赖，中断后仅丢失当前生成中的单元，无需优雅退出逻辑
- 共享主链路的前缀KV cache，大幅降低额外推理的算力开销

### 关键实验
在3个Agent基准（SWE-Bench Pro、Terminal-Bench 2.1、τ3-bench）、3款主流推理LLM上测试：9组模型-基准对全部降低平均轮次，6组主链路解码量最高降43%、平均降约20%；7组Pass@1无显著下降，2组分别提升12.4、10.2个百分点；受控重放测试下单任务中位延迟降10.9%；和算力匹配的主链路延长推理基线相比，所有适用场景下Pass@1更高，主链路顺序解码量减少1.3~3.2倍。

### 最值得记住的一句话
Agent的动作-观测空闲窗口是近乎免费的并行推理算力，只要设计合理的中断兼容辅助推理逻辑，就能在不增加主链路延迟的前提下提升效果。
