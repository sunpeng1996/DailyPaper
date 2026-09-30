---
title: Does the Unsafe Gradient Survive a Conversation? On the Fragility of Gradient-Based
  Jailbreak Detection in Multi-Turn Dialogue
title_zh: 多轮对话场景下基于梯度的越狱检测方法的脆弱性研究
authors:
- Omar Sheta
- Rinku Deuja
- Hadi Masoudi
- Minghong Fang
affiliations:
- University of Louisville
arxiv_id: '2609.36849'
url: https://arxiv.org/abs/2609.36849
pdf_url: https://arxiv.org/pdf/2609.36849
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM安全 · 多轮越狱检测
tags:
- LLM Safety
- Jailbreak Detection
- Multi-turn Dialogue
- Gradient-based Detection
- Adversarial Attack
one_liner: 通过扩展GradSafe验证多轮场景下梯度越狱检测受多因素影响存在严重脆弱性
practical_value: '- 部署多轮对话Agent的安全检测时，禁止用合成良性数据校准阈值，必须用自身业务真实对话数据调优，避免90%+的误拦截率

  - 若基于梯度方案做越狱检测，优先测试单轮窗口+max pooling架构，在Llama系列模型上该方案比长窗口/全历史累计的AUC高~0.07

  - 安全检测架构需适配不同基座模型：Llama系短窗口最优，Qwen系则是全历史累计方案效果最好，不可跨模型直接复用

  - 需定期针对新出现的多轮越狱攻击（如Crescendo）重测检测效果，现有梯度方案对这类上下文隐式攻击的AUC接近随机水平'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前安全对齐LLM大量以多轮对话助手形式部署，攻击者可将恶意意图拆分到多轮隐式表达，而现有基于梯度的越狱检测（如GradSafe）均针对单轮输入设计，其在多轮场景下的有效性未被验证，直接部署存在严重安全风险。

### 方法关键点
- 基于单轮GradSafe扩展Context Window Scanner（CWS）模块，滑动固定大小窗口截取用户轮次，计算每个窗口的梯度与预存 unsafe 参考方向的余弦相似度，取所有窗口的最大值作为对话级风险得分
- 对比单轮、多轮滑动窗口、全历史累计三种上下文处理策略，覆盖不同窗口大小、攻击类型、良性数据集、基座模型的变量控制测试

### 关键结果数字
实验数据集包含537条人工编写多轮越狱对话（MHJ）、149条Crescendo自动生成的成功越狱对话、2000条长度匹配的真实WildChat良性对话、183条合成良性对话，对比baseline包括单轮检测、全历史累计、Llama Guard 3。核心结果：
- 合成良性数据下W=3窗口AUC达0.98，迁移到真实WildChat数据后AUC骤降到0.76，误拦率超90%
- 真实场景下Llama系模型单轮窗口AUC最高达0.81，窗口越大AUC越低，全历史累计仅0.74
- 对Crescendo类隐式多轮攻击，单轮窗口AUC仅0.50接近随机；Qwen2.5-7B-Instruct上所有梯度检测方案AUC均在0.5~0.6的随机区间

### 最值得记住的一句话
多轮场景下的安全检测不能默认「更多上下文效果更好」，用合成数据评估得到的高性能在真实业务中几乎一定会严重高估，阈值和检测架构必须基于真实业务数据、适配基座模型和攻击类型单独校准。
