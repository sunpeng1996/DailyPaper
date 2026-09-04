---
title: 'Speak for Me: Giving LLMs the Situational Awareness to Participate in a Meeting'
title_zh: 赋予LLM情境感知能力的会议代理架构CAPA
authors:
- Muneeb Khan
- Frederic Kirstein
- Terry Ruas
- Bela Gipp
affiliations:
- University of Göttingen, Germany
arxiv_id: '2609.03923'
url: https://arxiv.org/abs/2609.03923
pdf_url: https://arxiv.org/pdf/2609.03923
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: 多轮对话Agent · 情境感知状态跟踪
tags:
- LLM Agent
- Situational Awareness
- State Tracking
- Multi-party Conversation
- Meeting Assistant
one_liner: 提出感知-行动-重校准的CAPA架构，将会议代理沉默率从51.4%降至2.5%，幻觉率仅0.6%
practical_value: '- 电商直播场控Agent、多用户客服转接代理、社群运营Agent的主动发言决策，可复用显式状态拆解思路，将用户诉求、发言权限、已回复内容、上下文话题等核心信息结构化存储，替代纯prompt喂长上下文的方案，解决长交互下的信息遗漏、响应不及时问题

  - 主动决策类Agent的反馈优化可借鉴双评委+状态重校准机制，将交互反馈直接更新到底层状态字段，而非仅优化输出话术，可解决Reflexion等输出层校正方案无法处理的沉默、漏响应类错误，适用于广告投放时机决策、推荐系统主动召回时机判定等场景

  - 多角色交互类Agent的效果评估可复用基于idea unit的episode级评估框架，同时考核响应时机、内容匹配度、合规性，比单纯的文本相似度、单点人工打分更贴合业务实际，可直接用于客服代理、直播场控Agent的效果评测'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有prompt驱动的LLM会议代理无法识别合适的发言时机，在AMI语料上51.4%的本该发言的场景保持沉默，核心原因是缺乏对参会者立场、发言权限、已覆盖内容等状态的显式跟踪，单纯拉长上下文窗口也无法解决长对话推理缺陷，导致代理要么漏发言要么发言冗余、跑题。
### 方法关键点
- 采用感知-行动-重校准的循环架构CAPA，维护显式结构化会议状态，包含活跃话题、已达成决策、待解决问题、参会者立场、已覆盖内容、发言权限6个核心字段
- 模块化拆分逻辑：Perceiver模块每轮从新的对话turn更新状态；Controller先决策是否发言、选定语义命题，Generator再基于用户风格生成话术；Recalibrator模块通过预测器+两个独立LLM评委的反馈更新状态，避免上下文漂移
- 设计episode级评估协议，基于参会者实际输出的idea unit为锚点，同时评估发言时机、内容匹配度、合理性，LLM评委与人工标注的Cohen's κ达0.71
### 关键实验
在137场AMI公开会议语料上对比纯prompt、Reflexion两类基线：CAPA将沉默率从51.4%降至2.5%，有效发言召回率从26.1%提升至52.2%，幻觉率维持在0.6%；ablation实验证明显式状态是效果提升的核心，单纯拉长上下文窗口无法复现同等提升，且架构可迁移到Gemini、Llama、Qwen等多个主流底座。
### 核心结论
多轮交互场景下主动代理的核心瓶颈是机会识别而非内容生成，显式结构化状态跟踪比单纯拉长上下文、输出层自校正的效果提升要显著得多
