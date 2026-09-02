---
title: 'From Production Traffic to Post-Training: Building a Self-Hosted LLM That
  Covers the Corporate Request Mix'
title_zh: 基于生产流量后训练的企业全场景自托管LLM构建方案
authors:
- Olga Tsymboi
- Dmitrii Stoianov
- Ramil Latypov
- Danil Taranets
- Daniil Dryabin
- Mikhail Gashkov
- Viktor Zelenkovskiy
- Aleksandr Fida
- Gleb Alektorov
- Nikita Gulyakov
affiliations:
- T-Tech
arxiv_id: '2609.01572'
url: https://arxiv.org/abs/2609.01572
pdf_url: https://arxiv.org/pdf/2609.01572
published: '2026-08-31'
collected: '2026-09-02'
category: Training
direction: LLM后训练 · 自托管模型部署
tags:
- Self-hosted LLM
- GRPO
- SLERP
- Model Merging
- Post-training
- Function Calling
one_liner: 通过分领域训练GRPO专家+两阶段SLERP合并，32B自托管LLM媲美7倍参数基线承载116M月请求
practical_value: '- 企业多场景LLM部署可复用分领域训练GRPO专家+SLERP合并的架构，无需为内容生成、工具调用、指令遵循等场景分别部署独立模型，大幅降低GPU资源消耗，尤其适合电商/推荐场景多业务线共用LLM的需求

  - 构建业务专属评估集时可采用模板感知采样方案，平衡样本多样性与生产分布代表性，解决电商/推荐场景大量模板化query导致的评估集偏差问题；同时对不同任务类型采用定制化评估规则，提升自动评估与人工标注的一致性

  - 多目标GRPO训练出现跨域奖励干扰时，可放弃联合训练，采用单领域专家训练后合并的方案，大幅降低调参难度；针对指令遵循的语义崩塌、工具调用的过度调用等reward
  hacking问题，可分别针对性修复后再合并，避免能力互相抵消

  - 低延迟高并发业务场景可优先优化32B级非推理模式模型，通过定向后训练即可逼近更大参数模型的业务效果，单GPU FP8部署即可承载高并发请求，大幅降低电商/推荐场景的LLM推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
企业受数据驻留监管约束必须自托管LLM，各业务线独立选型适配模型导致GPU资源碎片化、推理成本居高不下；联合多目标RL训练存在跨域奖励干扰，无法同时优化指令遵循、工具调用、内部任务适配三类核心业务需求。

### 方法关键点
- 从生产流量构建分层评估基准：采用模板感知采样平衡样本多样性与生产分布代表性，针对参考型/开放型任务采用定制化评估规则，自动评估与人工标注的加权Cohen's κ从0.62提升至0.85
- 后训练采用模块化架构：先统一做SFT混合全领域数据，再分3个独立分支训练GRPO专家：通用任务对齐专家、指令遵循专家（VerIF奖励+RM质量矫正避免语义崩塌）、工具调用专家（原生多语言合成数据+无关样本注入避免过度调用）
- 用两阶段SLERP合并专家：优先合并指令遵循、工具调用两个可验证奖励的专家，再合并通用专家，规避合并顺序带来的效果损失

### 关键结果
基于Qwen3-32B训练的非推理模式模型，内部Arena得分69.6超过7倍参数的Qwen3-235B基线的65.8，指令遵循得分0.85 vs 基线0.83，工具调用得分0.79 vs 基线0.77；生产环境承载116M月请求、200+内部服务，单GPU FP8部署95分位延迟3.2s，推理成本比大模型基线降低2.8~9倍。

最值得记住的一句话：企业级LLM后训练采用模块化拆分目标的方案，比联合多目标训练更易调试、扩展和落地，效果与成本收益更可控。
