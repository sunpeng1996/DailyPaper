---
title: On Evaluating and Improving Conversational Agents in Production
title_zh: 生产环境会话Agent的评估与优化框架
authors:
- Kasra Hosseini
- Wen-Sen Cheng
- Marco-Andrea Buchmann
- Emir Mulabegovic
- Weiwei Cheng
affiliations:
- Zalando SE, Germany
- Zalando, Switzerland
arxiv_id: '2609.32092'
url: https://arxiv.org/abs/2609.32092
pdf_url: https://arxiv.org/pdf/2609.32092
published: '2026-09-25'
collected: '2026-09-29'
category: Agent
direction: 会话Agent · 生产环境评估与迭代优化
tags:
- ConversationalAgent
- OfflineEvaluation
- UserSimulation
- LLM-as-Judge
- MultiAgentSystem
one_liner: 提出生产级多Agent会话导购系统的全链路评估优化框架，解决日志不可重放、随机波动、归因难三大痛点
practical_value: '- 评估生产级多Agent系统时，不要直接重放历史对话日志，改用基于历史交互的 grounded user simulation
  生成动态对话，避免系统修改后后续轮次失效的问题

  - 针对具体bad case做优化时，可构建行为专属的pass/fail断言集+固定场景cohort，结合多次重复跑的基线，用配对百分位bootstrap区间区分真实优化和系统随机波动，避免误判

  - 多Agent系统的问题归因不要只看结果展示层，要沿着全交互路径提假设验证，比如商品轮盘的品类错误可能来自query生成层而非curation层，小范围prompt修改即可解决

  - LLM-as-judge要做全链路校验：检查传入的证据字段是否完整、配置参数（如temperature）是否生效、统计方法是否正确，避免看似合理的评分误导决策'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生产环境LLM驱动的会话Agent（如电商导购）迭代时面临三大核心痛点：1）历史对话日志无法重放，系统修改后回复变化会导致后续历史轮次失效；2）LLM本身的随机性、商品库存/价格/用户个性化信号的动态变化，导致同一请求多次运行结果不同，无法区分是真实优化还是随机波动；3）聚合质量指标只能反映整体变化，无法定位具体问题行为的根因，难以指导迭代。

### 方法关键点
- Evaluation Harness模块：针对待优化的具体行为，生成可量化的pass/fail断言集，同时基于历史对话或目标描述构建固定的用户场景cohort，通过grounded用户模拟器动态生成后续对话轮次，而非重放日志
- 固定基线构建：对未修改的系统多次运行cohort，存储基线结果和波动范围，后续修改版本的对比都基于该基线，采用场景级配对百分位bootstrap区间计算差异，区分真实变化和随机噪声
- Improvement Orchestrator模块：基于断言结果自动生成优化假设，每个假设对应一个独立的系统修改版本，和基线对比，只有目标指标显著提升、护栏指标无显著退化且二次验证通过的版本才会进入人工审核和线上A/B测试流程

### 关键结果数字
在Zalando月活数百万的多语言电商会话导购系统上验证：1）商品轮盘品类错误优化：将curation层prompt的偏好要求改为严格规则，首屏商品品类匹配率从83.3%提升到89.3%；2）男性上下文下性别中性请求返回女性商品问题：将购物上下文设为系统prompt的默认绑定规则，首屏商品性别匹配率从73.3%提升到100%，任务完成分从4.27提升到4.96，均通过显著性校验。

### 最值得记住的一句话
生产环境多Agent系统的优化不能依赖通用聚合指标，要针对具体行为做专属评估，必须把系统随机波动和真实优化区分开，评估链路本身也要像业务系统一样做校验。
