---
title: Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study
  on Web Element Hallucination
title_zh: 机制可解释性能否解释LLM Agent故障？网页元素幻觉案例研究
authors:
- Mohamed Aghzal
- Mor Geva
- Gregory J. Stein
- Ziyu Yao
affiliations:
- George Mason University
- Tel Aviv University
arxiv_id: '2611.18514'
url: https://arxiv.org/abs/2611.18514
pdf_url: https://arxiv.org/pdf/2611.18514
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent可解释性 · 幻觉故障诊断
tags:
- Mechanistic Interpretability
- LLM Agent
- Hallucination
- Web Agent
- Linear Probe
- Activation Steering
one_liner: 以网页元素幻觉为案例，揭示现有机制可解释性工具应用于LLM Agent的局限与干预效果
practical_value: '- 电商导购Agent、搜索工具调用Agent可在prompt最后一个token的激活值上训练线性探针，提前预判幻觉（AUC 0.80），做前置拦截避免无效操作

  - 可将探针方向的activation steering集成到Agent推理链路，修复85%的幻觉，仅7%的正常操作被干扰，性价比极高

  - 幻觉探针/steering向量与prompt格式强绑定，修改工具列表、指令模板后必须重新训练，不可跨格式复用

  - 通用预训练SAE无法提取Agent场景的业务相关特征，若要做Agent内部状态解析，需用自有业务Agent交互轨迹重新训练SAE'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent在网页导航、工具调用等长序列任务中存在独有的故障模式（如幻觉不存在的网页元素、工具），现有Mechanistic Interpretability (MI) 方法均针对静态单轮LLM任务设计，能否解释Agent故障、能否用于故障修复尚不明确，是Agent落地可靠性的核心瓶颈。

### 方法关键点
- 选取网页Agent的网页元素幻觉为典型故障案例，在Online-Mind2Web真实网页交互数据集上测试Qwen2.5-7B-Instruct模型
- 从电路发现、特征识别两个维度验证现有MI方法的适配性：包括FFN/注意力头干预、激活修补、线性探针训练、activation steering、预训练SAE特征提取
- 额外测试探针在prompt格式变化下的鲁棒性，验证MI结果的泛用性

### 关键结果
- 数据集共300个交互episode、2071个动作，幻觉率32.6%
- 基于prompt最后一个token训练的线性探针预测幻觉的AUC达0.80，可在生成前预判故障
- 沿探针方向做activation steering可修复85%的幻觉，仅7%的正常动作被干扰
- 针对注意力头/FFN的单组件干预最多仅能修复8.9%的幻觉，预训练SAE无法提取和幻觉相关的可解释特征，prompt格式微调后探针效果大幅下降

**最值得记住的一句话**：现有MI方法可以检测并干预Agent故障，但无法完全解释故障成因，Agent场景需要适配动态序列、分布偏移特性的专属MI方法。
