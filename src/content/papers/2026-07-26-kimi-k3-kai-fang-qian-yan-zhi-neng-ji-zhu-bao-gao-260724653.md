---
title: 'Kimi K3: Open Frontier Intelligence'
title_zh: 《Kimi K3：开放前沿智能技术报告》
authors:
- Kimi Team
- Tongtong Bai
- Yifan Bai
- Yiping Bao
- M. C.
- Jianfeng Cai
- Xinyuan Cai
- Peizhou Cao
- Yuxuan Cao
- Ziwei Chai
affiliations:
- Moonshot AI (Kimi Team)
arxiv_id: '2607.24653'
url: https://arxiv.org/abs/2607.24653
pdf_url: https://arxiv.org/pdf/2607.24653
published: '2026-07-26'
collected: '2026-07-28'
category: LLM
direction: 开源大模型 · 多模态长上下文MoE
tags:
- MoE
- Long Context
- Multimodal
- Reinforcement Learning
- Open Source
one_liner: 开源2.8T参数多模态MoE大模型，1M上下文，性能逼近顶级闭源模型
practical_value: '- MoE架构优化可复用：Stable LatentMoE的SiTU-GLU激活、Quantile Balancing负载均衡方法，可直接应用于业务侧大参数MoE推荐/Agent模型的训练稳定性优化，降低专家闲置率

  - 长上下文工程方案可借鉴：KDA+无位置编码(NoPE)的长上下文设计、渐进式上下文扩展训练流程，可用于电商场景百万级商品库/用户行为序列的RAG、用户长期兴趣建模任务

  - 多能力蒸馏落地方法：Multi-Teacher On-Policy Distillation(MOPD)整合不同领域、不同推理强度专家能力的方案，可用于业务侧统一多任务Agent模型训练，避免维护多个垂直小模型的成本

  - 部署优化trick：MXFP4量化感知训练+EAGLE-3 speculative decoding的配套方案，可大幅降低大模型在推荐文案生成、Agent客服等在线业务的推理延迟和部署成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源大模型参数规模普遍停留在1T级以下，预训练底座能力与闭源顶尖模型差距持续拉大，同时长上下文、Agent、多模态能力的迭代受限于底座性能，开源生态亟需可落地的前沿规模大模型底座支撑下游业务创新。

### 方法关键点
- 架构设计：采用混合注意力（3层KDA+1层Gated MLA）、Attention Residuals跨层信息复用、Stable LatentMoE（896路由专家，单token激活16个，新增SiTU-GLU激活、Quantile Balancing负载均衡），原生多模态采用从0训练的MoonViT-V2视觉编码器，无需对比预训练
- 训练流程：预训练阶段采用渐进式上下文扩展，从8K逐步扩展到1M tokens，缩放效率较Kimi K2提升2.5倍；后训练采用SFT→分领域多推理强度RL→多教师在线蒸馏的三阶段pipeline，整合通用、Agent、编码三大领域9个专家能力
- 工程优化：配套MoonEP专家并行训练框架、百万token Agent RL的持久化沙箱环境，部署侧采用MXFP4量化感知训练+EAGLE-3 speculative解码，大幅降低推理成本

### 关键结果
在长序列编码、Agent、多模态、编码、推理等全维度基准测试中，整体性能仅次于GPT-5.6 Sol、Claude Fable 5，超过其余所有参测开源/闭源模型：Terminal-Bench 2.1得分70.0，仅落后GPT-5.6 Sol 3分；Agent基准GDPval-AA v2 Elo得分1686，超过Opus 4.8近100分；BrowseComp基准得分88.8，位列所有模型第一。

最值得记住的一句话：开源大模型完全可以通过架构、训练、工程的协同优化，在3T参数规模下实现逼近顶尖闭源模型的全维度能力，为下游搜索推荐、Agent等业务场景提供高自由度的前沿底座选择。
