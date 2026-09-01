---
title: 'CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling
  Agents'
title_zh: CAST：面向可靠长周期工具调用Agent的批评感知监督训练框架
authors:
- Amir Saeidi
- Zehua Zhang
- Rishitosh Singh
- Naman Ahuja
- Vivek Gupta
- Ali Payani
- Gaowen Liu
- Jayanth Srinivasa
- Chitta Baral
affiliations:
- Arizona State University
- Cisco Research
arxiv_id: '2608.30147'
url: https://arxiv.org/abs/2608.30147
pdf_url: https://arxiv.org/pdf/2608.30147
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: 长周期工具调用Agent 可靠性优化
tags:
- Tool-Calling Agent
- Reliability
- Actor-Critic
- SFT
- Long-Horizon Agent
one_liner: 提出批评感知训练框架CAST，显著提升长周期工具调用Agent的跨次执行可靠性
practical_value: '- 电商售后/客服Agent场景可复用CAST三级训练流程：先收集轨迹→标注动作级批评信号→训练批评模型+优化策略模型，解决退款、退货等高风险操作的误执行问题

  - 工具调用错误可拆分为幻觉/领域规则违反/工具误用三类，可直接复用该分类逻辑构建业务动作校验规则，降低高风险操作事故率

  - 小参数（4B/8B）专用批评模型效果远优于直接调用GPT-4等通用大模型作为校验器，误判率更低，可大幅降低推理成本同时提升校验准确率

  - 可复用pass^k指标衡量Agent跨次执行可靠性，解决单次成功率高但重复执行易出错的业务问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期工具调用Agent在电商售后、航司订票等场景中，单步错误（如退错单）会导致不可逆任务失败。现有方案要么是推理时加反思机制带来高延迟高成本，要么是RL类优化只有稀疏轨迹级奖励，无法给中间动作提供有效监督；通用大模型作为校验器又存在高误判率，频繁触发不必要的修改循环。

### 方法关键点
- 三阶段训练流程：1）用教师策略多次执行同任务收集成功/失败轨迹，构建经验池；2）用多Agent协同的验证框架，将轨迹级稀疏奖励转化为动作级结构化批评标注，标注包含是否有效+错误类型（幻觉/领域规则违反/工具误用）+判定理由；3）先基于标注训练专用批评模型CAST-Critic，再用Critic生成带批评信号的成功轨迹，监督微调策略模型CAST-Policy
- 推理支持两种模式：单独用微调后的CAST-Policy实现低延迟推理，或搭配CAST-Critic做实时动作校验进一步提升可靠性

### 关键结果
在τ-Bench和τ-Trait的零售、航司、电信、远程医疗4个领域测试，仅用零售域数据训练：
- 域内零售场景，CAST-Policy-4B对比Base 4B，pass^1提升18.9%，衡量跨次可靠性的pass^4提升10.4%；8B版本对比Base 8B pass^4提升9.6%
- 跨域场景平均pass^1提升3.7%，pass^4提升5.1%；CAST-Critic-8B仅用1/15参数量就比GPT-OSS-120B pass^4高15%，比GPT-4作为校验器的误判率低35pct

**最值得记住的一句话：训练专用的小参数批评模型，比直接用通用大模型做动作校验，成本更低、准确率更高、可靠性更强**
