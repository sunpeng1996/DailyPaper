---
title: 'When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk,
  and Defenses in Persona Skills'
title_zh: Persona技能隐私泄露、冒充风险基准及防御效果评估
authors:
- Yongli Xiang
- Zhifang Zhang
- Bojun Yang
- Ziming Hong
- Lei Feng
- Miao Xu
- Tongliang Liu
affiliations:
- The University of Sydney
- University of Queensland
- Southeast University
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2608.03700'
url: https://arxiv.org/abs/2608.03700
pdf_url: https://arxiv.org/pdf/2608.03700
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent个性化 · Persona技能安全评估
tags:
- Agent-Safety
- Persona-Skill
- Privacy-Leakage
- Impersonation-Risk
- Benchmark
one_liner: 构建端到端基准AntiSkillBench，系统评估Persona技能全链路隐私风险与现有防御的有效性
practical_value: '- 构建用户专属电商导购/数字分身Agent时，可直接复用Skill Coverage、QAAcc、VocabGain三个度量，检测Persona蒸馏环节泄露的用户属性、行为风格风险

  - 降低隐私泄露优先选择在线Privacy Sanitization（PS）方案，在用户输入阶段脱敏隐私属性与话术风格，可降低80%以上的沟通风格泄露，效果优于事后混淆

  - 需追溯未授权Persona技能盗用场景，可使用Semantic Backdoor Injection（SBD）注入语义水印，在直接蒸馏、三阶段蒸馏场景下溯源准确率可达98%

  - 现有防御对用户深层性格、背景信息防护效果有限，敏感用户属性不要纳入Persona蒸馏的原始Trace数据集，从源头规避泄露风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Persona技能将用户交互历史蒸馏为可跨Agent复用的可执行模块，是个性化Agent系统的核心技术，但现有针对单条记录、检索式记忆的隐私防御无法应对蒸馏带来的三大问题：分散隐私信息集中到技能artifact更易泄露、技能可移植性放大泄露影响、跨记录蒸馏可推断已删除标识的隐式属性，行业缺乏端到端基准评估全链路风险。

### 方法关键点
- 构建AntiSkillBench基准：包含7500条基于50个丰富用户画像（含人口属性、背景、大五人格、沟通风格）的多轮对话Trace，覆盖技能层隐私泄露、Agent层冒充两类风险的评估套件，以及在线/事后、主动抑制/被动溯源4类防御配置
- 风险度量设计3个核心指标：Skill Coverage（技能留存的用户信息占比）、QAAcc（装备技能的Agent回答用户属性问题的准确率）、VocabGain（Agent生成内容与用户话术的匹配度提升）
- 对比3种主流蒸馏策略：直接蒸馏、三阶段蒸馏、Colleague蒸馏，以及4种防御方案：在线Privacy Sanitization（PS）、事后Adversarial Obfuscation（ADV）、在线/事后Semantic Backdoor Injection（SBD）

### 关键结果
全场景下技能层平均Skill Coverage达55.2%~66.2%，其中沟通风格留存率最高达92%；Agent层QAAcc最高56%，VocabGain最高31.3%，风险跨GPT、Claude、Gemini三类主流Agent backbone、跨三种蒸馏策略普遍存在。现有防御效果有限：在线PS可将整体泄露率降低12~18个百分点，但对人格、背景信息防护效果差；SBD语义水印在直接/三阶段蒸馏下溯源准确率达98%，但在Colleague蒸馏下完全失效。

### 核心结论
Persona技能的隐私泄露是结构性的，不仅包含显性人口/背景属性，还会留存用户性格、沟通风格等隐性特征，现有防御无法实现全场景有效防护
