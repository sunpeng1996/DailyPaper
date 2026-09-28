---
title: 'Do Implicit Personalization and Explicit Styles Conflict? PsPLUG: A Lightweight
  Plug-in for Balancing Personalization and Style in Customized LLMs'
title_zh: PsPLUG：平衡个性化LLM隐式偏好与显式风格的轻量插件
authors:
- Yutong Song
- Jiang Wu
- Shaofan Yuan
- Chengze Shen
- Jian Wang
- Yu Wang
- Nikil Dutt
- Amir M. Rahmani
affiliations:
- University of California, Irvine
- TikTok
- Independent Researcher
arxiv_id: '2601.06362'
url: https://arxiv.org/abs/2601.06362
pdf_url: https://arxiv.org/pdf/2601.06362
published: '2026-09-19'
collected: '2026-09-28'
category: LLM
direction: 大模型个性化 · 风格可控生成
tags:
- Personalized-LLM
- Soft-Prompt
- Preference-Optimization
- Controllable-Generation
- PEFT
one_liner: 提出轻量软提示插件PsPLUG，解决显式风格指令下LLM个性化崩塌问题，支持偏好与风格可控平衡
practical_value: '- 复用残差建模思路，将用户偏好建模为基础模型通用输出的分布残差，避免风格/合规指令等全局约束覆盖个性化信号，可直接适配电商个性化客服、商品文案生成场景

  - 推理侧仅通过α系数调节用户嵌入权重即可动态平衡个性化强度与风格合规性，无需重新训练，可快速适配不同业务的管控要求（如客服场景要求语气专业同时贴合用户习惯）

  - 离线预计算用户profile embedding缓存，推理时仅需拼接3个token长度的前缀，开销远低于RAG和单用户LoRA，适合亿级用户规模的推荐/文案生成场景的低延迟部署

  - 构造风格约束下的正负偏好对（用户真实输出vs风格合规的通用输出）做DPO训练的方案，可直接复用在生成式推荐结果排序、个性化用户评论生成等任务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个性化LLM方案在显式风格指令（如正式、简洁、亲切）约束下普遍出现个性化崩塌：强指令会主导生成空间，覆盖用户隐式偏好，导致输出丢失用户专属表达习惯、兴趣特征，无法满足同时要求风格合规与个性化的业务场景需求。
### 方法关键点
- 核心建模思路：将个性化信号定义为用户真实输出分布与基础模型风格约束下通用输出分布的残差，避免两类信号耦合
- 架构设计：轻量软提示插件，仅训练三类参数：全局系统指令嵌入、用户历史embedding投影MLP、当前查询编码MLP，大模型backbone完全冻结
- 训练范式：构造风格约束下的偏好对（正例为用户真实输出，负例为基础模型符合风格要求的通用输出），基于Bradley-Terry pairwise loss优化，隔离用户偏好与风格信号
- 推理控制：引入可调系数α，仅缩放用户专属嵌入权重即可动态调节个性化强度，无需重训或改模型结构
### 关键实验结果
在LaMP基准6类个性化任务上对比RAG、PAG、PPlug、OPPU等SOTA基线：无风格约束时平均效果优于基线2%~5%，其中LaMP-3商品评分任务RMSE低至0.464，相对最优基线降低20.4%；加入4类风格约束后，在80%以上的风格-任务-指标组合中取得最优或次优效果，ROUGE指标相对基线最高提升4个点，同时风格对齐分在所有风格下均为最优；单用户存储开销仅为RAG的1/100、单用户LoRA的1/10，推理延迟与用户历史长度无关，适合大规模部署。
### 核心结论
个性化信号本质是用户行为与通用模型行为的分布残差，仅需极少量参数即可实现不依赖重训的可控个性化效果。
