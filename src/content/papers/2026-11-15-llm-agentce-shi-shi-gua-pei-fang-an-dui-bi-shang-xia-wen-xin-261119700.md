---
title: Where Should LLM Agents Adapt at Test Time? In Context, in Weights, or Both
title_zh: LLM Agent测试时适配方案对比：上下文、权重更新及两者结合
authors:
- Parsa Mirtaheri
- Mohammadreza Armandpour
- Keivan Alizadeh
- Iman Mirzadeh
- Parshin Shojaee
- Aryo Lotfi
- David Harrison
- Mehrdad Farajtabar
affiliations:
- UC San Diego
- Apple
arxiv_id: '2611.19700'
url: https://arxiv.org/abs/2611.19700
pdf_url: https://arxiv.org/pdf/2611.19700
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: Agent测试时自适应优化
tags:
- LLM Agent
- Test-time Adaptation
- ICL
- GRPO
- LoRA
one_liner: 系统对比LLM Agent三类测试时适配方案，验证上下文学习结合GRPO收益最高
practical_value: '- 做固定环境长期运行的垂直Agent（如电商客服、商家运营助手）优先落地ICL，原始轨迹回放即可拿到最大的 standalone
  收益，比单独做权重更新ROI更高

  - 解决ICL容易跳过任务校验的问题，可叠加GRPO做LoRA微调，既能保留ICL的环境知识复用（减少冗余查询/操作），又能恢复任务专属的校验逻辑，进一步提效

  - 业务场景做测试时自适应优先选GRPO而非SDPO，SDPO效果不稳定，很可能反向降低效果

  - 上下文管理优先选Prefix+仅留存成功轨迹的策略，比FIFO效果更好，能提供更稳定的适配基础'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长期运行在固定环境的LLM Agent（如代码库助手、数据库查询助手、电商运营工具）处理的任务共享底层环境结构，测试时可通过上下文留存或权重更新适配，但两类适配通道的单独贡献、是否互补长期缺乏统一框架下的量化对比，无法指导业务方案选型。

### 方法关键点
- 统一在线评估协议：任务按流输入，每个任务先评估再适配，Agent仅从自身交互结果和环境反馈学习，不引入外部标注或示范
- 覆盖三类适配机制：①ICL（4种策略组合：FIFO/Prefix留存 + 全量/仅成功尝试准入）②权重更新（GRPO/SDPO，均基于LoRA实现轻量更新）③两者混合方案
- 行为分析维度：从操作长度、环境查询次数、任务校验行为占比三个维度，拆解不同适配方案的行为差异定位收益来源

### 关键实验结果
基于Qwen3.5-9B在4个环境共109个任务、5种任务顺序下测试：
- 无适配基线成功率28.8%，单独最优ICL策略（Prefix+仅成功尝试准入）成功率达49.4%，单独GRPO达37.0%，单独SDPO反而降至27.1%
- 最优组合为ICL+GRPO，成功率达51.6%，在所有ICL策略下叠加GRPO均可稳定提效
- ICL可减少30%以上的冗余环境查询，但会降低40%左右的任务校验行为，叠加GRPO可恢复校验行为同时保留低查询量

**最值得记住的一句话**：LLM Agent测试时适配优先落地ICL拿基础收益，再叠加GRPO解决ICL的校验缺失问题，不要单独用SDPO做测试时更新
