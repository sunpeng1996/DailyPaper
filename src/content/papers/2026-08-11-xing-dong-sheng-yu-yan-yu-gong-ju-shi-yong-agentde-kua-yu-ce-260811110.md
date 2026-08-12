---
title: 'Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention
  in Tool-Using Agents'
title_zh: 行动胜于言语：工具使用Agent的跨语言策略留存度度量
authors:
- Sourabrata Mukherjee
- Kalika Bali
- Sunayana Sitaram
affiliations:
- Microsoft Research India
arxiv_id: '2608.11110'
url: https://arxiv.org/abs/2608.11110
pdf_url: https://arxiv.org/pdf/2608.11110
published: '2026-08-11'
collected: '2026-08-12'
category: Agent
direction: 多语言工具Agent 行为一致性度量
tags:
- Agent
- Cross-lingual
- Evaluation
- Tool Use
- Policy Retention
one_liner: 提出修正5类混淆的跨语言Agent行为一致性度量框架，验证10B+大模型跨语言策略留存稳定71-73%
practical_value: '- 做多语言Agent服务时，不要只看最终答案准确率，要额外监控工具调用序列一致性，避免非英语语种出现额外翻译成本、特有的故障模式

  - 评估多语言Agent性能时，必须加入同语言复现一致性作为基线，否则跨语言差异的结论可能被模型自身随机性、trace长度、空trace等混淆因素扭曲

  - 多语言Agent的英文枢轴效应无法通过prompt关闭，做非英语语种工具调用优化时，可直接基于英文枢轴链路做成本/延迟优化，无需尝试让模型直接用非英语规划

  - ReAct类Agent的解析失败率要单独上报，超过20%的模型不能参与排名，少量few-shot示例就能大幅降低解析失败率，无需微调模型'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言Agent评估仅对比最终输出准确率，完全忽略中间工具调用序列，而调用序列直接决定Agent的服务成本、延迟、故障模式、合规可审计性：相同答案的跨语言请求，可能因调用链路差异出现非英语语种成本更高、特有故障无法被英文回归测试覆盖、合规策略失效等问题，且此前无可靠的序列层面度量方法。
### 方法关键点
- 提出归一化策略留存度指标$	ilde{I}=I_{cross}/I_{within}$：$I_{cross}$为跨语言相同任务的trace相似度，$I_{within}$为同语言相同任务两次独立运行的trace相似度，消除模型自身随机性干扰
- 针对性修正5类混淆因素：空trace过滤、trace长度双向匹配、随机匹配基线校准、同种子采样对齐、消除短trace天然相似度高的偏差
- 基于统一的5种工具调用符号集，所有跨语言任务采用严格对齐的平行语料，保证任务语义完全一致
### 关键结果
- 实验覆盖8个模型、6个基准、41种语言，共238万次Agent rollout：greedy解码下，10B参数以上前沿大模型跨语言策略留存稳定在71-73%，模型差异仅能解释5.7%的方差，10B以下模型无该规律
- 非英语任务普遍存在英文枢轴效应：99%的推理过程为英文，翻译是最常用工具，移除翻译工具会降低跨语言一致性，直接prompt要求用目标语言推理的合规率低于1%
- 单个trace解析正则会导致模型准确率被低估26倍，仅需加入2个few-shot示例即可修复该测量误差，而非提升模型本身能力
### 核心结论
答案一致不代表行为一致，多语言Agent的成本、故障风险、可审计性藏在工具调用链路中，而非最终答案里。
