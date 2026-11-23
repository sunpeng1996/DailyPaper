---
title: The Assistant Persona Differs Across Languages in Activation Space
title_zh: 大语言模型不同语言下的助手人设激活空间存在显著差异
authors:
- Daniel Yoo
- Naama Rozen
- Evan Harris
affiliations:
- Carnegie Mellon University
- Tel Aviv University
- Independent Researcher
arxiv_id: '2611.27504'
url: https://arxiv.org/abs/2611.27504
pdf_url: https://arxiv.org/pdf/2611.27504
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 大语言模型 · 多语言人设对齐与安全
tags:
- Multilingual LLM
- Activation Steering
- Persona Alignment
- Model Safety
- Interpretability
one_liner: 验证多语言大模型助手人设轴跨语言不通用 与语料资源等级强相关 安全干预需适配对应语言
practical_value: '- 做多语言客服Agent、多语言推荐文案生成等场景时，不要直接复用英文的人设对齐、安全干预逻辑，需针对目标语言单独提取Assistant
  Axis做校准，避免低资源语言下出现人设漂移、安全降级问题

  - 若业务使用activation steering、activation capping等激活干预手段优化LLM输出，阈值必须按语言单独标定，英语标定的阈值会对所有非英语语言的默认态产生过度修正，影响正常输出的自然度

  - 涉及中文的多语言LLM业务需额外注意：中文Assistant Axis与其他高资源语言的差异远高于平均水平，必须单独做对齐与干预逻辑开发，不可直接复用其他语言的方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言LLM的助手人设提取、安全干预逻辑几乎都从英语数据中得到，默认假设跨语言通用，但实际观测到低资源语言下模型安全表现显著更差，背后的激活空间层面机制未被探明，需验证跨语言的助手人设表示是否存在一致性。

### 方法关键点
- 核心实验基于Qwen3-32B开展，覆盖31种语言，按Common Crawl语料占比划分为高/中/低资源三个等级，同时在Gemma 2 27B、Llama 3.3 70B上验证结论通用性
- 针对每种语言独立提取Assistant Axis，用GPT-5.6 Sol统一翻译所有prompt减少翻译偏差，仅采用完全符合角色扮演要求的响应构造向量
- 对比不同语言的Assistant Axis几何特征，通过激活steering、activation capping实验验证轴差异对安全干预效果的影响，用LLM-as-judge评估输出有害性

### 关键结果
- 非英语语言的Assistant Axis与英语轴的cosine相似度仅0.378~0.911，均值0.743，远低于两次英语独立提取的相似度0.969
- 各语言Assistant Axis与英语轴的相似度、轴范数、默认态到助极端的投影值，与语料资源等级的相关系数分别达0.774、0.904、0.831
- 沿对应语言自身Assistant Axis反向steering时，有害请求的响应率比使用英语轴高2.1个百分点，安全干预效果差距显著
- 英语标定的activation capping阈值会对所有非英语语言的默认激活态产生过度修正，低资源语言修正幅度更大

### 核心结论
多语言大模型不存在全局统一的助手人设表示，针对英语的人设对齐、安全干预策略无法直接迁移到其他语言，尤其是低资源语言
