---
title: Can Omni-modal LLMs Understand Spoken Intentions?
title_zh: 全模态大语言模型能否理解口语化意图？
authors:
- Zijie Xin
- Tianyi Wang
- Daoze Zhang
- Jie Yang
- Changli Tang
- Qijie Wei
- Fengyun Rao
- Xirong Li
affiliations:
- Renmin University of China
- WeChat Vision, Tencent Inc.
arxiv_id: '2611.24706'
url: https://arxiv.org/abs/2611.24706
pdf_url: https://arxiv.org/pdf/2611.24706
published: '2026-11-18'
collected: '2026-11-19'
category: Eval
direction: 全模态LLM · 口语意图理解评估
tags:
- Omni-modal LLM
- Spoken Intent Understanding
- Evaluation Benchmark
- Multimodal Interaction
- Video Understanding
one_liner: 提出O-IN-Bench基准，评估全模态LLM对视频场景下口语意图的理解与响应能力
practical_value: '- 开发语音交互类Agent（如电商直播语音助手、导购AI、智能家居交互Agent）时，需拆分「意图识别（是否需要响应）」「响应内容匹配场景」两个独立能力分别迭代优化，不要混同评估与训练

  - 构建多模态交互测试集时可复用对比样本对设计：同一请求搭配不同场景上下文，验证模型的场景感知能力，避免模型过拟合固定话术

  - 语音交互场景的评测体系可参考分维度打分逻辑，分别校验语言合规性、意图准确性、内容匹配度，相比整体打分更容易定位模型缺陷'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
全模态LLM已支持通过音视频通话直接响应口语请求，同类请求的响应依赖用户与助手共享的场景上下文，但现有视听基准多将问题作为独立文本输入，交互基准多对响应整体打分，无法区分模型「是否识别到需要响应的请求」「响应是否满足用户需求」两类能力。
### 方法
提出O-IN-Bench基准评估全模态LLM的口语意图理解能力，要求模型输入带原生语音的完整视频，输出文本响应或[SILENCE]（无需响应时）；包含1000个中英双语样本覆盖5大类16小类场景，设计同请求搭配不同场景的对比样本对验证上下文感知能力，配套分维度（语言、意图、内容）的专属评分规则及O-IN-Engine自动校验机制。
### 结果
30种全模态模型配置中Gemini3.7-Flash表现最优，总得分59.6；其意图判断通过率74.4%，但内容匹配通过率仅42.6%；非向助手发起的同伴对话场景下强模型仍易误响应，需满足多人需求的场景最优得分仅25.9%
