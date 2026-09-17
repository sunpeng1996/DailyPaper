---
title: 'Another Blueprint In The Wall: How to Ask Frontier AI Like a Kid?'
title_zh: 孩童式提问法：引导前沿大模型输出共通架构设计蓝图
authors:
- Afshin Khadangi
affiliations:
- University of Luxembourg
arxiv_id: '2609.14803'
url: https://arxiv.org/abs/2609.14803
pdf_url: https://arxiv.org/pdf/2609.14803
published: '2026-09-12'
collected: '2026-09-17'
category: LLM
direction: 大模型Prompt设计 · 架构输出引导
tags:
- Prompt Engineering
- LLM Architecture
- Elicitation Method
- Epistemic Jailbreak
- Convergence Analysis
one_liner: 通过学生视角提问框架引导6款前沿大模型收敛输出下一代大模型共通架构设计范式
practical_value: '- 做Agent/LLM4Rec的Prompt设计时，可加入「面向低认知受众解释」的framing约束，大幅提升不同LLM输出结果的一致性，降低多模型协作适配成本

  - 需引导LLM输出推荐系统架构、电商运营策略等领域结构化方案时，可复用三阶段递进提问+受众framing的范式，提升输出可用性与收敛性

  - 若需要获取创新性架构设计思路，可适当降低技术严谨性约束，触发epistemic jailbreak效应，得到更具启发性的方案'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有大模型提问范式难以引导不同厂商前沿模型输出稳定收敛的技术方案，输出异质性高，无法提炼通用设计规律。
### 方法关键点
选取OpenAI、Anthropic、xAI、Google DeepMind旗下共6款前沿大模型，每款开展10轮独立会话，采用三阶段递进Prompt序列，实验组加入「面向学生受众解释」的语境框架，对照组移除该框架仅保留架构设计请求。
### 关键结果
实验组超80%输出收敛到包含持久latent state、自适应计算、内存、专家路由、验证、停止控制、延迟解码7个核心模块的共通架构；对照组输出异质性提升60%以上，无稳定收敛结构。额外观察到GPT-5.6 Sol与GPT-6 Astra独立输出的下一代架构重合度极高，验证了提问语境对大模型输出的强调控作用。
