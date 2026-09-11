---
title: 'SpecGuard: Inference-Time Backdoor Detection For Free'
title_zh: SpecGuard：零额外计算开销的LLM推理阶段后门检测器
authors:
- Rui Wen
- Ahmed Salem
- Andrew Paverd
- Mark Russinovich
- Zheng Li
affiliations:
- Institute of Science Tokyo
- Microsoft Security Response Center
- Microsoft Azure
- Shandong University
arxiv_id: '2609.11799'
url: https://arxiv.org/abs/2609.11799
pdf_url: https://arxiv.org/pdf/2609.11799
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: LLM推理安全 · 运行时后门检测
tags:
- Backdoor Detection
- Speculative Decoding
- LLM Security
- Runtime Monitoring
- Inference Optimization
one_liner: 复用推测解码已有验证信号，实现零额外模型计算开销的LLM推理时后门激活检测
practical_value: '- 若业务已上线 speculative decoding 加速 LLM 服务（如Agent工具调用、生成式推荐文案/广告话术生成），可直接复用现有accept/reject统计做运行时风险检测，无额外模型计算开销，完全不影响推理
  latency

  - 依赖第三方LoRA/微调模型的业务场景（如电商个性化素材生成、垂类Agent服务），无需每次模型更新都做全量离线安全审计，仅监控 draft-target
  接受率的异常偏移，即可快速发现后门激活，仅隔离可疑请求无需全量下线模型

  - 部署时可直接复用论文验证的优化trick：基于正常业务流量校准接受率基线，采用双侧异常评分（过高/过低接受率都报警）覆盖 draft 被投毒的极端场景，搭配多尺度窗口（单query、5、20、100）覆盖孤立触发、低频批量触发等不同攻击模式

  - 针对攻击者在恶意输出后拼接正常文本稀释检测信号的对抗场景，无需统计全序列接受率，仅计算生成前8个token的接受率即可保留90%以上的检测能力，该trick可直接落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM 普遍依赖第三方微调、开源下载的 checkpoint 或 LoRA 插件，易被植入后门：正常输入下表现正常，遇到特定触发器时输出攻击者控制的恶意内容。离线全量审计成本高，且模型/插件更新频繁无法每次都覆盖；现有运行时后门检测方法要么对触发器形式有强假设易漏检，要么需要额外输入扰动、多一次生成步骤，难以适配 latency 敏感的线上服务。

### 方法关键点
- 核心观察：speculative decoding 流程中，干净的 draft 模型不会预测后门触发后的恶意输出，导致后门激活时 draft token 的接受率会发生显著偏移，该信号是现有推理流程已经生成的副产品，无额外计算开销
- 计算单query的 draft token 接受率，与正常流量校准的基线对比，异常则触发报警
- 理论证明存在效力-隐蔽性 tradeoff：攻击者要压低接受率偏移的信号，必须大幅弱化后门恶意输出的效果
- 部署优化：采用双侧异常评分覆盖 draft 被投毒的场景，多尺度窗口适配不同触发频率，早期token统计对抗恶意输出后拼接正常文本的信号稀释

### 关键结果
- 覆盖4种主流后门类型、3个模型家族（LLaMA 3、Gemma 3、Qwen3，最高32B参数），单query检测AUROC达0.929~0.974，效果与需要额外一次生成的CleanGen相当，且无额外推理开销
- 可检测隐藏在系统prompt、RAG上下文、检索结果中的触发器，输入层面检测方法ONION对这类触发器的AUROC仅0.226~0.653，远低于SpecGuard
- 自适应攻击者若要将检测AUROC降到接近随机水平，攻击成功率会从100%下跌到10%以下

> 最值得记住：speculative decoding 的验证信号不仅能加速推理，还能作为零成本的运行时异常行为传感器，复用在线流程已有信号做安全监控，是性价比极高的工程优化方向
