---
title: 'Safin-1: Safety from Within through Memory-Native State Evolution'
title_zh: Safin-1：基于原生记忆状态演化的内生安全大模型
authors:
- Ming Zhang
- Kaisen Yang
- Shu Yu
- Ermo Hua
- Zhekai Chen
- Cheng Jin
- Jingnan Zheng
- Yi Zhang
- Zhongtian Ma
- Jiawei Zhou
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2609.00092'
url: https://arxiv.org/abs/2609.00092
pdf_url: https://arxiv.org/pdf/2609.00092
published: '2026-08-30'
collected: '2026-09-02'
category: LLM
direction: 大模型内生安全 · 记忆路由架构
tags:
- LLM Safety
- Memory Routing
- Test-time Adaptation
- State Evolution
- Parameter Efficient Tuning
one_liner: 提出基于MARCH记忆路由的Safin-1大模型，通过可插拔安全状态实现更优的安全-效用tradeoff
practical_value: '- 可借鉴可插拔持久化状态的设计思路，冻结推荐系统LLM backbone的前提下，注入业务专属状态（如合规风控、品类偏好约束）实现快速适配，避免全量微调的资源消耗和能力退化

  - MARCH的Top-K稀疏路由机制可直接复用在长会话用户行为记忆检索场景，用压缩状态锚替代全量KV cache，降低长上下文推荐/客服Agent的推理延迟和显存开销

  - 安全对齐的训练构造可迁移到推荐内容合规场景，构造不同上下文长度的正负样本混合训练，在降低违规内容生成率的同时减少对正常推荐请求的过度拦截

  - 针对长序列任务，可参考移除RoPE的优化思路，在依赖长程记忆检索的推荐Agent场景下提升长度外推能力，适配超长用户行为序列建模需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型安全对齐多依赖外部防护、后处理或全量/参数微调，易出现过拒绝、通用能力退化问题；同时长序列任务下KV cache开销大，单循环状态存在记忆遗忘瓶颈，亟需将专项能力内化为模型原生可调用属性，同时提升长上下文处理效率。

### 方法关键点
- 核心架构为MARCH（Memory-Anchor Routing across Context History），周期性将循环状态快照为可寻址的状态锚，通过内容条件路由选择历史状态或空选项，与当前状态残差融合，不改变原有循环更新逻辑
- 扩展路由状态库支持可学习的持久化能力状态，实例化为Safety State，训练时冻结大模型backbone，仅优化安全状态参数，可按需插拔
- 实现Producer-Reader高效架构，默认Top-4稀疏路由，128K序列下吞吐量是稠密路由的2倍以上，核心runtime降低一个数量级

### 关键结果
- 0.8B小模型验证：NIAH任务比基线提升47%，LongBench得分提升25%，长上下文检索能力平均提升14%
- 4B/35B规模SFT后：平均越狱攻击成功率（ASR）比Qwen3.5基线降低0.6~1pct，AIME 2025推理得分提升8~8.2pct
- 加载Safety State后：4B模型ASR降低42.3%，35B模型降低52.3%，过拒绝率仅提升0.4~2pct，远低于同训练条件下LoRA的5~10pct，能力保留率优于LoRA

最值得记住的结论：将可插拔的持久化能力状态与原生记忆路由结合，是实现低overhead、低退化的大模型专项能力适配的可行路径
