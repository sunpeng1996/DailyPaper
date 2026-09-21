---
title: MLLMs Hallucinate when Information Distribution Drifts in Synergy Heads
title_zh: 多模态大模型协同注意力头信息漂移致幻觉问题与HEAL校正方案
authors:
- Meng&#39;en Qin
- Junye Chen
- Jucheng Liu
- Youlu Xing
- Song Wang
- Ruize Han
affiliations:
- Shenzhen University of Advanced Technology
arxiv_id: '2609.09206'
url: https://arxiv.org/abs/2609.09206
pdf_url: https://arxiv.org/pdf/2609.09206
published: '2026-09-04'
collected: '2026-09-21'
category: Multimodal
direction: 多模态大模型 · 幻觉缓解 注意力头校准
tags:
- MLLM
- Hallucination Mitigation
- Attention Head
- Causal Intervention
- Inference Optimization
one_liner: 通过头级信息解耦与动态校准，在推理阶段降低多模态大模型幻觉，可无改造接入主流MLLM架构
practical_value: '- 电商多模态导购、AI商品图文描述生成场景可直接复用HEAL作为推理层插件，无需重训即可降低商品属性、品牌等幻觉，跨主流MLLM架构适配成本低于10人日

  - 生成式推荐、多模态Agent团队可复用因果噪声干预+反事实双重差分方法，定位Transformer注意力头功能冗余，针对性裁剪/校准头输出，可在不损失效果的前提下降低10%+推理延迟

  - 可借鉴动态校准思路，对生成式推荐的文案生成、Semantic ID生成任务的注意力头做分布对齐，缓解生成内容偏离用户/商品真实属性的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MLLM在电商导购、多模态推荐等场景落地的核心瓶颈是幻觉问题，现有注意力层面的幻觉缓解方法依赖注意力权重等间接信号，无法捕捉幻觉生成背后的真实信息偏移，且单模态增强易陷入“增强视觉导致输出生硬、增强语言导致幻觉加重”的跷跷板困境，亟需可解释、低侵入的缓解方案。
### 方法关键点
- 通过因果噪声干预替换注意力头输出，过滤对结果无贡献的冗余头，降低后续计算量
- 用反事实双重差分方法解耦剩余头的信息分布，将头分为冗余、视觉专属、语言专属、协同四类，发现幻觉仅和协同头内的信息分布偏离均衡相关，和模态专属头的数量/强度无强关联
- 推理阶段给协同头的视觉/语言value向量动态注入校准因子，在KV缓存更新后、注意力计算前执行，不影响FlashAttention/PagedAttention的底层实现，可直接作为插件接入所有主流MLLM
- 工程上采用周期更新头类型（间隔10-15步）、并行干预、批量化差分计算优化，推理 overhead 控制在15%以内
### 关键结果
在LLaVA、Qwen-VL、InternVL等7款主流MLLM上验证，跨POPE、CHAIR等幻觉基准及LLaVA-Bench、MME等通用能力基准：相比SOTA方法，POPE准确率最高提升1.9pp，CHAIR幻觉错误率最高降低28%，通用能力评分最高提升6.5pp，无明显生成长度下降。
### 核心结论
多模态幻觉的核心诱因不是模态专属头的强弱，而是协同头内视觉与语言信息的分布偏离均衡，仅对协同头做校准即可实现幻觉缓解与生成质量的平衡
