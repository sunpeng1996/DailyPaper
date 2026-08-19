---
title: 'Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What
  Accuracy Cannot See'
title_zh: 低资源语言推理调优：SFT的价值、RL的修复与精度的盲区
authors:
- Ayoub Kirouane
- Christos Petrocheilos
affiliations:
- Sophea AI, KIEFER SA, Greece
arxiv_id: '2608.17744'
url: https://arxiv.org/abs/2608.17744
pdf_url: https://arxiv.org/pdf/2608.17744
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: 低资源语言大模型推理调优
tags:
- Low-Resource Language
- SFT
- RL
- MoE
- Model Evaluation
- LoRA
one_liner: 验证低资源语言下MoE推理调优的价值不在精度，而在可量化行为维度，RL可修复SFT指令遵循缺陷
practical_value: '- 小语种出海场景的LLM/Agent调优不要只卡精度指标，重点监控推理语言fidelity、token消耗、指令遵循率等业务核心行为指标，避免被训练噪声误导

  - 小语种CoT语料不要直接翻译英文现成样本，直接用LLM原生生成对应语言的推理轨迹并做正确性校验，可大幅提升推理结构有效性

  - 模型优化实验前必须先跑seed控制基线：同配置多seed精度波动可达7.7pp，远大于多数算法优化的收益，单轮A/B结果完全不可信

  - 电商Agent/客服等需要结构化输出的场景，可采用预注册可验证奖励的RL修复SFT的指令遵循缺陷：答案格式错误率从24%降至2.5%，回答泄露率从3.5%降至0'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
低资源语言大模型推理调优通常仅用单一精度指标评估，既无法反映推理语言、token成本、格式合规性等业务核心需求，也容易被训练噪声干扰得到完全错误的结论，急需建立更科学的评估体系和调优范式。
### 方法关键点
- 选取阿里、OpenAI、英伟达3家的3.6~4.0B active参数MoE模型，采用r=32的LoRA微调，全流程可在单台8卡B200节点复现
- 构建11.8万条希腊语语料，推理轨迹为LLM原生生成而非翻译，通过STaR规则校验正确性
- 提出6维行为评估指标（正确性、语言保真度、推理预算、终止性、推理步数、预算超支率），过滤与输出长度强相关的无效指标
- 对比SFT的3种训练范式，采用预注册可验证奖励的RL修复SFT的指令遵循缺陷
### 关键结果
- 同配置仅修改随机seed，精度波动可达7.7pp，远超所有数据和算法优化的效果；SFT后模型用问题对应语言推理的比例从0%提升至98%左右，无中途语言切换
- SFT存在答案格式错误率高（24%）、回答泄露到推理通道（3.5%）、不遵循语言切换指令等缺陷，RL修复后格式错误率降至2.5%，回答泄露率降为0，语言指令遵循率提升9.1pp
- 推理语料与非推理语料混合单阶段训练会导致23.6%的空推理轨迹，仅用推理语料训练的精度比两阶段范式高6.9pp，无空轨迹问题
### 核心结论
低资源语言调优的核心价值几乎都在精度看不见的行为维度，单轮精度对比在高训练噪声下没有任何参考意义。
