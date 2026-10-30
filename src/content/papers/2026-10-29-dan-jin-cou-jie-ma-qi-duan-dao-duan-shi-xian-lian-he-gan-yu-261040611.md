---
title: 'When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint
  Generation in One Compact Decoder'
title_zh: 单紧凑解码器端到端实现联合干预门控与Memory-Grounded提示生成
authors:
- A. J. A. Jubayer Talukder
- Mohammad Ariful Haque
affiliations:
- Bangladesh University of Engineering and Technology (BUET)
arxiv_id: '2610.40611'
url: https://arxiv.org/abs/2610.40611
pdf_url: https://arxiv.org/pdf/2610.40611
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: 主动会话Agent · 端到端轻量部署优化
tags:
- Proactive Agent
- Early Exit
- LoRA
- Memory Grounded Generation
- LLM Deployment
one_liner: 用单个1B参数解码器共享权重同时做干预门控与提示生成，比双模型流水线快1.31-1.76倍效果相当
practical_value: '- 做主动干预类Agent（如电商实时客服提示、直播话术推荐）可复用单解码器中间层做门控的架构，相比双模型流水线省900+MB显存，推理提速1.3x以上

  - 记忆模块对生成质量的影响远大于模型规模：移除用户画像记忆会让提示生成Exact Match降24.7个点，同架构1B和8B生成器效果无显著差异，业务侧优先优化记忆库而非盲目堆参数

  - 门控阈值必须随模型迭代单独校准，不同模型达到相同误报率的阈值差可达3倍以上，直接复用旧阈值会导致F1最多降28个点

  - 端到端任务中Exact Match是严格下界，任务专属LLM-as-judge与人类偏好的相关性比Exact Match高20%-77%，业务评估优先选任务适配的LLM
  judge'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有主动会话助手采用「小门控模型+大生成模型」的双阶段流水线，任务割裂导致端到端效果差、部署成本高，业界对门控收益、生成质量的关键影响因子缺乏量化认知。
**方法关键点**：
- 基于单1B参数Llama-3.2解码器+共享LoRA适配器实现端到端训练，同时覆盖干预门控与1-3词短提示生成两个任务
- 门控头挂载在解码器中间层（可选k=6/10），门控判定无需干预则直接终止前向传播，否则继续走完剩余层完成生成，全程仅需1次前向传播
- 生成直接输入全量用户记忆Profile，无额外检索模块
**关键结果**：
在包含28058个决策点的半合成对话数据集上测试：
- 单模型端到端Exact Match达0.2908~0.2929，超过双模型基线的0.2548~0.2619，端到端精度提升3.35~3.74pct
- 推理时延较1B双模型流水线降低31%~43%，较1B门控+8B生成流水线降低60%~71%，显存仅1.05GB，比双模型省900+MB
- 消融实验显示移除用户记忆Profile会让Exact Match下降24.7pct，而同架构1B与8B生成器效果无显著差异，检索模块无额外收益
- 1144条人类评分验证单模型提示有用性与1B双模型流水线持平，略低于8B生成器
**核心结论**：主动干预类任务中记忆模块对效果的影响远大于模型规模，单模型共享权重架构可在保效果的前提下大幅降低部署成本
