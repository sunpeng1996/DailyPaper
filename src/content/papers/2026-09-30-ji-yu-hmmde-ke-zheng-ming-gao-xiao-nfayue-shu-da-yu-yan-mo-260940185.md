---
title: Provably Tractable NFA-Constrained Language Generation via HMMs
title_zh: 基于HMM的可证明高效NFA约束大语言模型生成框架
authors:
- Jialiang Sun
- Kuldeep Meel
affiliations:
- University of Toronto
arxiv_id: '2609.40185'
url: https://arxiv.org/abs/2609.40185
pdf_url: https://arxiv.org/pdf/2609.40185
published: '2026-09-30'
collected: '2026-10-01'
category: LLM
direction: 大语言模型约束生成 · NFA约束
tags:
- Constrained Generation
- NFA
- HMM
- LLM Decoding
- Regular Expression
one_liner: 提出带理论误差保障的多项式时间NFA约束语言生成引擎NFA-LM
practical_value: '- Agent的function call、电商广告文案合规校验、结构化订单生成等场景，可复用NFA-LM替代XGrammar这类分布无感知约束解码方案，既100%满足Regex类约束，又避免生成凑约束的低质量内容

  - 针对多关键词、间隔匹配等复杂正则约束，优先用NFA而非DFA建模约束规则，可避免DFA状态指数级爆炸导致的解码超时，适配电商/广告场景的复杂合规、营销词要求

  - HMM蒸馏+离线预计算后缀权重的架构可复用在低延迟约束生成场景，预计算阶段离线完成，生成阶段仅需查表重加权LM下一词分布，无需实时复杂约束校验'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM约束生成方案存在明显缺陷：分布无感知类方法（如XGrammar、PICARD）解码时mask非法token，会扭曲原始LM输出分布，易生成重复、无意义的凑约束内容；分布感知类方法（如Ctrl-G）依赖DFA建模正则约束，复杂规则下DFA状态呈指数级爆炸，无多项式时间误差保障，无法适配多关键词、间隔匹配等复杂规则场景，而NFA是正则表达式更紧凑的表示形式，可天然避免DFA的状态爆炸问题。
### 方法关键点
- 从基座LM蒸馏轻量HMM，用HMM近似基座LM的未来序列约束满足概率，规避直接求解#NFA（#P完全问题）的超高复杂度
- 预计算阶段从NFA终止状态反向逐层采样后缀样本，结合FPRAS估计每个前缀对应的约束满足概率，误差可通过理论参数控制
- 生成阶段用预计算的HMM约束概率重加权基座LM的下一词分布，在保证约束满足的前提下最小化对原始LM分布的扭曲
### 关键实验
在CommonGen数据集上测试10类复杂Regex约束（对应NFA状态数远小于DFA），对比基座LLM、XGrammar、Ctrl-G：NFA-LM约束满足率100%，Gemma-4-E2B上平均耗时28.5s，远低于Ctrl-G的155.6s（Ctrl-G仅43.4%样本在256s超时阈值内完成），生成质量评分2.48，远高于XGrammar的1.84，最大相对误差仅0.00315，远低于理论设定的0.1误差边界。
### 核心结论
针对Regex类结构化约束生成场景，基于NFA+FPRAS的分布感知解码方案，可同时实现100%约束满足、低延迟、高质量生成，是比DFA、分布无感知mask更优的工业落地方向
