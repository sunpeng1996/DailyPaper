---
title: 'PersonaFactory: Stylistic User Prompt Augmentation with Synthetic Persona
  Bank'
title_zh: PersonaFactory：基于合成人物库的风格化用户Prompt增强方法
authors:
- Bich Ngoc Doan
- Hanna Yukhymenko
- Imanol Schlag
affiliations:
- EPFL
- ETH Zurich
arxiv_id: '2611.34785'
url: https://arxiv.org/abs/2611.34785
pdf_url: https://arxiv.org/pdf/2611.34785
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: 合成Persona · LLM对话训练数据增强
tags:
- Persona Generation
- Prompt Augmentation
- Synthetic Training Data
- Conversational LLM
- Multilingual NLP
one_liner: 构建带结构化风格层的74万合成人物库，生成124万跨85语种的风格化对话数据
practical_value: '- 电商客服Agent、个性化推荐的用户模拟场景，可直接复用双层结构化Persona建模方案，拆分用户属性与可量化风格轴，在保留用户需求核心意图的前提下控制生成风格，大幅提升模拟用户的真实度

  - 做用户query改写、个性化营销文案生成的业务，可借鉴「固定核心请求+每句最多叠加2个风格标记」的改写策略，避免风格过度修饰导致意图偏移，同时实现千人千面的query/文案风格适配

  - 跨语种、跨区域的搜索推荐/广告业务，可直接复用开源的74万Persona库，快速生成不同地域、语言、文化背景的用户测试query，用于多语言模型的鲁棒性评测，降低真人标注成本

  - 训练对话式导购Agent的团队，可用该流水线增强现有对话训练数据，提升Agent对不同风格用户query的理解能力和响应适配度，优化用户交互体验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM训练用的合成对话数据风格高度同质化，多为标准正式的书面语，缺少真实用户常见的非正式输入、方言、代码切换、拼写错误、缩写等特征，导致训练出的模型对真实用户query理解鲁棒性差，个性化响应能力不足；传统Persona模拟方案要么仅用短文本描述无法精准控制输出风格，要么自由生成容易偏离原始请求意图，无法复用现有高质量对话数据的意图轨迹。
### 方法关键点
- 提出双层结构化Persona schema：背景层覆盖年龄、地域、职业、母语、AI接受度等属性，风格层拆解为大小写、标点使用、emoji习惯、缩写偏好、拼写错误率等7个可量化维度，搭配2-4个专属语言习惯和示例消息，职业与地域独立采样避免刻板印象
- 四步增强流水线：1）支持保守同语言匹配/跨语种随机匹配两种策略，无匹配时保留原prompt；2）约束式用户轮次改写，固定原始请求核心信息，代码、URL、数字等片段掩码还原，每轮最多叠加2个风格标记避免过度修饰；3）助理回复重生成时用原始对话下一轮用户消息做弱监督，保证对话轨迹不变；4）6维度LLM校验门过滤意图偏移、语言不匹配等坏例
### 关键结果
生成74.3万结构化Persona库，123.8万跨85语种的风格化对话数据开源可用；对比自由文本Persona描述，结构化风格表示的风格保真度领先27个百分点，意图保留率持平92%；全量语料的意图保留率达96.6%，风格匹配率67.1%；人类盲测中59%的生成对话被误认为是真人输入，区分准确率仅55%接近随机水平；用增强数据训练的LLM在真实用户query上的用户偏好度优于基线，跨语种指令跟随能力提升最显著。
### 核心结论
固定核心意图+可量化的分轴风格控制，远比模糊的自由文本Persona描述效率更高、保真度更好
