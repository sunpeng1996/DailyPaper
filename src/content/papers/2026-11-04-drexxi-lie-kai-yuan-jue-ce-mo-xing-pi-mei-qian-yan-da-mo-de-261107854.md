---
title: 'Towards Foundation Decision Models: Drex'
title_zh: Drex系列开源决策模型：媲美前沿大模型的低延迟通用决策方案
authors:
- Nischay Dhankhar
- Alisher Amantay
- Zhanibek Datbayev
- Darkhan Akhmetov
- Yash Shah
- Nurmukhamed Ubaidullayev
- Raman Saparkhan
- Dos Baha
- Abulhair Saparov
affiliations:
- Nace.AI Research Team
arxiv_id: '2611.07854'
url: https://arxiv.org/abs/2611.07854
pdf_url: https://arxiv.org/pdf/2611.07854
published: '2026-11-04'
collected: '2026-11-06'
category: LLM
direction: LLM推理优化 · 通用决策模型
tags:
- Decision Model
- Low Latency
- Open Source
- Multimodal
- RLAF
one_liner: 开源4款不同规模决策模型，性能媲美前沿LLM，推理延迟低10倍以上
practical_value: '- 推荐/广告排序、候选打分场景可直接替换现有 autoregressive LLM 链路：Drex 无需多 token 生成，单
  forward pass 即可输出所有候选的概率分布，推理延迟降低1个数量级，尤其适配候选集动态变化的业务场景

  - Agent 路由、工具选择、意图判断场景可复用其架构设计：无需预定义固定分类头，运行时动态传入候选选项即可，配合选项重排一致性正则训练，可大幅降低候选顺序带来的结果抖动

  - 训练 pipeline 可迁移到业务分类/打分模型：在 SFT 阶段加入选项/状态打乱的一致性损失，后续用 RLAF 校准，可在少标注数据下提升模型泛化性和概率校准度，减少过拟合'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于 autoregressive LLM 的决策类任务（分类、打分、多选等）存在输出不稳定、需要后处理解析、推理延迟和成本高的问题；传统判别式模型依赖固定分类头，无法适配动态候选集的业务场景，亟需兼顾通用性、低延迟、高准确率的通用决策方案。
### 方法关键点
- 共发布4款不同参数规模的决策模型：8B DLM、9B v1.5、35B MoE（3B激活）v2.0、27B 多模态 Max，均无需 autoregressive 解码，直接输出用户给定候选集的概率分布
- 两类架构设计：指针架构（v1.5/v2.0/DLM）上下文编码一次后 KV cache 复用，可低成本支持同一上下文下的多问题查询；Max 采用部分层双向注意力+无偏线性读出头，精度更高，支持多模态输入
- 三阶段训练 pipeline：SFT 阶段加入选项重排、状态打乱的一致性正则，降低结果波动；RLAF（带KL约束的调整反馈强化学习）阶段校准概率分布，提升校准度；Max 额外增加视觉 SFT 阶段支持多模态决策
### 关键结果
- Decision Index 0.4.1 公开榜单上，Drex Max 得分67.52，比此前SOTA Jev 1.14.0高6.8分，仅落后 Claude Opus 5.5 1.6分；平均推理延迟183ms，仅为 GPT-6 Sol 的1/11、Claude Opus 5.5的1/19
- 消融实验显示：RLAF 可提升 Decision Index 得分2.0分，一致性正则可将选项重排的 top1 结果翻转率从6.3%降至4.2%
### 核心结论
结构化决策任务上，专用决策模型可以用不到1/10的成本达到前沿通用LLM的同等精度，是生产落地的最优选择
