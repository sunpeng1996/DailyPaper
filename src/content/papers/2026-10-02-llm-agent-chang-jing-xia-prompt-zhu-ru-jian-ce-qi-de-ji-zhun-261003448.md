---
title: 'Passing the Test You Trained On: Re-evaluating Prompt-Injection Detectors
  for LLM Agents'
title_zh: LLM Agent 场景下 Prompt 注入检测器的基准评估偏差研究
authors:
- Zhuowen Liu
affiliations:
- Japan Advanced Institute of Science and Technology (JAIST)
arxiv_id: '2610.03448'
url: https://arxiv.org/abs/2610.03448
pdf_url: https://arxiv.org/pdf/2610.03448
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 安全 · Prompt 注入防御评估
tags:
- Prompt Injection
- LLM Agent
- Security Evaluation
- Benchmark
- Guardrail
one_liner: 揭示Prompt注入检测器基准排名迁移性差，输入形式而非攻击字符串决定实际检测效果
practical_value: '- 选型Prompt注入检测器时不能仅依赖公开基准得分，必须用自身业务的真实工具输出测试**1% FPR下的TPR**和任务拦截率：BIPIA上最优的检测器在Agent场景下1%
  FPR下TPR仅2%

  - 优先选择训练数据输入形式与业务场景匹配的检测器：如果业务Agent处理JSON订单、商品评价等结构化工具输出，优先选训练过Agent风格结构化输入的检测器，而非仅训练过短Prompt注入的模型

  - 工程上可实现免费优化：工具输出送入检测器前先移除YAML/JSON键、HTML标记等序列化冗余信息，同时给检测器标注输入类型（如`tool_result`），可将默认FPR最多降低20倍，几乎不影响检测效果

  - 自研检测器时，避免用公开基准的同分布数据做训练，优先用真实业务的工具输出构造评估集，不要用通用Prompt注入基准的得分代表业务效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent广泛使用Prompt注入检测器过滤工具输出，从业者通常依赖公开基准得分选择检测器，但无人验证这些得分是否能代表Agent真实部署场景的表现，也很少检查检测器训练数据与基准的重叠，极易出现误拦正常请求导致业务失败，或漏过攻击造成安全风险的问题。

### 方法关键点
- 构造无标注偏差的Agent场景数据集：重放AgentDojo、τ-bench两个Agent基准的ground-truth工具调用，得到天然无注入的负样本，通过差分重放注入攻击得到正样本，避免了子串匹配标签的错误
- 覆盖15个主流开源/许可公开的Prompt注入检测器（含Meta Prompt Guard 2、PIGuard等）+2个任务感知LLM Judge，跨3代检测模型架构
- 指标优先关注1% FPR下的TPR，匹配业务场景可接受的低误拦率需求，同时审计公开训练数据的检测器，验证训练分布对效果的影响

### 关键实验结果
- 检测排名跨基准迁移性极差：BIPIA与AgentDojo的检测排名Kendall τ仅为0.01，两个Agent基准之间的τ也仅0.28；BIPIA上最优的PIGuard在1% FPR下TPR达95.1%，但在AgentDojo上仅为2.1%
- 误报率跨Agent基准稳定性高（Kendall τ=0.67），训练过Agent风格结构化工具输出的Horizon-Labs无任何基准数据重叠的情况下，在两个Agent基准上1% FPR下TPR分别达82.2%、100%，FPR接近0

> 最值得记住的一句话：Prompt注入检测器的公开基准得分不能直接指导Agent场景选型，输入形式匹配度和低FPR下的真实业务测试结果才是核心依据
