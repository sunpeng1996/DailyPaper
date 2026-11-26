---
title: 'Latent-in-the-Middle: On the Security of Cross-Model Latent Communication
  in Multi-Agent Systems'
title_zh: 多智能体系统跨模型隐态通信的安全性分析与防御方案
authors:
- Manit Baser
- Vyoman Jain
- Rachel Yeo Hui Min
- Xianglin Yang
- Meenatchi Sundaram Muthu Selva Annamalai
- Dinil Mon Divakaran
affiliations:
- National University of Singapore
- Singapore University of Technology and Design
- University of Toronto
- A*STAR Institute of Advanced Intelligence and Computing
arxiv_id: '2611.34278'
url: https://arxiv.org/abs/2611.34278
pdf_url: https://arxiv.org/pdf/2611.34278
published: '2026-11-25'
collected: '2026-11-26'
category: MultiAgent
direction: 多智能体 · 跨模型隐态通信安全
tags:
- Multi-Agent
- KV cache
- Jailbreak
- Prompt Injection
- Security
one_liner: 提出CHASM框架分析多智能体跨模型KV缓存传输风险并给出低开销防御方案
practical_value: '- 若业务中使用跨模型KV缓存复用（如模型级联降本、子Agent代理处理外部上下文），不要默认下游对齐大模型能保留原生安全能力，尤其是电商导购、广告生成等涉及用户输入/第三方内容的场景需额外做安全校验

  - 可直接复用HANDOFFGUARD的低秩KV校正方案，仅需新增约10M参数，几乎不增加推理延迟，即可将非信任源带来的越狱风险压到接近原生水平，适合生产部署

  - 校准跨模型KV映射的mapper时，可在通用语料外补充越狱、Prompt Injection的拒绝样本，能以极低开销降低约60%的非信任源攻击成功率

  - 若多Agent系统支持动态切换模型，建议限制同一会话的模型切换次数，实测多次切换可将越狱成功率最高抬升38.8pp'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多智能体系统为降低通信与prefill开销，广泛采用跨模型KV缓存传输机制复用上游模型的上下文编码结果，最多可降延迟25x，但该机制让下游对齐模型直接使用未亲自编码的上下文缓存，原有安全对齐、Prompt Injection防御的有效性未被验证，存在未知安全风险。
### 方法关键点
- 提出CHASM攻击框架，覆盖4类越狱攻击面：输入越狱模板、触发多次模型切换、控制上游源模型、白盒优化感知mapper的对抗后缀，外加间接Prompt Injection（IPI）攻击面
- 实验覆盖Qwen3、Llama3、Ministral3共3个主流模型家族，NVIDIA ridge、MLP、CacheBridge、SwaT共4种主流mapper，2种校准语料的24种配置
- 提出轻量防御HANDOFFGUARD，在目标模型侧对传入的KV缓存做低秩残差修正，训练时对齐目标模型原生输出，无需修改原有模型与mapper
### 关键结果
- 零样本越狱攻击成功率最高提升69.2pp，感知mapper的白盒GCG攻击成功率最高达92.5%，远高于原生GCG的37.5%
- 原生IPI成功率仅0.4%的Meta-SecAlign-8B，经过KV缓存传输后IPI成功率最高达44.2%，防御几乎失效
- HANDOFFGUARD的p1版本可将非信任源的越狱成功率控制在仅高于原生4.5pp以内，几乎不损失MMLU、GSM8K任务能力，安全请求过拒率仅提升1.2pp以内
### 核心结论
跨模型KV缓存传输的安全边界由处理上下文的最弱上游节点决定，而非负责最终输出的对齐大模型本身
