---
title: 'Separating Syntax from Language: A Mechanistic Account of Translation in Multilingual
  LLMs'
title_zh: 从语言中分离句法：多语种大语言模型翻译的机制解释
authors:
- Mikhail Sonkin
- Tanja Baeumel
- Daniil Gurgurov
- Josef van Genabith
- Simon Ostermann
affiliations:
- Saarland University
- German Research Center for Artificial Intelligence (DFKI)
- Centre for European Research in Trusted AI (CERTAIN)
- University of Göttingen
arxiv_id: '2609.01356'
url: https://arxiv.org/abs/2609.01356
pdf_url: https://arxiv.org/pdf/2609.01356
published: '2026-09-01'
collected: '2026-09-03'
category: LLM
direction: 多语种LLM · 翻译机制解析
tags:
- mLLM
- Machine Translation
- Syntactic Representation
- Probing
- Attention Head
one_liner: 拆解多语种LLM翻译为语义、句法、表层语言生成三阶段，识别出语种无关的句法专属注意力头
practical_value: '- 跨境电商多语种文案生成场景可复用翻译三阶段拆解逻辑，单独调优句法模块适配小语种语序规则，降低生成语法错误率

  - 跨语言搜索推荐的Query改写/翻译需求，可固定句法专属注意力头仅微调表层语言参数，大幅降低多语种适配的训练成本

  - 多语种Agent的跨语言交互模块可参考模块化翻译架构，减少不同语种切换时的语义漂移，提升交互一致性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
多语种LLM（mLLM）翻译性能优异，但内部表征转换机制尚未完全厘清，此前研究仅将翻译拆解为语义独立表征、语种特定生成两个阶段，颗粒度较粗无法支撑精准干预。

### 方法关键点
构建隔离跨语言词序差异的受控多语种数据集，采用因果干预、探针技术追踪翻译全流程的表征转换路径，定位功能特异性的注意力头模块。

### 关键结果
1. 翻译实际分为三独立阶段：先生成跨语言通用语义表征，再确定目标语言句法（词序），最后生成表层语言形式；2. 识别出对句法变换高度敏感、完全不受语种身份影响的独立注意力头；3. 句法结构确定是翻译的独立前置阶段，进一步细化了mLLM翻译的模块化拆解结论，为精准控制翻译过程提供了机制支撑。
