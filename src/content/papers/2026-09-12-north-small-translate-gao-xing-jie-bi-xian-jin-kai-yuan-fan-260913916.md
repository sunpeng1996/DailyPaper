---
title: 'North Small Translate: Advanced Cost-Effective Translation (Cohere CAT+)'
title_zh: North Small Translate：高性价比先进开源翻译模型（Cohere CAT+）
authors:
- Tom Kocmi
- Alexandre Bérard
- Phil Blunsom
- Samuel Cahyawijaya
- Shaun Cassini
- Nicholas Frosst
- Ona de Gibert
- Aidan Gomez
- Nithya Govindarajan
- Shun Kiyono
affiliations:
- Cohere
arxiv_id: '2609.13916'
url: https://arxiv.org/abs/2609.13916
pdf_url: https://arxiv.org/pdf/2609.13916
published: '2026-09-12'
collected: '2026-09-15'
category: LLM
direction: 多语言大模型 · 机器翻译优化
tags:
- MoE
- MachineTranslation
- DPO
- ReinforcementLearning
- MultilingualLLM
one_liner: 基于MoE架构的高性价比翻译模型，5步训练加难度采样，50语种性能登顶1T参数以下梯队
practical_value: '- 跨语种电商/广告文案翻译场景，可复用难度采样+Post-Edit偏好蒸馏策略，定向优化业务特有错误（如商品名、专业术语错译）的表现

  - 低时延要求的生成场景可参考「非推理基础模型+可选Agentic流程」的分层架构，常规请求走高吞吐快路径，高优请求走多步自检后编辑路径平衡效果与成本

  - 多任务微调时可复用多样化指令生成策略，避免静态prompt过拟合，同时提升模型对自定义规则（如术语约束、格式要求）的遵从度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM驱动的机器翻译普遍依赖推理步骤，生产部署时延高、吞吐低；同时训练数据中易翻译样本占比超过90%，学习信号弱，小语种、结构化格式（JSON/HTML）翻译、术语约束等细分场景性能差，亟需兼顾成本与效果的生产级翻译方案。

### 方法关键点
1. 架构：基于218B总参数、25B激活参数的MoE底座Command A+，训练为非推理模型优先保障吞吐，额外提供Agentic翻译流程（生成初版→错误检测→后编辑迭代）覆盖高优场景
2. 训练流程：采用5步递进训练，依次为粗粒度SFT（扩展语种覆盖到50种）、细粒度SFT（优化核心翻译及周边任务）、DPO对齐、LLM-as-Judge驱动的在线RL、小学习率轻量DPO修复RL引入的小语种性能退化
3. 数据策略：通过难度采样过滤90%以上易翻译样本，仅保留模型出错的难例构建训练集；通过Post-Edit驱动的偏好蒸馏生成贴近模型真实错误的DPO正负样本，大幅提升训练效率

### 关键结果
在WMT26测试集上，模型50语种综合得分83.6，超过Mistral Large 3、Qwen 3.5等所有1T参数以下开源模型，Agentic版本得分进一步提升至84.4；术语翻译准确率48.9、结构化翻译得分93.7，均大幅领先多数竞品。

### 核心结论
对于生产级生成任务，优先保障基础模型吞吐，再通过可选Agentic流程覆盖高要求场景，配合定向难例采样的训练策略，是平衡成本与效果的核心路径
