---
title: 'LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in
  Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay'
title_zh: 混合大语言模型循环记忆跨模型迁移：无需前缀重放的4B到9B状态切换
authors:
- Simon P. Villani
arxiv_id: '2609.25053'
url: https://arxiv.org/abs/2609.25053
pdf_url: https://arxiv.org/pdf/2609.25053
published: '2026-09-06'
collected: '2026-09-23'
category: LLM
direction: LLM推理优化 · 跨模型记忆迁移
tags:
- KV Cache
- Hybrid LLM
- Cross-Model Memory Transfer
- State Handoff
- Inference Efficiency
one_liner: 首次实现同架构不同大小混合LLM间无需前缀重放的持久循环推理状态跨模型迁移
practical_value: '- Agent/多模型协作场景可复用该思路：用小模型处理长会话上下文，直接迁移状态到更大模型做复杂推理（如电商定制化推荐、复杂咨询解答），省掉大模型的prefill开销，降低延迟

  - 混合LLM部署的流量调度场景：流量高峰切小模型、低谷切大模型时无需重放用户历史会话上下文，用户无感知，大幅降低推理资源浪费

  - 混合模型状态迁移优先复用架构匹配的循环/卷积状态，仅对KV做映射，再加上小于1M参数量的轻量残差校正即可达到接近原生的效果，无需全量微调，落地成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有跨模型KV Cache迁移仅适配全注意力模型，混合LLM（注意力+GDN循环结构）除KV外还包含循环矩阵、卷积历史等持久状态，仅迁移KV效果损失大，且跨模型切换时需要重放历史前缀，长上下文场景下prefill成本极高，亟需实现完整混合状态的跨模型无损迁移。

### 方法关键点
- 测试对象为架构完全匹配的Qwen3.5 4B→9B同系列混合模型，二者GDN层持久状态形状完全对齐，仅隐藏层维度、参数规模不同
- 最优迁移策略：仅对KV做线性 ridge 映射翻译，GDN的循环矩阵、卷积历史直接复用，无需额外学习映射
- 新增434k参数量的轻量残差校正模块，冻结两个大模型，优化目标为对齐迁移后与原生9B的输出分布KL散度

### 关键结果
- 实验1（64篇PG19文档）：仅迁移KV时NLL比原生9B高0.954 nats/token，加入GDN全状态后NLL下降0.747 nats/token，所有文档效果均提升
- 实验2（64篇FineWeb-Edu文档）：加入轻量校正后迁移的9B模型比继续用4B推理NLL低0.052 nats/token，仅比原生9B高0.076 nats/token，原生上下文恢复率（NCR）达0.918

**最值得记住的一句话**：同架构同系列混合LLM的持久循环状态存在天然功能兼容性，直接复用比学习映射效果更优，仅需极小参数量的校正即可实现接近原生的跨模型状态迁移效果
