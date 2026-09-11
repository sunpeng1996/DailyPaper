---
title: 'EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing
  Agents'
title_zh: EvoSafeHarness：面向Agent安全的模型与领域专属管控框架演化方法
authors:
- Nanxi Li
- Yingzi Ma
- Yulong Cao
- Edward Suh
- Bo Li
- Dawn Song
- Chaowei Xiao
affiliations:
- Johns Hopkins University
- University of Wisconsin–Madison
- NVIDIA
- University of Illinois Urbana–Champaign
- UC Berkeley
arxiv_id: '2609.05903'
url: https://arxiv.org/abs/2609.05903
pdf_url: https://arxiv.org/pdf/2609.05903
published: '2026-09-04'
collected: '2026-09-11'
category: Agent
direction: Agent安全 · 动态演化安全管控框架
tags:
- Agent Safety
- LLM Agent
- Security Harness
- Adversarial Defense
- Auto Optimization
one_liner: 自动生成适配不同模型与领域的Agent安全管控框架，显著优化安全-效用trade-off，优于现有固定方案
practical_value: '- 电商/广告Agent业务上线安全管控时，无需套用通用策略，可复用该演化框架为不同基座模型、不同业务场景（导购/支付/售后）生成专属安全策略，平衡安全风险和用户体验

  - 安全策略测试阶段可复用「Criticizer对抗审核+分级测试」流水线，避免策略过拟合测试用例，提升上线后对未知攻击的鲁棒性

  - 安全规则设计可参考核心思路：放弃字符串匹配类硬拦截，基于请求来源（用户/外部工具）、动作与任务相关性、业务语义约束做校验，跨场景迁移性更强

  - 多基座部署的业务可按模型对齐程度调整管控强度：高对齐模型用轻量语义校验，低对齐模型用多层过滤，避免强管控浪费高对齐模型的效用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent固定通用安全harness存在跨模型/领域适配性差问题：高对齐模型用严格策略会大幅损失效用，弱模型用宽松策略残留安全风险，不同业务场景的安全语义差异大，通用规则无法同时覆盖所有场景的安全需求。
### 方法关键点
- 将harness拆分为**自然语言策略P**和**可执行代码逻辑C**两部分，支持灵活修改迭代，不受固定架构约束
- 四步闭环优化：Designer生成候选harness → Criticizer做无基准依赖的对抗性审核，筛除过拟合测试用例的规则 → 分级测试环境从静态检查到全量测试逐步筛选，降低计算成本 → Analyzer拆解失败trace反馈迭代
- 优化目标为`score = 效用U - 攻击成功率ASR`，避免"拒绝所有请求"的无效最优解
### 关键结果
在4个主流Agent安全基准上对比CaMeL、DRIFT、Progent等基线：
1. DecodingTrust-Agent的15个模型×领域场景下，平均ASR从45.6%降至10.0%，仅损失3.3%效用，14个场景性能最优
2. AgentDojo上实现82.8%效用、0% ASR，效用是CaMeL同安全等级的2倍；零样本迁移到未见过的AgentDyn场景仍保持75%效用、0% ASR
3. 面对自适应PAIR攻击，16轮攻击预算下平均ASR仍低于20%
### 核心结论
不存在通用最优的Agent安全管控方案，适配所用模型能力和业务领域语义的定制方案才能拿到最优的安全-效用平衡
