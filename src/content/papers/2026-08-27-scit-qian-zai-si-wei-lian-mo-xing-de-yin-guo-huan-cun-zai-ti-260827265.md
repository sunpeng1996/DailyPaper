---
title: 'SCIT: Testing Causal Cache Carriers in Latent Chain-of-Thought Models'
title_zh: SCIT：潜在思维链模型的因果缓存载体检测方法
authors:
- Yi Ding
- Lijun Huang
- Menglin Yang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2608.27265'
url: https://arxiv.org/abs/2608.27265
pdf_url: https://arxiv.org/pdf/2608.27265
published: '2026-08-27'
collected: '2026-08-28'
category: Reasoning
direction: 隐式思维链因果机制诊断
tags:
- KV cache
- Latent Chain-of-Thought
- Causal Interpretability
- Transformer
- Mechanistic Analysis
one_liner: 提出后缀缓存互换测试SCIT，定位隐式思维链推理的因果载体
practical_value: '- 排查LLM推理Agent逻辑错误时，可复用SCIT的缓存互换思路，定位推理结果依赖Prompt前缀还是隐式推理缓存，快速定位电商智能导购、推荐理由生成场景的幻觉来源

  - 优化Latent CoT类轻量化推理模型部署时，参考论文结论：1B级小模型优先缓存中后层Value后缀提升推理效率，8B级大模型优先缓存Prompt前缀KV降低延迟，适配电商场景高并发推理需求

  - 做LLM推理鲁棒性验证时，可复用SCIT的匹配扰动测试逻辑，通过替换指定缓存段验证推理逻辑的因果可靠性，避免广告文案、商品推荐理由生成时出现逻辑错误'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Latent Chain-of-Thought把推理过程从显式文本转移到连续隐状态，大幅提升了推理紧凑性，但也隐藏了推理的因果载体。现有分析只能确定隐式推理是否影响结果，无法定位Transformer内部到底哪个组件承载了推理计算，导致模型调试、效率优化、鲁棒性验证都缺乏可解释依据。

### 方法关键点
- 提出SCIT（Suffix Cache Interchange Test）因果检测协议，构造精确的源-接收者反事实对，通过替换指定缓存段、控制变量（KV组件拆分、隐状态耦合、语义源控制、匹配扰动），定位承载反事实计算的最小组件
- 检测框架分4步：替换指定缓存切片、遍历干预选项（缓存段、KV组件、隐状态耦合方式）、多维度验证（目标胜率、概率边际、自由生成、随机扰动）、基于阈值判定载体类型（激活载体、载体漂移、无有效载体）
- 针对算术推理任务构造严格反事实数据集，所有源-接收者对的答案、中间变量完全已知，避免开放场景的语义歧义

### 关键结果
- CODI-GPT2算术任务上，反事实推理核心载体是中后层（8-9层）的Value缓存后缀，目标胜率达0.875~0.992，隐状态、Key缓存、单Token触发的胜率均低于0.03；匹配扰动该区域后目标胜率从1.00降至0.21，验证充分性与必要性
- 模型规模变化会引发载体漂移：1B级算术类任务仍以隐式后缀Value/KV为核心载体，8B级能力达标模型的推理载体迁移到Prompt前缀KV，目标胜率达1.00，隐式后缀几乎无贡献

最值得记住的结论：隐式思维链的推理载体没有通用结论，是由模型规模、训练路径、任务类型共同决定的能力门控型分布，而非统一的隐式后缀机制。
