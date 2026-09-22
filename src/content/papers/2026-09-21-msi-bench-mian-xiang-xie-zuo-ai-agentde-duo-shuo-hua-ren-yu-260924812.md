---
title: 'MSI-Bench: Evaluating Multi-Speaker Voice Interaction for Collaborative AI
  Agents'
title_zh: MSI-Bench：面向协作AI Agent的多说话人语音交互评测基准
authors:
- Chenxu Xiong
- Dongming Shen
- Yuzhi Tang
- Wentao Ma
- Mu Li
- Alex Smola
affiliations:
- Boson AI
arxiv_id: '2609.24812'
url: https://arxiv.org/abs/2609.24812
pdf_url: https://arxiv.org/pdf/2609.24812
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent 多说话人语音交互评测
tags:
- Multi-Speaker
- Voice Agent
- Benchmark
- Collaborative Agent
- Bilingual Evaluation
one_liner: 发布中英双语1152用例的多说话人语音交互评测基准，定位当前语音Agent三类核心瓶颈
practical_value: '- 做多用户场景语音Agent（智能客服、家庭助手、办公助手）时，可直接复用MSI-Bench的三类能力维度（记忆/指令遵循/推理）设计业务评测用例，无需从零搭建框架

  - 开源语音Agent落地的核心瓶颈是多说话人音频前端，业务优化可优先投入说话人分离、远场语音识别模块，收益远高于直接微调大模型

  - 多角色场景Agent必须新增「是否被用户寻址」的判断逻辑，避免未被呼叫就响应的体验问题，同时要实现说话人维度的权限、隐私隔离规则，避免信息泄露

  - 评测多模态语音Agent时，可复用论文的LLM原子规则自动判分+工具调用确定性校验方案，大幅降低人工标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前语音Agent默认适配单用户一对一交互，而家庭、会议、团队办公等实际协作场景都是多说话人环境，现有评测基准仅覆盖交互时机、单轮语义理解，未考虑说话人维度的权限、隐私、记忆约束，导致Agent频繁出现越权回应、隐私泄露、指令混淆等问题。

### 方法关键点
- 定义三类核心评测维度：多说话人记忆（背景语音检索、约束范围跟踪）、多说话人指令遵循（选择性披露、说话人权限约束）、多说话人推理（约束序列整合、优先级判断），共6种测试模式
- 全自动化数据生成pipeline：输入场景、语言、说话人配置后，经LLM生成剧本、评测规则、工具调用真值，再通过TTS合成带空间距离、背景噪音的多说话人音频
- 评测方案：采用原子评分规则+LLM自动判分+工具调用确定性校验，新增旁观者干扰鲁棒性、未被寻址响应率两个体验类指标

### 关键结果
数据集共1152个测试用例，中英各576个，覆盖8个真实场景；评测12个模型15种配置，最强闭源模型英语全通过率66.8%、中文54.5%，最强开源模型英语34.0%、中文19.3%；开源模型性能瓶颈90%来自音频前端，输入带说话人标注的转录文本可提升21-44个百分点的全通过率，闭源模型的瓶颈则是说话人维度的推理决策。

最值得记住的一句话：多说话人语音Agent的核心优化方向是三个独立维度：说话人感知的音频前端、说话人维度的决策推理、知晓何时保持沉默的交互约束
