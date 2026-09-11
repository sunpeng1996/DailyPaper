---
title: 'Recognizing Is Not Reversing: A Controlled Inversion Test of Fact-Preserving
  News Framing'
title_zh: 新闻框架识别≠反转：保事实的新闻框架可控反转测试
authors:
- Yi Liu
affiliations:
- University of Science and Technology of China
arxiv_id: '2609.11769'
url: https://arxiv.org/abs/2609.11769
pdf_url: https://arxiv.org/pdf/2609.11769
published: '2026-09-10'
collected: '2026-09-11'
category: Eval
direction: LLM能力评估 · 文本去偏改写
tags:
- LLM Evaluation
- News Framing
- Text Rewriting
- Factual Preservation
- Bias Mitigation
one_liner: 提出保事实新闻框架可控反转测试，证实LLM框架识别与反转能力存在显著差距
practical_value: '- 做电商商品文案、信息流内容去偏/中性化改造时，不能仅依赖LLM的立场识别结果，需额外加反转效果校验，避免识别正确但改写未达预期的问题

  - 搭建可控文本改写pipeline时，可将识别、改写、校验拆为独立模块分别选型：识别选准确率高的模型（如Kimi），改写选反转率高的模型（如Qwen），校验复用FactF1、IRR指标

  - 做商品评价、客服话术的情感/立场修正时，可借鉴三层框架分类（词汇、主体权重、信息显著性）针对性设计prompt和微调数据，提升改写目标达成率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM新闻改写相关评估仅覆盖生成、检测、中性化程度维度，无法验证模型是否能在完全保留核心事实的前提下撤销已知的框架注入操作，也无法区分事实保真、框架识别、框架反转三类独立能力，导致文本去偏、中性改写等场景的效果不可控。

### 方法关键点
- 定义三类新闻框架注入算子：词汇层面修改评价用词、句法层面调整主体权重/语态、篇章层面调整信息排序/显著性，每个算子分低中高三个强度，注入过程全程保留核心原子事实，记录所有编辑操作映射
- 构建540条标注完备的新闻平行语料：基于60篇基准新闻，每篇生成9种框架变体，所有变体经过严格的事实校验、框架有效性校验
- 设计两阶段评估范式：先让LLM识别输入文本的框架类型、方向，再基于自身识别结果做保事实的框架反转改写，分别用FactF1（事实保留率）、IRR（编辑反转率）评估改写效果

### 关键结果
测试Qwen、DeepSeek、Kimi三款主流LLM，事实保留率FactF1均稳定在0.83~0.84区间，但框架反转率IRR仅为0.044~0.068；即使框架类型、方向完全识别正确，pooled IRR也仅提升到0.071，仍有92.9%的注入编辑未被反转；三类框架中，词汇类最容易识别，信息显著性类反转率最低，比最高反转率的算子低59%~80%。

### 核心结论
LLM对文本立场/框架的识别能力，不直接等价于其修改该立场/框架的能力，两类能力存在显著割裂。
