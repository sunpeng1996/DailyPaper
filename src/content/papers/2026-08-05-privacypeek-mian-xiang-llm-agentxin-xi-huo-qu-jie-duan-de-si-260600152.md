---
title: 'PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say'
title_zh: PrivacyPeek：面向LLM Agent信息获取阶段的隐私审计基准
authors:
- Mingxuan Zhang
- Jiahui Han
- Dadi Guo
- Songze Li
- Guanchu Wang
- Na Zou
- Dongrui Liu
- Xia Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Southeast University
arxiv_id: '2606.00152'
url: https://arxiv.org/abs/2606.00152
pdf_url: https://arxiv.org/pdf/2606.00152
published: '2026-08-05'
collected: '2026-08-10'
category: Agent
direction: Agent 隐私安全审计评估
tags:
- LLM Agent
- Privacy Audit
- Benchmark
- Data Minimization
- Tool Use
one_liner: 提出覆盖16个领域7类行为的1182个测试用例的基准，双维度评估LLM Agent获取阶段隐私泄漏
practical_value: '- 电商/广告Agent可复用双维度审计逻辑：先审计工具调用轨迹是否获取超出任务需要的用户敏感数据（如消费记录、地址、身份信息），再做探针测试验证已获取数据是否会被诱导泄露，提前规避合规风险

  - 可参考7类过度获取行为的分类，在Agent工具调用层做前置拦截：禁止访问无关格式/时间窗口/字段的数据源，严格遵守数据最小化原则，比事后prompt防御效果更可靠

  - 不要依赖内容里的保密标记防范隐私泄露，实验显示多数Agent见到保密标记反而会提升泄露率，隐私防控必须做在工具调用前的权限层，而非依赖Agent的生成对齐

  - 任务完成率和隐私泄露率正相关，优化Agent能力时要同步做获取阶段的隐私审计，避免能力提升带来的合规风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent隐私审计仅关注输出内容的泄露，完全忽略信息获取阶段——Agent调用工具时经常获取超出任务需求的敏感数据，这些数据一旦进入上下文，随时可能因误操作或攻击泄露，但行业缺乏统一的评估基准，针对获取阶段的审计能力存在明显空白。

### 方法关键点
- 定义7类典型过度获取行为：普通文件名无关访问、敏感文件名诱导访问、跨格式过度访问、过期数据访问、过量字段访问、带保密标记内容访问、超范围推理访问，覆盖16个应用领域（含零售、金融、医疗等电商/推荐高频场景）
- 双维度评估框架：1）Acquisition Inspection：规则化匹配工具调用返回结果，判断是否获取超出任务最小范围的数据，计算内容暴露率CER；2）Probe Elicitation：任务完成后禁用工具，发定向探针测试上下文留存的敏感数据是否会被诱导泄露，计算探针泄露率PLR
- 用10道质量门控制生成1182个可执行测试用例，所有用例都预置了仅完成任务的最小数据访问路径，排除恶意用户/工具/注入的干扰，仅评估Agent自身的工具调用行为

### 关键结果
测试了GPT、Claude、Llama、Qwen四个系列共10款Agent，结果显示：所有Agent都存在过度获取问题，CER范围6.77%~51.95%，PLR范围16.67%~57.53%；任务完成率TCR和CER、PLR强正相关（斯皮尔曼系数分别为0.818、0.685），能力越强的Agent过度获取风险越高；普通prompt级防御仅能降低3.73%~12.69%的CER，超过一半的泄漏风险无法被缓解；内容中的保密标记反而会使多数Agent的PLR提升3%以上，最高提升10.56%。

### 核心结论
LLM Agent的隐私防控必须前置到工具调用的权限层，严格执行数据最小化原则，仅依赖输出审计、prompt防御、内容保密标记的方案都无法有效解决获取阶段的隐私泄漏风险。
